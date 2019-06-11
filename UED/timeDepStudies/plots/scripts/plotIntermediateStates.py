import numpy as np
import sys
sys.path.append('../../../plots/scripts')
sys.path.append('/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts')
from plotClass import plotCLASS
from plotParams import pltParams

params = pltParams()

plc = plotCLASS()


plotTsmeared = False
runs = ["20180627_1551", "20180629_1630", "20180630_1925", "20180701_0746"]
#runs = ["20180627_1551"]
maxX = [1.1, 1.1, 1.1, 1.1]
#maxX = [2, 1.1, 1.1, 1.1]
minX = [0, 0, -0.2, -0.2]
#minX = [-0.125, -0.3, -0.2, -0.2]
mergeFolder = "/reg/ued/ana/scratch/nitroBenzene/mergeScans/"
simFolder = "/reg/ued/ana/scratch/nitroBenzene/simulations/"

names = ["gsEP", "gsNO", "s1min", "s1s0CI", "s1t2STC", "s2s1CI", "s3min", "s4min", "t1min", "t1s0STCEP", "t1s0STC-NO", "t2min", "t2t1CI"]

selectTimes = [ [0.1, 2.1, 3, 6.5, 12],#[0, 0.5, 1, 4, 8],
                [0, 0.25, 0.5, 0.75, 1],
                [0, 0.25, 0.5, 0.75, 1],
                [0, 0.25, 0.5, 0.75, 1]]

gsSMS = np.fromfile(simFolder
          + "nitrobenzene_sMsPatternLineOut_Qmax-12.376500_Ieb-5.000000_scrnD-4.000000_elE-3700000.000000_Bins[555].dat", dtype=np.double)

#################################################
#####  Plotting time dependent diffraction  #####
#################################################

colRange = [[-4e-4, 4e-4], [-3e-3, 3e-3], [-3e-3, 3e-3], [-3e-3, 3e-3]]
for i,run in enumerate(runs):
  opts = {
    "colorRange" : colRange[i],
    "colorMap"   : 'seismic',
    "xTitle"     : "Time [ps]",
    "yTitle"     : r"Q [$\AA^{-1}$]",
    "yRebin"     : 8
    }


  timeDelay = np.fromfile("../../../mergeScans/results/timeDelays["
        + str(params.timeSteps[i] + 1) + "].dat", np.double)
  #if i == 0:
  #  timeDelay += 0.125
 
  for nm in names:
    plc.print1d(
        ["../../results/data-" + run
          + "_fitCoeffs-" + nm  
          + "_bins[" + str(params.timeSteps[i]) + "].dat"],
        "../data-" + run
          + "_fitCoeffs-" + nm,
          X=timeDelay[1:])

    if i == 0:
      curSMS = np.fromfile(simFolder + nm
                  + "_sMsPatternLineOut_Qmax-12.376500_Ieb-5.000000_scrnD-4.000000_elE-3700000.000000_Bins[555].dat", dtype=np.double)
      plc.print1d(
          np.reshape(curSMS - gsSMS, (1,-1)),
          "../sim-" + nm + "_sMs",
          xRange=params.QrangeAzm,
          isFile=False)




