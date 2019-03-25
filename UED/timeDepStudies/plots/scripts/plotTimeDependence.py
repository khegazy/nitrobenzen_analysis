import numpy as np
import sys
sys.path.append('../../../plots/scripts')
sys.path.append('/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts')
from plotClass import plotCLASS
from plotParams import pltParams

params = pltParams()

plc = plotCLASS()


plotTsmeared = False
#runs = ["20180629_1630", "20180627_1551", "20180630_1925", "20180701_0746"]
#runs = ["20180627_1551", "20180629_1630", "20180630_1925", "20180701_0746"]
runs = ["20180627_1551"]
maxX = [2, 1.1, 1.1, 1.1]
smear = "0.025000"
mergeFolder = "/reg/ued/ana/scratch/nitroBenzene/mergeScans/"

selectTimes = [ [0.1, 2.1, 3, 6.5, 12],#[0, 0.5, 1, 4, 8],
                [0, 0.25, 0.5, 0.75, 1],
                [0, 0.25, 0.5, 0.75, 1],
                [0, 0.25, 0.5, 0.75, 1]]

#################################################
#####  Plotting time dependent diffraction  #####
#################################################
#colRange = [[-2e-3, 2e-3], [-2e-3, 2e-3], [-2e-3, 2e-3], [-2e-3, 2e-3]]
#colRange = [[-7e-3, 7e-3], [-7e-3, 7e-3], [-7e-3, 7e-3], [-7e-3, 7e-3]]
colRange = [-3e-3, 3e-3]
for i,run in enumerate(runs):
  opts = {
    "colorRange" : colRange,
    "colorMap"   : 'seismic',
    "xTitle"     : "Time [ps]",
    "yTitle"     : r"Q [$\AA^{-1}$]",
    "yRebin"     : 8
    #"TearlySub"  : 3
    }

  timeDelay = np.fromfile("../../../mergeScans/results/timeDelays["
        + str(params.timeSteps[i] + 1) + "].dat", np.double)
 

  plc.print2d(mergeFolder + "data-" 
          + run + "-azmAvgDiff["
          + str(params.timeSteps[i]) 
          + "," + str(params.NradAzmBins) + "].dat",
        "../data-" + run + "-azmAvgDiffFull",
        X=timeDelay,
        yRange=params.QrangeAzm,
        options=opts)

  plc.print2d("../../results/data-" 
          + run + "_azmAvgSubtractFinalState["
          + str(params.timeSteps[i]) 
          + "," + str(params.NradAzmBins) + "].dat",
        "../data-" + run + "-azmAvgSubtractFinalStateFull",
        X=timeDelay,
        yRange=params.QrangeAzm,
        options=opts)
   
  plc.print2d("../../results/data-" 
          + run + "_sMsSubtractFinalState["
          + str(params.timeSteps[i]) 
          + "," + str(params.NradAzmBins) + "].dat",
        "../data-" + run + "-sMsSubtractFinalStateFull",
        X=timeDelay,
        yRange=params.QrangeAzm,
        options=opts)

  if plotTsmeared:
    plc.print2d(mergeFolder + "data-"
            + run + "-tSmeared-" + smear + "-azmAvgDiff["
            + str(params.smearTimeSteps[i]) 
            + "," + str(params.NradAzmBins) + "].dat",
          "../data-" + run + "-tSmearedAzmAvgDiffFull",
          xRange=[timeDelay[0], timeDelay[-1]],
          yRange=params.QrangeAzm,
          options=opts)

  opts["xSlice"] = [-0.125, maxX[i]]
  plc.print2d(mergeFolder + "data-"
          + run + "-azmAvgDiff["
          + str(params.timeSteps[i]) 
          + "," + str(params.NradAzmBins) + "].dat",
        "../data-" + run + "-azmAvgDiff",
        X=timeDelay,
        yRange=params.QrangeAzm,
        options=opts)
  
  plc.print2d("../../results/data-" 
          + run + "_azmAvgSubtractFinalState["
          + str(params.timeSteps[i]) 
          + "," + str(params.NradAzmBins) + "].dat",
        "../data-" + run + "-azmAvgSubtractFinalState",
        X=timeDelay,
        yRange=params.QrangeAzm,
        options=opts)
 
  plc.print2d("../../results/data-" 
          + run + "_sMsSubtractFinalState["
          + str(params.timeSteps[i]) 
          + "," + str(params.NradAzmBins) + "].dat",
        "../data-" + run + "-sMsSubtractFinalState",
        X=timeDelay,
        yRange=params.QrangeAzm,
        options=opts)
 
  if plotTsmeared:
    plc.print2d(mergeFolder + "data-"
            + run + "-tSmeared-" + smear + "-azmAvgDiff["
            + str(params.smearTimeSteps[i]) 
            + "," + str(params.NradAzmBins) + "].dat",
          "../data-" + run + "-tSmearedAzmAvgDiff",
          xRange=[timeDelay[0], timeDelay[-1]],
          yRange=params.QrangeAzm,
          options=opts)

######################################################
#####  Plotting time dependent pair correlation  #####
######################################################

colRange = [-7e-2, 7e-2]#, [-1e-2, 1e-2], [-1e-2, 1e-2], [-1e-2, 1e-2]]
for i,run in enumerate(runs):
  opts = {
    "colorRange" : colRange,
    "colorMap"   : 'seismic',
    "xTitle"     : "Time [ps]",
    "yTitle"     : r"R [$\AA$]",
    #"TearlySub"  : 3
    #"interpolate": [200, 100]
    }

  timeDelay = np.fromfile("../../../mergeScans/results/timeDelays["
        + str(params.timeSteps[i] + 1) + "].dat", np.double)
  
  plc.print2d("../../results/data-" + run + "_pairCorrOdd["
          + str(params.timeSteps[i]) + "," 
          + str(params.NpairCorrBins) + "].dat",
        "../data-" + run + "_pairCorrFull",
        X=timeDelay,
        yRange=params.Rrange,
        options=opts)

  plc.print2d("../../results/data-" + run + "_pairCorrSubtractFinalState["
          + str(params.timeSteps[i]) + "," 
          + str(params.NpairCorrBins) + "].dat",
        "../data-" + run + "_pairCorrSubtractFinalStateFull",
        X=timeDelay,
        yRange=params.Rrange,
        options=opts)

  if plotTsmeared:
    plc.print2d("../../results/data-" + run + "_tSmeared_pairCorrOdd["
            + str(params.smearTimeSteps[i]) + "," 
            + str(params.NpairCorrBins) + "].dat",
          "../data-" + run + "_tSmearedPairCorrFull",
          xRange=[timeDelay[0], timeDelay[-1]],
          yRange=params.Rrange,
          options=opts)


  opts["xSlice"] = [-0.125, maxX[i]]
  plc.print2d("../../results/data-" + run + "_pairCorrOdd["
          + str(params.timeSteps[i]) + "," 
          + str(params.NpairCorrBins) + "].dat",
        "../data-" + run + "_pairCorr",
        X=timeDelay,
        yRange=params.Rrange,
        options=opts)

  plc.print2d("../../results/data-" + run + "_pairCorrSubtractFinalState["
          + str(params.timeSteps[i]) + "," 
          + str(params.NpairCorrBins) + "].dat",
        "../data-" + run + "_pairCorrSubtractFinalState",
        X=timeDelay,
        yRange=params.Rrange,
        options=opts)

  if plotTsmeared:
    plc.print2d("../../results/data-" + run + "_tSmeared_pairCorrOdd["
            + str(params.smearTimeSteps[i]) + "," 
            + str(params.NpairCorrBins) + "].dat",
          "../data-" + run + "_tSmearedPairCorr",
          xRange=[timeDelay[0], timeDelay[-1]],
          yRange=params.Rrange,
          options=opts)



"""
########################################
#####  Plotting Phynel Simulation  #####
########################################


NdissTimeSteps = "400"
NrotTimeSteps = "800"
xZoomFine = [0, 1]
xZoomMed = [0, 2]
timeDepSimDir = "/reg/ued/ana/scratch/nitroBenzene/simulations/timeDependent/"
#timeDepSimDir = "/reg/neh/home/khegazy/analysis/nitrobenzene/simulations/timeDependent/"
dissTimeDelay = np.fromfile(
      timeDepSimDir + "dissociation_phenyl-N2O_timeDelays["
      + NdissTimeSteps + "].dat", np.double)
rotTimeDelay = np.fromfile(
      timeDepSimDir + "rotation_nitrobenzene_timeDelays["
      + NrotTimeSteps + "].dat", np.double)
opts = {
  "colorRange" : [-3e-1, 3e-1],
  "colorMap"   : 'seismic',
  "xTitle"     : "Time [ps]",
  "yTitle"     : r"R [$\AA$]",
  }

opts["xSlice"] = xZoomFine
plc.print2d("../../results/"
        "sim-nitrobenzene-dissociation-phenyl-N2O_pairCorrOdd["
        +NdissTimeSteps+",369].dat",
      "../sim-nitrobenzene-dissociation-phenyl-N2O_pairCorr",
      X=dissTimeDelay,
      yRange=params.Rrange,
      options=opts)

opts["xSlice"] = xZoomMed
plc.print2d("../../results/"
        "sim-nitrobenzene-dissociation-phenyl-N2O_pairCorrOdd["
        +NdissTimeSteps+",369].dat",
      "../sim-nitrobenzene-dissociation-phenyl-N2O_pairCorrFull",
      X=dissTimeDelay,
      yRange=params.Rrange,
      options=opts)


opts["xSlice"] = xZoomFine
plc.print2d("../../results/"
        "sim-nitrobenzene-rotation-nitrobenzene_pairCorrOdd["
        +NrotTimeSteps+",369].dat",
      "../sim-nitrobenzene-rotation_pairCorr",
      X=rotTimeDelay,
      yRange=params.Rrange,
      options=opts)

opts["xSlice"] = xZoomMed
plc.print2d("../../results/"
        "sim-nitrobenzene-rotation-nitrobenzene_pairCorrOdd["
        +NrotTimeSteps+",369].dat",
      "../sim-nitrobenzene-rotation_pairCorrFull",
      X=rotTimeDelay,
      yRange=params.Rrange,
      options=opts)


diffColorRange = [-2e-2, 2e-2]
smsColorRange = [-6e-1, 6e-1]
opts = {
  "colorRange" : smsColorRange,
  "colorMap"   : 'seismic',
  "xTitle"     : "Time [ps]",
  "yTitle"     : r"Q [$\AA^{-1}$]",
  }

opts["xSlice"] = xZoomFine
opts["colorRange"] = smsColorRange
opts["ySlice"] = [0,10]
plc.print2d(timeDepSimDir
        + "dissociation_phenyl-N2O_azmAvgSMS_Qmax-12.376500_Ieb-5.000000"
        + "_scrnD-4.000000_elE-3700000.000000_Bins["
        + NdissTimeSteps + ",555].dat",
      "../sim-dissociation-phenyl-N2O-azmAvgSMS",
      X=dissTimeDelay,
      yRange=params.QrangeAzm,
      options=opts)

opts["xSlice"] = xZoomFine
opts["colorRange"] = diffColorRange
plc.print2d(timeDepSimDir
        + "dissociation_phenyl-N2O_azmAvg_Qmax-12.376500_Ieb-5.000000"
        + "_scrnD-4.000000_elE-3700000.000000_Bins["
        + NdissTimeSteps + ",555].dat",
      "../sim-dissociation-phenyl-N2O-azmAvg",
      X=dissTimeDelay,
      yRange=params.QrangeAzm,
      options=opts)

opts["xSlice"] = xZoomFine
opts["colorRange"] = smsColorRange
plc.print2d(timeDepSimDir
        + "rotation_nitrobenzene_azmAvgSMS_Qmax-12.376500_Ieb-5.000000"
        + "_scrnD-4.000000_elE-3700000.000000_Bins["
        + NrotTimeSteps + ",555].dat",
      "../sim-rotation-nitrobenzene-azmAvgSMS",
      X=rotTimeDelay,
      yRange=params.QrangeAzm,
      options=opts)

opts["xSlice"] = xZoomMed
opts["colorRange"] = smsColorRange
plc.print2d(timeDepSimDir
        + "rotation_nitrobenzene_azmAvgSMS_Qmax-12.376500_Ieb-5.000000"
        + "_scrnD-4.000000_elE-3700000.000000_Bins["
        + NrotTimeSteps + ",555].dat",
      "../sim-rotation-nitrobenzene-azmAvgSMSFull",
      X=rotTimeDelay,
      yRange=params.QrangeAzm,
      options=opts)

opts["xSlice"] = xZoomFine
opts["colorRange"] = diffColorRange
plc.print2d(timeDepSimDir
        + "rotation_nitrobenzene_azmAvg_Qmax-12.376500_Ieb-5.000000"
        + "_scrnD-4.000000_elE-3700000.000000_Bins["
        + NrotTimeSteps + ",555].dat",
      "../sim-rotation-nitrobenzene-azmAvg",
      X=rotTimeDelay,
      yRange=params.QrangeAzm,
      options=opts)

opts["xSlice"] = xZoomMed
opts["colorRange"] = diffColorRange
plc.print2d(timeDepSimDir
        + "rotation_nitrobenzene_azmAvg_Qmax-12.376500_Ieb-5.000000"
        + "_scrnD-4.000000_elE-3700000.000000_Bins["
        + NrotTimeSteps + ",555].dat",
      "../sim-rotation-nitrobenzene-azmAvgFull",
      X=rotTimeDelay,
      yRange=params.QrangeAzm,
      options=opts)

"""


"""
#######################################
#####  Plotting averaged regions  #####
#######################################

opts1d = {
    "xTitle"  : "Time [ps]",
    "labels"  : ["1.1-1.7",
                  "1.7-2.0",
                  "2.0-2.75",
                  "3.0-4.0",
                  "4.0-5.0"
                  ]
    }
"""
"""
opts2d = {
    #"colorRange" : [-1e-1, 1e-1],
    "colorMap"   : 'seismic',
    "xTitle"     : "Time [ps]",
    "yTitle"     : r"R [$\AA$]",
    }


for i,run in enumerate(runs):
  if i is not 0:
    continue
  Rfiles = [
      "../../results/data-" + run 
        + "-Rmean1.100000-1.700000-Bins["
        + str(params.timeSteps[i]) + "].dat",
      "../../results/data-" + run 
        + "-Rmean1.700000-2.000000-Bins["
        + str(params.timeSteps[i]) + "].dat",
      "../../results/data-" + run 
        + "-Rmean2.000000-2.750000-Bins["
        + str(params.timeSteps[i]) + "].dat",
      "../../results/data-" + run 
        + "-Rmean3.000000-4.000000-Bins["
        + str(params.timeSteps[i]) + "].dat",
      "../../results/data-" + run 
        + "-Rmean4.000000-5.000000-Bins["
        + str(params.timeSteps[i]) + "].dat"]

  timeDelay = np.fromfile("../../../mergeScans/results/timeDelays["
      + str(params.timeSteps[i] + 1) + "].dat", np.double)

  opts1d["xSlice"] = [-0.125, maxX[i]]
  opts2d["xSlice"] = [-0.125, maxX[i]]
  plc.print1d(Rfiles, 
      "../data-" + run + "-Rmeans",
      X=timeDelay[:-1],
      options=opts1d)

  plc.print2d(
      "../../results/data-" + run + "-dissociationFitPC["
        + str(params.timeSteps[i]) + ","
        + str(params.NpairCorrBins) + "].dat",
      "../data-" + run + "-dissociationFitPC",
      X=timeDelay,
      yRange=params.Rrange,
      options=opts2d)

  plc.print2d(
      "../../results/data-" + run + "-fluctuationsOverFinalStatePC["
        + str(params.timeSteps[i]) + ","
        + str(params.NpairCorrBins) + "].dat",
      "../data-" + run + "-fluctuationsOverFinalStatePC",
      X=timeDelay,
      yRange=params.Rrange,
      options=opts2d)


  del opts1d["xSlice"]
  del opts2d["xSlice"]
  plc.print1d(Rfiles, 
      "../data-" + run + "-RmeansFull",
      X=timeDelay[:-1],
      options=opts1d)
"""



##################################################
#####  Plotting Final State Fits to TD Data  #####
##################################################

colRange = [-3e-3, 3e-3]
for i,run in enumerate(runs):
  opts = {
    "xTitle"     : "Time [ps]",
    "labels"     : ["phenoxyRadical", "phenylRadical"]
    }

  timeDelay = np.fromfile("../../../mergeScans/results/timeDelays["
        + str(params.timeSteps[i] + 1) + "].dat", np.double)
 
  resFolder = "../../results/"
  """
  files = [resFolder + "sim-" + run\
              + "-offset_sMsFitCoeffsLinComb_Bins["\
              + str(params.timeSteps[i]) + "].dat","""
  files = [resFolder + "sim-" + run\
              + "-phenoxyRadical_sMsFitCoeffsLinComb_Bins["\
              + str(params.timeSteps[i]) + "].dat",
          resFolder + "sim-" + run\
              + "-phenylRadical_sMsFitCoeffsLinComb_Bins["\
              + str(params.timeSteps[i]) + "].dat"]
  """
  errFiles = [resFolder + "sim-" + run\
              + "-offset_sMsFitCoeffErrorsLinComb_Bins["\
              + str(params.timeSteps[i]) + "].dat","""
  errFiles = [resFolder + "sim-" + run\
              + "-phenoxyRadical_sMsFitCoeffErrorsLinComb_Bins["\
              + str(params.timeSteps[i]) + "].dat",
          resFolder + "sim-" + run\
              + "-phenylRadical_sMsFitCoeffErrorsLinComb_Bins["\
              + str(params.timeSteps[i]) + "].dat"]

  plc.print1d(files,
        "../sim-" + run + "-sMsFitFinalStateCoeffsFull",
        X=timeDelay[:-1],
        errors=errFiles,
        options=opts)

  opts["xSlice"] = [-0.125, maxX[i]]
  plc.print1d(files,
        "../sim-" + run + "-sMsFitFinalStateCoeffs",
        X=timeDelay[:-1],
        errors=errFiles,
        options=opts)


  data,_ = plc.importImage(mergeFolder + "data-"
          + run + "-sMsAzmAvgDiff["
          + str(params.timeSteps[i]) + "," 
          + str(params.NradAzmBins) + "].dat")
  fit,_ = plc.importImage("../../results/sim-"
          + run + "_sMsFinalStateFitLinComb_Bins["
          + str(params.timeSteps[i]) + "," 
          + str(params.NradAzmBins) + "].dat")

  opts = {
    "xTitle"     : r"Q [$\AA^{-1}$]",
    "labels"     : ["data", "fit"],
    "ySlice"     : [-0.9, 0.9]
    }
  for j in range(params.timeSteps[i]):
    plc.print1d(np.array([data[j,:], fit[j,:]]),
        "../data-" + run + "_fitLinComb_time-"
          + str(timeDelay[j]),
        options=opts,
        isFile=False)
