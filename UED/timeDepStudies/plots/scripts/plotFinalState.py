import numpy as np
import sys
sys.path.append('../../../plots/scripts')
sys.path.append('/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts')
from plotClass import plotCLASS
from plotParams import pltParams

params = pltParams()

plc = plotCLASS()


#runs = ["20180629_1630", "20180627_1551", "20180630_1925", "20180701_0746"]
runs = ["20180627_1551"]
timeSteps = [29, 18, 19, 19]
maxX = [2, 1.1, 1.1, 1.1]
scale = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]


phenoxyPC = "../../results/sim-phenoxyRadical_pairCorrOdd["\
    + str(params.NpairCorrBins) + "].dat"
phenylPC  = "../../results/sim-phenylRadical_pairCorrOdd["\
    + str(params.NpairCorrBins) + "].dat"
phenoxyRAW = "/reg/ued/ana/scratch/nitroBenzene/simulations/"\
    + "phenoxyRadical_diffFinalState["\
    + str(params.NradAzmBins) + "].dat"
phenylRAW = "/reg/ued/ana/scratch/nitroBenzene/simulations/"\
    + "phenylRadical_diffFinalState["\
    + str(params.NradAzmBins) + "].dat"
phenoxySMS = "/reg/ued/ana/scratch/nitroBenzene/simulations/"\
    + "phenoxyRadical_sMsFinalState["\
    + str(params.NradAzmBins) + "].dat"
phenylSMS = "/reg/ued/ana/scratch/nitroBenzene/simulations/"\
    + "phenylRadical_sMsFinalState["\
    + str(params.NradAzmBins) + "].dat"


opts = {
  "xTitle"     : r"Q [$\AA^{-1}$]",
  "labels"     : ["Phenoxy + NO", "Phenyl + NO2"]
  }

plc.print1d([phenoxySMS, phenylSMS],
    "../sim-compareTheories_sMsFinalState",
    xRange=params.QrangeAzm,
    options=opts)

plc.print1d([phenoxyRAW, phenylRAW],
    "../sim-compareTheories_finalState",
    xRange=params.QrangeAzm,
    options=opts)



atoms = ["hydrogen", "carbon", "nitrogen", "oxygen"]
atomZ = [1, 6, 7, 8]
Natoms = [5, 6, 1, 2]
bondFilePrefix = "/reg/ued/ana/scratch/nitroBenzene/simulations/nitrobenzene_bonds_"

bondTypes    = []
bondWeight   = []
for i in range(len(atoms)):
  if atoms[i] == "hydrogen":
    continue
  for j in range(i, len(atoms)):
    if atoms[j] == "hydrogen":
      continue
    if (i == j) and (Natoms[i] == 1):
      continue
    bondTypes.append(atoms[i]+"-"+atoms[j])
    bondWeight.append(atomZ[i]*atomZ[j])

bondCoeffs  = np.zeros(
                (len(bondTypes), params.NpairCorrBins),
                dtype=np.float32)
rDelta = (params.Rrange[1] - params.Rrange[0])/float(params.NpairCorrBins)
for i,bt in enumerate(bondTypes):
  bonds = np.fromfile(bondFilePrefix+bt+".dat", np.double)
  for bnd in bonds:
    bInd = int(params.NpairCorrBins*(bnd-params.Rrange[0])
              /(params.Rrange[1]-params.Rrange[0]))
    bondCoeffs[i,bInd] += bondWeight[i]


opts = {
  "xTitle"     : r"R [$\AA$]",
  "labels"     : ["Phenoxy + NO", "Phenyl + NO2"] + bondTypes
  }
pcTheoryImages = []
image,_ = plc.importImage(phenoxyPC)
pcTheoryImages.append(image)
image,_ = plc.importImage(phenylPC)
pcTheoryImages.append(image)
plotImages = np.vstack((pcTheoryImages, bondCoeffs/1000.))

plc.print1d(plotImages,
    "../sim-compareTheories_finalState_pairCorrOdd",
    xRange=params.Rrange,
    options=opts,
    isFile=False)


###################################
#####  Comparing final state  #####
###################################


for i,run in enumerate(runs):

  #####  Pair Correlation  #####
  opts = {
    "labels"  : ["Data", "Phenoxy + NO", "Phenyl + NO2"] + bondTypes,
    "xTitle"  : r"R [$\AA$]"
  }
  opts["ySlice"] = [-0.3, 0.4]
  image,_ = plc.importImage("../../results/data-"\
              + run + "_finalState_pairCorrOdd["\
              + str(params.NpairCorrBins) + "].dat")
  plotImages = np.vstack((image, pcTheoryImages, bondCoeffs/1000.))

  plc.print1d(plotImages, 
      "../compareFinalState-phenoxyRadical-pairCorrOdd",
      xRange=params.Rrange,
      isFile=False,
      options=opts)


  #####  Diffraction  #####
  opts = {
    "labels"  : ["Data", "Phenoxy + NO", "Phenyl + NO2"],
    "xTitle"  : r"Q [$\AA^{-1}$]" 
  }

  opts["ySlice"] = [-0.7, 0.3]
  plc.print1d( 
        ["/reg/ued/ana/scratch/nitroBenzene/mergeScans/data-"\
          + run + "-sMsFinalState[" + str(params.NradAzmBins) + "].dat",
        "../../results/sim-phenoxyRadical_sMsFinalState_scaled["
          + str(params.NradAzmBins) + "].dat",
        "../../results/sim-phenylRadical_sMsFinalState_scaled["
          + str(params.NradAzmBins) + "].dat"] ,
      "../compareFinalStates_sMsAzmAvgDiff",
      xRange=params.QrangeAzm,
      options=opts)
  
  opts["ySlice"] = [-0.01, 0.005]
  plc.print1d( 
        ["/reg/ued/ana/scratch/nitroBenzene/mergeScans/data-"\
          + run + "-diffFinalState[" + str(params.NradAzmBins) + "].dat",
        "../../results/sim-phenoxyRadical_diffFinalState_scaled["
          + str(params.NradAzmBins) + "].dat",
        "../../results/sim-phenylRadical_diffFinalState_scaled["
          + str(params.NradAzmBins) + "].dat"] ,
      "../compareFinalStates_azmAvgDiff",
      xRange=params.QrangeAzm,
      options=opts)
  
#######################################
#####  Testing low Q theory fill  #####
#######################################

"""
colRange = [-2e-1, 2e-1]#, [-1e-2, 1e-2], [-1e-2, 1e-2], [-1e-2, 1e-2]]
for i,run in enumerate(runs):
  for scl in scale:
    opts = {
      "colorRange" : colRange,
      "xTitle"     : "Time [ps]",
      "yTitle"     : r"R [$\AA$]",
      #"interpolate": [200, 100]
      }

    timeDelay = np.fromfile("../../../mergeScans/results/timeDelays["
          + str(timeSteps[i] + 1) + "].dat", np.double)
    
    plc.print2d("../../results/data-" + run + "-lowQscale-"
          + "%.6f" %(scl) + "-pairCorrOdd["
          + str(timeSteps[i]) + "," + str(params.NpairCorrBins) + "].dat",
          "../data-" + run + "-lowQscale-" + str(scl),
          X=timeDelay,
          yRange=params.Rrange,
          options=opts)

    opts["xSlice"] = [-0.3, maxX[i]]
    plc.print2d("../../results/data-" + run + "-lowQscale-"
          + "%.6f" %(scl) + "-pairCorrOdd["
          + str(timeSteps[i]) + "," + str(params.NpairCorrBins) + "].dat",
          "../data-" + run + "-lowQfullScale-" + str(scl),
          X=timeDelay,
          yRange=params.Rrange,
          options=opts)

files = ["../../results/sim-phenoxyRadical-pairCorrOdd[" + str(params.NpairCorrBins) + "].dat"]
plc.print1d(files,
    "../sim-phenoxyRadical-pairCorrDiff",
    xRange=params.Rrange)
"""
