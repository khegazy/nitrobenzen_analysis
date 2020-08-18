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


for i,run in enumerate(runs):

  timeDelay = np.fromfile("../../../mergeScans/results/timeDelays-"
     +run + "_bins[" + str(params.timeSteps[i] + 1) + "].dat", np.double)


  dfrctnRanges = [[1.25, 2.25], [2, 3], [3,4], [4, 5.5], [6, 7]]
  dfrctnLOs, dfrctnErrLOs = plc.getRangeLineOut(mergeFolder + "data-"
      + run + "-azmAvgDiff["
      + str(params.timeSteps[i])
      + "," + str(params.NradAzmBins) + "].dat",
    1,
    dfrctnRanges,
    np.linspace(0, 1, params.NradAzmBins)*params.QrangeAzm[-1],
    errorFileName = mergeFolder + "data-"
        + run + "-azmAvgSEM["
        + str(params.timeSteps[i]) + ","
        + str(params.NradAzmBins) + "].dat")
 

  pCorrRanges = [[1.1, 1.5], [2, 2.75], [4, 4.5]]
  pCorrLOs, pCorrErrLOs = plc.getRangeLineOut("../../results/data-"
          + run + "_pairCorrOdd["
          + str(params.timeSteps[i]) + ","
          + str(params.NpairCorrBins) + "].dat",
        1,
        pCorrRanges,
        np.linspace(0, 1, params.NpairCorrBins)*params.Rrange[-1],
        errorFileName = mergeFolder + "data-"
            + run + "-pairCorrSEM["
            + str(params.timeSteps[i]) + ","
            + str(params.NpairCorrBins) + "].dat")

