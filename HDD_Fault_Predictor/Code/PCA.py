# -*- coding: utf-8 -*-
"""ML_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s20tIF-holM3I8rxWmyFTjTeYH-Iggmr
"""

import numpy as np
import pandas as pd
import classification as clf
import matplotlib.pyplot as plt
import variance as v




def PCA(data):

    df = pd.read_csv(data, delimiter=",", encoding="latin1")


    del df['serial_number']
    del df['Unnamed: 0']
    del df['dt']



    mapping = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26
    }

    df = df.replace({
    "manufacturer": mapping,
    })

    del df['manufacturer']

    X = df.iloc[:,0:-1]
    y = df.iloc[:,-1]





    #mean normalization



    X = X.astype(int)


    X = (X-X.mean())/(X.max()-X.min())


# ****
# Deleting manufacturer as that feature has only one class which will not work with PCA. 
# But don't do this later on if the dataset has multiple Manufacturers.
# ****







    transpose_data = X.T



    matrix = np.cov(transpose_data)


    eigen_val, eigen_vec = np.linalg.eig(matrix)


    diction = {}
    for key, value in zip(eigen_val, eigen_vec):
        diction[key] = value

#sorting by eigenvalue

    d = sorted(diction.items(), key=lambda item: item[0], reverse=True)

    list_of_PCA = []

    for i,j in d:
        list_of_PCA.append(j)

    sorted_eig_vec=pd.DataFrame(list_of_PCA)

    idx = np.argsort(eigen_val, axis=0)[::-1]
    # plot the graph to choose PCA_components numbers...
    v.plot_for_variance(eigen_val, idx)

    #choosing first 4 PCA as they give 95% of variance

    pc_d = pd.DataFrame()

    for i in range(0, 4):

        # tranfrom the data using PCA

        df_t = pd.DataFrame(X.to_numpy().dot(sorted_eig_vec[i]), columns=['PCA' + str(i + 1)])
        pc_d = pd.concat([pc_d, df_t], axis=1)  # PC






    pc_d['class'] = y




    x_f = pc_d.iloc[:, 0:4]
    y_c = pc_d.iloc[:, -1]


    return pc_d.to_csv('../Data/PCA_Features.csv')












