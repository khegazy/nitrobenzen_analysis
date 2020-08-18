import numpy as np
import sys
sys.path.append('../../../plots/scripts')
sys.path.append('/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts')
from plotClass import plotCLASS
from plotParams import pltParams
import matplotlib.pyplot as plt

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


startQ = 1.25 
endQ = 2

start = startQ*555/12.3
end   = endQ*555/12.3

for i,run in enumerate(runs):

  print("run", run)
  times = np.fromfile("../../../mergeScans/results/timeDelays-" + run + "_bins["
      + str(timeSteps[i] + 1) + "].dat", np.double)
  times = times[:-1]


  fileName = params.mergeResultFolder\
      + "/data-" + run + "-azmAvgDiff"\
      + "[" + str(timeSteps[i]) + "," + str(params.NradAzmBins) + "].dat"
  image,shape = plc.importImage(fileName)

  inp = np.mean(image[:18,start:end], axis=1)
  plt.plot(times[:18], inp)

  print(np.mean(image[:17,start:end]))

  plt.savefig("../temporalLO_" +run+ "_"+str(startQ) + "_" + str(endQ) + ".png")


