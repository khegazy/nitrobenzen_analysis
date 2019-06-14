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

runNames = "20180629_1630"
stagePos = ["1530000", "1530500", "1542350", "1542450", "1542550", "1542650"]
stagePos = ["1530000", "1530500", "1542450", "1542550", "1542650"]
stagePos = ["1530000", "1530500", "1542450", "1542650"]

cuts = {
    "1530500" : [[1,2]],
    "1530000" : [[5.5, 6.5]],
    "1542450" :[[4.6, 5.2]]
    }

atmDiff = np.fromfile(
    "/reg/ued/ana/scratch/nitroBenzene/simulations/nitrobenzene_atmDiffractionPatternLineOut_Qmax-12.376500_Ieb-5.000000_scrnD-4.000000_elE-3700000.000000_Bins[555].dat", np.double)

fullReference = np.fromfile(
    "/reg/ued/ana/scratch/nitroBenzene/mergeScans/data-20180629_1630-azmReference_r" +
        "12"+
        "_t1234" +
        "_bins[" + str(params.NradAzmBins) + "].dat", np.double);

singleRefs = []
sumReference = np.zeros(params.NradAzmBins, float)
scale = 250/(atmDiff*(1+np.arange(params.NradAzmBins)))
for stg in stagePos:
  image = np.fromfile(
      "/reg/ued/ana/scratch/nitroBenzene/mergeScans/data-20180629_1630_reference-" +
        stg + "_bins[" + str(params.NradAzmBins) + "].dat", np.double)

  if stg in cuts:
    for cts in cuts[stg]:
      ind1 = int(params.NradAzmBins*cts[0]/params.QrangeAzm[1])
      ind2 = int(params.NradAzmBins*cts[1]/params.QrangeAzm[1])
      image[ind1:ind2] = np.nan

  singleRefs.append(image)

singleRefs = np.array(singleRefs)
meanReference = np.nanmean(singleRefs, axis=0)
singleRefs -= np.reshape(meanReference, (1,-1))
singleRefs *= scale

opts = {
    "xTitle"  : r"Q [$\AA^{-1}$]",
    "ySlice"  : [-0.015, 0.015],
    "labels"  : stagePos
    }
plc.print1d(singleRefs,
    "../references/referenceCompare1630",
    xRange=params.QrangeAzm,
    isFile=False,
    options=opts)

