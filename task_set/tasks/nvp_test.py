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

"""Tests for task_set.tasks.mlp."""

from task_set.tasks import family_test_utils
from task_set.tasks import nvp
import tensorflow.compat.v1 as tf


class NvpTest(family_test_utils.TaskFamilyTestCase):

  def __init__(self, *args, **kwargs):
    super(NvpTest, self).__init__(nvp.sample_nvp_family_cfg, nvp.get_nvp_family,
                                  *args, **kwargs)


if __name__ == "__main__":
  tf.test.main()
