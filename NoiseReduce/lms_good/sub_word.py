import numpy as np
import librosa
import soundfile as sf
import pyroomacoustics as pra

# x 参考信号
# d 麦克风信号
# N 滤波器阶数
# mu 迭代步长
def lms(x, d, N = 4, mu = 0.1):
  nIters = min(len(x),len(d)) - N
  u = np.zeros(N)
  w = np.zeros(N)
  e = np.zeros(nIters)
  for n in range(nIters):
    u[1:] = u[:-1]
    u[0] = x[n]
    e_n = d[n] - np.dot(u, w)
    w = w + mu * e_n * u
    e[n] = e_n
  return e

if __name__ == "__main__":
    x, sr  = librosa.load('1/voice.wav',sr=16000)  # 参考信号
    d, sr  = librosa.load('1/mixed.wav',sr=16000)  # 混合信号

    # 手动对齐远端与近端
    ref_offset = 1568-1
    mixed_offset = 13104-1

    x = x[ref_offset:]
    d1 = d[:mixed_offset-1]
    d = d[mixed_offset:]

    e =  lms(x, d,N=256,mu=0.1)
    # sf.write('x.wav', x, sr, subtype='PCM_16')
    # sf.write('d.wav', d, sr, subtype='PCM_16')
    res = np.append(d1, e)
    sf.write('1/lms_sub_word.wav', res, sr, subtype='PCM_16')
    # print(len(x)) 