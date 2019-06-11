import numpy as np
import sys
sys.path.append('../../../plots/scripts')
sys.path.append('/reg/neh/home/khegazy/baseTools/UEDanalysis/plots/scripts')
from plotClass import plotCLASS
from plotParams import pltParams
from scipy.ndimage import gaussian_filter

params = pltParams()

plc = plotCLASS()


#runs = ["20180629_1630", "20180627_1551", "20180630_1925", "20180701_0746"]
runs = ["20180627_1551"]

##################################
#####  Plotting Power Scans  #####
##################################

energyTable = {
    55: 62,
    54: 55,
    53: 46,
    52: 40,
    51: 35,
    50: 29,
    49: 25,
    48: 20,
    47: 16
    }

throttles = np.fromfile(
              "../../results/data-20180627_PowerScan_throttles[8].dat", 
              np.double)
energies = []
for v in throttles:
  energies.append(energyTable[v])

for i,run in enumerate(runs):

  #####  Pair Correlation  #####
  opts = {
    "xTitle"  : "Energy uJ",
    "yTitle"  : "Ratio",
    "xSlice"  : [energies[0]-5, energies[-1]+5]
  }

  plc.print1d(["../../results/data-20180627_PowerScan_powerScanLinearity[8].dat"], 
      "../data-20180627_PowerScan_powerScanLinearity",
      errors=["../../results/data-20180627_PowerScan_powerScanLinearitySEM[8].dat"],
      X=energies,
      options=opts)
