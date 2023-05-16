import simpy
import numpy as np
import protocols
env = simpy.Environment()
rng = np.random.default_rng()

lora_channels = simpy.Resource(env, 3)
wifi_channels = simpy.Resource(env,8)

lora_sim = protocols.Lora(env, rng, lora_channels)
wifi_sim = protocols.Wifi(env, rng, wifi_channels)

env.run(until=20)
