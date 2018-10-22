import os
import sys
sys.path.append("/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts")
sys.path.append("/reg/neh/home/khegazy/baseTools/UEDanalysis/timeDepStudies")
from plotClass import plotCLASS
from fitPairCorr import fitPairCorr
import tensorflow as tf
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt




if __name__ == "__main__":
 
  plc = plotCLASS()
  debug = False

  parameters = {
      "maxTrain"    : 1300,
      "saveEvery"   : 20,
      "atoms"       : ["carbon", "nitrogen", "oxygen"],
      "singleAtoms" : ["nitrogen"],
      "Nbins"       : 555,
      "NfitFxns"    : 50,
      "qPerPix"     : 0.0223,
      "elEnergy"    : 3.7e6}

  fitCls = fitPairCorr(parameters)

  #####  Get Data  #####
  simDir = "/reg/ued/ana/scratch/nitroBenzene/simulations/"
  phnxy = "phenoxyRadical_sMsPatternLineOut_Qmax-12.376500_Ieb-5.000000_scrnD-4.000000_elE-3700000.000000_Bins[555].dat"
  refer = "nitrobenzene_sMsPatternLineOut_Qmax-12.376500_Ieb-5.000000_scrnD-4.000000_elE-3700000.000000_Bins[555].dat"

  data = np.fromfile(simDir+phnxy, dtype=np.double)\
               - np.fromfile(simDir+refer, dtype=np.double)

  var  = 1./(np.abs(data) + 1e-4)

  fitCls.add_data(data, var)


  #####################
  #####  Fitting  #####
  #####################
  
  with tf.Session() as sess:

    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())

    fitCls.fit(sess)

    ###  Plot Fit  ###
    plotFit = np.stack((data, fitCls.get_fit(sess)))
    plc.print1d(plotFit, "./plots/compareFit", isFile=False)

    ###  Plot Coefficients  ###
    fitCoeffs = fitCls.get_fitCoeff(sess)

    for i in range(len(fitCls.bondTypes)):
      plc.print1d(fitCoeffs[i,:], 
          "./plots/fitCoeffs_" + fitCls.bondTypes[i], 
          isFile=False)

    fitCoeffs = fitCoeffs.sum(axis=0)
    plc.print1d(fitCoeffs, "./plots/fitCoeffs_all", isFile=False)


    ###  Check Parameters  ###
    if debug:
      output = [
          fitCls.deBrogW,
          fitCls.atomicNorm,
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

      opts = {"yLog" : True}
      print("shape qs", qInp.shape, qEval.shape, bondScatAmps.shape)
      print("DeBroglie Wavelength (angs): ", deBrog) # forgot to m->angs
      plc.print1d(atmNorm, "./plots/testFit_atomicNorm", options=opts, isFile=False)
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



