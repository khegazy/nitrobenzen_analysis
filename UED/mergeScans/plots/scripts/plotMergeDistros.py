import numpy as np
import matplotlib.pyplot as plt

data1 = np.fromfile("../../testDistro0[197].dat", dtype=np.double)
data2 = np.fromfile("../../testDistro1[196].dat", dtype=np.double)
data3 = np.fromfile("../../testDistro2[197].dat", dtype=np.double)

#data1 = np.fromfile(, dtype=np.double)

plt.hist(data1, bins=50)
plt.savefig("../mergeDistro_300.png")
plt.close()
plt.hist(data2, bins=50)
plt.savefig("../mergeDistro_243.png")
plt.close()
plt.hist(data3, bins=50)
plt.savefig("../mergeDistro_188.png")
plt.close()
