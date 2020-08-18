#include "/reg/neh/home5/khegazy/baseTools/tools/parameters.h"

parameterClass::parameterClass(std::string runName) {

  run = runName;

  // Molecule
  //molecule = finalState3;
  molecule = initialState;
  radicalNames.push_back("nitrobenzene");
  radicalNames.push_back("phenoxyRadical");
  radicalNames.push_back("phenylRadical");
  radicalNames.push_back("nitrosobenzene");
  radicalNames.push_back("hotGroundState");
  radicalNames.push_back("hotTripletState");
  molName = radicalNames[molecule];


  // Image parameters
  Nlegendres = 1;
  NradLegBins = 50;
  NmaxRadBins = 750;
  //NradAzmBins = 445;
  NradAzmBins = 555;
  imgSize = 895;
  imgEdgeBuffer = 20;
  hasRef = false;
  refStagePosCut = -1;
  imgShutterTime = 20;
  imgNormRadMin = 0.16; //0.25; //0.4; //0.045; //0.06; //0.045;
  imgNormRadMax = 0.6; //0.721; //0.33; //0.721;


  // PV
  getPVs        = true;
  pvSampleTimes = 5;
  pressureSmear = 180;
  pvFolder      = "/reg/ued/ana/scratch/nitroBenzene/PV/";

  // Power Scans
  range1Qbegin = 1.8;
  range1Qend   = 2.5;
  range2Qbegin = 2.8;
  range2Qend   = 3.75;

  // Time Zero
  tZeroQranges.resize(3);
  tZeroQranges[0].push_back(3);     tZeroQranges[0].push_back(3.5);
  tZeroQranges[1].push_back(3.75);  tZeroQranges[1].push_back(5);
  tZeroQranges[2].push_back(2);     tZeroQranges[2].push_back(3);

  tZeroRatio.resize(2);
  tZeroRatio[0] = 1;
  tZeroRatio[1] = 0;

  // Merging scans
  mergeNormalizeImgs  = false;
  Qnormalize          = true;
  mergeSTDscale       = 3; //2.6; FIX ME CHANGE compare to Thomas
  mergeImageSTDScale  = 2.3;
  legImageNoiseCut    = 12;
  azmImageNoiseCut    = 105;

  mergeGaussSmoothRef = false;
  mergeGSmoothSTD     = 5;

  testMergeNbootStrap = false;
  useBootstrapSEM     = true;
  computeBootstrapSEM = false;
  mergeNbootstrap     = 10000;


  timeWnHigh = 0.8;
  timeFiltOrder  = 5;
  timeFilterType = "lowpass";
  smearTimeBinWindow  = 100;
  timeSmearSTD        = 0.025;
  scanImgAzmSTDcut    = 4;
  scanImgAzmRefSTDcut = 4;

  saveMergeIntermediates = false;
  saveMergeInterFolder = "/reg/ued/ana/scratch/nitroBenzene/mergeScans/intermediates";



  // Analysis Parameters
  signalRranges.resize(5);
  signalRranges[0].push_back(1.1);  signalRranges[0].push_back(1.7);
  signalRranges[1].push_back(1.7);  signalRranges[1].push_back(2.0);
  signalRranges[2].push_back(2.0);  signalRranges[2].push_back(2.75);
  signalRranges[3].push_back(3.0);  signalRranges[3].push_back(4.0);
  signalRranges[4].push_back(4.0);  signalRranges[4].push_back(5.0);


  // Background removal
  XrayHighCut       = 1e4; //30000;
  XrayLowCut        = 4e3;
  XraySTDcut        = 3;
  XrayWindow        = 20;
  xRayHitDist       = false;

  refCorrection     = "NULL";

  hotPixel          = 1750;
  bkgSTDcut         = 15;
  shellWidth        = 1;
  Npoly             = 3;
  stdIncludeLeft    = 3; //1;
  distSTDratioLeft  = 0.5;
  stdCutLeft        = 3.5;
  meanBinSize       = 12;
  stdIncludeRight   = 1;
  distSTDratioRight = 0.75;
  stdChangeRatio    = 0.02;
  stdCutRight       = 7; //2.25; //2.75;
  outlierSTDcut     = 3.;
  outlierVerbose    = false;
  plotRadPixDist    = false;
  indicesPath       = "/reg/neh/home/khegazy/analysis/radialFitIndices/";

  outlierMapSTDcut        = 1.5;//75;
  outlierCoreValThresh    = 5000; //90; //65; //5e5;
  outlierCoreRad          = 2; 
  outlierClusterRad       = 3; 
  outlierMinClusterSize   = 50;
  outlierMinPixelSize     = outlierMinClusterSize;
  outlierMinDensity       = 0.0;//0.2;
  outlierShapeVarCut      = 400.5;
  outlierShapeEdgeCut     = 2.75;
  outlierBorderValThresh  = 10; //75; //1e5;
  outlierBorderDistLimit  = 2;
  outlierBorderRad        = 3;
  outlierPadRad           = 7;
  outlierrMaxScale        = 1;
  outlierrMinScale        = 0;
  outliercMaxScale        = 4;
  outliercMinScale        = 0;
 

  readoutStart         = 0.7; //0.94; // Use ratio < 1. Converts to bins at the end
  readoutEnd           = 1; // Use ratio < 1. Converts to bins at the end
   
  // Centering
  scanAvgCenter     = true;
  I0centers         = false;
  computeCenters    = false;
  centerFxnType     = 3;
  centerShellWidth  = 15; 
  centerSTDcut      = 3;

  meanInds.push_back(140); 
  meanInds.push_back(155); 
  meanInds.push_back(170); 
  meanInds.push_back(185); 
  meanInds.push_back(200); 
  meanInds.push_back(250); 

  I0ellRats.push_back(0.25);    I0ellRats.push_back(0.5);
  I0ellRats.push_back(0.75);    I0ellRats.push_back(0.85);
  centerDir = "/reg/ued/ana/scratch/nitroBenzene/preProcessing/centers/";

  // Filtering
  order  = 5;
  WnLow  = 0.005;
  WnHigh = 0.08;
  filterType = "lowpass";
  pltFilterVerbose = false;

  // Remove low order polynomial noise
  NlowOrderPoly         = 6;
  lowPolySubtractStudy  = false;

  // Pair correlation parameters
  NautCpadding      = 10000;
  holeRat           = 0.15;
  rMaxLegRat        = 0.75;
  rMaxAzmRat        = 0.07; //0.052;
  padDecayRat       = 0.5;

  pCorrGaussFilter  = true;
  pCorrButterFilter = false;
  pCorrQcut         = 10;
  //filterVar         = std::pow(NradAzmBins/3.25, 2);
  //filterVar         = std::pow(NradAzmBins/4, 2);
  filterVar         = std::pow(NradAzmBins/4, 2);
  pCorrWnHigh       = 0.6;
  pCorrFilterOrder  = 2;
  pCorrFilterType   = "lowpass";
  lowQfillSimScale  = 0.3;
  fillLowQfile      = "/reg/neh/home5/khegazy/analysis/nitrobenzene/UED/timeDepStudies/results/sim-phenoxyRadicalLowQfill[555].dat";
  fillLowQtheory    = false;
  fillLowQzeros     = true;
  fillLowQsine      = false;
  fillLowQfitTheory = false;
  useFilledHole     = false;


  subtractReference = true;

  // Simulation parameters
  compareSims     = false;
  simPairCorr     = true;
  getBonds        = true;
  simPltVerbose   = false;
  NradSimBins     = NradAzmBins;
  Iebeam          = 5;
  elEnergy        = 3.7e6;
  screenDist      = 4;
  xyzDir          = "/reg/neh/home/khegazy/analysis/nitrobenzene/simulation/XYZfiles/";
  simOutputDir    = "/reg/ued/ana/scratch/nitroBenzene/simulations/";
  //simOutputDir    = "/reg/neh/home/khegazy/analysis/nitrobenzene/simulation/diffractionPattern/output/";
  //simOutputDir    = "/reg/ued/ana/scratch/nitroBenzene/simulations/";
  fsFitOffset     = false;
  fsFilterSMS     = false; 
  fsFilterVar     = std::pow(NradAzmBins/4.5, 2); 
  fitQbegin       = 1.2;
  fitQend         = 8;
  fsQfitBegin     = 1;
  fsQfitEnd       = 8;
  fsRfitBegin     = 1.1;
  fsRfitEnd       = 5;

  simHotFinalState  = false;
  hotFSrefVar       = filterVar*1.1;
  hotFStdepVar      = filterVar*0.9;

  //finalStates.push_back("phenylRadical");
  //finalStates.push_back("phenoxyRadical");
  //finalStates.push_back("nitrosobenzene");
  finalStates.push_back("hotGroundState");
  finalStates.push_back("hotTripletState");
  intermediateStates.push_back("gsEP");
  intermediateStates.push_back("gsNO");
  intermediateStates.push_back("s1min");
  intermediateStates.push_back("s1s0CI");
  intermediateStates.push_back("s1t2STC");
  intermediateStates.push_back("s2s1CI");
  intermediateStates.push_back("s3min");
  intermediateStates.push_back("s4min");
  intermediateStates.push_back("t1min");
  intermediateStates.push_back("t1s0STCEP");
  intermediateStates.push_back("t1s0STC-NO");
  intermediateStates.push_back("t2min");
  intermediateStates.push_back("t2t1CI");

  preProcOutputDir    = "/reg/ued/ana/scratch/nitroBenzene/rootFiles/";
  preProcI0OutputDir  = "/reg/ued/ana/scratch/nitroBenzene/I0/";
  mergeScansOutputDir = "/reg/ued/ana/scratch/nitroBenzene/mergeScans/";
  scanSearchOutputDir = "/reg/ued/ana/scratch/nitroBenzene/scanSearch/";
  radialPixelDist     = "/reg/ued/ana/scratch/nitroBenzene/radialPixelDist/";
  backgroundImage     = "NULL";
  backgroundFolder    = "/reg/ued/ana/scratch/nitroBenzene/background/";
  indexPath           = "/reg/neh/home/khegazy/analysis/radialFitIndices/";

  pltCent     = false;
  verbose     = true; 
  pltVerbose  = false;


  scaleStagePos = 1e4;

  if (runName.compare("20161102_LongScan1") == 0) {

    NradLegBins = 30;
    imgMatType = "uint32";

    QperPix = 0.0223;
    maxQleg = QperPix*imgSize/2;

    hasRef          = true;
    refStagePosCut  = 38.0;
    std::cout<<"add references used in subtraction!\n";
    std::exit(0);

    timeZero = 0.5;
    legStdCut = 1.5;

    /////  Center Finding Parameters  /////
    // Rough center finding
    sigma = 8;
    blockCentR = 560;
    blockCentC = 485;
    minRad = 90;
    maxRad = 340;
    meanInd = 335;
    COMstdScale = 0.025;

    // Fine centering
    centerFxnType = 2;
    centerShellWidth = 130; //70;
    holeR = 547;
    holeC = 492;
    holeRad = 60;
 
    cntrScale = 10;
    cntrMinScale = 1;
    cntrPowellTol = 0.2;
    cntrFracTol1d = 0.01;

    // Laser Background Removal Parameters
    hasLaserBkg = true;
    laserClusterRemoval = false;
    decayConst = -1.0/400.0;
    coreValThresh = 6.0e-3; //90; //65; //5e5;
    coreRad = 4; 
    clusterRad = 1; 
    minClusterSize = 550;
    minPixelSize = 300;
    minDensity = 0.2;//0.2;
    borderValThresh = 5.8e-3; //75; //1e5;
    borderRad = 3;
    padRad = 10;

    nanMap.clear();
    nanMap.resize(imgSize);
    for (int ir=0; ir<imgSize; ir++) {
      nanMap[ir].resize(imgSize, 0);
      if ((ir > 350) && (ir < 500)) {
        for (int ic=(int)imgSize*0.8; ic<imgSize; ic++) {
          nanMap[ir][ic] = NANVAL;
        }
      }
    }

    /*
    for (int ir=imgSize/2-40; ir<imgSize/2+40; ir++) {
      for (int ic=imgSize/2-120; ic<imgSize/2; ic++) {
        nanMap[ir][ic] = nanVal;
      }
    }
    for (int ir=imgSize/2-200; ir<imgSize/2+50; ir++) {
      for (int ic=imgSize-225; ic<imgSize-115; ic++) {
        nanMap[ir][ic] = nanVal;
      }
    }
    for (int ir=imgSize/2-60; ir<imgSize/2+35; ir++) {
      for (int ic=imgSize-75; ic<imgSize; ic++) {
        nanMap[ir][ic] = nanVal;
      }
    }
    */


  }
  else if ((runName.compare("20180701_0746") == 0)
            || (runName.compare("20180701_0738") == 0)
            || (runName.compare("20180701") == 0)) {

    // Image parameters
    QperPix = 0.0223;
    legStdCut = 3.0;
    NbinsSkip = 50; //27;
    imgMatType = "uint16";

    // Filtering
    suppressBins = 75;
    padMaxHeight = 3;

    // Measurement parameters
    timeZero = 0.3;
    hasRef = true;
    refStagePosCut = 154.0;
    refSubtractStagePos.push_back((int)(153.0*scaleStagePos));
    refSubtractStagePos.push_back((int)(153.01*scaleStagePos));

    // Bad scans
    /*
    for (int i=169; i<=175; i++) {
      badScans.push_back(i);
    }
    //for (int i=179; i<=181; i++) {
    //  badScans.push_back(i);
    //}
    badScans.push_back(131);
    badScans.push_back(165);
    badScans.push_back(203);
    badScans.push_back(103);
    badScans.push_back(53);
    badScans.push_back(57);
    badScans.push_back(90);
    badScans.push_back(91);
    badScans.push_back(98);
    for (int i=166; i<203; i++) {
      badScans.push_back(i);
    }
    */

    badScans.push_back(37);
    badScans.push_back(38);
    badScans.push_back(41);
    badScans.push_back(57);
    badScans.push_back(87);
    badScans.push_back(96);
    badScans.push_back(111);
    badScans.push_back(147);
    badScans.push_back(152);
    for (int i=166; i<203; i++) {
      badScans.push_back(i);
    }

    badImages[4].push_back(1542450);
    badImages[4].push_back(1542850);
    badImages[6].push_back(1542550);
    badImages[17].push_back(1542450);
    badImages[18].push_back(1543150);
    badImages[29].push_back(1543550);
    badImages[35].push_back(1530500);
    badImages[62].push_back(1543550);
    badImages[68].push_back(1542450);
    badImages[98].push_back(1543550);
    badImages[98].push_back(1544300);
    badImages[101].push_back(1542350);
    badImages[105].push_back(1530500);
    badImages[131].push_back(1543250);
    badImages[131].push_back(1543400);
    badImages[149].push_back(1542350);
    badImages[155].push_back(1543250);

    //badImages[187].push_back(1542550);
    //badImages[196].push_back(1550300);


    // Background
    backgroundImage = "backgroundImg-20180701_0738.dat";
    hasLaserBkg = true;
    laserClusterRemoval = false;

    int row, col;
    int rad = 57;
    int hRad = 45;
    nanMap.clear();
    nanMap.resize(1024);
    for (uint ir=0; ir<nanMap.size(); ir++) {
      nanMap[ir].resize(1024, 0);
    }
    if (false) {
      for (int ir=510; ir<660; ir++) {
        for (int ic=443; ic<583; ic++) {
          row = ir - 570;
          col = ic - 535;
          if (rad > std::sqrt(row*row + col*col)) {
            nanMap[ir][ic] = NANVAL;
          }
          row = ir - 590;
          col = ic - 518;
          if (sqrt(row*row + col*col) < hRad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }

      rad = 48;
      for (int ir=420; ir<660; ir++) {
        for (int ic=443; ic<583; ic++) {
          row = ir - 565;
          col = ic - 510;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }

      rad = 40;
      for (int ir=540; ir<610; ir++) {
        for (int ic=560; ic<630; ic++) {
          row = ir - 575;
          col = ic - 575;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }

      rad = 60;
      for (int ir=560; ir<680; ir++) {
        for (int ic=510; ic<630; ic++) {
          row = ir - 585;
          col = ic - 550;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }
    }


    // Remove hole
    holeR = 587; //590;
    holeC = 512; //513;
    holeRad = 43; //50;

    /////  Center Finding Parameters  /////
    // Rough center finding
    sigma = 8;
    blockCentR = 560;
    blockCentC = 505;
    minRad = 70;
    maxRad = 325;
    meanInd = 350;
    COMstdScale = 0.075;

    cntrScale = 10;
    cntrMinScale = 0.5;
    cntrPowellTol = 0.5;
    cntrFracTol1d = 0.005;

    // PVs
    pvMap["pressure"]    = "pressureSampleChamber_07_01_2018_07_47_00-07_02_2018_08_41_10-17932.dat";
    pvMap["UVcounts"]    = "UVsampleChamberCam_07_01_2018_07_47_00-07_02_2018_08_41_10-17932.dat";
    pvMap["bunkerTemp"]  = "bunkerTemperature_07_01_2018_07_47_00-07_02_2018_08_41_10-17932.dat";
    pvMap["highBayTemp"] = "highBayTemperature_07_01_2018_07_47_00-07_02_2018_08_41_10-17932.dat"; 
 
  }
  else if ((runName.compare("20180630_1925") == 0)
            || (runName.compare("20180630_1917") == 0)
            || (runName.compare("20180630") == 0)) {

    // Image parameters
    QperPix = 0.0223;
    legStdCut = 3.0;
    NbinsSkip = 50; //31;
    imgMatType = "uint16";

    // Measurement parameters
    timeZero = 0.3;
    hasRef = true;
    refStagePosCut = 154.0;
    refSubtractStagePos.push_back((int)(153.0*scaleStagePos));
    refSubtractStagePos.push_back((int)(153.01*scaleStagePos));

    // Filtering
    suppressBins = 75;
    padMaxHeight = 4;

    // Bad scans
    /*
    badScans.push_back(20);
    badScans.push_back(86);
    badScans.push_back(97);
    */

    badScans.push_back(8);
    badScans.push_back(62);
    badScans.push_back(86);
    badScans.push_back(97);

    badImages[20].push_back(1543550);
    badImages[26].push_back(1543250);
    badImages[27].push_back(1542750);
    badImages[27].push_back(1545800);
    badImages[46].push_back(1542950);
    badImages[68].push_back(1542650);
    badImages[68].push_back(1543400);
    badImages[70].push_back(1542350);
    badImages[75].push_back(1544000);
    badImages[76].push_back(1542350);
    badImages[94].push_back(1543400);
    badImages[96].push_back(1543050);

    // Background
    backgroundImage = "backgroundImg-20180630_1917.dat";
    hasLaserBkg = true;
    laserClusterRemoval = false;

    int row, col;
    int rad = 58;
    int hRad = 50;
    nanMap.clear();
    nanMap.resize(1024);
    for (uint ir=0; ir<nanMap.size(); ir++) {
      nanMap[ir].resize(1024, 0);
    }
    if (false) {
      for (int ir=510; ir<660; ir++) {
        for (int ic=443; ic<583; ic++) {
          row = ir - 570;
          col = ic - 535;
          if (rad > std::sqrt(row*row + col*col)) {
            nanMap[ir][ic] = NANVAL;
          }
          row = ir - 590;
          col = ic - 518;
          if (sqrt(row*row + col*col) < hRad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }

      rad = 48;
      for (int ir=420; ir<660; ir++) {
        for (int ic=443; ic<583; ic++) {
          row = ir - 565;
          col = ic - 510;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }

      rad = 40;
      for (int ir=540; ir<610; ir++) {
        for (int ic=560; ic<630; ic++) {
          row = ir - 575;
          col = ic - 575;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }

      rad = 60;
      for (int ir=560; ir<680; ir++) {
        for (int ic=510; ic<630; ic++) {
          row = ir - 585;
          col = ic - 550;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }
    }


    // Remove hole
    holeR = 590;
    holeC = 513;
    holeRad = 50;

    /////  Center Finding Parameters  /////
    // Rough center finding
    sigma = 8;
    blockCentR = 574;
    blockCentC = 505;
    minRad = 70;
    maxRad = 325;
    meanInd = 350;
    COMstdScale = 0.075;

    cntrScale = 10;
    cntrMinScale = 1;
    cntrPowellTol = 1;
    cntrFracTol1d = 0.01;

    // PV
    pvMap["pressure"]    = "pressureSampleChamber_06_30_2018_19_25_55-07_01_2018_07_15_50-8521.dat";
    pvMap["UVcounts"]    = "UVsampleChamberCam_06_30_2018_19_25_55-07_01_2018_07_15_50-8521.dat";
    pvMap["bunkerTemp"]  = "bunkerTemperature_06_30_2018_19_25_55-07_01_2018_07_15_50-8521.dat";
    pvMap["highBayTemp"] = "highBayTemperature_06_30_2018_19_25_55-07_01_2018_07_15_50-8521.dat";
  }
  else if ((runName.compare("20180629_1630") == 0)
            || (runName.compare("20180629_1619") == 0)
            || (runName.compare("20180629") == 0)) {

    // Image parameters
    QperPix = 0.0223;
    legStdCut = 3.0;
    NbinsSkip = 50; //28;
    imgMatType = "uint16";

    // Measurement parameters
    timeZero = 0.3;
    hasRef = true;
    refStagePosCut = 154.0;
    refSubtractStagePos.push_back((int)(153.0000001*scaleStagePos));
    refSubtractStagePos.push_back((int)(153.0500001*scaleStagePos));
    //refSubtractStagePos.push_back((int)(154.2350001*scaleStagePos));
    refSubtractStagePos.push_back((int)(154.2450001*scaleStagePos));
    //refSubtractStagePos.push_back((int)(154.2550001*scaleStagePos));
    refSubtractStagePos.push_back((int)(154.2650001*scaleStagePos));

    // Bad Regions
    std::pair<float, float> brp;
    brp.first = 1;    brp.second = 2;
    badRegions[1530500].push_back(brp);
    brp.first = 5.5;  brp.second = 6.5;
    badRegions[1530000].push_back(brp);
    brp.first = 4.6;  brp.second = 5.2;
    badRegions[1542450].push_back(brp);


    // Filtering
    suppressBins = 75;
    padMaxHeight = 2;

    NfinalPoints  = 3;

    // Bad scans
    /*
    for (int i=163; i<177; i++) {
      badScans.push_back(i);
    }
    badScans.push_back(163);
    badScans.push_back(176);
    badScans.push_back(197);
    */

    badScans.push_back(89);
    badScans.push_back(197);
    for (int i=162; i<177; i++) {
      badScans.push_back(i);
    }
    badImages[19].push_back(1542450);
    badImages[26].push_back(1542750);
    badImages[26].push_back(1550300);
    badImages[84].push_back(1542550);
    badImages[87].push_back(1543050);
    badImages[108].push_back(1542750);
    badImages[110].push_back(1543050);
    badImages[121].push_back(1543400);
    badImages[135].push_back(1544000);
    badImages[136].push_back(1542950);
    badImages[140].push_back(1542650);
    badImages[163].push_back(1542750);
    badImages[163].push_back(1544000);
    badImages[184].push_back(1542550);
    badImages[198].push_back(1544150);

    // Background
    backgroundImage = "backgroundImg-20180629_1619.dat";
    hasLaserBkg = true;
    laserClusterRemoval = false;

    int row, col;
    int rad = 57;
    int hRad = 48;
    nanMap.clear();
    nanMap.resize(1024);
    for (uint ir=0; ir<nanMap.size(); ir++) {
      nanMap[ir].resize(1024, 0);
    }
    if (true) {
      for (int ir=520; ir<660; ir++) {
        for (int ic=443; ic<583; ic++) {
          row = ir - 570;
          col = ic - 535;
          if (rad > std::sqrt(row*row + col*col)) {
            nanMap[ir][ic] = NANVAL;
          }
          row = ir - 590;
          col = ic - 518;
          if (sqrt(row*row + col*col) < hRad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }

      rad = 45;
      for (int ir=420; ir<660; ir++) {
        for (int ic=443; ic<583; ic++) {
          row = ir - 565;
          col = ic - 510;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }

      for (int ir=540; ir<610; ir++) {
        for (int ic=560; ic<630; ic++) {
          row = ir - 575;
          col = ic - 575;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }

      rad = 58;
      for (int ir=560; ir<680; ir++) {
        for (int ic=510; ic<630; ic++) {
          row = ir - 585;
          col = ic - 550;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }

      rad = 85;
      for (int ir=0; ir<rad; ir++) {
        for (int ic=0; ic<rad; ic++) {
          if (sqrt(ir*ir + ic*ic) < rad) {
            nanMap[595+ir][488-ic] = NANVAL;
          }
        }
      }

      rad = 14;
      for (int ir=-1*rad; ir<rad; ir++) {
        for (int ic=-1*rad; ic<rad; ic++) {
          if (sqrt(ir*ir + ic*ic) < rad) {
            nanMap[630+ir][490+ic] = NANVAL;
          }
        }
      }

      int radM = 90;
      int radm = 45;
      for (int ir=0; ir<radM; ir++) {
        for (int ic=0; ic<radM; ic++) {
          if (494 + ic < 540) continue;
          if (sqrt(ir*ir + ic*ic) < radM && sqrt(ir*ir + ic*ic) > radm) {
            nanMap[575-ir][494+ic] = NANVAL;
          }
        }
      }
    }


   

    // Remove hole
    holeR = 590;
    holeC = 513;
    holeRad = 50;

    /////  Center Finding Parameters  /////
    // Rough center finding
    sigma = 8;
    blockCentR = 568;
    blockCentC = 495;
    minRad = 70;
    maxRad = 350;
    meanInd = 350;
    COMstdScale = 0.075;

    cntrScale = 10;
    cntrMinScale = 1;
    cntrPowellTol = 1;
    cntrFracTol1d = 0.01;

    I0minPixVal = 500;
    I0approxR   = 166;
    I0approxC   = 245;
    gasShiftCut = 0.07;

    // Pressure measurements
    pvMap["pressure"]    = "pressureSampleChamber_06_29_2018_16_30_40-06_30_2018_16_04_40-16970.dat";
    pvMap["UVcounts"]    = "UVsampleChamberCam_06_29_2018_16_30_40-06_30_2018_16_04_40-16970.dat";
    pvMap["bunkerTemp"]  = "bunkerTemperature_06_29_2018_16_30_40-06_30_2018_16_04_40-16970.dat";
    pvMap["highBayTemp"] = "highBayTemperature_06_29_2018_16_30_40-06_30_2018_16_04_40-16970.dat";
  }
  else if ((runName.compare("20180627_1551") == 0)
            || (runName.compare("20180627_1116") == 0)
            || (runName.compare("20180627") == 0)) {

    // Image parameters
    QperPix = 0.0223;
    legStdCut = 3.0;
    NbinsSkip = 50; //25;
    imgMatType    = "uint16";

    // Filtering
    suppressBins = 75;
    padMaxHeight = 6.5;

    // Measurement parameters
    timeZero        = 0.0;
    hasRef          = true;
    NfinalPoints    = 4;
    refStagePosCut  = 154.0; //154.290;
    refSubtractStagePos.push_back((int)(153.0*scaleStagePos));
    refSubtractStagePos.push_back((int)(153.01*scaleStagePos));
    //refSubtractStagePos.push_back((int)(154.2750*scaleStagePos));
    //refSubtractStagePos.push_back((int)(154.2850*scaleStagePos));

    // Bad Regions
    std::pair<float, float> brp;
    brp.first = 5.3;    brp.second = 5.8;
    badRegions[1530000].push_back(brp);
    brp.first = 6.2;    brp.second = 7;
    badRegions[1530100].push_back(brp);
 
    // Bad scans
    /*
    badScans.push_back(9);
    badScans.push_back(38);
    badScans.push_back(91);
    badScans.push_back(107);
    badScans.push_back(108);
    badScans.push_back(121);
    */
    for (int i=1; i<=15; i++) {
      badScans.push_back(i);
    }
    for (int i=47; i<=49; i++) {
      badScans.push_back(i);
    }
    for (int i=100; i<=121; i++) {
      badScans.push_back(i);
    }
    //for (int i=1; i<=121; i++) {
    //  badImages[i].push_back(1530000);
    //}

    /*
    badScans.push_back(79);
    badScans.push_back(53);
    badScans.push_back(23);
    badScans.push_back(37);
    badScans.push_back(87);
    badScans.push_back(18);
    badScans.push_back(55);
    badScans.push_back(39);
    */

/*
    badScans.push_back(19);
    badScans.push_back(75);
    badScans.push_back(25);
    badScans.push_back(92);
    badScans.push_back(74);
    badScans.push_back(48);
*/

    /*
    for (int i=58; i<=68; i++) {
      badScans.push_back(i);
    }
    */

    //badScans.push_back(37);
    //badScans.push_back(74);
    //badScans.push_back(40);
    //badScans.push_back(33);
    //badScans.push_back(83);
    //badScans.push_back(29);

    /*
    for (int i=32; i<=37; i++) {
      badScans.push_back(i);
    }
    badScans.push_back(73);
    badScans.push_back(74);
    badScans.push_back(29);
    */


    //badScans.push_back(18);
    //badScans.push_back(40);
    //badScans.push_back(92);
    //badScans.push_back(52);
    /*
    badImages[7].push_back(1530100);
    badImages[20].push_back(1543950);
    badImages[24].push_back(1544250);
    badImages[26].push_back(1544550);
    badImages[32].push_back(1530100);
    badImages[46].push_back(1543650);
    badImages[48].push_back(1565700);
    badImages[63].push_back(1544100);
    badImages[65].push_back(1544100);
    badImages[70].push_back(1543450);
    badImages[71].push_back(1542750);
    badImages[72].push_back(1542750);
    badImages[86].push_back(1544400);
    badImages[96].push_back(1544250);
    badImages[102].push_back(1543350);
    badImages[115].push_back(1530100);
    */

    /*
    for (int i=10; i<=18; i++) {
      badImages[i].push_back(1530000);
      badImages[i].push_back(1530100);
    }
    for (int i=49; i<=56; i++) {
      badImages[i].push_back(1530000);
      badImages[i].push_back(1530100);
    }
    for (int i=76; i<=79; i++) {
      badImages[i].push_back(1530000);
      badImages[i].push_back(1530100);
    }
    for (int i=85; i<=100; i++) {
      badScans.push_back(i);
    }
    */

    /*
    badScans.push_back(9);
    badScans.push_back(38);
    badScans.push_back(91);
    badScans.push_back(108);
    badScans.push_back(121);
    */

    /*
    for (int i=32; i<=34; i++) {
      badScans.push_back(i);  // Pressure inscrease
    }
    for (int i=51; i<=52; i++) {
      badScans.push_back(i);  // Pressure inscrease
    }
    for (int i=63; i<=71; i++) {
      badScans.push_back(i);  // Pressure inscrease
    }
    for (int i=90; i<=96; i++) {
      badScans.push_back(i);  // Pressure inscrease
    }
    */

    // Original
    /*
    badScans.push_back(108);
    badScans.push_back(121);
    badScans.push_back(24);
    badScans.push_back(38);
    badScans.push_back(48);
    badScans.push_back(91);
    badScans.push_back(9);
    */

    // Background
    backgroundImage = "backgroundImg-20180627_1116.dat";
    //refCorrection   = "/reg/neh/home/khegazy/analysis/nitrobenzene/UED/mergeScans/results/data-20180627_1551_azmAvgDiff_referenceCorrection[555].dat";
    hasLaserBkg     = true;
    laserClusterRemoval = false;

    int row, col;
    int rad = 52;
    int hRad = 55;
    nanMap.clear();
    nanMap.resize(1024);
    for (uint ir=0; ir<nanMap.size(); ir++) {
      nanMap[ir].resize(1024, 0);
    }
    if (true) {
      for (int ir=520; ir<660; ir++) {
        for (int ic=443; ic<583; ic++) {
          row = ir - 570;
          col = ic - 535;
          if (rad > std::sqrt(row*row + col*col)) {
            nanMap[ir][ic] = NANVAL;
          }
          row = ir - 590;
          col = ic - 518;
          if (sqrt(row*row + col*col) < hRad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }

      rad = 50;
      for (int ir=420; ir<660; ir++) {
        for (int ic=443; ic<583; ic++) {
          row = ir - 565;
          col = ic - 510;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }

      rad = 46;
      for (int ir=530; ir<700; ir++) {
        for (int ic=560; ic<630; ic++) {
          row = ir - 575;
          col = ic - 575;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }

      for (int ir=600; ir<630; ir++) {
        for (int ic=550; ic<630; ic++) {
          nanMap[ir][ic] = NANVAL;
        }
      }

      rad = 15;
      for (int ir=572; ir<612; ir++) {
        for (int ic=640; ic<670; ic++) {
          row = ir - 587;
          col = ic - 652;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }
      rad = 20;
      for (int ir=560; ir<610; ir++) {
        for (int ic=342; ic<392; ic++) {
          row = ir - 582;
          col = ic - 367;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }
      rad = 15;
      for (int ir=700; ir<747; ir++) {
        for (int ic=57; ic<98; ic++) {
          row = ir - 722;
          col = ic - 78;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }
    }
      rad = 15;
      for (int ir=700; ir<747; ir++) {
        for (int ic=57; ic<98; ic++) {
          row = ir - 722;
          col = ic - 78;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }
      rad = 20;
      for (int ir=560; ir<610; ir++) {
        for (int ic=342; ic<392; ic++) {
          row = ir - 582;
          col = ic - 367;
          if (sqrt(row*row + col*col) < rad) {
            nanMap[ir][ic] = NANVAL;
          }
        }
      }

    // Remove hole
    holeR = 590; //587; //590;
    holeC = 513; //512; //513;
    holeRad = 45; //43; //45;

    /////  Center Finding Parameters  /////
    // Rough center finding
    sigma = 8;
    blockCentR = 573;
    blockCentC = 500;
    minRad = 70;
    maxRad = 325;
    meanInd = 350;
    COMstdScale = 0.075;

    cntrScale = 10;
    cntrMinScale = 1;
    cntrPowellTol = 1;
    cntrFracTol1d = 0.01;

    I0minPixVal = 500;
    I0approxR = 155;
    I0approxC = 243;
    gasShiftCut = 0.07;

    // PV files / variables
    pvMap["pressure"]    = "pressureSampleChamber_06_27_2018_15_51_20-06_28_2018_13_27_15-15553.dat";
    pvMap["UVcounts"]    = "UVsampleChamberCam_06_27_2018_15_51_20-06_28_2018_13_27_15-15553.dat";
    pvMap["bunkerTemp"]  = "bunkerTemperature_06_27_2018_15_51_20-06_28_2018_13_27_15-15553.dat";
    pvMap["highBayTemp"] = "highBayTemperature_06_27_2018_15_51_20-06_28_2018_13_27_15-15553.dat";

    throttle = 103; //uJ or 53 degrees

    // Variables for studies
    bkgStudyRanges.resize(4);
    bkgStudyRanges[0].push_back(5.5);   bkgStudyRanges[0].push_back(6);
    bkgStudyRanges[1].push_back(6);     bkgStudyRanges[1].push_back(6.8);
    bkgStudyRanges[1].push_back(5.5);   bkgStudyRanges[1].push_back(6.8);
    bkgStudyRanges[2].push_back(2);     bkgStudyRanges[2].push_back(3);
    bkgStudyRanges[3].push_back(4);     bkgStudyRanges[3].push_back(5.5);

  }
  else if (runName.compare("simulateReference") == 0) {
    
    QperPix = 0.0223;
    NbinsSkip = 50; //28;
    switch (molecule) {
      case initialState: {
        xyzFiles.push_back("17050202_Nitrobenzene_opt_B3LYP_6-31G.xyz");
        break;
      }

      case finalState1: {
        xyzFiles.push_back("18062101_phenyloxy_opt_B3LYP_6-31G.xyz");
        xyzFiles.push_back("18062102_NO_opt_B3LYP_6-31G.xyz");
        break;
      }

      case finalState2: {
        xyzFiles.push_back("./hotEnsemble/ring.xyz");
        xyzFiles.push_back("./hotEnsemble/ONO.xyz");
        //xyzFiles.push_back("phenyl.xyz");
        //xyzFiles.push_back("nitrogenDioxide.xyz");
        break;
      }

      case finalState3: {
        xyzFiles.push_back("./hotEnsemble/O_dissoc.xyz");
        xyzFiles.push_back("O.xyz");
        //xyzFiles.push_back("nitrosobenzene.xyz");
        //xyzFiles.push_back("O.xyz");
        break;
      }

      case finalState4: {
        xyzFiles.push_back("./hotEnsemble/singlet_aligned.xyz");
        break;
      }
      
      case finalState5: {
        xyzFiles.push_back("./hotEnsemble/triplet_aligned.xyz");
        break;
      }
      /*
      case intermediateStates: {                    
        // Intermediate States
        xyzFiles.push_back("gsEP.xyz");
        xyzFiles.push_back("gsNO.xyz");
        xyzFiles.push_back("s1min.xyz");
        xyzFiles.push_back("s1s0CI.xyz");
        xyzFiles.push_back("s1t2STC.xyz");
        xyzFiles.push_back("s2s1CI.xyz");
        xyzFiles.push_back("s3min.xyz");
        xyzFiles.push_back("s4min.xyz");
        xyzFiles.push_back("t1min.xyz");
        xyzFiles.push_back("t1s0STCEP.xyz");
        xyzFiles.push_back("t1s0STC-NO.xyz");
        xyzFiles.push_back("t2min.xyz");
        xyzFiles.push_back("t2t1CI.xyz");
      }
      */

      default: {
        std::cerr << "ERROR: do not recognize molecule enum!!!\n";
        exit(0);
      }
    }
  }
  else if (runName.compare("doRunLists") == 0) {
  }
  else if (runName.compare("other") == 0) {
  }
  else {
    std::cerr << "ERROR: Cannot set values for run " + runName + "!!!\n";
    exit(0);
  }

  readoutAzmBinStart = readoutStart*NradAzmBins; //400
  readoutAzmBinEnd   = readoutEnd*NradAzmBins; //450
  readoutLegBinStart = readoutStart*NradLegBins;
  readoutLegBinEnd   = readoutEnd*NradLegBins;


  refStagePosCut *= scaleStagePos;
  maxQazm   = QperPix*NradAzmBins;
  maxRbins  = rMaxAzmRat*((NradAzmBins + NautCpadding)/2 + 1);
  maxR      = maxRbins*(2*PI/(QperPix*(NradAzmBins + NautCpadding)));

  R1Bin = 1/(2*PI/(QperPix*(NradAzmBins + NautCpadding)));
  R8Bin = 8/(2*PI/(QperPix*(NradAzmBins + NautCpadding)));

}


