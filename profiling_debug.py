from distracting_control import suite
import time
import numpy as np


dynamic = True
davis_path = "/home/sahand/datasets/DAVIS/JPEGImages/480p/"

env = suite.load(domain_name="reacher", task_name="easy",
                 difficulty=None, pixels_only=True,
                 background_dataset_path=davis_path,
                 background_kwargs={'video_alpha': 0.4, 'num_videos': 4, 'ground_plane_alpha': 0.0,
                                    'dynamic': dynamic, 'dynamic_bg_freq': 4})


# Step through an episode and print out reward, discount and observation.
start = time.time()
action_spec = env.action_spec()
time_step = env.reset()

while not time_step.last():
  action = np.random.uniform(action_spec.minimum,
                             action_spec.maximum,
                             size=action_spec.shape)
  time_step = env.step(action)
  # print(time_step.reward, time_step.discount, time_step.observation)

print(f"Time Elapsed: {time.time() - start}")
