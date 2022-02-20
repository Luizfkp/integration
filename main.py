import numpy as np
import scipy.integrate

import matplotlib.pyplot as plt

doc = "test.txt"
dt_gft = np.transpose(np.genfromtxt(doc))
integrated_val = scipy.integrate.simps(dt_gft[1], dt_gft[0], dx=1, axis=-1, even='avg')
print(integrated_val)
plt.plot(dt_gft[0], dt_gft[1])
plt.show()