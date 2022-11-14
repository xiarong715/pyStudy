import numpy as np
import librosa
import soundfile as sf
import pyroomacoustics as pra

from scipy.linalg import hankel

def bnlms(x, d, N = 4, L=4, mu = 0.1):
  beta = 0.9
  nIters = min(len(x),len(d))//L
  u = np.zeros(L+N-1)
  h = np.zeros(N)
  e = np.zeros(nIters*L)
  norm = np.full(L,1e-3)
  for n in range(nIters):
    u[:-L] = u[L:]
    u[-L:] = x[n*L:(n+1)*L]
    d_n = d[n*L:(n+1)*L]
    A = hankel(u[:L],u[-N:])
    e_n = d_n - np.dot(A,h)
    norm = beta*norm + (1-beta)*(np.sum(A**2,axis=1))
    h = h + mu*np.dot(A.T/(norm+1e-3),e_n)/L
    e[n*L:(n+1)*L] = e_n
  return e

if __name__ == "__main__":
    x, sr  = librosa.load('noise.wav',sr=8000)
    d, sr  = librosa.load('mixed.wav',sr=8000)

    e = bnlms(x, d, N=256, L=4, mu=0.1)
    e = np.clip(e,-1,1)
    # sf.write('x.wav', x, sr, subtype='PCM_16')
    # sf.write('d.wav', d, sr, subtype='PCM_16')
    sf.write('bnlms.wav', e, sr, subtype='PCM_16')