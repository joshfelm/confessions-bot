from facebook_scraper import get_posts
import re
from textgenrnn import textgenrnn
import os.path
from os import path
from os import listdir
from os.path import isfile, join
import glob, os
import tensorflow as tf
import time
import datetime
from datetime import date

tf.config.optimizer.set_jit(True)

i = 0
filelist = []
for file in glob.glob("./posts/*.txt"):
    filelist.append(file)

# for file in glob.glob("./posts/archive/*.txt"):
#     filelist.append(file)

texts = []

for f in filelist:
    fileop=open(f, "r")
    if fileop.mode == 'r':
        texts.append(fileop.read())

# train network
model_name = 'bristruths-bot_word'
# textgen = textgenrnn(name=model_name)

textgen = textgenrnn(weights_path='./bot-config/bristruths-bot_word_weights.hdf5',
                       vocab_path='./bot-config/bristruths-bot_word_vocab.json',
                       config_path='./bot-config/bristruths-bot_word_config.json')

model_cfg = {
    'rnn_size': 128,
    'rnn_layers': 4,
    'rnn_bidirectional': True,
    'max_length': 40,
    'max_words':10000,
    'dim_embeddings': 100,
    'word_level': True,
}

train_cfg = {
    'line_delimited': False,
    'num_epochs': 10,
    'gen_epochs': 2,
    'batch_size': 1024,
    'train_size': 0.8,
    'dropout': 0.0,
    'max_gen_length': 300,
    'validation': False,
    'is_csv': False
}

train_function = textgen.train_on_texts
model_cfg = {
    'word_level': True,   # set to True if want to train a word-level model (requires more data and smaller max_length)
    'rnn_size': 128,   # number of LSTM cells of each layer (128/256 recommended)
    'rnn_layers': 3,   # number of LSTM layers (>=2 recommended)
    'rnn_bidirectional': True,   # consider text both forwards and backward, can give a training boost
    'max_length': 10,   # number of tokens to consider before predicting the next (20-40 for characters, 5-10 for words recommended)
    'max_words': 10000,   # maximum number of words to model; the rest will be ignored (word-level model only)
}

train_cfg = {
    'line_delimited': False,   # set to True if each text has its own line in the source file
    'num_epochs': 20,   # set higher to train the model for longer
    'gen_epochs': 5,   # generates sample text from model after given number of epochs
    'train_size': 0.8,   # proportion of input data to train on: setting < 1.0 limits model from learning perfectly
    'dropout': 0.0,   # ignore a random proportion of source tokens each epoch, allowing model to generalize better
    'validation': False,   # If train__size < 1.0, test on holdout dataset; will make overall training slower
    'is_csv': False   # set to True if file is a CSV exported from Excel/BigQuery/pandas
}

# The train function (comment this out if you don't want to train and only generate text)
# train_function(
#     texts=texts,
#     new_model=False,        # Change this to true to retrain model from scratch
#     num_epochs=train_cfg['num_epochs'],
#     gen_epochs=train_cfg['gen_epochs'],
#     batch_size=1024,
#     train_size=train_cfg['train_size'],
#     dropout=train_cfg['dropout'],
#     validation=train_cfg['validation'],
#     is_csv=train_cfg['is_csv'],
#     rnn_layers=model_cfg['rnn_layers'],
#     rnn_size=model_cfg['rnn_size'],
#     rnn_bidirectional=model_cfg['rnn_bidirectional'],
#     max_length=model_cfg['max_length'],
#     dim_embeddings=100,
#     word_level=model_cfg['word_level'])

# this temperature schedule cycles between 1 very unexpected token, 1 unexpected token, 2 expected tokens, repeat.
# changing the temperature schedule can result in wildly different output!
temperature = [1.0, 0.5, 0.2, 0.7, 0.2, 0.2, 0.5]   
prefix = '\n'   # if you want each generated text to start with a given seed text

if train_cfg['line_delimited']:
  n = 1000
  max_gen_length = 60 if model_cfg['word_level'] else 300
else:
  n = 100
  max_gen_length = 50 if model_cfg['word_level'] else 280  # max length = lenght of tweet
  
gen_file = './gentext/gentext-'+str(datetime.datetime.now())+'.txt'

print("generating texts")
textgen.generate_to_file(gen_file,
                         temperature=temperature,
                         prefix=prefix,
                         n=n,
                         max_gen_length=max_gen_length)
