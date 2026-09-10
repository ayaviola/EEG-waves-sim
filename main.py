import numpy as np
import matplotlib.pyplot as plt

'''
This program is a very simple demonstration to show you how unstructured data becomes 
decoded and readable in order for us to pull out conclusive results via FFT. 
'''

frq_sample_rate = 500 
time = np.linspace(0, 4, 4*frq_sample_rate, endpoint=False)

def sine_wave_eq(amplitude, freq, t):
    return amplitude * np.sin(2 * np.pi * freq * t)

theta_wave = sine_wave_eq(amplitude=1.5, freq=6, t=time)
alpha_waave = sine_wave_eq(amplitude=2.5, freq= 10, t=time)
beta_wave = sine_wave_eq(amplitude=0.5, freq=21, t=time)

rn = np.random.normal(0, 0.7, len(time))

combined_waves_data = eeg_signal = theta_wave + alpha_waave + beta_wave + rn

'''
use fft, also remember important eqs:
f = 1/T
T = 1/f
amp = max value - min value / 2
'''
fft_values = np.fft.rfft(eeg_signal)
fft_frqs = np.fft.rfftfreq(len(time), 1/frq_sample_rate)
amplitudes = np.abs(fft_values) / len(time) * 2

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, eeg_signal, color='pink', lw=1)
plt.title('Little EEG Signal Simulation')
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (mu *V)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(fft_frqs, amplitudes, color='purple', lw=2)
plt.title('Isolareed individual frequencies using FFT')
plt.xlabel('Frequency (in Hz)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()