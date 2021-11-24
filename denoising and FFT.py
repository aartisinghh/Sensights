import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pywt
import sys
import tsfel
import math
df_100 = pd.read_csv('100.csv')
data = df_100["\'MLII\'"].to_numpy()
index = df_100["\'sample #\'"].to_numpy()

#Denoising
#https://github.com/MProx/Wavelet-denoising/blob/master/wavelets.py


# Create wavelet object and define parameters
w = pywt.Wavelet('sym4')
maxlev = pywt.dwt_max_level(len(data), w.dec_len)
# maxlev = 2 # Override if desired
print("maximum level is " + str(maxlev))
threshold = 0.04 # Threshold for filtering

# Decompose into wavelet components, to the level selected:
coeffs = pywt.wavedec(data, 'sym4', level=maxlev)

#cA = pywt.threshold(cA, threshold*max(cA))

plt.figure()
for i in range(1, len(coeffs)):
    plt.subplot(maxlev, 1, i)
    plt.plot(coeffs[i])
    coeffs[i] = pywt.threshold(coeffs[i], threshold*max(coeffs[i]))
    plt.plot(coeffs[i])


datarec = pywt.waverec(coeffs, 'sym4')


mintime = 54000
maxtime = mintime + 2000


plt.figure()
plt.subplot(2, 1, 1)
plt.plot(index[mintime:maxtime], data[mintime:maxtime])
plt.xlabel('index')
plt.ylabel('microvolts (uV)')
plt.title("Raw signal")
plt.subplot(2, 1, 2)
plt.plot(index[mintime:maxtime], datarec[mintime:maxtime])
plt.xlabel('index')
plt.ylabel('microvolts (uV)')
plt.title("De-noised signal using wavelet techniques")
plt.tight_layout()
plt.show()


#fft of denoised and raw data
dt = 0.001
n = len(datarec)
yf = np.fft.fft(datarec, n)
yf_raw = np.fft.fft(data, n)
PSD = yf*np.conj(yf)/n
PSD_raw = yf_raw*np.conj(yf_raw)/n
freq = (1/(dt*n))*np.arange(n)
L = np.arange(1, np.floor(n/2), dtype = 'int')

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(freq[L], PSD_raw[L])
plt.title("Raw fft")
plt.subplot(2, 1, 2)
plt.plot(freq[L], PSD[L])
plt.title("De-noised fft")
plt.tight_layout()
plt.show()



#peak-to-peak distance
ppd = tsfel.feature_extraction.features.pk_pk_distance(datarec)
print(ppd)

