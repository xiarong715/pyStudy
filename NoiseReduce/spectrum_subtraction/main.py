import numpy as np
import fire
import librosa
import soundfile as sf


def sayHello():
    print("hello world")


def sub_spectrum():
    mix, fs = librosa.load("mixed.wav", sr=None)

    # 对整个语音作短时傅里叶变换
    s_mix = librosa.stft(mix, n_fft=256, hop_length=128, win_length=256)
    mag_mix = np.abs(s_mix)
    # D,T = np.shape(s_mix)
    power_mix = mag_mix ** 2

    phase_nosiy= np.angle(s_mix)

    # 取前一小段语音作为噪声，作短时傅里叶变换。短时傅里叶变换是对每一帧进行的。取前30帧作为噪声
    mag_noise = np.mean(np.abs(s_mix[:, :30]), axis=1, keepdims=True)
    power_noise = mag_noise ** 2
    # Power_nosie = np.tile(Power_nosie,[1,T])

    # 减谱去噪，功率谱相减
    power_enhence = power_mix - power_noise
    power_enhence[power_enhence < 0] = 0
    mag_enhence = np.sqrt(power_enhence)

    # 反傅里叶变换
    s_enhence = mag_enhence*np.exp(1j*phase_nosiy)
    enhence = librosa.istft(s_enhence, hop_length=128, win_length=256)

    # 保存处理后的音频
    sf.write("result.wav", enhence, fs)

if __name__ == '__main__':
    fire.Fire(sub_spectrum)
