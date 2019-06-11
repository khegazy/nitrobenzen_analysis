#!/bin/bash

names=( gsEP.xyz gsNO.xyz s1min.xyz s1s0CI.xyz s1t2STC.xyz s2s1CI.xyz s3min.xyz s4min.xyz t1min.xyz t1s0STCEP.xyz t1s0STC-NO.xyz t2min.xyz t2t1CI.xyz )

for i in "${names[@]}"
do
  echo ${i::-4}
  echo $i
  ./simulateRefPatterns.exe -Ofile ${i::-4} -InpXYZ $i
done

