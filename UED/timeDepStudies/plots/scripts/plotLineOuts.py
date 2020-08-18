import numpy as np
import sys
import copy
sys.path.append('../../../plots/scripts')
sys.path.append('/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts')
from plotClass import plotCLASS
from plotParams import pltParams

import matplotlib.pyplot as plt

params = pltParams()

plc = plotCLASS()


runs = ["20180627_1551", "20180629_1630", "20180630_1925", "20180701_0746"]
runs = ["20180627_1551", "20180629_1630"]

Q = np.arange(params.NradAzmBins)*params.QrangeAzm[1]/params.NradAzmBins

optsDiff = {
    #"yLim"    : [-0.003, 0.003],
    #"yLim"    : [-1.5, 1.5],
    "xTitle"  : r"Q [$\AA^{-1}$]", 
    #"Qscale"  : Q,
    #"smooth"  : 1 
    }
optsCorr = {
    "yLim"    : [-0.009, 0.009],
    "xTitle"  : r"R [$\AA$]", 
    #"smooth"  : 7 
    }


###############################
#####  Line Outs in Time  #####
###############################

selectQ = [ [[1.75, 2.25], [3.1, 3.8], [4, 5], [5, 5.5]],
            [[1.2, 1.8], [2, 2.5], [2.5,3.5], [3.75,4.75], [5.5,6.5]]]
selectR = [ [[0.8, 1.4], [1.4, 2.0], [2.0, 2.75], [2.75, 3.75], [3.8, 4.75], [5, 5.5]],
            [[1, 1.5], [1.5, 2.2], [2.2, 2.9], [3, 4], [4, 5], [5, 6]]]

q = np.linspace(0, 1, params.NradAzmBins)*params.QrangeAzm[1]
r = np.linspace(0, 1, params.NpairCorrBins)*params.Rrange[1]
xlims = [-0.1, 1.5]
colors = ['k', 'r', 'b', 'y', 'g', 'cyan']
for i,run in enumerate(runs):

  times = np.fromfile("../../../mergeScans/results/timeDelays-"
      + run + "_bins[" + str(params.timeSteps[i] + 1) + "].dat", np.double)
  times -= times[1] - times[0]
  times = times[1:]
  optsDiff["labels"] = []
  for qv in selectQ[i]:
    optsDiff["labels"].append(
        "{} - {}".format(qv[0], qv[1]) + r" [$\AA^{-1}$]")
  optsCorr["labels"] = []
  for pc in selectR[i]:
    optsCorr["labels"].append(
        "{} - {}".format(pc[0], pc[1]) + r" [$\AA$]")


  #qInds = np.searchsorted(q, selectQ[i])
  #rInds = np.searchsorted(r, selectR[i])

  fileName = params.mergeResultFolder\
      + "/data-" + run + "-sMsAzmAvgDiff"\
      + "[" + str(params.timeSteps[i]) + ","\
      + str(params.NradAzmBins) + "].dat"
  """
  plc.printLineOut(fileName, 1, qInds,
      "../data-" + run + "_diffLO_time_full", 
      X=times, addNeighbors=True, options=optsDiff)
  """
  """
  dfrctnLOs, dfrctnErrLOs = plc.getRangeLineOut(
      fileName, 1, selectQ[i], q,
      errorFileName = params.mergeResultFolder + "/data-"\
        + run + "-sMsSEM["\
        + str(params.timeSteps[i]) + ","\
        + str(params.NradAzmBins) + "].dat")

  fig, ax = plt.subplots()
  for j,(p,e) in enumerate(zip(dfrctnLOs, dfrctnErrLOs)):
    ax.errorbar(times, p, yerr=e,
        color=colors[j], label=optsDiff["labels"][j])
  ax.legend()
  ax.set_xlim([times[0], times[-1]])
  fig.savefig("../data-" + run + "_diffLO_time_full.png")
  ax.set_xlim(xlims)
  fig.savefig("../data-" + run + "_diffLO_time.png")
  plt.close()
  """

  
  fileName = "../../results/data-"\
      + run + "_pairCorrOdd["\
      + str(params.timeSteps[i]) + ","\
      + str(params.NpairCorrBins) + "].dat"
  pairCorrLOs = plc.getRangeLineOut(
      fileName, 1, selectR[i], r)
  """
      errorFileName = params.mergeResultFolder + "/data-"\
        + run + "-pairCorrSEM["\
        + str(params.timeSteps[i]) + ","\
        + str(params.NpairCorrBins) + "].dat")
  """
  """
  plc.printLineOut(fileName, 1, rInds,
      "../data-" + run + "_pairCorrLO_time_full", 
      X=times, addNeighbors=True, options=optsCorr)
  """
  fig, ax = plt.subplots()
  #for p,e in zip(pairCorrLOs, pairCorrErrLOs):
  print("SIZES", len(colors), len(optsCorr["labels"]), len(pairCorrLOs))
  for j,p in enumerate(pairCorrLOs):
    ax.plot(times, p,
        color=colors[j], label=optsCorr["labels"][j])
  ax.legend()
  ax.set_xlim([times[0], times[-1]])
  fig.savefig("../data-" + run + "_pairCorrLO_time_full.png")
  ax.set_xlim(xlims)
  fig.savefig("../data-" + run + "_pairCorrLO_time.png")
  plt.close()


sys.exit(0)
##############################
#####  Line Outs in Q/R  #####
##############################

selectTimes = [ [-0.01, 0.25, 0.5, 3.75, 6.5],#[0, 0.5, 1, 4, 8],
                [-0.05, 0.1, 0.2, 0.9, 5],
                [0, 0.25, 0.5, 0.75, 1],
                [0, 0.25, 0.5, 0.75, 1]]

for i,run in enumerate(runs):

  optsDiff["labels"] = []
  optsCorr["labels"] = []
  for tm in selectTimes[i]:
    optsDiff["labels"].append(str(tm) + " ps")
    optsCorr["labels"].append(str(tm) + " ps")


  print("run", run)
  times = np.fromfile("../../../mergeScans/results/timeDelays-"
      + run + "_bins[" + str(params.timeSteps[i] + 1) + "].dat", np.double)

  timeInds = np.searchsorted(times, selectTimes[i])
  timeInds[timeInds>=times.shape[0]-1] = -1

  fileName = params.mergeResultFolder\
      + "/data-" + run + "-sMsAzmAvgDiff"\
      + "[" + str(params.timeSteps[i]) + "," + str(params.NradAzmBins) + "].dat"
  plc.printLineOut(fileName, 0, timeInds, "../data-" + run + "_diffLO", 
      xRange=params.QrangeAzm, options=optsDiff)
  
  fileName = "../../results/data-"\
      + run + "_pairCorrOdd["\
      + str(params.timeSteps[i]) + "," + str(params.NpairCorrBins) + "].dat"
  plc.printLineOut(fileName, 0, timeInds, "../data-" + run + "_pairCorrLO", 
      xRange=params.Rrange, options=optsCorr)

