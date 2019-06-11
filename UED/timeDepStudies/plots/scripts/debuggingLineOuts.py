import numpy as np
import sys
sys.path.append('../../../plots/scripts')
from plotClass import plotCLASS
from plotParams import pltParams

params = pltParams()

plc = plotCLASS()


selectTimes = [ [0.4, 0.45, 0.55], 
                [],
                [],
                []]

runs = ["20180627_1551", "20180629_1630", "20180630_1925", "20180701_0746"]
timeSteps = [29, 18, 19, 19]

Q = np.arange(params.NradAzmBins)*params.QrangeAzm[1]/params.NradAzmBins

optsDiff = {
    "yLim"    : [-0.03, 0.02],
    "xTitle"  : r"Q [$\AA^{-1}$]", 
    "Qscale"  : Q,
    "smooth"  : 1 
    }
optsCorr = {
    "yLim"    : [-0.2, 0.15],
    "xTitle"  : r"R [$\AA$]", 
    #"smooth"  : 7 
    }

for i,run in enumerate(runs):

  optsDiff["labels"] = []
  optsCorr["labels"] = []
  for tm in selectTimes[i]:
    optsDiff["labels"].append(str(tm) + " ps")
    optsCorr["labels"].append(str(tm) + " ps")


  print("run", run)
  times = np.fromfile("../../../mergeScans/results/timeDelays["
      + str(timeSteps[i] + 1) + "].dat", np.double)

  timeInds = np.searchsorted(times, selectTimes[i])
  timeInds[timeInds>=times.shape[0]-1] = -1
  print(timeInds)

  fileName = params.mergeResultFolder\
      + "/data-" + run + "-azmAvgDiff"\
      + "[" + str(timeSteps[i]) + "," + str(params.NradAzmBins) + "].dat"
  plc.printLineOut(fileName, 0, timeInds, "../debugData-" + run + "-diffLO", 
      xRange=params.QrangeAzm, options=optsDiff)
  
  fileName = "../../results/data-"\
      + run + "-pairCorrOdd["\
      + str(timeSteps[i]) + "," + str(params.NpairCorrBins) + "].dat"
  plc.printLineOut(fileName, 0, timeInds, "../debugData-" + run + "-pairCorrLO", 
      xRange=params.Rrange, options=optsCorr)
