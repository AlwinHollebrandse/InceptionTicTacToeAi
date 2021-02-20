import argparse
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import HelperFunctions
import keras
import keras.layers as kl
import keras.models as km
import keras.optimizers as ko

"""
NeuralNet for the game of TicTacToe.
Author: Evgeny Tyurin, github.com/evg-tyurin
Date: Jan 5, 2018.
Based on the OthelloNNet by SourKream and Surag Nair.
"""
class TicTacToeNNet():
    def __init__(self, args):
        # game params
        self.board_x, self.board_y = HelperFunctions.getBoardSize()
        self.action_size = HelperFunctions.getActionSize()
        self.args = args

        # Neural Net
        self.input_boards = keras.Input(shape=(self.board_x, self.board_y))    # s: batch_size x board_x x board_y

        x_image = kl.Reshape((self.board_x, self.board_y, 1))(self.input_boards)                # batch_size  x board_x x board_y x 1
        h_conv1 = kl.Activation('relu')(kl.BatchNormalization(axis=3)(kl.Conv2D(args.num_channels, 3, padding='same')(x_image)))         # batch_size  x board_x x board_y x num_channels
        h_conv2 = kl.Activation('relu')(kl.BatchNormalization(axis=3)(kl.Conv2D(args.num_channels, 3, padding='same')(h_conv1)))         # batch_size  x board_x x board_y x num_channels
        h_conv3 = kl.Activation('relu')(kl.BatchNormalization(axis=3)(kl.Conv2D(args.num_channels, 3, padding='same')(h_conv2)))        # batch_size  x (board_x) x (board_y) x num_channels
        h_conv4 = kl.Activation('relu')(kl.BatchNormalization(axis=3)(kl.Conv2D(args.num_channels, 3, padding='valid')(h_conv3)))        # batch_size  x (board_x-2) x (board_y-2) x num_channels
        h_conv4_flat = kl.Flatten()(h_conv4)
        s_fc1 = kl.Dropout(args.dropout)(kl.Activation('relu')(kl.BatchNormalization(axis=1)(kl.Dense(1024)(h_conv4_flat))))  # batch_size x 1024
        s_fc2 = kl.Dropout(args.dropout)(kl.Activation('relu')(kl.BatchNormalization(axis=1)(kl.Dense(512)(s_fc1))))          # batch_size x 1024
        self.pi = kl.Dense(self.action_size, activation='softmax', name='pi')(s_fc2)   # batch_size x self.action_size
        self.v = kl.Dense(1, activation='tanh', name='v')(s_fc2)                    # batch_size x 1

        self.model = km.Model(inputs=self.input_boards, outputs=[self.pi, self.v])
        self.model.compile(loss=['categorical_crossentropy','mean_squared_error'], optimizer=ko.Adam(args.lr))
