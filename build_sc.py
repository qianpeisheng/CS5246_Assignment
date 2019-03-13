# python3.5 build_sc.py <pretrained_vectors_gzipped_file_absolute_path> <train_text_path> <train_label_path> <model_file_path>

import os
import math
import sys
import gzip

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

def train_model(embeddings_file, train_text_file, train_label_file, model_file):
    # write your code here. You can add functions as well.
		# use torch library to save model parameters, hyperparameters, etc. to model_file
    print('Finished...')
		
if __name__ == "__main__":
    # make no changes here
		embeddings_file = sys.argv[1]
		train_text_file = sys.argv[2]
		train_label_file = sys.argv[3]
		model_file = sys.argv[4]
    train_model(embeddings_file, train_text_file, train_label_file, model_file)
