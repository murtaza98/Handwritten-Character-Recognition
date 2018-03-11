import keras.backend as K
import math
import numpy as np
import h5py
import matplotlib.pyplot as plt

def convert_to_one_hot(Y, C):
    Y = np.eye(C)[Y.reshape(-1)].T
    return Y



def mean_pred(y_true, y_pred):
    return K.mean(y_pred)

def load_dataset():
    train_dataset = h5py.File('datasets/dataset_number_characters.hdf5', "r")
    train_set_x_orig = np.array(train_dataset["train_img"][:]) # your train set features
    train_set_y_orig = np.array(train_dataset["train_labels"][:]) # your train set labels


    
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    
    return train_set_x_orig, train_set_y_orig