import numpy as np
import sys
sys.path.append('../../../plots/scripts')
from plotClass import plotCLASS
from plotParams import pltParams

params = pltParams()

plc = plotCLASS()


qBins = [85,87,88,90]

runs = ["20180627_1551", "20180629_1630"] #, "20180630_1925", "20180701_0746"]
timeSteps = [29, 18, 19, 19]

Q = np.arange(params.NradAzmBins)*params.QrangeAzm[1]/params.NradAzmBins

optsDiff = {
    "xLim"    : [-0.25, 1.1],
    "xTitle"  : r"time [ps]", 
    }
optsCorr = {
    "yLim"    : [-0.2, 0.15],
    "xTitle"  : r"R [$\AA$]", 
    #"smooth"  : 7 
    }

"""
optsDiff["labels"] = []
optsCorr["labels"] = []
for iq in qBins:
  optsDiff["labels"].append(str(iq*0.0223) + r" $\AA^{-1}$")
  optsCorr["labels"].append(str(iq*0.0223) + r" $\AA^{-1}$")
  """

for i,run in enumerate(runs):

  print("run", run)
  times = np.fromfile("../../../mergeScans/results/timeDelays["
      + str(timeSteps[i] + 1) + "].dat", np.double)
  times = times[:-1]

  if run is "20180627_1551":
    optsDiff["yLim"] = [-0.009, 0.008]
  elif run is "20180629_1630":
    optsDiff["yLim"] = [-0.003, 0.007]

  fileName = params.mergeResultFolder\
      + "/data-" + run + "-azmAvgDiff"\
      + "[" + str(timeSteps[i]) + "," + str(params.NradAzmBins) + "].dat"
  plc.printLineOut(fileName, 1, qBins, "../data-" + run + "-timeLO", 
      X=times, options=optsDiff)

  """
  fileName = "../../results/data-"\
      + run + "-pairCorrOdd["\
      + str(timeSteps[i]) + "," + str(params.NpairCorrBins) + "].dat"
  plc.printLineOut(fileName, 0, timeInds, "../data-" + run + "-pairCorrLO", 
      xRange=params.Rrange, options=optsCorr)
  """
