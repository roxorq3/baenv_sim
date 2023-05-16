import numpy as np


class Lora:
    def __init__(self, env, rng, channels):
        self.env = env
        self.rng = rng
        self.channels = channels
        self.action = env.process(self.run())

    # Skip synchronization?
    def synchronization(self):
        return



    def send(self):
        print("Requesting channel")
        with self.channels.request() as rq:
            yield rq
            print("Channel received")
            print("Starting to transmit")
            yield self.env.timeout(np.abs(self.rng.standard_normal()))
            print("Done transmitting")
            yield self.env.timeout(1)
            print("Opening receive windows")
            yield self.env.timeout(np.abs(self.rng.standard_normal()))
            print("Closing receive windows")

    def run(self):
        while True:
            yield self.env.process(self.send())
