
#手动求求语谱图

import librosa
import numpy as np
import matplotlib.pyplot as plt

#计算每帧对应的时间
def FrameTimeC(frameNum, frameLen, inc, fs):
    ll = np.array([i for i in range(frameNum)])
    return ((ll - 1) * inc + frameLen / 2) / fs

#分帧函数
def enframe(x, win, inc=None):
    nx = len(x)
    if isinstance(win, list) or isinstance(win, np.ndarray):
        nwin = len(win)
        nlen = nwin  # 帧长=窗长
    elif isinstance(win, int):
        nwin = 1
        nlen = win  # 设置为帧长
    if inc is None:
        inc = nlen
    nf = (nx - nlen + inc) // inc
    frameout = np.zeros((nf, nlen))
    indf = np.multiply(inc, np.array([i for i in range(nf)]))
    for i in range(nf):
        frameout[i, :] = x[indf[i]:indf[i] + nlen]
    if isinstance(win, list) or isinstance(win, np.ndarray):
        frameout = np.multiply(frameout, np.array(win))
    return frameout

#加窗
def hanning_window(N):
    nn = [i for i in range(N)]
    return 0.5 * (1 - np.cos(np.multiply(nn, 2 * np.pi) / (N - 1)))

#短时傅里叶变换
def STFFT(x, win, nfft, inc):
    xn = enframe(x, win, inc)
    xn = xn.T
    y = np.fft.fft(xn, nfft, axis=0)
    return y[:nfft // 2, :]

path=r"/root/work/pyStudy/NoiseReduce/voice.wav"#audio002.wav
data, fs = librosa.load(path, sr=None, mono=False)#sr=None声音保持原采样频率， mono=False声音保持原通道数

wlen = 256
nfft = wlen
win = hanning_window(wlen)
inc = 128

y = STFFT(data, win, nfft, inc)

FrequencyScale = [i * fs / wlen for i in range(wlen // 2)] #频率刻度
frameTime = FrameTimeC(y.shape[1], wlen, inc, fs) #每帧对应的时间
LogarithmicSpectrogramData=10*np.log10((np.abs(y)*np.abs(y))) #取对数后的数据

#np.savetxt("SpectrogramData.txt",LogarithmicSpectrogramData)

plt.pcolormesh(frameTime, FrequencyScale,LogarithmicSpectrogramData)
plt.colorbar()
#plt.savefig('语谱图22.png')
plt.show()

#掉包实现
plt.specgram(data, NFFT=256, Fs=fs, window=np.hanning(256))
plt.ylabel('Frequency')
plt.xlabel('Time(s)')
#plt.savefig('语谱图11.png')
plt.show()
