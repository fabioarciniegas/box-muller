import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

histogram_from_athena=\
    {"100.666664":6.0,"109.0":1.0,"116.0":2.0,"119.5":2.0,"123.0":1.0,"127.0":1.0,"141.5":2.0,"145.0":1.0,"153.5":2.0,"156.33333":3.0,"160.0":1.0,"170.0":1.0,"192.0":1.0,"240.0":1.0,"30.0":1.0,"318.0":1.0,"36.0":1.0,"4.75":4.0,"41.0":3.0,"46.666668":3.0,"51.666668":3.0,"54.57143":7.0,"56.25":8.0,"60.375":8.0,"65.0":1.0,"71.0":1.0,"90.333336":3.0}




def raw_numbers_from_histogram_map(h):
    result = []
    values = [math.floor(float(i)) for i in histogram_from_athena.keys()]
    for i,v in enumerate(values):
        for t in range(i):
            result.append(v)
    return result


plt.hist([math.floor(float(i)) for i in histogram_from_athena.keys()], weights=histogram_from_athena.values(),
         bins=len(histogram_from_athena.keys()),density=True)

mu,sd = norm.fit(raw_numbers_from_histogram_map(histogram_from_athena))


x_min,x_max = plt.xlim()
x = np.linspace(x_min,x_max)
p = norm.pdf(x, mu, sd)
plt.plot(x, p, linewidth=2, color='r')
plt.show()

print(f"μ = %.2f, σ = %.2fmu, 3.5 z-score value (anomaly)= %.2f" % (mu,sd,abs((3.5*sd+mu))))