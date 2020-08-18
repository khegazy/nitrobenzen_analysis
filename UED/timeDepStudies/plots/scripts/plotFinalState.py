import numpy as np
import sys
import glob
sys.path.append('../../../plots/scripts')
sys.path.append('/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts')
from plotClass import plotCLASS
from plotParams import pltParams
from scipy.ndimage import gaussian_filter

params = pltParams()

plc = plotCLASS()


#runs = ["20180629_1630", "20180627_1551", "20180630_1925", "20180701_0746"]
runs = ["20180627_1551", "20180629_1630"]
timeSteps = [29, 18, 19, 19]
maxX = [2, 1.1, 1.1, 1.1]
scale = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]


phenoxyPC = "../../results/sim-phenoxyRadical_pairCorrOdd["\
    + str(params.NpairCorrBins) + "].dat"
phenylPC  = "../../results/sim-phenylRadical_pairCorrOdd["\
    + str(params.NpairCorrBins) + "].dat"
nitrosobenzenePC  = "../../results/sim-nitrosobenzene_pairCorrOdd["\
    + str(params.NpairCorrBins) + "].dat"
hotGroundStatePC  = "../../results/sim-hotGroundState_pairCorrOdd["\
    + str(params.NpairCorrBins) + "].dat"
hotTripletStatePC  = "../../results/sim-hotTripletState_pairCorrOdd["\
    + str(params.NpairCorrBins) + "].dat"
phenoxyRAW = "/reg/ued/ana/scratch/nitroBenzene/simulations/"\
    + "phenoxyRadical_diffFinalState["\
    + str(params.NradAzmBins) + "].dat"
phenylRAW = "/reg/ued/ana/scratch/nitroBenzene/simulations/"\
    + "phenylRadical_diffFinalState["\
    + str(params.NradAzmBins) + "].dat"
nitrosobenzeneRAW = "/reg/ued/ana/scratch/nitroBenzene/simulations/"\
    + "nitrosobenzene_diffFinalState["\
    + str(params.NradAzmBins) + "].dat"
hotGroundStateRAW = "/reg/ued/ana/scratch/nitroBenzene/simulations/"\
    + "hotGroundState_diffFinalState["\
    + str(params.NradAzmBins) + "].dat"
hotTripletStateRAW = "/reg/ued/ana/scratch/nitroBenzene/simulations/"\
    + "hotTripletState_diffFinalState["\
    + str(params.NradAzmBins) + "].dat"
phenoxySMS = "/reg/ued/ana/scratch/nitroBenzene/simulations/"\
    + "phenoxyRadical_sMsFinalState["\
    + str(params.NradAzmBins) + "].dat"
phenylSMS = "/reg/ued/ana/scratch/nitroBenzene/simulations/"\
    + "phenylRadical_sMsFinalState["\
    + str(params.NradAzmBins) + "].dat"
nitrosobenzeneSMS = "/reg/ued/ana/scratch/nitroBenzene/simulations/"\
    + "nitrosobenzene_sMsFinalState["\
    + str(params.NradAzmBins) + "].dat"
hotGroundStateSMS = "/reg/ued/ana/scratch/nitroBenzene/simulations/"\
    + "hotGroundState_sMsFinalState["\
    + str(params.NradAzmBins) + "].dat"
hotTripletStateSMS = "/reg/ued/ana/scratch/nitroBenzene/simulations/"\
    + "hotTripletState_sMsFinalState["\
    + str(params.NradAzmBins) + "].dat"

simLabels = ["Phenoxy + NO", "Phenyl + NO2", "Nitrosobenzene + O", "hot S0", "hot T1"]

opts = {
  "xTitle"     : r"Q [$\AA^{-1}$]",
  "labels"     : simLabels,
  "legOpts"      : {"fontsize" : 15},
  "xTitleSize"  : 18,
  "yTitleSize"  : 18,
  "xTickSize"   : 15,
  "yTickSize"   : 15
  }

plc.print1d([phenoxyRAW, phenylRAW, nitrosobenzeneRAW, hotGroundStateRAW, hotTripletStateRAW],
    "../sim-compareTheories_finalState",
    xRange=params.QrangeAzm,
    options=opts)

opts["ySlice"] = [-1.2, 0.6]
opts["noData"] = True
plc.print1d([phenoxySMS, phenylSMS, nitrosobenzeneSMS, hotGroundStateSMS, hotTripletStateSMS],
    "../sim-compareTheories_sMsFinalState",
    xRange=params.QrangeAzm,
    options=opts)
del opts["noData"]

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
  "xTitle"      : r"R [$\AA$]",
  "labels"      : simLabels + bondTypes,
  "ySlice"      : [-0.15, 0.1],
  #"labels"     : ["Phenoxy + NO", "Phenyl + NO2", "Nitrosobenzene + O"],
  "legOpts"     : {"fontsize" : 15},
  "xTitleSize"  : 18,
  "yTitleSize"  : 18,
  "xTickSize"   : 15,
  "yTickSize"   : 15
 
  }
pcTheoryImages = []
image,_ = plc.importImage(phenoxyPC)
pcTheoryImages.append(image)
image,_ = plc.importImage(phenylPC)
pcTheoryImages.append(image)
image,_ = plc.importImage(nitrosobenzenePC)
pcTheoryImages.append(image)
image,_ = plc.importImage(hotGroundStatePC)
pcTheoryImages.append(image)
image,_ = plc.importImage(hotTripletStatePC)
pcTheoryImages.append(image)
plotImages = np.array(pcTheoryImages)
#plotImages = np.vstack((pcTheoryImages, bondCoeffs/2000.))


opts["noData"] = True
plc.print1d(plotImages,
    "../sim-compareTheories_finalState_pairCorrOdd",
    xRange=params.Rrange,
    options=opts,
    isFile=False)
del opts["noData"]


###################################
#####  Comparing final state  #####
###################################


for i,run in enumerate(runs):

  #####  Pair Correlation  #####
  opts = {
    "labels"  : ["Data"] + simLabels,# + bondTypes,
    #"labels"  : ["Data", "Phenoxy + NO", "Phenyl + NO2", "Nitrosobenzene + O"],
    "xTitle"  : r"R [$\AA$]",
    #"legOpts"      : {"fontsize" : 15},
    #"xTitleSize"  : 18,
    #"yTitleSize"  : 18,
    #"xTickSize"   : 15,
    #"yTickSize"   : 15
  }
  opts["ySlice"] = [-0.4, 0.5]

  dataImage,_ = plc.importImage(params.mergeResultFolder + "/data-"\
              + run + "_pairCorrFinalState["\
              + str(params.NpairCorrBins) + "].dat")
  scale = 1./np.abs(np.amin(dataImage[60:]))
  dataImage *= scale

  pcTheoryImages = []
  pcTheoryImages_bestFits = []
  image,_ = plc.importImage(
      "../../results/sim-phenoxyRadical_pairCorrFinalState_scaled-"
        + run + "[" + str(params.NpairCorrBins) + "].dat")
  image *= scale
  pcTheoryImages.append(image)
  image,_ = plc.importImage(
      "../../results/sim-phenylRadical_pairCorrFinalState_scaled-"
        + run + "[" + str(params.NpairCorrBins) + "].dat")
  image *= scale
  pcTheoryImages.append(image)
  image,_ = plc.importImage(
      "../../results/sim-nitrosobenzene_pairCorrFinalState_scaled-"
        + run + "[" + str(params.NpairCorrBins) + "].dat")
  image *= scale
  pcTheoryImages.append(image)
  image,_ = plc.importImage(
      "../../results/sim-hotGroundState_pairCorrFinalState_scaled-"
        + run + "[" + str(params.NpairCorrBins) + "].dat")
  image *= scale
  pcTheoryImages.append(image)
  pcTheoryImages_bestFits.append(image)
  image,_ = plc.importImage(
      "../../results/sim-hotTripletState_pairCorrFinalState_scaled-"
        + run + "[" + str(params.NpairCorrBins) + "].dat")
  image *= scale
  pcTheoryImages.append(image)
  pcTheoryImages_bestFits.append(image)




  #pcTheoryImages are not scaled to data by fit
  plotImages = np.vstack((dataImage, pcTheoryImages))
  #plotImages = np.vstack((dataImage, pcTheoryImages, bondCoeffs/250.))
  plotImages_bestFits = np.vstack((dataImage, pcTheoryImages_bestFits))

  opts["ySlice"] = [-1.2, 1.1]
  opts["legOpts"] = { "loc" : 4}
  plc.print1d(plotImages, 
      "../data-" + run + "_pairCorr_compareFinalStates",
      xRange=params.Rrange,
      isFile=False,
      options=opts)

  opts["labels"] = ["Data", "hot S0", "hot T1"]
  plc.print1d(plotImages_bestFits, 
      "../data-" + run + "_pairCorr_compareFinalStates_bestFits",
      xRange=params.Rrange,
      isFile=False,
      options=opts)

  Raxis = np.linspace(0, 1., params.NpairCorrBins)*params.Rrange[1]
  np.savetxt("Raxis.txt", Raxis, delimiter=" ")
  np.savetxt("pcFinalStateData_{}.txt".format(run), dataImage, delimiter=" ")

  #####  Diffraction  #####
  opts = {
    "labels"  : ["Data"] + simLabels,
    "xTitle"  : r"Q [$\AA^{-1}$]",
    "xRebin"   : 5,
    #"legOpts"      : {"fontsize" : 15},
    #"xTitleSize"  : 18,
    #"yTitleSize"  : 18,
    #"xTickSize"   : 15,
    #"yTickSize"   : 15
  }

  opts["ySlice"] = [-0.11, 0.11]
  #opts["ySlice"] = [-0.7, 0.6]
  files = ["/reg/ued/ana/scratch/nitroBenzene/mergeScans/data-"\
          + run + "_sMsFinalStateFittedTo[" + str(params.NradAzmBins) + "].dat",
        "../../results/sim-phenoxyRadical_sMsFinalState_scaled-"
          + run + "[" + str(params.NradAzmBins) + "].dat",
        "../../results/sim-phenylRadical_sMsFinalState_scaled-"
          + run + "[" + str(params.NradAzmBins) + "].dat", 
        "../../results/sim-nitrosobenzene_sMsFinalState_scaled-"
          + run + "[" + str(params.NradAzmBins) + "].dat", 
        "../../results/sim-hotGroundState_sMsFinalState_scaled-"
          + run + "[" + str(params.NradAzmBins) + "].dat",
        "../../results/sim-hotTripletState_sMsFinalState_scaled-"
          + run + "[" + str(params.NradAzmBins) + "].dat"] 
  files_bestFits = ["/reg/ued/ana/scratch/nitroBenzene/mergeScans/data-"\
          + run + "_sMsFinalStateFittedTo[" + str(params.NradAzmBins) + "].dat",
        "../../results/sim-hotGroundState_sMsFinalState_scaled-"
          + run + "[" + str(params.NradAzmBins) + "].dat",
        "../../results/sim-hotTripletState_sMsFinalState_scaled-"
          + run + "[" + str(params.NradAzmBins) + "].dat"] 

  errFiles = ["/reg/ued/ana/scratch/nitroBenzene/mergeScans/data-"\
          + run + "_sMsFinalStateSEMFittedTo[" + str(params.NradAzmBins) + "].dat",
          None,
          None,
          None,
          None,
          None]
  errFiles_bestFits = ["/reg/ued/ana/scratch/nitroBenzene/mergeScans/data-"\
          + run + "_sMsFinalStateSEMFittedTo[" + str(params.NradAzmBins) + "].dat",
          None,
          None]

  plc.print1d(files, 
      "../data-" + run + "_sMsAzmAvgDiff_compareFinalStates",
      errors=errFiles,
      xRange=params.QrangeAzm,
      options=opts)

  files = ["/reg/ued/ana/scratch/nitroBenzene/mergeScans/data-"\
        + run + "_sMsFinalStateFittedTo[" + str(params.NradAzmBins) + "].dat",
      "../../results/sim-" + run + "_sMsFinalState_scaledLinComb_Bins["\
        + str(params.NradAzmBins) + "].dat"]
  files += glob.glob("../../results/sim-" + run\
      + "_sMsFinalState_scaledLinComb_contribution*")
  errFiles = ["/reg/ued/ana/scratch/nitroBenzene/mergeScans/data-"\
          + run + "_sMsFinalStateSEMFittedTo[" + str(params.NradAzmBins) + "].dat"]
  for i in range(len(files) - 1):
    errFiles += [None]
  print(files)  
  plc.print1d(files, 
      "../data-" + run + "_sMsAzmAvgDiff_compareFinalStates_linCombFits",
      errors=errFiles,
      xRange=params.QrangeAzm,
      options=opts)


  sys.exit(0)



  opts["labels"] = ["Data", "hot S0", "hot T1"]
  plc.print1d(files_bestFits, 
      "../data-" + run + "_sMsAzmAvgDiff_compareFinalStates_bestFits",
      errors=errFiles_bestFits,
      xRange=params.QrangeAzm,
      options=opts)

 
  smsData = np.fromfile(files[0], dtype=np.double)
  smsErr  = np.fromfile(errFiles[0], dtype=np.double)
  Qaxis = np.linspace(0, 1., params.NradAzmBins)*params.QrangeAzm[1]
  np.savetxt("Qaxis.txt", Qaxis, delimiter=" ")
  np.savetxt("smsFinalStateData_{}.txt".format(run), smsData, delimiter=" ")
  np.savetxt("smsFinalStateSEM_{}.txt".format(run), smsErr, delimiter=" ")
 

  continue 
  # Time Dependend Fit
  tdFits, _ = plc.importImage(
      "../../results/sim-" + run
      + "_sMsFinalStateFitLinComb_Bins["
      + str(params.timeSteps[i]) + ","
      + str(params.NradAzmBins) + "].dat")

  tdData, _ = plc.importImage(
      params.mergeResultFolder + "data-"
      + run + "-sMsAzmAvgDiff["
      + str(params.timeSteps[i])
      + "," + str(params.NradAzmBins) + "].dat")
  for k in range(tdFits.shape[0]):
    smooth = gaussian_filter(tdData[k,:], 10)
    plc.print1d(np.array([smooth, tdFits[k,:]]),
        "../data-" + run 
        + "_sMsFitTimeDelay-" + str(k),
        xRange=params.QrangeAzm,
        isFile=False,
        options=opts)

  """
  tdData, _ = plc.importImage("/reg/ued/ana/scratch/nitroBenzene/mergeScans/data-"\
          + run + "_sMsFinalStateFittedTo[" + str(params.NradAzmBins) + "].dat")
  smooth = gaussian_filter(tdData, 10)
  tdFits = [smooth]
  tdFit, _ = plc.importImage(
        "../../results/sim-phenoxyRadical_sMsFinalState_scaled["
          + str(params.NradAzmBins) + "].dat")
  tdFits.append(tdFit)
  tdFit, _ = plc.importImage(
        "../../results/sim-phenylRadical_sMsFinalState_scaled["
          + str(params.NradAzmBins) + "].dat")
  tdFits.append(tdFit)
  tdFit, _ = plc.importImage(
        "../../results/sim-nitrosobenzene_sMsFinalState_scaled["
          + str(params.NradAzmBins) + "].dat") 
  tdFits.append(tdFit)
  plc.print1d(np.array(tdFits),
      "../data-" + run 
      + "_sMsSmooth",
      xRange=params.QrangeAzm,
      isFile=False,
      options=opts)
      """

 

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
