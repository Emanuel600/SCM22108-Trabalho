import numpy as np
import pandas as pd

import Line_Handler as lh
import Decodings as dec
import Encodings as enc

from pathlib import Path

# Function dictionary for easy access to encoding and decoding functions
ENCODING_FUNCTIONS = {
    'AMI': enc.AMI,
    'CMI': enc.CMI,
    'Manchester': enc.Manchester
}

DECODING_FUNCTIONS = {
    'AMI': dec.AMI,
    'CMI': dec.CMI,
    'Manchester': dec.Manchester
}

# Result Template
Run_Results = pd.DataFrame(
    columns = ['RUN', 'SNR', 'BER']
)

def Generate_Array(function, signal, L, run=1, Tb=1, dB=1):
    encoded_signal = ENCODING_FUNCTIONS[function](signal, Tb)
    noisy_signal   = lh.Attenuate_And_Add_Noise(encoded_signal[1], dB)
    trinary_signal = lh.Get_Trinary(noisy_signal, L=L)
    decoded_signal = DECODING_FUNCTIONS[function](trinary_signal, Tb)

    vector_path_str = "Arrays/" + function + "/dB_" + str(dB) + "/"
    Path(vector_path_str).mkdir(parents=True, exist_ok=True)
    np.save(vector_path_str + 'Decoded_' + function + '_Vector-run_' + str(run+1) + '.npy', decoded_signal)

def Generate_All_Arrays(function, signal, L, n_runs=200, Tb=1, dB_init=5, dB_fin=45):
    for dB in range(dB_init, dB_fin+1):
        vector_path = Path("Arrays/" + function + "/dB_" + str(dB) + "/")
        vector_path.mkdir(parents=True, exist_ok=True)
        file_count = sum(1 for item in vector_path.iterdir() if item.is_file())
        for run in range(file_count, n_runs):
            Generate_Array(function, signal, L, run, Tb, dB)

def Run_Tests(function, original_signal, L, n_runs=200, Tb=1, dB_init=5, dB_fin=45):
    Generate_All_Arrays(function, original_signal, L, n_runs, Tb, dB_init, dB_fin)
    csv_path = Path("Results/" + function + "_Run_Results.csv")
    Path("Results/").mkdir(exist_ok=True)
    for dB in range(dB_init, dB_fin+1):
        vector_path_str = "Arrays/" + function + "/dB_" + str(dB) + "/"
        vector_path = Path(vector_path_str)

        file_count = sum(1 for item in vector_path.iterdir() if item.is_file())
        assert(file_count == n_runs), f"Expected {n_runs} files in {vector_path_str}, but found {file_count}."

        for run in range(1, n_runs+1):
            vector_file = vector_path / ('Decoded_' + function + '_Vector-run_' + str(run) + '.npy')
            assert(vector_file.is_file()), f"Expected file {vector_file} does not exist."
            decoded_signal = np.load(vector_file)[1]
            if run == 1:  # Print results for the first run of each SNR level
                print(f"SNR {dB} dB, BER: {np.mean(original_signal != decoded_signal)}")
                print(f"Original signal: {original_signal}")
                print(f"Decoded signal:  {decoded_signal}")
            new_row = pd.DataFrame({
                'RUN': [run],
                'SNR': [dB],
                'BER': [np.mean(original_signal != decoded_signal)]
            })
            if csv_path.exists():
                new_row.to_csv(csv_path, mode='a', index=False, header=False)
            else:
                new_row.to_csv(csv_path, index=False, header=False)

