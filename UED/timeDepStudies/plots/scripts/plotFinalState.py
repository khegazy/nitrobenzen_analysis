import numpy as np
import sys
sys.path.append('../../../plots/scripts')
sys.path.append('/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts')
from plotClass import plotCLASS
from plotParams import pltParams

params = pltParams()

plc = plotCLASS()


#runs = ["20180629_1630", "20180627_1551", "20180630_1925", "20180701_0746"]
runs = ["20180627_1551"]
timeSteps = [29, 18, 19, 19]
maxX = [2, 1.1, 1.1, 1.1]
scale = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]

opts = {
  "xTitle"     : r"Q [$\AA^{-1}$]",
  }

plc.print1d(["/reg/ued/ana/scratch/nitroBenzene/simulations/phenoxyRadical_sMsFinalState["
    + str(params.NradAzmBins) + "].dat"],
    "../sim-phenoxyRadical_sMsFinalState",
    xRange=params.QrangeAzm,
    options=opts)

opts = {
  "xTitle"     : r"R [$\AA$]",
  }

plc.print1d(["../../results/sim-nitrobenzenephenoxyRadicalFinal-pairCorrOdd["
    + str(params.NpairCorrBins) + "].dat"],
    "../sim-nitrobenzenephenoxyRadicalFinal-pairCorrOdd",
    xRange=params.Rrange,
    options=opts)


######################################################
#####  Plotting time dependent pair correlation  #####
######################################################

colRange = [-2e-1, 2e-1]#, [-1e-2, 1e-2], [-1e-2, 1e-2], [-1e-2, 1e-2]]
for i,run in enumerate(runs):
  for scl in scale:
    opts = {
      "colorRange" : colRange,
      "xTitle"     : "Time [ps]",
      "yTitle"     : r"R [$\AA$]",
      #"interpolate": [200, 100]
      }

    timeDelay = np.fromfile("../../../mergeScans/results/timeDelays["
          + str(timeSteps[i] + 1) + "].dat", np.double)
    
    plc.print2d("../../results/data-" + run + "-lowQscale-"
          + "%.6f" %(scl) + "-pairCorrOdd["
          + str(timeSteps[i]) + "," + str(params.NpairCorrBins) + "].dat",
          "../data-" + run + "-lowQscale-" + str(scl),
          X=timeDelay,
          yRange=params.Rrange,
          options=opts)

    opts["xSlice"] = [-0.3, maxX[i]]
    plc.print2d("../../results/data-" + run + "-lowQscale-"
          + "%.6f" %(scl) + "-pairCorrOdd["
          + str(timeSteps[i]) + "," + str(params.NpairCorrBins) + "].dat",
          "../data-" + run + "-lowQfullScale-" + str(scl),
          X=timeDelay,
          yRange=params.Rrange,
          options=opts)

files = ["../../results/sim-phenoxyRadical-pairCorrOdd[" + str(params.NpairCorrBins) + "].dat"]
plc.print1d(files,
    "../sim-phenoxyRadical-pairCorrDiff",
    xRange=params.Rrange)
