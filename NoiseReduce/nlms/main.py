import numpy as np
import librosa
import soundfile as sf
import pyroomacoustics as pra

def nlms(x, d, N=4, mu=0.1):
  nIters = min(len(x),len(d)) - N
  u = np.zeros(N)
  w = np.zeros(N)
  e = np.zeros(nIters)
  for n in range(nIters):
    u[1:] = u[:-1]
    u[0] = x[n]
    e_n = d[n] - np.dot(u, w)
    w = w + mu * e_n * u / (np.dot(u,u)+1e-3)
    e[n] = e_n
  return e

if __name__ == "__main__":
    x, sr  = librosa.load('noise.wav',sr=8000)
    d, sr  = librosa.load('mixed.wav',sr=8000)

    e =  nlms(x, d,N=256,mu=0.1)
    # sf.write('x.wav', x, sr, subtype='PCM_16')
    # sf.write('d.wav', d, sr, subtype='PCM_16')
    sf.write('nlms.wav', e, sr, subtype='PCM_16')