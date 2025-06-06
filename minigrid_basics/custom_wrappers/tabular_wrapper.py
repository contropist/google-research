# coding=utf-8
# Copyright 2025 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wrapper to make the environment tabular.

All we do is to look at the size of the grid and assign an id to each possible
coordinate. Walls are still states at first, for sake of simplicity. We also
return the image, in case someone is interested in using both.
"""

import gym
import gym_minigrid  # pylint: disable=unused-import


class TabularWrapper(gym.core.ObservationWrapper):
  """Wrapper to convert a GridWorld environment into a tabular one.

  All we do is to look at the size of the grid and assign an id to each possible
  coordinate. Walls are still states at first, for sake of simplicity. We also
  return the image in case someone is interested in using both.

  TODO(marlosm): Deal with combinatorial explosion generated by objects.
  """

  def __init__(self, env, tile_size=8, get_rgb=False):
    super().__init__(env)

    self.tile_size = tile_size
    self.get_rgb = get_rgb
    self.pos_to_state = {}
    self.state_to_pos = {}
    curr_state = 0
    for y in range(self.height):
      for x in range(self.width):
        curr_cell = env.grid.get(x, y)
        grid_pos = x + y * env.width
        if (curr_cell is not None and curr_cell.type != 'goal' and
            curr_cell.type != 'lava'):
          self.pos_to_state[grid_pos] = -1
        else:
          self.pos_to_state[grid_pos] = curr_state
          self.state_to_pos[curr_state] = [x, y]
          curr_state += 1
    self.num_states = curr_state
    obs_space_dict = {'state': gym.spaces.Discrete(self.num_states)}
    if self.get_rgb and 'image' in self.observation_space.spaces:
      # Re-use the image obs spec from the env we are wrapping.
      obs_space_dict['image'] = self.observation_space['image']
    self.observation_space = gym.spaces.Dict(obs_space_dict)

  def observation(self, obs=None):
    if obs is None:
      obs = self.gen_obs()
    env = self.unwrapped
    agent_x_pos, agent_y_pos = env.agent_pos
    state_number = self.pos_to_state[agent_x_pos + agent_y_pos * env.width]

    if self.get_rgb:
      rgb_img = env.render(
          mode='rgb_array', highlight=False, tile_size=self.tile_size)

      return {'state': state_number, 'image': rgb_img}
    else:
      return {'state': state_number}
