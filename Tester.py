import numpy as np
import pandas as pd

import Line_Handler as lh
import Decodings as dec
import Encodings as enc

from pathlib import Path

# Result Template
Run_Results = pd.DataFrame({
    'Run': 0,
    'SNR': 0,
    'Pb' : 0
})

def Generate_AMI_Vector(signal, L, run=1, Tb=1, dB=1):
    encoded_signal = enc.AMI(signal, Tb)
    noisy_signal   = lh.Attenuate_And_Add_Noise(encoded_signal, dB)
    trinary_signal = lh.Get_Trinary(noisy_signal, L=L)
    decoded_signal = dec.AMI(trinary_signal, Tb)

    vector_path_str = 
    Path("Vectors/AMI/dB_"+str(dB)).mkdir(parents=True, exist_ok=True)
    np.save('Decoded_AMI_Vector-run_' + str(run) + '.npy', decoded_signal)

def Generate_AMI_Vectors(signal, L, n_runs=200, Tb=1, dB_init=5, dB_fin=45):
    for dB in range(dB_init, dB_fin+1):
        vector_path = Path("Vectors/AMI/dB_"+str(dB))
        vector_path.mkdir(parents=True, exist_ok=True)
        file_count = sum(1 for item in vector_path.iterdir() if item.is_file())
        for run in range(file_count+1, n_runs):
            Generate_AMI_Vector(signal, L, run, Tb, dB)

def Generate_Run_Result()

