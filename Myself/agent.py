import tensorflow as tf
import numpy as np

from tensorflow.keras import optimizers, losses
from tensorflow.keras import Model
from collections import deque

import random

class DQN(Model):
    def __init__(self):
        super(DQN, self).__init__()
        self.layer1 = tf.keras.layers.Dense(64, activation='relu')
        self.layer2 = tf.keras.layers.Dense(64, activation='relu')
        self.layer3 = tf.keras.layers.Flatten()
        self.value = tf.keras.layers.Dense(10)

    def call(self, state):
        layer1 = self.layer1(state)
        #print(layer1.shape)
        layer2 = self.layer2(layer1)
        #print(layer2.shape)
        layer3 = self.layer3(layer2)
        #print(layer3.shape)
        value = self.value(layer3)
        #print(value.shape)
        return value

class Agent:
    def __init__(self):
        # hyper parameters
        self.lr = 0.001
        self.gamma = 0.99

        self.dqn_model = DQN()
        self.dqn_target = DQN()
        
        self.opt = optimizers.Adam(lr=self.lr, )

        self.batch_size = 64
        self.state_size = 4
        self.action_size = 20

        self.memory = deque(maxlen=2000)

    def update_target(self):
        self.dqn_target.set_weights(self.dqn_model.get_weights())

    def get_action(self, state, epsilon):
        q_value = self.dqn_model(tf.convert_to_tensor(state, dtype=tf.float32))[0]
        if np.random.rand() <= epsilon:
            print("random")
            action = np.random.choice(self.action_size)
        else:
            print("greedy")
            action = np.argmin(q_value) 
        return action, q_value

    def append_sample(self, state, action, reward, next_state):
        self.memory.append((state, action, reward, next_state))

    def update(self):
        mini_batch = random.sample(self.memory, self.batch_size)

        states = [i[0] for i in mini_batch]
        actions = [i[1] for i in mini_batch]
        next_states = [i[2] for i in mini_batch]
        rewards = [i[3] for i in mini_batch]


        dqn_variable = self.dqn_model.trainable_variables
        #print(dqn_variable)

        writer = tf.summary.create_file_writer("./tmp")
        with writer.as_default():
        
            # other model code would go here
            tf.summary.scalar("my_metric", 0.5)
            writer.flush()

        with tf.GradientTape() as tape:
            tape.watch(dqn_variable)
            
            rewards = tf.convert_to_tensor(rewards, dtype=tf.float32)
            #print("rewards\n",rewards)
            actions = tf.convert_to_tensor(actions, dtype=tf.int32)
            #print("actions\n",actions)
            #dones = tf.convert_to_tensor(dones, dtype=tf.float32)

            target_q = self.dqn_target(tf.convert_to_tensor(next_states))
            #print("next_state\n",tf.convert_to_tensor(next_states, dtype=tf.float32))
            print("target_q\n",target_q)
            next_action = tf.argmin(target_q, axis=1)
            print("next_action_argmin\n",next_action)
            #print("next_action :     ",next_action)
            #print("next_action\n",next_action)
            target_value = tf.reduce_sum(tf.one_hot(next_action, self.action_size) * target_q, axis=1)
            print("target_value\n",target_value)
            # print("------------------------\n",tf.convert_to_tensor(states).shape, tf.convert_to_tensor(next_states).shape)
            target_value = self.gamma * target_value + rewards * 10
            # print("state check\n",tf.convert_to_tensor(states))

            main_q = self.dqn_model(tf.convert_to_tensor(states, dtype=tf.float32))

            

            print("main_q\n",main_q)
            main_value = tf.reduce_sum(tf.one_hot(actions, self.action_size) * main_q, axis=1)

            error = tf.losses.mean_squared_error(target_value, main_value)

            #error = tf.square(main_value - target_value) * 0.5
            #error = tf.reduce_mean(error)
            #input()


        dqn_grads = tape.gradient(error, dqn_variable)
        self.opt.apply_gradients(zip(dqn_grads, dqn_variable))
