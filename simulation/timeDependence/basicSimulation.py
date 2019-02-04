import numpy as np
import copy
from subprocess import call
import sys
sys.path.append('/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts')
from plotClass import plotCLASS

plc = plotCLASS()

XYZfile = "../XYZfiles/17050202_Nitrobenzene_opt_B3LYP_6-31G.xyz"    

class atomStruct:
  
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

def writeXYZfile(atoms, folder, fileName):
  with open(folder+fileName+".xyz", "w") as xyz:
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


################################
#####  Simulation Classes  #####
################################

class dissociation:

  def __init__(self, atoms):
    self.startTime = 0. #ps
    self.endTime = 1. #ps
    self.m_N2O = (2*8 + 7)*1.7e-27      #kg
    self.m_phenyl = (5 + 6*6)*1.7e-27   #kg
    self.momentum = np.sqrt(4.8e-19*2*self.m_N2O*self.m_phenyl/(self.m_N2O + self.m_phenyl))
    self.velocityScale = (self.momentum/self.m_N2O)*1e10*1e-12    #Angs/ps
    #self.velocityScale = np.sqrt(4.8e-19/(0.5*23*1.7e-27))*1e10*1e-12   #Angs/ps
    print("dissocition (angs/ps): ", self.velocityScale)

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
    self.velocity = atoms['N0'].position - atoms[closestC].position
    self.velocity *= self.velocityScale/np.linalg.norm(self.velocity)


  def update(self, atoms, atomsOrig, time):
    print("testDist inUp: ",np.linalg.norm(atomsOrig["O0"].position-atomsOrig["C0"].position))
    atoms['N0'].position = atomsOrig['N0'].position + time*self.velocity
    atoms['O0'].position = atomsOrig['O0'].position + time*self.velocity
    atoms['O1'].position = atomsOrig['O1'].position + time*self.velocity
    print("testDist innUp: ",np.linalg.norm(atomsOrig["O0"].position-atomsOrig["C0"].position))

    return atoms


class rotation:

  def __init__(self, atoms):
    self.startTime      = 0. #ps
    self.endTime        = 2. #ps
    self.TaccStart      = 0.1 #ps
    self.rotationPeriod = 0.4 #ps
    self.rotationFreq   = 2.*np.pi/self.rotationPeriod
    self.deltaTaccStop  = 0.05
    self.rotationAcc    = self.rotationFreq/self.deltaTaccStop
    self.thetas = []
    self.distO1 = []
    self.distO2 = []

    ###  Find carbon closest to N  ###
    closestC = ''
    minDist = 10
    for key,val in atoms.iteritems():
      if val.atomType != 'C':
        continue
      
      if np.linalg.norm(val.position - atoms['N0'].position) < minDist:
        minDist   = np.linalg.norm(val.position - atoms['N0'].position)
        closestC  = key

    ###  Calculate rotation axis  ###
    self.angMomVec = atoms['N0'].position - atoms[closestC].position
    self.angMomVec /= np.linalg.norm(self.angMomVec)

    self.W = np.array( [[0, -1*self.angMomVec[2], self.angMomVec[1]],
                        [self.angMomVec[2], 0, -1*self.angMomVec[0]],
                        [-1*self.angMomVec[1], self.angMomVec[0], 0]])
    self.W2 = np.dot(self.W, self.W)


  def update(self, atoms, atomsOrig, time):

    time -= self.TaccStart
    if time < 0:
      return copy.deepcopy(atomsOrig)

    if (time > self.deltaTaccStop):
      theta = 0.5*self.rotationAcc*self.deltaTaccStop**2\
          + self.rotationFreq*(time - self.deltaTaccStop)
    else:
      theta = 0.5*self.rotationAcc*time**2

    self.thetas.append(theta % 2*np.pi)
    # Rodrigues Rotation Formula
    rotationMat = np.eye(3) + np.sin(theta)*self.W + (1 - np.cos(theta))*self.W2
    #print(atomsOrig["O0"].position - atomsOrig["N0"].position)
    #print(np.dot(rotationMat,atomsOrig["O0"].position - atomsOrig["N0"].position))
    atoms["O0"].position = atomsOrig["N0"].position\
                            + np.dot(
                                rotationMat, 
                                atomsOrig["O0"].position - atomsOrig["N0"].position)
    atoms["O1"].position = atomsOrig["N0"].position\
                            + np.dot(
                                rotationMat, 
                                atomsOrig["O1"].position - atomsOrig["N0"].position)

    self.distO1.append(np.linalg.norm(atoms["O0"].position-atoms["C1"].position))
    self.distO2.append(np.linalg.norm(atoms["O1"].position-atoms["C1"].position))
    print("testDist inUp: ",np.linalg.norm(atoms["O0"].position-atoms["N0"].position))
    return atoms


class bending:

  def __init__(self, atoms):
    self.bendPeriod = 0.4 #ps
    self.maxBendAng = 2*np.pi/6 #rad
    self.endTime    = 5.  #ps

    ###  Find carbon closest to N  ###
    self.closestC = ''
    minDist = 10
    for key,val in atoms.iteritems():
      if val.atomType != 'C':
        continue
      
      if np.linalg.norm(val.position - atoms['N0'].position) < minDist:
        minDist   = np.linalg.norm(val.position - atoms['N0'].position)
        self.closestC  = key

    ###  Calculate rotation axis  ###
    self.angMomVec = atoms['N0'].position - atoms[self.closestC].position
    self.angMomVec /= np.linalg.norm(self.angMomVec)

    self.W = np.array( [[0, -1*self.angMomVec[2], self.angMomVec[1]],
                        [self.angMomVec[2], 0, -1*self.angMomVec[0]],
                        [-1*self.angMomVec[1], self.angMomVec[0], 0]])
    self.W2 = np.dot(self.W, self.W)


  def update(self, atoms, atomsOrig, time):

    theta = self.maxBendAng*np.sin(time*self.bendPeriod)

    # Rodrigues Rotation Formula
    rotationMat = np.eye(3) + np.sin(theta)*self.W + (1 - np.cos(theta))*self.W2
    rotationMatNeg = np.eye(3) - np.sin(theta)*self.W + (1 - np.cos(theta))*self.W2
    for key,val in atomsOrig.iteritems():
      if val.atomType == 'C' and key != self.closestC:
        if val.position[0] > atomsOrig[self.closestC]:
          atoms[key].position = np.dot(rotationMat, val.position)
        else:
          atoms[key].position = np.dot(rotationMatNeg, val.position)

    return atoms



if __name__ == "__main__":


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



  ###  Get Delay Times  ###

  useDelayTimes = False
  delayTimes = np.fromfile(
      "../../UED/mergeScans/results/timeDelays[30].dat", 
      dtype=np.double)

  dt        = 0.0025  #ps

  #########################
  #####  Simulations  #####
  #########################

  simulations = {
      "dissociation_phenyl-N2O" : dissociation(atomsOrig),
      "rotation_nitrobenzene"   : rotation(atomsOrig)
      #"bending_nitrobenzene"    : bending(atomsOrig)
      }

  simFolder = "/reg/ued/ana/scratch/nitroBenzene/simulations/"
  groundStateSMS = np.fromfile(
      simFolder+"nitrobenzene_sMsPatternLineOut"+
        "_Qmax-12.376500_Ieb-5.000000_scrnD-4.000000"+
        "_elE-3700000.000000_Bins[555].dat", dtype=np.double)
  groundState = np.fromfile(
      simFolder+"nitrobenzene_molDiffractionPatternLineOut"+
        "_Qmax-12.376500_Ieb-5.000000_scrnD-4.000000"+
        "_elE-3700000.000000_Bins[555].dat", dtype=np.double)


  #############################
  #####  Simulation Loop  #####
  #############################

  for name, simulation in simulations.iteritems():

    sampleTimes = None
    if (useDelayTimes):
      sampleTimes = delayTimes
    else:
      Nsteps    = int((simulation.endTime-simulation.startTime)/dt)
      sampleTimes = np.linspace(simulation.startTime, simulation.endTime, Nsteps)

    sInd = 0
    diffSMSTD = []
    diffTD = []
    for tm in sampleTimes:
      if tm < 0:
        call(["cp", XYZfile, 
          simFolder+"timeDependent/"+name+"_time-"+str(tm)+".xyz"])
        diffTD.append(groundState)
        diffSMSTD.append(groundStateSMS)
        sInd += 1
      else:
        break

    tmInd = 0
    for tm in sampleTimes[sInd:]:
      if tm > simulation.endTime:
        break

      # Update
      atoms = simulation.update(atoms, atomsOrig, tm)
      print("testDist outUp: ",np.linalg.norm(atoms["O0"].position-atoms["C0"].position))

      fileName = name+"_time-"+str(tm)
      writeXYZfile(atoms, simFolder+"timeDependent/XYZfiles/", fileName)

      print(tm, atoms["N0"].position)
      ###  Simulate Diffraction Pattern  ###
      call(["./../diffractionPattern/simulateRefPatterns.exe",
          "-XYZdir", simFolder+"timeDependent/XYZfiles",
          "-InpXYZ", fileName+".xyz",
          "-Ofile", fileName,
          "-Odir", simFolder+"/timeDependent/"])

      diffSMSLO = np.fromfile(simFolder+"timeDependent/" + fileName +
          "_sMsPatternLineOut_Qmax-12.376500_Ieb-5.000000" +
          "_scrnD-4.000000_elE-3700000.000000_Bins[555].dat",
          dtype=np.double)
      diffLO = np.fromfile(simFolder+"timeDependent/" + fileName +
          "_molDiffractionPatternLineOut_Qmax-12.376500_Ieb-5.000000" +
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

    outFileName = simFolder + "timeDependent/"\
        + name + "_azmAvgSMS"\
        + "_Qmax-12.376500_Ieb-5.000000"\
        + "_scrnD-4.000000_elE-3700000.000000_Bins["\
        + str(diffTD.shape[0])+","+str(diffTD.shape[1])+"].dat"
    with open(outFileName, "wb") as outFile:
      diffSMSTD.tofile(outFile)

    outFileName = simFolder+"timeDependent/"\
        + name + "_azmAvg"\
        + "_Qmax-12.376500_Ieb-5.000000"\
        + "_scrnD-4.000000_elE-3700000.000000_Bins["\
        + str(diffTD.shape[0])+","+str(diffTD.shape[1])+"].dat"
    with open(outFileName, "wb") as outFile:
      diffTD.tofile(outFile)



    timeFileName = simFolder+"timeDependent/"\
        + name + "_timeDelays["\
        + str(diffTD.shape[0])+"].dat"
    with open(timeFileName, "wb") as outFile:
      sampleTimes.tofile(outFile)

  """
  plc.print2d(diffTD,
      "testing",
      isFile=False)
  """
