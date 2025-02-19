import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import pandas as pd

SEQ_LENGTH = 12

# Transformer Model
class TimeSeriesTransformer(keras.Model):
    def __init__(self, d_model=64, num_heads=8, num_layers=3, dropout=0.1):
        super(TimeSeriesTransformer, self).__init__()
        self.embedding = layers.Dense(d_model)
        self.encoder_layers = [
            layers.MultiHeadAttention(num_heads=num_heads, key_dim=d_model)
            for _ in range(num_layers)
        ]
        self.dropout_layers = [layers.Dropout(dropout) for _ in range(num_layers)]
        self.norm_layers = [layers.LayerNormalization() for _ in range(num_layers)]
        self.decoder = layers.Dense(SEQ_LENGTH)
    
    def call(self, inputs):
        x = self.embedding(inputs)
        for mha, dropout, norm in zip(self.encoder_layers, self.dropout_layers, self.norm_layers):
            attn_output = mha(x, x)
            attn_output = dropout(attn_output)
            x = norm(x + attn_output)
        return self.decoder(x[:, -1, :])
    

class TimeSeriesLSTM(keras.Model):
    def __init__(self, lstm_units=64, num_layers=3, dropout=0.1):
        super(TimeSeriesLSTM, self).__init__()
        self.lstm_layers = [
            layers.LSTM(lstm_units, return_sequences=True, dropout=dropout) 
            for _ in range(num_layers - 1)
        ]
        self.lstm_layers.append(layers.LSTM(lstm_units, return_sequences=False, dropout=dropout))
        self.dense = layers.Dense(SEQ_LENGTH)
    
    def call(self, inputs):
        x = inputs
        for lstm in self.lstm_layers:
            x = lstm(x)
        return self.dense(x)
    
class TimeSeriesNN(keras.Model):
    def __init__(self, hidden_units=128, num_layers=3, dropout=0.1):
        super(TimeSeriesNN, self).__init__()
        self.hidden_layers = [
            layers.Dense(hidden_units, activation='relu') 
            for _ in range(num_layers)
        ]
        self.dropout_layers = [
            layers.Dropout(dropout) 
            for _ in range(num_layers)
        ]
        self.output_layer = layers.Dense(SEQ_LENGTH)
    
    def call(self, inputs):
        x = inputs
        for hidden, dropout in zip(self.hidden_layers, self.dropout_layers):
            x = hidden(x)
            x = dropout(x)
        return self.output_layer(x)