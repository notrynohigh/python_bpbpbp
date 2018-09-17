import numpy as np
import pandas as pd
from pandas import Series
from matplotlib import pyplot
import os
import math
import time

import wavelet

cur_dir = os.getcwd()
os.chdir(cur_dir)

fileName = "50ms3.txt"

data = pd.read_table(fileName,sep='CRLF',names=['raw'],engine='python')
row = data.shape[0]

data['pressure'] = np.ones((row,1), dtype=np.int)

for i in range(row):
    data.pressure.loc[i] = int(data.iloc[i,0])
    
####基础绘图
pyplot.figure()
pyplot.title(fileName, fontproperties="SimHei")
pyplot.plot(data.pressure, color="g")
pyplot.legend("P",loc="upper left")
pyplot.axhline(0,linestyle=":",color="g")
pyplot.show()

wavelet.plot_signal_decomp(data.pressure,'db5', "blood pressure")
