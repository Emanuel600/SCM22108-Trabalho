import numpy as np

import random

def Attenuate_And_Add_Noise(signal, SNR_db):
    a            = random.uniform(0, 1)
    signal       = a*np.array(signal).astype(float)
    signal_power = np.mean(signal**2)
    snr_lin      = 10 ** (SNR_db / 10)
    noise_power  = signal_power/snr_lin
    noise        = np.random.normal(0, np.sqrt(noise_power), np.shape(signal))

    return (signal+noise)

def Get_Trinary(signal, L=0.5):
    signal = np.where(signal<(-L), -1, signal)
    signal = np.where(signal>L, 1, signal)
    signal = np.where((signal>-L) & (signal<L), 0, signal)

    return signal