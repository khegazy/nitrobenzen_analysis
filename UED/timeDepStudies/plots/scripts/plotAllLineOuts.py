import numpy as np
import sys
sys.path.append('../../../plots/scripts')
from plotClass import plotCLASS
from plotParams import pltParams

params = pltParams()

plc = plotCLASS()

runs = ["20180629_1630", "20180627_1551", "20180630_1925", "20180701_0746"]
timeSteps = [18, 29, 19, 19]

opts = {
    "yLim"    : [-0.1, 0.1]
    }
for i,run in enumerate(runs):

  inds = np.arange(timeSteps[0])
  fileName = params.mergeResultFolder\
      + "/data-" + run + "-sMsAzmAvgDiff"\
      + "[" + str(timeSteps[i]) + "," + str(params.NradAzmBins) + "].dat"
  plc.printLineOut(fileName, 0, inds, "../data-" + run + "-diffLO", 
      xRange=params.QrangeAzm, samePlot=False, options=opts)
