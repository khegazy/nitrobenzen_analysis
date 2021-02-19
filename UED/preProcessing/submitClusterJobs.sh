#!/bin/bash 

MAINDIR=/cds/home/k/khegazy/analysis/2018/nitrobenzene/UED
OUTDIR=/cds/group/ued/scratch/khegazy/nitrobenzene/preProcessing/
FILETORUN=preProcessing.exe

COMPUTECENTERS=false


if [ -z "$1" ]; then
  echo "ERROR SUBMITTING JOBS!!!   Must give the type and and optionally the name of the run (i.e Run/Background and 20180701_0746)!"
  exit
fi

RUNTYPE=${1}

if [ -z "$2" ]; then
  RUNNAME="*"
else
  RUNNAME=${2}"*"
fi

if [ -z "$3" ]; then
  RESUBMIT=false
else
  RESUBMIT=true
fi

#make clean; make
sleep 5
OUTPUTDIR=${OUTDIR}/logs/
for file in runLists/runList_${RUNTYPE}-${RUNNAME}
do

  strPos=$(($strPos + $subDLength + 11))

  CUTBEGINNING=${file#*runList_}
  OUTPUTFILENAME=${CUTBEGINNING%.*} #${1}-${2}
  ROOTFILENAME=${OUTDIR}${OUTPUTFILENAME}".root"

  if [[ "$RESUBMIT" = true ]] && [[ ! -f ${ROOTFILENAME} ]]; then
    continue
  fi

  if [[ "$file" == *"I0"* ]]; then
    continue 
  fi

  echo "Submitting "${file}
  echo ${OUTPUTDIR}${OUTPUTFILENAME}".log"
  bsub -q psanaq -o${OUTPUTDIR}${OUTPUTFILENAME}".log" ./${FILETORUN} ${file}
  #bsub -q psanaq -o${OUTPUTDIR}${OUTPUTFILENAME}".log" ./${FILETORUN} ${file} -computeCenters 1


  #if [ COMPUTECENTERS ]; then

  #  echo "HHHHHHHHEEEEEEEEEERRRRRRRRr"
  #  bsub -q psanaq -o${OUTPUTDIR}${OUTPUTFILENAME}".log" ./${FILETORUN} ${file} -computeCenters 1
  #else
  #  bsub -q psanaq -o${OUTPUTDIR}${OUTPUTFILENAME}".log" ./${FILETORUN} ${file}
  #fi

done
