import os
import numpy as np
from scipy import interpolate
import tkinter as tk
from tkinter import filedialog

default_path = r'D:\Arpad\Raman\raw\\'
calibrate_data = True

bearbeitet_path = r'D:\Arpad\Raman\calibrated\\'
filenames = filedialog.askopenfilenames(initialdir=default_path, title="Select spectra to be processed", filetypes=(("Text Files", "*.txt"),))

if not os.path.exists(r'D:\Arpad\Raman\calibrated\2020-08-11\\'):  # OJO CARPETA
    os.makedirs(r'D:\Arpad\Raman\calibrated\2020-08-11\\')

out_folder = bearbeitet_path + r'2020-08-11\\'  # OJO CARPETA
pure_names = [os.path.splitext(os.path.basename(filename))[0] for filename in filenames]

names, ns, ne = np.unique(pure_names, return_index=True, return_inverse=True)

z_n, r_n = names.shape[0], len(names)

if calibrate_data:
    root = tk.Tk()
    root.withdraw()
    file_k = filedialog.askopenfilename(initialdir=r'D:\Ceci\Raman\\', title="Select file with correct peak positions", filetypes=(("Text Files", "*.txt"),))
    file_g = filedialog.askopenfilename(initialdir=r'D:\Ceci\Raman\raw\\', title="Select file with peak positions from calibration measurement", filetypes=(("Text Files", "*.txt"),))

    correct = np.loadtxt(os.path.join(file_k))
    gemessen = np.loadtxt(os.path.join(file_g))
    polynom = np.polyfit(gemessen, correct, 2)

for i in range(r_n):
    # merge data
    ind = np.where(ne == i)[0]
    for k, index in enumerate(ind):
        data = np.loadtxt(filenames[index])
        w = data[:, 0]
        I_k = data[:, 1]
        if k == 0:
            M = np.zeros((len(w), len(ind)+1))
            M[:, 0] = w
            M[:, k+1] = I_k
        else:
            M[:, k+1] = I_k

    # calibrate data
    if calibrate_data:
        x_calib = polynom[0]*M[:, 0]**2 + polynom[1]*M[:, 0] + polynom[2]
        M[:, 0] = x_calib
        np.savetxt(os.path.join(out_folder, names[i]+'.txt'), M, delimiter='\t')
    del M
