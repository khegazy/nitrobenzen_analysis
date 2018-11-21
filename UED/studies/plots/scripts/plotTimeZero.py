import glob
import numpy as np
import sys
import os
import threading
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
sys.path.append('../../../plots/scripts')
sys.path.append('/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts')
from plotClass import plotCLASS
from plotParams import pltParams


params = pltParams()
plc = plotCLASS()

runNames = ["20180627_1551"] #, "20180629_1630", "20180630_1925", "20180701_0746"]
for i,run in enumerate(runNames):

  timeDelay = np.fromfile("../../../mergeScans/results/timeDelays["
        + str(params.timeSteps[i] + 1) + "].dat", np.double)

  refVals = np.fromfile("../../results/data-"
        + run + "-referenceQmeans"
        + "-Bins[3].dat", dtype=np.double)


  mean1, _ = plc.importImage("../../results/data-" + run 
              + "-Qmean2.000000-3.000000-Bins["
              + str(params.timeSteps[i]) + "].dat")
  mean2, _ = plc.importImage("../../results/data-" + run 
              + "-Qmean3.000000-3.500000-Bins["
              + str(params.timeSteps[i]) + "].dat")
  mean3, _ = plc.importImage("../../results/data-" + run 
              + "-Qmean3.750000-5.000000-Bins["
              + str(params.timeSteps[i]) + "].dat")
  ratio = (mean3+refVals[2])/(mean2+refVals[1])
 
  opts = {
      "xTitle"  : "Time [ps]",
      "labels"  : ["2-3", "3-3.5", "3.75-5"]
      }

  plc.print1d(np.vstack((mean1, mean2, mean3)),
      "../timeZero/signalTurnOnFull",
      X=timeDelay[:-1],
      isFile=False,
      options=opts)

  opts["xSlice"] = [-0.3, 1]
  plc.print1d(np.vstack((mean1, mean2, mean3)),
      "../timeZero/signalTurnOn",
      X=timeDelay[:-1],
      isFile=False,
      options=opts)

  del opts["labels"]
  plc.print1d(ratio,
      "../timeZero/signalRatioTurnOn",
      X=timeDelay[:-1],
      isFile=False,
      options=opts)


  for ir in range(1, 101):

    refVals = np.fromfile("../../results/data-"
        + run + "-referenceQmeans-scanLines-"
        + str(ir) + "-" + str(ir+19) + "-Bins[3].dat", dtype=np.double)

    mean1, _ = plc.importImage("../../results/data-" + run 
                + "-Qmean2.000000-3.000000"
                + "-scanLines-" + str(ir) + "-" + str(ir+19)
                + "-Bins[" + str(params.timeSteps[i]) + "].dat")
    mean2, _ = plc.importImage("../../results/data-" + run 
                + "-Qmean3.000000-3.500000"
                + "-scanLines-" + str(ir) + "-" + str(ir+19)
                + "-Bins[" + str(params.timeSteps[i]) + "].dat")
    mean3, _ = plc.importImage("../../results/data-" + run 
                + "-Qmean3.750000-5.000000"
                + "-scanLines-" + str(ir) + "-" + str(ir+19)
                + "-Bins[" + str(params.timeSteps[i]) + "].dat")
    ratio = (mean3+refVals[2])/(mean2+refVals[1])
   
    opts = {
        "xTitle"  : "Time [ps]",
        "xSlice"  : [-0.3, 1]
        }
    plc.print1d(ratio,
        "../timeZero/signalRatioTurnOn-scanLines"
          + str(ir)+"-"+str(ir+19),
        X=timeDelay[:-1],
        isFile=False,
        options=opts)

    opts["labels"] = ["2-3", "3-3.5", "3.75-5"],
    plc.print1d(np.vstack((mean1, mean2, mean3)),
        "../timeZero/signalTurnOn-scanLines"
          + str(ir)+"-"+str(ir+19),
        X=timeDelay[:-1],
        isFile=False,
        options=opts)


