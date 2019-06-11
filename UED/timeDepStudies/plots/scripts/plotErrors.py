import numpy as np
import sys
sys.path.append('../../../plots/scripts')
sys.path.append('/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts')
from plotClass import plotCLASS
from plotParams import pltParams

params = pltParams()

plc = plotCLASS()


plotTsmeared = False
#runs = ["20180629_1630", "20180627_1551", "20180630_1925", "20180701_0746"]
#runs = ["20180627_1551", "20180629_1630", "20180630_1925", "20180701_0746"]
runs = ["20180627_1551"]
maxX = [2, 1.1, 1.1, 1.1]
smear = "0.025000"
mergeFolder = "/reg/ued/ana/scratch/nitroBenzene/mergeScans/"

selectTimes = [ [0.1, 2.1, 3, 6.5, 12],#[0, 0.5, 1, 4, 8],
                [0, 0.25, 0.5, 0.75, 1],
                [0, 0.25, 0.5, 0.75, 1],
                [0, 0.25, 0.5, 0.75, 1]]

#################################################
#####  Plotting time dependent diffraction  #####
#################################################
#colRange = [[-2e-3, 2e-3], [-2e-3, 2e-3], [-2e-3, 2e-3], [-2e-3, 2e-3]]
#colRange = [[-7e-3, 7e-3], [-7e-3, 7e-3], [-7e-3, 7e-3], [-7e-3, 7e-3]]
colRange = [-3e-3, 3e-3]

opts = {
    "colorRange" : colRange,
    "colorMap"   : 'seismic',
    "xTitle"     : "Time [ps]",
    "yTitle"     : r"Q [$\AA^{-1}$]",
    "yRebin"     : 8
    #"TearlySub"  : 3
    }

opts1d = {
    "xTitle"     : r"Q [$\AA^{-1}$]",
    "yLog"       : True,
    "xTicks"     : np.arange(0,13, 1)
    }


for i,run in enumerate(runs):
  timeDelay = np.fromfile("../../../mergeScans/results/timeDelays["
        + str(params.timeSteps[i] + 1) + "].dat", np.double)
 

  dfrctnSEM,_ = plc.importImage(mergeFolder + "data-"
          + run + "-azmAvgSEM["
          + str(params.timeSteps[i]) + "," 
          + str(params.NradAzmBins) + "].dat")
  sMsSEM,_ = plc.importImage(mergeFolder + "data-"
          + run + "-sMsSEM["
          + str(params.timeSteps[i]) + "," 
          + str(params.NradAzmBins) + "].dat")

  plc.print2d(dfrctnSEM,
        "../data-" + run + "_azmAvgSEMFull",
        X=timeDelay,
        yRange=params.QrangeAzm,
        isFile=False,
        options=opts)

  plc.print2d(sMsSEM,
        "../data-" + run + "_sMsSEMFull",
        X=timeDelay,
        yRange=params.QrangeAzm,
        isFile=False,
        options=opts)


  dfrctnSEMq = np.sqrt(np.mean(dfrctnSEM**2, axis=0)/dfrctnSEM.shape[0])
  sMsSEMq = np.sqrt(np.mean(sMsSEM**2, axis=0)/sMsSEM.shape[0])

  plc.print1d(dfrctnSEMq,
        "../data-" + run + "_azmAvgSEM_qDist",
        xRange=params.QrangeAzm,
        isFile=False,
        options=opts1d)

  opts1d["ySlice"] = [5e-3, 1] 
  plc.print1d(sMsSEMq,
        "../data-" + run + "_sMsSEM_qDist",
        xRange=params.QrangeAzm,
        isFile=False,
        options=opts1d)
  del opts1d["ySlice"]

