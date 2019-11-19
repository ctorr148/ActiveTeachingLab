"""
LearnNet

Problem network
"""

import global_params
from components import patterns, noise, weights
from utils import init, learning, forgetting

learning_rate = 0.337
forgetting_rate = 1

time_steps = global_params.time_steps
patterns = patterns.patterns
init_weights = init.initialize_weights(1)
target_weights = weights.combine_target_weights()
noise = noise.noise

# learning_weights_ = learning.learn_weights(init_weights, target_weights, learning_rate)
forgetting_weights = forgetting.forget_weights(init_weights, forgetting_rate)
print(forgetting_weights)