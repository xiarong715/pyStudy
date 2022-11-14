from matplotlib import pyplot
import numpy as np
import soundfile as sf
import io
import noisereduce as nr

normal_data, normal_rate = sf.read('voice.wav')
noise_data, noise_rate = sf.read('noise.wav')
mixed_data, mixed_rate = sf.read('mixed.wav')

print(noise_data.shape)

print(mixed_data.shape)

rate = normal_rate

pyplot.plot(noise_data)
noise_data = noise_data[40000:200000]
pyplot.plot(noise_data)

reduce_version = nr.reduce_noise(y=mixed_data, y_noise=noise_data, sr=rate)

sf.write('voice_reduced_noise.wav', reduce_version, rate)

# http://public:public@192.168.43.99/tools-ci/gitatools.git