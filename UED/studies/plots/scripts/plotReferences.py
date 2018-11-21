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

  reference = np.fromfile("../../results/data-"
        + run + "-referenceQmeans"
        + "-Bins[3].dat", dtype=np.double)

  opts = {
      "xTitle"  : r"Q [$\AA^{-1}$]",
      }

  fileName = "/reg/ued/ana/scratch/nitroBenzene/mergeScans/data-"\
              + run + "-referenceAzm[" + str(params.NradAzmBins) + "].dat"
  avgReference,_ = plc.importImage(fileName)

  plc.print1d(avgReference,
      "../references/totalReference-" + run,
      xRange=params.QrangeAzm,
      isFile=False,
      options=opts)


  for ir in range(1, 101):

    fileName = "/reg/ued/ana/scratch/nitroBenzene/scanSearch/size20/data-"\
              + run + "-scanLines"\
              + str(ir) + "-" + str(ir+19)\
              + "-referenceAzm[" + str(params.NradAzmBins) + "].dat"

    reference,_ = plc.importImage(fileName)
    plotRef   = reference - avgReference

    opts = {
        "xTitle"  : r"Q [$\AA^{-1}$]",
        "ySlice"  : [-0.05, 0.05]
        }
    plc.print1d(plotRef,
        "../references/reference-" + run + "-scanLines"
          + str(ir)+"-"+str(ir+19),
        xRange=params.QrangeAzm,
        isFile=False,
        options=opts)

