import simpy
import numpy as np
import protocols
env = simpy.Environment()
rng = np.random.default_rng()

lora_channels = simpy.Resource(env, 3)

lora_sim = protocols.Lora(env, rng, lora_channels)

env.run(until=20)
