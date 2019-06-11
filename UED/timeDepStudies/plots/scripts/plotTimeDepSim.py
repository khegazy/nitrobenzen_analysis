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
runs = ["20180627_1551", "20180629_1630", "20180630_1925", "20180701_0746"]
#runs = ["20180627_1551"]
maxX = [1.1, 1.1, 1.1, 1.1]
#maxX = [2, 1.1, 1.1, 1.1]
minX = [0, 0, -0.2, -0.2]
#minX = [-0.125, -0.3, -0.2, -0.2]
smear = "0.025000"
mergeFolder = "/reg/ued/ana/scratch/nitroBenzene/mergeScans/"

selectTimes = [ [0.1, 2.1, 3, 6.5, 12],#[0, 0.5, 1, 4, 8],
                [0, 0.25, 0.5, 0.75, 1],
                [0, 0.25, 0.5, 0.75, 1],
                [0, 0.25, 0.5, 0.75, 1]]

#################################################
#####  Plotting time dependent diffraction  #####
#################################################
colRange = [[-4e-4, 4e-4], [-3e-3, 3e-3], [-3e-3, 3e-3], [-3e-3, 3e-3]]
#colRange = [[-3e-3, 3e-3], [-3e-3, 3e-3], [-3e-3, 3e-3], [-3e-3, 3e-3]]
#colRange = [[-7e-3, 7e-3], [-7e-3, 7e-3], [-7e-3, 7e-3], [-7e-3, 7e-3]]
#colRange = [-3e-3, 3e-3]


########################################
#####  Plotting Phynel Simulation  #####
########################################


NdissTimeSteps = "400"
NrotTimeSteps = "800"
Nrot90TimeSteps = "80"
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
rot90TimeDelay = np.fromfile(
      timeDepSimDir + "rotate90_nitrobenzene_timeDelays["
      + Nrot90TimeSteps + "].dat", np.double)
opts = {
  "colorRange" : [-2e-1, 2e-1],
  "colorMap"   : 'seismic',
  "colorTextSize" : 15,
  "xTitle"     : "Time [ps]",
  "yTitle"     : r"R [$\AA$]",
  "xTitleSize"  : 18,
  "yTitleSize"  : 18,
  "xTickSize"   : 15,
  "yTickSize"   : 15
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

opts["xSlice"] = [0, 0.2]
"""
plc.print2d("../../results/"
        "sim-nitrobenzene-rotate90_nitrobenzene_pairCorrOdd["
        +Nrot90TimeSteps+",369].dat",
      "../sim-rotate90_nitrobenzene_pairCorrFull",
      X=rot90TimeDelay,
      yRange=params.Rrange,
      options=opts)
      """

plc.print2d("../../results/"
        "sim-nitrobenzene-rotate90_nitrobenzene_timeSmoothed_pairCorrOdd["
        +Nrot90TimeSteps+",369].dat",
      "../sim-rotate90_nitrobenzene_timeSmoothed_pairCorrFull",
      X=rot90TimeDelay,
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


diffColorRange = [-1e-2, 1e-2]
smsColorRange = [-6e-1, 6e-1]
opts = {
  "colorRange" : smsColorRange,
  "colorMap"   : 'seismic',
  "colorTextSize" : 15,
  "xTitle"     : "Time [ps]",
  "yTitle"     : r"Q [$\AA^{-1}$]",
  "xTitleSize"  : 18,
  "yTitleSize"  : 18,
  "xTickSize"   : 15,
  "yTickSize"   : 15
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

opts["xSlice"] = [0, 0.2]
opts["colorRange"] = diffColorRange
plc.print2d(timeDepSimDir
        + "rotate90_nitrobenzene_azmAvg_Qmax-12.376500_Ieb-5.000000"
        + "_scrnD-4.000000_elE-3700000.000000_Bins["
        + Nrot90TimeSteps + ",555].dat",
      "../sim-rotate90_nitrobenzene-azmAvg",
      X=rot90TimeDelay,
      yRange=params.QrangeAzm,
      options=opts)

plc.print2d(timeDepSimDir
        + "rotate90_nitrobenzene_azmAvg_timeSmoothed_Qmax-12.376500_Ieb-5.000000"
        + "_scrnD-4.000000_elE-3700000.000000_Bins["
        + Nrot90TimeSteps + ",555].dat",
      "../sim-rotate90_nitrobenzene-azmAvg_timeSmoothed",
      X=rot90TimeDelay,
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


