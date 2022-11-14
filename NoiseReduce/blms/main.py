import numpy as np
import librosa
import soundfile as sf
import pyroomacoustics as pra

from scipy.linalg import hankel

def blms(x, d, N=4, L=4, mu = 0.1):
  nIters = min(len(x),len(d))//L
  u = np.zeros(L+N-1)
  w = np.zeros(N)
  e = np.zeros(nIters*L)
  for n in range(nIters):
    u[:-L] = u[L:]
    u[-L:] = x[n*L:(n+1)*L]
    d_n = d[n*L:(n+1)*L]
    A = hankel(u[:L],u[-N:])
    e_n = d_n - np.dot(A,w)
    w = w + mu*np.dot(A.T,e_n)/L
    e[n*L:(n+1)*L] = e_n
  return e

if __name__ == "__main__":
    x, sr  = librosa.load('noise.wav',sr=8000)
    d, sr  = librosa.load('mixed.wav',sr=8000)

    e =  blms(x, d,N=256,L=4,mu=0.2)
    # sf.write('x.wav', x, sr, subtype='PCM_16')
    # sf.write('d.wav', d, sr, subtype='PCM_16')
    sf.write('blms.wav', e, sr, subtype='PCM_16')