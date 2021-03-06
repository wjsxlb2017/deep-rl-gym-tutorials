from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

class Env(object):
    """Minimal wrapper around OpenAI Gym Env to allow
    for preprocessing observation and reward clipping
    during steps."""
    def __init__(self, env, observation_preprocess=None, reward_clipper=None):
        self.env = env
        self.op = observation_preprocess
        self.clip = reward_clipper

    def reset(self):
        obs = self.env.reset()
        if self.op: obs = self.op(obs)
        return obs

    def step(self, action):
        obs, reward, terminal, info = self.env.step(action)
        if self.op: obs = self.op(obs)
        if self.clip: reward = self.clip(reward)
        return obs, reward, terminal, info

    def render(self):
        self.env.render()

    @property
    def monitor(self):
        return self.env.monitor

    @property
    def action_space(self):
        return self.env.action_space

    @property
    def observation_space(self):
        return self.env.observation_space
