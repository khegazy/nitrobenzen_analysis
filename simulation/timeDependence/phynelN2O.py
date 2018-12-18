import numpy as np
from subprocess import call
import sys
sys.path.append('/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts')
from plotClass import plotCLASS

plc = plotCLASS()

XYZfile = "../XYZfiles/17050202_Nitrobenzene_opt_B3LYP_6-31G.xyz"    

class atomStruct:
  
  atomType = ''
  position = None
  
  def __init__(self, atmT, pos):
    self.atomType = atmT
    self.position = pos
  

def findItemEnd(line, sInd):
  eInd = sInd
  for itm in line[sInd:]:
    if itm != ' ' and itm != '\n':
      eInd += 1
    else:
      return eInd

def findNextItem(line, eInd):
  sInd = eInd
  for itm in line[eInd:]:
    if itm == " ":
      sInd += 1
    else:
      return sInd

def writeXYZfile(atoms, fileName):
  with open("./XYZfiles/"+fileName+".xyz", "w") as xyz:
    xyz.write("   "+str(len(atoms)));
    xyz.write("\n\n")
    posLine = 9*3*2*4*" " + 6*" "
    for key,val in atoms.iteritems():
      x,y,z = "","",""
      if val.position[0] > 0:
        x = " %.7f" % (val.position[0])
      else:
        x = "%.7f" % (val.position[0])
      if val.position[1] > 0:
        y = " %.7f" % (val.position[1])      
      else:
        y = "%.7f" % (val.position[1])
      if val.position[2] > 0:
        z = " %.7f" % (val.position[2])
      else:
        z = "%.7f" % (val.position[2])

      posLine = " "+val.atomType + " "*(5-len(val.atomType))
      posLine += x[:9] + 4*" "
      posLine += y[:9] + 4*" "
      posLine += z[:9] + "\n"

      xyz.write(posLine)
    xyz.close()




velocityScale = np.sqrt(4.8e-19/(0.5*23*1.7e-27))*1e10*1e-12   #Angs/ps
print("velocityScale ",velocityScale)
rotationPeriod = 0.4 #ps

###################################
#####  Import Atom Positions  #####
###################################

atoms = {}
atomsOrig = {}
atomCount = {
  'C' : 0,
  'H' : 0,
  'N' : 0,
  'O' : 0}

with open(XYZfile, "r") as pFile:
  for i,line in enumerate(pFile):
    if i < 2:
      continue
    sInd = 1
    eInd = findItemEnd(line, sInd) 
    atomType = line[sInd:eInd]

    pos = []
    for j in range(3):
      sInd = findNextItem(line, eInd)
      eInd = findItemEnd(line, sInd)
      pos.append(float(line[sInd:eInd]))

    atoms[atomType+str(atomCount[atomType])] = atomStruct(atomType, np.array(pos))
    atomsOrig[atomType+str(atomCount[atomType])] = atomStruct(atomType, np.array(pos))
    atomCount[atomType] += 1


###  Find carbon closest to N  ###
closestC = ''
minDist = 10
for key,val in atoms.iteritems():
  if val.atomType != 'C':
    continue
  
  if np.linalg.norm(val.position - atoms['N0'].position) < minDist:
    minDist   = np.linalg.norm(val.position - atoms['N0'].position)
    closestC  = key


###  Calculate velocity  ###
velocity = atoms['N0'].position - atoms[closestC].position
velocity *= velocityScale/np.linalg.norm(velocity)

###  Get Delay Times  ###

delayTimes = np.fromfile(
    "../../UED/mergeScans/results/timeDelays[30].dat", 
    dtype=np.double)

dt        = 0.0025  #ps
startTime = delayTimes[0]
endTime   = 1.
Nsteps    = int((endTime-startTime)/dt)
print("Nsteps", Nsteps)
sampleTimes = np.linspace(startTime, endTime, Nsteps)
#sampleTimes = delayTimes



#############################
#####  Simulation Loop  #####
#############################

sInd = 0
diffSMSTD = []
diffTD = []
simFolder = "/reg/ued/ana/scratch/nitroBenzene/simulations/"
groundStateSMS = np.fromfile(
    simFolder+"nitrobenzene_sMsPatternLineOut"+
      "_Qmax-12.376500_Ieb-5.000000_scrnD-4.000000"+
      "_elE-3700000.000000_Bins[555].dat", dtype=np.double)
groundState = np.fromfile(
    simFolder+"nitrobenzene_molDiffractionPatternLineOut"+
      "_Qmax-12.376500_Ieb-5.000000_scrnD-4.000000"+
      "_elE-3700000.000000_Bins[555].dat", dtype=np.double)
for tm in sampleTimes:
  if tm < 0:
    call(["cp", XYZfile, "./XYZfiles/phynel_N2O-time-"+str(tm)+".xyz"])
    diffTD.append(groundState)
    diffSMSTD.append(groundStateSMS)
    sInd += 1
  else:
    break

tmInd = 0
for tm in sampleTimes[sInd:]:
  if tm > endTime:
    break

  atoms['N0'].position = atomsOrig['N0'].position + tm*velocity
  atoms['O0'].position = atomsOrig['O0'].position + tm*velocity
  atoms['O1'].position = atomsOrig['O1'].position + tm*velocity

  fileName = "phynel_N2O-time-"+str(tm)
  writeXYZfile(atoms, fileName)

  ###  Simulate Diffraction Pattern  ###
  call(["./../diffractionPattern/simulateRefPatterns.exe",
      "-XYZdir", "./XYZfiles",
      "-InpXYZ", fileName+".xyz",
      "-Ofile", fileName])

  diffSMSLO = np.fromfile(simFolder+
      "phynel_N2O-time-"+str(tm)+
      "_sMsPatternLineOut_Qmax-12.376500_Ieb-5.000000"+
      "_scrnD-4.000000_elE-3700000.000000_Bins[555].dat",
      dtype=np.double)
  diffLO = np.fromfile(simFolder+
      "phynel_N2O-time-"+str(tm)+
      "_molDiffractionPatternLineOut_Qmax-12.376500_Ieb-5.000000"+
      "_scrnD-4.000000_elE-3700000.000000_Bins[555].dat",
      dtype=np.double)

  diffTD.append(diffLO)
  diffSMSTD.append(diffSMSLO)


diffTD = np.array(diffTD)
diffSMSTD = np.array(diffSMSTD)

# Subtract T0
for i in range(diffTD.shape[0]):
  diffTD[i,:]     = diffTD[i,:] - groundState
  diffSMSTD[i,:]  = diffSMSTD[i,:] - groundStateSMS

outFileName = simFolder+"phynel_N2O-azmAvgSMS"\
    + "_Qmax-12.376500_Ieb-5.000000"\
    + "_scrnD-4.000000_elE-3700000.000000_Bins["\
    +str(diffTD.shape[0])+","+str(diffTD.shape[1])+"].dat"
with open(outFileName, "wb") as outFile:
  diffSMSTD.tofile(outFile)

outFileName = simFolder+"phynel_N2O-azmAvg"\
    + "_Qmax-12.376500_Ieb-5.000000"\
    + "_scrnD-4.000000_elE-3700000.000000_Bins["\
    +str(diffTD.shape[0])+","+str(diffTD.shape[1])+"].dat"
with open(outFileName, "wb") as outFile:
  diffTD.tofile(outFile)



timeFileName = simFolder+"phynel_N2O-timeDelays["\
    +str(diffTD.shape[0])+"].dat"
with open(timeFileName, "wb") as outFile:
  sampleTimes.tofile(outFile)

"""
plc.print2d(diffTD,
    "testing",
    isFile=False)
"""