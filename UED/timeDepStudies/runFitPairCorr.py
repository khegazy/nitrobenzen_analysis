import os
import sys
sys.path.append("/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts")
sys.path.append("/reg/neh/home/khegazy/baseTools/UEDanalysis/timeDepStudies")
from plotClass import plotCLASS
from fitPairCorr import fitPairCorr
import tensorflow as tf
import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from enum import Enum

class molOpts(Enum):
  data          = 0
  nitrobenzene  = 1
  phenoxyNO     = 2
  phenoxyNOdiff = 3



if __name__ == "__main__":

  #####  Variables  ##### 
  #molecule = molOpts.nitrobenzene
  molecule = molOpts.phenoxyNOdiff
  sineFit = True
  debug   = False

  parameters = {
      "maxTrain"    : 50000,
      "saveEvery"   : 20,
      "atoms"       : ["hydrogen", "carbon", "nitrogen", "oxygen"],
      "Natoms"      : [5, 6, 1, 2],
      "Rrange"      : [0.5,9],
      "Nbins"       : 555,
      "startBin"    : 50,
      "NfitFxns"    : 750,
      "doNormalEqn" : False,
      "qPerPix"     : 0.0223,
      "elEnergy"    : 3.7e6}

  plc = plotCLASS()

  
  # Simulation/Data Paths
  nitrobenzene_bondFile =\
      "/reg/ued/ana/scratch/nitroBenzene/simulations/nitrobenzene_bonds_"
  phenoxyNO_bondFile =\
      "/reg/ued/ana/scratch/nitroBenzene/simulations/phenoxyRadical_bonds_"

  simDir = "/reg/ued/ana/scratch/nitroBenzene/simulations/"
  phenoxyNO_simPath       = "phenoxyRadical_sMsPatternLineOut_"\
                              + "Qmax-12.376500_Ieb-5.000000_scrnD-4.000000_"\
                              + "elE-3700000.000000_Bins[555].dat"
  nitrobenzene_simPath    = "nitrobenzene_sMsPatternLineOut_"\
                              + "Qmax-12.376500_Ieb-5.000000_scrnD-4.000000_"\
                              + "elE-3700000.000000_Bins[555].dat"
  nitrobenzeneATM_simPath = "nitrobenzene_atmDiffractionPatternLineOut_"\
                              + "Qmax-12.376500_Ieb-5.000000_scrnD-4.000000_"\
                              + "elE-3700000.000000_Bins[555].dat"


  #####  Get Data  #####
  if molecule is molOpts.data:
    sys.exit(0)
  elif molecule is molOpts.nitrobenzene:
    fxnToFit    = np.fromfile(
                    simDir+nitrobenzene_simPath, 
                    dtype=np.double)
    bondPrefix  = nitrobenzene_bondFile
    parameters["sineTransFile"] =\
                  "./results/fitPairCorrNitrobenzene_maxR-9.862436[369].dat"
  elif molecule is molOpts.phenoxyNO:
    fxnToFit    = np.fromfile(
                    simDir+phenoxyNO_simPath, 
                    dtype=np.double)
    bondPrefix  = nitrobenzene_bondFile
    parameters["sineTransFile"] =\
                  "./results/fitPairCorr"
  elif molecule is molOpts.phenoxyNOdiff:
    fxnToFit  = np.fromfile(
                  simDir+phenoxyNO_simPath, 
                  dtype=np.double)\
                - np.fromfile(
                  simDir+nitrobenzene_simPath, 
                  dtype=np.double)
    parameters["sineTransFile"] =\
                  "./results/fitPairCorrPhenoxyDiff_maxR-9.862436[369].dat"
  else:
    raise RuntimeError("Do not recognize molecule %s" % (repr(molecule))) 

  

  variance  = np.ones(fxnToFit.shape[0]) #1./(np.abs(data) + 1e-4)
  #variance  = 1./(np.abs(fxnToFit) + 1e-4)

  atomicScat = np.fromfile(simDir+nitrobenzeneATM_simPath, dtype=np.double)


  # Get Bonds
  bondTypes    = []
  for i in range(len(parameters["atoms"])):
    if parameters["atoms"][i] == "hydrogen":
      continue
    for j in range(i, len(parameters["atoms"])):
      if parameters["atoms"][j] == "hydrogen":
        continue
      if (i == j) and (parameters["Natoms"][i] == 1):
        continue
      bondTypes.append(parameters["atoms"][i]+"-"+parameters["atoms"][j])

  bondCoeffs  = np.zeros(
                  (len(bondTypes), parameters["NfitFxns"]), 
                  dtype=np.float32)
  if molecule is molOpts.nitrobenzene or molecule is molOpts.phenoxyNO:
    for i,bt in enumerate(bondTypes):
      bonds = np.fromfile(bondPrefix+bt+".dat", np.double)
      for bnd in bonds:
        bInd = int(parameters["NfitFxns"]*(bnd-parameters["Rrange"][0])
                  /(parameters["Rrange"][1]-parameters["Rrange"][0]))
        bondCoeffs[i,bInd] += 2
  elif molecule is molOpts.phenoxyNOdiff:
    oldBondTypes  = bondTypes[:]
    bondTypes     = []
    btInd         = 0
    for bt in oldBondTypes:
      if ("hydrogen" in bt) or ("carbon-carbon" == bt):
        continue
      bondTypes.append(bt)
      bonds = np.fromfile(nitrobenzene_bondFile+bt+".dat", np.double)
      for bnd in bonds:
        bInd = int(parameters["NfitFxns"]*(bnd-parameters["Rrange"][0])
                  /(parameters["Rrange"][1]-parameters["Rrange"][0]))
        bondCoeffs[btInd,bInd] -= 2

      if ("carbon-nitrogen" != bt) and ("oxygen-oxygen" != bt):
        bonds = np.fromfile(phenoxyNO_bondFile+bt+".dat", np.double)
        for bnd in bonds:
          bInd = int(parameters["NfitFxns"]*(bnd-parameters["Rrange"][0])
                    /(parameters["Rrange"][1]-parameters["Rrange"][0]))
          bondCoeffs[btInd,bInd] += 2
      btInd += 1




  #########################
  #####  Build Model  #####
  #########################

  fitCls = fitPairCorr(
      parameters,
      fxnToFit,
      variance,
      sineFit,
      debug)


  #####################
  #####  Fitting  #####
  #####################
  
  with tf.Session() as sess:

    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())

    #Li, Ri = fitCls.debugFxn(sess)
    #print(Li)
    #print(Ri)
    if not parameters["doNormalEqn"]:
      fitCls.fit(sess)

    ###  Plot Fit  ###
    #plotFit = np.stack((data, fitCls.get_fit(sess)/np.exp(-1*(np.arange(555)/(555./3.25))**2/2.)))
    plotFit = np.stack((fxnToFit, fitCls.get_fit(sess)))
    if "startBin" in parameters:
      plotFit[:,:parameters["startBin"]] = 0
    opts = {
        "xTitle" : r"Q [$\AA^{-1}$]"}
    plc.print1d(plotFit, 
        "./plots/compareFit", 
        xRange=[0, parameters["Nbins"]*parameters["qPerPix"]],
        isFile=False,
        options=opts)

    ###  Plot Coefficients  ###
    sineTrans = fitCls.evaluate(sess, [fitCls.sineTransform])
    sineTrans[0] /= 7.
    fitCoeffs = fitCls.get_fitCoeff(sess)

    print("FTC ",fitCoeffs.shape)
    for i in range(fitCoeffs.shape[0]):
      plc.print1d(fitCoeffs[i,:], 
          "./plots/fitCoeffs_" + bondTypes[i], 
          xRange=parameters["Rrange"],
          isFile=False)

    #fitCoeffs = fitCoeffs.sum(axis=0)
    opts = {
        "labels" : ["sine Transform", "Fit"] + bondTypes,
        "xTitle" : r"R [$\AA$]"}
    plc.print1d(np.vstack(
                  (np.vstack((np.array(sineTrans), fitCoeffs),),
                    bondCoeffs/60.)),  
        "./plots/fitCoeffs_raw", 
        xRange=parameters["Rrange"],
        isFile=False,
        options=opts)

    fitCoeffs = gaussian_filter1d(fitCoeffs, 20, axis=1)*6
    plc.print1d(np.vstack((np.array(sineTrans), fitCoeffs)), 
        "./plots/fitCoeffs_filt", 
        xRange=parameters["Rrange"],
        isFile=False)

    plc.print1d(sineTrans[0],
        "./plots/fitSineTrans",
        xRange=parameters["Rrange"],
        isFile=False)


    ###  Check Parameters  ###
    if debug:
      output = [
          fitCls.deBrogW,
          fitCls.molAtomicScat,
          fitCls.scatAmps,
          fitCls.qInp,
          fitCls.qEval,
          fitCls.bondScatAmps,
          fitCls.bondNormAmps,
          fitCls.interp,
          fitCls.Sargs,
          fitCls.sinusiods,
          fitCls.sinusiodsDR]

      deBrog, atmNorm, scatAmps, qInp, qEval, bondScatAmps,\
      bondNormAmps, interp, Sargs, sinusiods, sinusiodsDR\
          = sess.run(output)

      print("atmScat", atmNorm)
      opts = {"yLog" : True}
      print("shape qs", qInp.shape, qEval.shape, bondScatAmps.shape)
      print("DeBroglie Wavelength (angs): ", deBrog) # forgot to m->angs
      plc.print1d(np.vstack((atomicScat,atmNorm)), "./plots/testFit_atomicScat", options=opts, isFile=False)
      opts["labels"] = fitCls.atoms
      plc.print1d(scatAmps, "./plots/testFit_scatteringAmps", options=opts, isFile=False)
      plc.print1d(qInp[0,:,0], "./plots/testFit_qInp", isFile=False)
      plc.print1d(qEval[0,:,0], "./plots/testFit_qEval", isFile=False)
      opts["labels"] = fitCls.bondTypes
      plc.print1d(bondScatAmps, "./plots/testFit_bondScatAmps", 
          options=opts, isFile=False)
      opts["labels"] = fitCls.bondTypes
      plc.print1d(bondNormAmps, "./plots/testFit_bondNormAmps", isFile=False)
      opts["labels"] = fitCls.atoms
      plc.print1d(interp, "./plots/testFit_interp", options=opts, isFile=False)
      plc.print2d(Sargs, "./plots/testFit_Sargs", isFile=False)
      plc.print2d(sinusiods, "./plots/testFit_sinusiods", isFile=False)
      plc.print2d(sinusiodsDR, "./plots/testFit_sinusiodsDR", isFile=False)



