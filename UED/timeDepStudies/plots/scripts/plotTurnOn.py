import sys
import numpy as np
import copy
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
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
runs = ["20180629_1630"]
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
simLabels = ["phenoxyRadical", "phenylRadical"]
dfrScale = np.array(
            [[18, 1.25, 1, 5, 3],
            [4, 1.25, 1, 5.5, 100]])
pCorrScale = np.array(
              [[200, 1.25, 10],
              [3, 2, 20]])
titles = []
for i,run in enumerate(runs):
  if run == "20180629_1630":
    i += 1

  allLOs = []
  timeDelay = np.fromfile("../../../mergeScans/results/timeDelays-"
    + run + "_bins[" + str(params.timeSteps[i] + 1) + "].dat", np.double)

  dfrctnRanges = [[1, 2], [2, 3], [3,4], [4, 5.5], [6, 7]]
  dfrctnLOs, dfrctnErrLOs = plc.getRangeLineOut(mergeFolder + "data-" 
          + run + "-azmAvgDiff["
          + str(params.timeSteps[i]) 
          + "," + str(params.NradAzmBins) + "].dat",
        1, 
        dfrctnRanges,
        np.linspace(0, 1, params.NradAzmBins)*params.QrangeAzm[-1],
        errorFileName = mergeFolder + "data-"
            + run + "-azmAvgSEM["
            + str(params.timeSteps[i]) + ","
            + str(params.NradAzmBins) + "].dat")

  allLOs = dfrctnLOs
  """
  for k in range(len(dfrctnLOs)):
    dfrctnLOs[k] *= dfrScale[k]
    dfrctnErrLOs[k] *= dfrScale[k]
    """

  pCorrRanges = [[1.1, 1.5], [2, 2.75], [4, 4.5]]
  pCorrLOs, pCorrErrLOs = plc.getRangeLineOut("../../results/data-" 
          + run + "_pairCorrOdd["
          + str(params.timeSteps[i]) + "," 
          + str(params.NpairCorrBins) + "].dat",
        1, 
        pCorrRanges,
        np.linspace(0, 1, params.NpairCorrBins)*params.Rrange[-1],
        errorFileName = mergeFolder + "data-"
            + "20180627_1551-pairCorrSEM["
            #+ run + "-pairCorrSEM["
            + str(params.timeSteps[0]) + ","
            #+ str(params.timeSteps[i]) + ","
            + str(params.NpairCorrBins) + "].dat")
  for k in range(len(pCorrErrLOs)):
    pCorrErrLOs[k] = pCorrErrLOs[k][:params.timeSteps[i]]

  allLOs = allLOs + pCorrLOs
  """
  for k in range(len(pCorrLOs)):
    pCorrLOs[k] *= pCorrScale[k]
    pCorrErrLOs[k] *= pCorrScale[k]
    """



##################################################
#####  Plotting Final State Fits to TD Data  #####
##################################################

 
  resFolder = "../../results/"
  """
  files = [resFolder + "sim-" + run\
              + "-offset_sMsFitCoeffsLinComb_Bins["\
              + str(params.timeSteps[i]) + "].dat","""
  files = [resFolder + "sim-" + run\
              + "-phenoxyRadical_sMsFitCoeffsLinComb_Bins["\
              + str(params.timeSteps[i]) + "].dat"]
  """
          resFolder + "sim-" + run\
              + "-phenylRadical_sMsFitCoeffsLinComb_Bins["\
              + str(params.timeSteps[i]) + "].dat"]
              """
  """
  errFiles = [resFolder + "sim-" + run\
              + "-offset_sMsFitCoeffErrorsLinComb_Bins["\
              + str(params.timeSteps[i]) + "].dat","""
  errFiles = [resFolder + "sim-" + run\
              + "-phenoxyRadical_sMsFitCoeffErrorsLinComb_Bins["\
              + str(params.timeSteps[i]) + "].dat"]
  """
          resFolder + "sim-" + run\
              + "-phenylRadical_sMsFitCoeffErrorsLinComb_Bins["\
              + str(params.timeSteps[i]) + "].dat"]
              """

  tind = np.argmin(np.abs(2 - timeDelay))
  for ii,ind in enumerate([0, tind]):
    simFits = []
    simFitErrs = []
    scalesim = 5
    if ii:
      curTimeDelay = copy.deepcopy(timeDelay[1:ind+1])
    else:
      curTimeDelay = copy.deepcopy(timeDelay[1:])

    for i in range(len(files)):
      image, shape = plc.importImage(files[i])
      imageErr, shapeErr = plc.importImage(errFiles[i])
      if ii:
        simFits.append(image[:ind]*scalesim)
        simFitErrs.append(imageErr[:ind]*scalesim)
      else:
        simFits.append(image*scalesim)
        simFitErrs.append(imageErr*scalesim)
      simFits[-1] -= np.mean(simFits[-1])
      if ii is 0:
        allLOs.append(image)

    simMax = np.amax(simFits[0])
    simMin = np.amin(simFits[0]*1.1)

    Nplots = len(dfrctnLOs) + len(pCorrLOs)
    fig, axs = plt.subplots(1, Nplots, sharey=True)

    fitX = np.ones((simFits[0].shape[0], 2))
    fitY = simFits[0]
    for i,dfr in enumerate(dfrctnLOs):

      dfrErrLO = copy.deepcopy(dfrctnErrLOs[i])
      if ii:
        dfr = dfr[:ind]
        dfrErrLO = dfrErrLO[:ind]

      fitX[:,1] = dfr[:]
      norm = np.linalg.inv(np.dot(fitX.transpose(), fitX))
      fit = np.dot(norm, np.dot(fitX.transpose(), fitY))
      dfr = dfr*np.abs(fit[1]) + fit[0]
      dfrErrLO *= np.abs(fit[1])
      dfr -= np.mean(dfr)
      dfr *= dfrScale[ii,i]
      dfrErrLO *= dfrScale[ii,i]
      
      print("shapes ",norm.shape,dfr.shape, timeDelay.shape, dfrctnErrLOs[i].shape)
      title = "Q: " + str(dfrctnRanges[i][0]) + " - " + str(dfrctnRanges[i][1])
      titles.append(title)
      axs[i].set_title(title)
      axs[i].xaxis.set_major_locator(MaxNLocator(3))
      if ii is 0:
        axs[i].set_ylim([-0.125, 16])
      if ii is 1:
        axs[i].set_ylim([-0.125, 2])
      curMin = min(np.amin(dfr), simMin)
      curMax = max(np.amax(dfr), simMax)
      axs[i].set_xlim([curMin, curMax])
      axs[i].set_xlim([np.amin(dfr), np.amax(dfr)])
      axs[i].errorbar(dfr, curTimeDelay, xerr=dfrErrLO,\
          color='k', linestyle='-')
      #for j,sdfr in enumerate(simFits):
      #  axs[i].errorbar(sdfr, curTimeDelay, xerr=simFitErrs[j],\
      #    color='b', linestyle='-')

    axShift = len(dfrctnLOs)
    for i,dfr in enumerate(pCorrLOs):
     
      pCorrErrLO = copy.deepcopy(pCorrErrLOs[i])
      if ii:
        dfr = dfr[:ind]
        pCorrErrLO = pCorrErrLO[:ind]

      fitX[:,1] = dfr[:]
      norm = np.linalg.inv(np.dot(fitX.transpose(), fitX))
      fit = np.dot(norm, np.dot(fitX.transpose(), fitY))
      fdfr = dfr*np.abs(fit[1]) + fit[0]
      pCorrErrLO *= np.abs(fit[1])
      fdfr -= np.mean(fdfr)
      fdfr *= pCorrScale[ii,i]
      pCorrErrLO *= pCorrScale[ii,i]

   
      print("shapes ",fdfr.shape, timeDelay.shape, dfrctnErrLOs[i].shape)
      title = "R: " + str(pCorrRanges[i][0]) + " - " + str(pCorrRanges[i][1])
      titles.append(title)
      axs[i+axShift].set_title(title)
      if ii is 0:
        axs[i].set_ylim([-0.125, 16])
      if ii is 1:
        axs[i].set_ylim([-0.125, 2])
      curMin = min(np.amin(fdfr), simMin)
      curMax = max(np.amax(fdfr), simMax)
      axs[i+axShift].set_xlim([curMin, curMax])
      axs[i+axShift].set_xlim([np.amin(fdfr), np.amax(fdfr)])
      axs[i+axShift].xaxis.set_major_locator(MaxNLocator(3))
      axs[i+axShift].errorbar(fdfr, curTimeDelay, xerr=pCorrErrLO,\
          color='k', linestyle='-')
      #for j,sdfr in enumerate(simFits):
      #  axs[i+axShift].errorbar(sdfr, curTimeDelay, xerr=simFitErrs[j],\
      #    color='b', linestyle='-')


    ###  Plot Images  ###
    plt.tight_layout()
    plt.subplots_adjust(wspace=0.1, hspace=0)
    if ii is 0:
      fig.savefig("../data-" + run + "_turnOnSignalsFull.png")
    if ii is 1:
      fig.savefig("../data-" + run + "_turnOnSignals.png")

    """
    # First 2ps
    for i in range(Nplots):
      axs[i].set_ylim([-0.125, 2])
    fig.savefig("../data-" + run + "_turnOnSignals.png")
    plt.close()
    """


  #####  Correlation Matrix  #####
  titles.append("fit Coeff")

  fig, ax = plt.subplots()
  arrAllLOs = np.array(allLOs)
  R = np.corrcoef(arrAllLOs)
  for i in range(R.shape[0]):
    R[i,i] = 0
  X,Y = np.meshgrid(np.arange(arrAllLOs.shape[0]+1), np.arange(arrAllLOs.shape[0]+1))
  plot = ax.pcolor(X, Y, R, cmap='seismic', vmin=-0.5, vmax=0.5)
  fig.colorbar(plot)
  ax.set_xticklabels(titles, rotation='vertical')
  mticks = ax.get_xticks()
  ax.set_xticks((mticks[:-1]+mticks[1:])/2)
  ax.set_yticklabels(titles)
  mticks = ax.get_yticks()
  ax.set_yticks((mticks[:-1]+mticks[1:])/2)
  plt.subplots_adjust(bottom=0.2)
  fig.savefig("../data-" + run + "_turnOnSignals_correlationMatrixFull.png")

  # First 2ps
  R = np.corrcoef(arrAllLOs[:,:tind])
  for i in range(R.shape[0]):
    R[i,i] = 0
  X,Y = np.meshgrid(np.arange(arrAllLOs.shape[0]+1), np.arange(arrAllLOs.shape[0]+1))
  plot = ax.pcolor(X, Y, R, cmap='seismic', vmin=-0.5, vmax=0.5)
  fig.savefig("../data-" + run + "_turnOnSignals_correlationMatrix.png")

