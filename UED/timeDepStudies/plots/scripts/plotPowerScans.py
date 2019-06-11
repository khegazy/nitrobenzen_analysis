import numpy as np
import sys
sys.path.append('../../../plots/scripts')
sys.path.append('/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts')
from plotClass import plotCLASS
from plotParams import pltParams

params = pltParams()

plc = plotCLASS()


runs = ["20180627_PowerScan"]
throttles = ["48.000000","49.000000","50.000000","51.000000","52.000000","53.000000","54.000000","55.000000"]

#################################################
#####  Plotting time dependent diffraction  #####
#################################################
for i,run in enumerate(runs):
  for j,throttle in enumerate(throttles):
    opts = {
      "xTitle" : r"Q [$\AA^{-1}$]",
      "ySlice" : [-0.025, 0.025]
      }

    plc.print1d(["/reg/ued/ana/scratch/nitroBenzene/mergeScans/data-" 
          + run + "-throttle-"
          + throttle + "-azmAvgDiff["
          + str(params.NradAzmBins) + "].dat"],
          "../data-" + run 
          + "-throttle-" + throttle
          + "-azmAvgDiff",
          xRange=params.QrangeAzm,
          options=opts)


