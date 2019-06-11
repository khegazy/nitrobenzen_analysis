import numpy as np
import copy
import sys
sys.path.append('../../../plots/scripts')
sys.path.append('/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts')
from plotClass import plotCLASS
from plotParams import pltParams

params = pltParams()

plc = plotCLASS()


plotTsmeared = False
#runs = ["20180627_1551", "20180629_1630", "20180630_1925", "20180701_0746"]
runs = ["20180627_1551", "20180629_1630"]
maxX = [1.1, 1.5, 1.1, 1.1]
#maxX = [2, 1.1, 1.1, 1.1]
minX = [0, 0, -0.2, -0.2]
#minX = [0, -0.3, -0.2, -0.2]
smear = "0.025000"
mergeFolder = "/reg/ued/ana/scratch/nitroBenzene/mergeScans/"

selectTimes = [ [0.1, 2.1, 3, 6.5, 12],#[0, 0.5, 1, 4, 8],
                [0, 0.25, 0.5, 0.75, 1],
                [0, 0.25, 0.5, 0.75, 1],
                [0, 0.25, 0.5, 0.75, 1]]

#################################################
#####  Plotting time dependent diffraction  #####
#################################################
colRange = [[-4e-4, 4e-4], [-4e-4, 4e-4], [-3e-3, 3e-3], [-3e-3, 3e-3]]
#colRange = [[-3e-3, 3e-3], [-3e-3, 3e-3], [-3e-3, 3e-3], [-3e-3, 3e-3]]
#colRange = [[-7e-3, 7e-3], [-7e-3, 7e-3], [-7e-3, 7e-3], [-7e-3, 7e-3]]
#colRange = [-3e-3, 3e-3]
for i,run in enumerate(runs):
  opts = {
    "colorRange"  : colRange[i],
    "colorMap"    : 'seismic',
    #"colorTextSize" : 15,
    "xTitle"      : "Time [ps]",
    "yTitle"      : r"Q [$\AA^{-1}$]",
    "yRebin"      : 8,
    "yTicks"      : np.arange(int(params.QrangeAzm[-1]) + 1),
    #"xTitleSize"  : 18,
    #"yTitleSize"  : 18,
    #"xTickSize"   : 15,
    #"yTickSize"   : 15
    }


  timeDelay = np.fromfile("../../../mergeScans/results/timeDelays-"
        + run + "_bins[" + str(params.timeSteps[i] + 1) + "].dat", np.double)
 

  plc.print2d(mergeFolder + "data-" 
          + run + "-azmAvgDiff["
          + str(params.timeSteps[i]) 
          + "," + str(params.NradAzmBins) + "].dat",
        "../data-" + run + "-azmAvgDiffFull",
        X=timeDelay,
        yRange=params.QrangeAzm,
        options=opts)

  """
  plc.print2d("../../results/data-" 
          + run + "_azmAvgSubtractFinalState["
          + str(params.timeSteps[i]) 
          + "," + str(params.NradAzmBins) + "].dat",
        "../data-" + run + "-azmAvgSubtractFinalStateFull",
        X=timeDelay,
        yRange=params.QrangeAzm,
        options=opts)

  tdData, _  = plc.importImage(mergeFolder + "data-"
          + run + "-azmAvgDiff["
          + str(params.timeSteps[i]) 
          + "," + str(params.NradAzmBins) + "].dat")
  np.savetxt("X.txt", timeDelay, delimiter=" ")
  Qaxis = np.linspace(0, 1., tdData.shape[1])*params.QrangeAzm[1]
  np.savetxt("Qaxis.txt", Qaxis, delimiter=" ")
  np.savetxt("diffData.txt", tdData, delimiter=" ")
   
  plc.print2d("../../results/data-" 
          + run + "_sMsSubtractFinalState["
          + str(params.timeSteps[i]) 
          + "," + str(params.NradAzmBins) + "].dat",
        "../data-" + run + "-sMsSubtractFinalStateFull",
        X=timeDelay,
        yRange=params.QrangeAzm,
        options=opts)
  """

  if plotTsmeared:
    plc.print2d(mergeFolder + "data-"
            + run + "-tSmeared-" + smear + "-azmAvgDiff["
            + str(params.smearTimeSteps[i]) 
            + "," + str(params.NradAzmBins) + "].dat",
          "../data-" + run + "-tSmearedAzmAvgDiffFull",
          xRange=[timeDelay[0], timeDelay[-1]],
          yRange=params.QrangeAzm,
          options=opts)

  opts["xSlice"] = [minX[i], maxX[i]]
  plc.print2d(mergeFolder + "data-"
          + run + "-azmAvgDiff["
          + str(params.timeSteps[i]) 
          + "," + str(params.NradAzmBins) + "].dat",
        "../data-" + run + "-azmAvgDiff",
        X=timeDelay,
        yRange=params.QrangeAzm,
        options=opts)


  """
  data,_ = plc.importImage(mergeFolder + "data-"
          + run + "-azmAvgDiff["
          + str(params.timeSteps[i]) 
          + "," + str(params.NradAzmBins) + "].dat")
  ref1 = np.fromfile("/reg/ued/ana/scratch/nitroBenzene/mergeScans/data-20180627_1551_reference-1530000_bins[555].dat", np.double)
  ref2 = np.fromfile("/reg/ued/ana/scratch/nitroBenzene/mergeScans/data-20180627_1551_reference-1530100_bins[555].dat", np.double)
  ref1 = np.reshape(ref1, (1,-1))
  ref2 = np.reshape(ref2, (1,-1))
  refs = np.concatenate((ref1, ref2), axis=0)
  allData = np.concatenate((refs, data), axis=0)
  allTime = np.insert(timeDelay, 0, -0.075)
  allTime = np.insert(allTime, 0, -0.15)
  print(allTime)
  opts["xSlice"] = [-0.15, maxX[i]]
  plc.print2d(allData, "ComparingReference", 
      X=allTime, 
      yRange=params.QrangeAzm,
      isFile=False,
      options=opts)
  sys.exit()
  """

  """
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
        """
 
  if plotTsmeared:
    plc.print2d(mergeFolder + "data-"
            + run + "-tSmeared-" + smear + "-azmAvgDiff["
            + str(params.smearTimeSteps[i]) 
            + "," + str(params.NradAzmBins) + "].dat",
          "../data-" + run + "-tSmearedAzmAvgDiff",
          xRange=[timeDelay[0], timeDelay[-1]],
          yRange=params.QrangeAzm,
          options=opts)


td27, _ = plc.importImage(
    params.mergeResultFolder + "data-"
    + runs[0] + "-sMsAzmAvgDiff["
    + str(params.timeSteps[0])
    + "," + str(params.NradAzmBins) + "].dat")
timeDelay27 = np.fromfile(
      "../../../mergeScans/results/timeDelays-20180627_1551_bins[" 
    + str(params.timeSteps[0] + 1) + "].dat", np.double)

td29, _ = plc.importImage(
    params.mergeResultFolder + "data-"
    + runs[1] + "-sMsAzmAvgDiff["
    + str(params.timeSteps[1])
    + "," + str(params.NradAzmBins) + "].dat")
#td29 -= np.reshape(np.mean(td29[:3,:], axis=0), (1,-1))
timeDelay29 = np.fromfile(
    "../../../mergeScans/results/timeDelays-20180629_1630_bins["
    + str(params.timeSteps[1] + 1) + "].dat", np.double)

opts = {
  "xTitle"  : r"Q [$\AA^{-1}$]",
  "ySlice"  : [-0.7, 0.5],
  "xSlice"  : [0.5, 8],
  "xRebin"  : 5,
  "xTicks"  : np.arange(int(params.QrangeAzm[-1]) + 1)
}

plc.print1d(td29[:3,:],
    "../data-" + runs[1]
    + "_sMsCompareLO_delay-refs",
    xRange=params.QrangeAzm,
    isFile=False,
    options=opts)

opts["labels"] = ["20180627_1551", "20180629_1630"]
for i,tm in enumerate(timeDelay29):
  if tm < 0 or i == td29.shape[0]:
    continue
  ind27 = np.argmin(np.abs(timeDelay27 - tm))
  plc.print1d(np.array([td27[ind27,:], td29[i,:]]),
      "../data-" + runs[0] + "-" + runs[1]
      + "_sMsCompareLO_delay-" + str(tm),
      xRange=params.QrangeAzm,
      isFile=False,
      options=opts)
print("PASSED")

######################################################
#####  Plotting time dependent pair correlation  #####
######################################################
print("Plotting pair corrs")
colRange = [[-9e-3, 9e-3], [-9e-3, 9e-3], [-5e-2, 5e-2], [-5e-2, 5e-2]]
#colRange = [-6e-2, 6e-2]
for i,run in enumerate(runs):
  print("run",run)
  opts = {
    "colorRange" : colRange[i],
    "colorMap"   : 'seismic',
    #"colorTextSize" : 15,
    "xTitle"     : "Time [ps]",
    "yTitle"     : r"R [$\AA$]",
    "yTicks"  : np.arange(int(params.Rrange[-1]) + 1),
    #"xTitleSize"  : 18,
    #"yTitleSize"  : 18,
    #"xTickSize"   : 15,
    #"yTickSize"   : 15
    #"interpolate": [200, 100]
    }


  timeDelay = np.fromfile("../../../mergeScans/results/timeDelays-" 
        + run + "_bins[" + str(params.timeSteps[i] + 1) + "].dat", np.double)
  
  plc.print2d("../../results/data-" + run + "_pairCorrOdd["
          + str(params.timeSteps[i]) + "," 
          + str(params.NpairCorrBins) + "].dat",
        "../data-" + run + "_pairCorrFull",
        X=timeDelay,
        yRange=params.Rrange,
        options=opts)

  

  """
  plc.print2d("../../results/data-" + run + "_pairCorrSubtractFinalState["
          + str(params.timeSteps[i]) + "," 
          + str(params.NpairCorrBins) + "].dat",
        "../data-" + run + "_pairCorrSubtractFinalStateFull",
        X=timeDelay,
        yRange=params.Rrange,
        options=opts)
  """

  if plotTsmeared:
    plc.print2d("../../results/data-" + run + "_tSmeared_pairCorrOdd["
            + str(params.smearTimeSteps[i]) + "," 
            + str(params.NpairCorrBins) + "].dat",
          "../data-" + run + "_tSmearedPairCorrFull",
          xRange=[timeDelay[0], timeDelay[-1]],
          yRange=params.Rrange,
          options=opts)


  opts["xSlice"] = [minX[i], maxX[i]]
  plc.print2d("../../results/data-" + run + "_pairCorrOdd["
          + str(params.timeSteps[i]) + "," 
          + str(params.NpairCorrBins) + "].dat",
        "../data-" + run + "_pairCorr",
        X=timeDelay,
        yRange=params.Rrange,
        options=opts)

  """
  plc.print2d("../../results/data-" + run + "_pairCorrSubtractFinalState["
          + str(params.timeSteps[i]) + "," 
          + str(params.NpairCorrBins) + "].dat",
        "../data-" + run + "_pairCorrSubtractFinalState",
        X=timeDelay,
        yRange=params.Rrange,
        options=opts)
  """

  if plotTsmeared:
    plc.print2d("../../results/data-" + run + "_tSmeared_pairCorrOdd["
            + str(params.smearTimeSteps[i]) + "," 
            + str(params.NpairCorrBins) + "].dat",
          "../data-" + run + "_tSmearedPairCorr",
          xRange=[timeDelay[0], timeDelay[-1]],
          yRange=params.Rrange,
          options=opts)

  tdData, _  = plc.importImage("../../results/data-" + run + "_pairCorrOdd["
          + str(params.timeSteps[i]) + "," 
          + str(params.NpairCorrBins) + "].dat")
  Raxis = np.linspace(0, 1., tdData.shape[1])*params.Rrange[1]
  np.savetxt("Raxis.txt", Raxis, delimiter=" ")
  np.savetxt("pCorrData.txt", tdData, delimiter=" ")

  # Ratios
  range1 = [int(params.NpairCorrBins*0.9/params.Rrange[1]), 
      int(params.NpairCorrBins*1.5/params.Rrange[1])]
  range2 = [int(params.NpairCorrBins*2.1/params.Rrange[1]), 
      int(params.NpairCorrBins*2.9/params.Rrange[1])]
  tdTempData = copy.copy(tdData)
  tdTempData[:,range2[1]:] = 0
  tdTempData[:,range1[1]:range2[0]] = 0
  tdTempData[:,:range1[0]] = 0

  plc.print2d(tdTempData,
      "../data-" + run + "_pairCorr_ratioRegions-2div1.5",
      X=timeDelay,
      yRange=params.Rrange,
      isFile=False,
      options=opts)

  ratio1 = np.sum(tdData[:,range2[0]:range2[1]], axis=1)/np.sum(tdData[:,range1[0]:range1[1]], axis=1)
  finState = np.mean(ratio1[-4:])
  opts["text"] = [0.1, 8, "Final State: " + str(finState)]
  opts["line"] = [[opts["xSlice"], [finState, finState], "k", 1]]
  plc.print1d(ratio1,
      "../data-" + run + "_pairCorr_ratio-2div1.5",
      X=timeDelay[1:],
      isFile=False,
      options=opts)

  del opts["yTitle"]
  del opts["xSlice"]
  opts["text"] = [8, 8, "Final State: " + str(finState)]
  opts["line"] = [[[timeDelay[1], timeDelay[-1]], [finState, finState], "k", 1]]
  plc.print1d(ratio1,
      "../data-" + run + "_pairCorrFull_ratio-2div1.5",
      X=timeDelay[1:],
      isFile=False,
      options=opts)



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
  "yTicks"  : np.arange(int(params.Rrange[-1]) + 1)
  }

opts["xSlice"] = xZoomFine
plc.print2d("../../results/"
        "sim-nitrobenzene-dissociation-phenyl-N2O_pairCorrOdd["
        +NdissTimeSteps+",369].dat",
      "../sim-nitrobenzene-dissociation-phenyl-N2O_pairCorr",
      X=dissTimeDelay,
      yRange=params.Rrange,
      options=opts)
 
plc.print2d("../../results/"
        "sim-nitrobenzene-dissociation-phenyl-N2O_timeSmoothed_pairCorrOdd["
        +NdissTimeSteps+",369].dat",
      "../sim-nitrobenzene-dissociation-phenyl-N2O_timeSmoothed_pairCorr",
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

plc.print2d("../../results/"
        "sim-nitrobenzene-dissociation-phenyl-N2O_timeSmoothed_pairCorrOdd["
        +NdissTimeSteps+",369].dat",
      "../sim-nitrobenzene-dissociation-phenyl-N2O_timeSmoothed_pairCorrFull",
      X=dissTimeDelay,
      yRange=params.Rrange,
      options=opts)

"""
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
"""


diffColorRange = [-2e-2, 2e-2]
smsColorRange = [-6e-1, 6e-1]
opts = {
  "colorRange" : smsColorRange,
  "colorMap"   : 'seismic',
  "xTitle"     : "Time [ps]",
  "yTitle"     : r"Q [$\AA^{-1}$]",
  "yTicks"  : np.arange(int(params.QrangeAzm[-1]) + 1)
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

plc.print2d(timeDepSimDir
        + "dissociation_phenyl-N2O_azmAvgSMS_timeSmoothed_Qmax-12.376500_Ieb-5.000000"
        + "_scrnD-4.000000_elE-3700000.000000_Bins["
        + NdissTimeSteps + ",555].dat",
      "../sim-dissociation-phenyl-N2O-azmAvgSMS_timeSmoothed",
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

plc.print2d(timeDepSimDir
        + "dissociation_phenyl-N2O_azmAvg_timeSmoothed_Qmax-12.376500_Ieb-5.000000"
        + "_scrnD-4.000000_elE-3700000.000000_Bins["
        + NdissTimeSteps + ",555].dat",
      "../sim-dissociation-phenyl-N2O-azmAvg_timeSmoothed",
      X=dissTimeDelay,
      yRange=params.QrangeAzm,
      options=opts)

"""
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

  opts1d["xSlice"] = [0, maxX[i]]
  opts2d["xSlice"] = [0, maxX[i]]
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

print("exiting before plotting td fits")
sys.exit(0)
##################################################
#####  Plotting Final State Fits to TD Data  #####
##################################################
print("final state td fit")
colRange = [-3e-3, 3e-3]
for i,run in enumerate(runs):
  opts = {
    "xTitle"     : "Time [ps]",
    "labels"     : ["phenoxyRadical", "phenylRadical"]
    }

  timeDelay = np.fromfile("../../../mergeScans/results/timeDelays-" 
        + run + "_bins[" + str(params.timeSteps[i] + 1) + "].dat", np.double)
 
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

  opts["xSlice"] = [0, maxX[i]]
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
