import numpy as np
def wav2pcm(wavfile, pcmfile, data_type=np.int16):
    f = open(wavfile, "rb")
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype= data_type)
    data.tofile(pcmfile)

wav2pcm("/root/work/AudioProc/data/me/mixed.wav", "/root/work/AudioProc/data/me/mixed.pcm")
wav2pcm("/root/work/AudioProc/data/me/noise.wav", "/root/work/AudioProc/data/me/noise.pcm")
wav2pcm("/root/work/AudioProc/data/me/voice.wav", "/root/work/AudioProc/data/me/voice.pcm")