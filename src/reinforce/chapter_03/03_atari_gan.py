""" Chapter 03 - GAN on Atari Images

@File: 03_atari_gan.py"""
import argparse as ap

import cv2
import gymnasium as gym
import numpy as np
import torch as th

LATENT_VECTOR_SIZE = 100
DISCR_FILTERS = 64
GENER_FILTERS = 64
BATCH_SIZE = 16

# dimension input image will be rescaled
IMAGE_SIZE = 64

LEARNING_RATE = 0.0001
REPORT_EVERY_ITER = 100
SAVE_IMAGE_EVERY_ITER = 1000


class InputWrapper(gym.ObservationWrapper):
    """
    Preprocessing of input numpy array:
    1. resize image into predefined size
    2. move color channel axis to a first place
    """

    def __init__(self, *args):
        super(InputWrapper, self).__init__(*args)

        assert isinstance(self.observation_space, gym.spaces.Box)

        old_space = self.observation_space
        self.observation_space = gym.spaces.Box(
            self.observation(old_space.low),
            self.observation(old_space.high),
            dtype=np.float32)

    def observation(self, observation):
        # resize image
        new_obs = cv2.resize(observation, (IMAGE_SIZE, IMAGE_SIZE))

        # transform (210, 160, 3) -> (3, 210, 160)
        new_obs = np.moveaxis(new_obs, 2, 0)

        return new_obs.astype(np.float32)


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument("--mps", default=False, action='store_true', help="Enable MPS computation")
    args = parser.parse_args()

    device = th.device("MPS" if args.mps else "cpu")
    envs = [InputWrapper(gym.make(name))
            for name in ('Breakout-v0', 'AirRaid-v0', 'Pong-v0')]
    input_shape = envs[0].observation_space.shape



    print('Done.')
