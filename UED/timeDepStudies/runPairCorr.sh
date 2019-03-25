#!/bin/bash 

./pairCorr.exe 20180627_1551 -FillQ zeros
#./pairCorr.exe 20180627_1551 -lowQtheory ./results/sim-phenoxyRadical_LowQfill_scale-0.400000_Bins[555].dat 
#./pairCorr.exe 20180629_1630 -lowQtheory ./results/sim-phenoxyRadical_LowQfill_scale-0.400000_Bins[555].dat 
#./pairCorr.exe 20180630_1925 -lowQtheory ./results/sim-phenoxyRadical_LowQfill_scale-0.400000_Bins[555].dat
#./pairCorr.exe 20180701_0746 -lowQtheory ./results/sim-phenoxyRadical_LowQfill_scale-0.400000_Bins[555].dat

#SMOOTH='0.025000'
#./pairCorr.exe 20180627_1551 -Idir /reg/ued/ana/scratch/nitroBenzene/mergeScans/ -Fname data-20180627_1551-tSmeared-${SMOOTH}-sMsAzmAvgDiff[1152,555].dat -Osuf -tSmeared -FillQ zeros
#./pairCorr.exe 20180629_1630 -Idir /reg/ued/ana/scratch/nitroBenzene/mergeScans/ -Fname data-20180629_1630-tSmeared-${SMOOTH}-sMsAzmAvgDiff[402,555].dat -Osuf -tSmeared -lowQtheory ./results/sim-phenoxyRadicalLowQfill[555].dat
#./pairCorr.exe 20180630_1925 -Idir /reg/ued/ana/scratch/nitroBenzene/mergeScans/ -Fname data-20180630_1925-tSmeared-${SMOOTH}-sMsAzmAvgDiff[402,555].dat -Osuf -tSmeared -lowQtheory ./results/sim-phenoxyRadicalLowQfill[555].dat
#./pairCorr.exe 20180701_0746 -Idir /reg/ued/ana/scratch/nitroBenzene/mergeScans/ -Fname data-20180701_0746-tSmeared-${SMOOTH}-sMsAzmAvgDiff[402,555].dat -Osuf -tSmeared -lowQtheory ./results/sim-phenoxyRadicalLowQfill[555].dat

#######################################
#####  Time Dependend Simulation  #####
#######################################

#NTIME=450
#./pairCorr.exe simulateReference -Idir /reg/ued/ana/scratch/nitroBenzene/simulations/timeDependent/ -Fname dissociation_phenyl-N2O_azmAvgSMS_Qmax-12.376500_Ieb-5.000000_scrnD-4.000000_elE-3700000.000000_Bins[400,555].dat -Osuf -dissociation-phenyl-N2O -FillQ zeros 
#./pairCorr.exe simulateReference -Idir /reg/ued/ana/scratch/nitroBenzene/simulations/timeDependent/ -Fname rotation_nitrobenzene_azmAvgSMS_Qmax-12.376500_Ieb-5.000000_scrnD-4.000000_elE-3700000.000000_Bins[800,555].dat -Osuf -rotation-nitrobenzene -FillQ false 

#######################################################
#####  Difference PC with Simulated Final States  #####
#######################################################

#./pairCorr.exe simulateReference -Idir /reg/ued/ana/scratch/nitroBenzene/simulations/ -Fname phenoxyRadical_sMsPatternLineOut_Qmax-12.376500_Ieb-5.000000_scrnD-4.000000_elE-3700000.000000_Bins[555].dat -Osuf PhenoxyDiff -saveLowQtheory true -SubR true -FillQ false -FitPC true

##############################################
#####  Reference Image / Theory Compare  #####
##############################################

#RUNNAMES=( "20180627_1551" "20180629_1630" "20180630_1925" "20180701_0746" )

#./pairCorr.exe simulateReference -Idir /reg/ued/ana/scratch/nitroBenzene/simulations/ -Fname nitrobenzene_sMsPatternLineOut_Qmax-12.376500_Ieb-5.000000_scrnD-4.000000_elE-3700000.000000_Bins[555].dat -FillQ false -Osuf Nitrobenzene -FitPC true

#for run in "${RUNNAMES[@]}"
#do
#  ./pairCorr.exe ${run} -Idir ../staticDiffraction/results/ -Fname staticDiffraction_${run}[555].dat -Osuf -reference -FillQ theory -FitPC true
#done

### change molecule to phenoxyRadical
#./pairCorr.exe simulateReference -Idir /reg/ued/ana/scratch/nitroBenzene/simulations/ -Fname phenoxyRadical_sMsPatternLineOut_Qmax-12.376500_Ieb-5.000000_scrnD-4.000000_elE-3700000.000000_Bins[555].dat -FillQ false
