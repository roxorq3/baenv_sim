import simpy
import numpy as np

AUTH_TIME = 0


class Lora:
    def __init__(self, env, rng, channels):
        self.env = env
        self.rng = rng
        self.channels = channels
        self.action = env.process(self.run())

    def auth(self):
        print("Starting authentication")
        yield self.env.timeout(np.abs(self.rng.standard_normal()))
        print("Done with authentication")

    def send(self):
        print("Starting to transmit")
        with self.channels.request() as rq:
            yield rq
            print("Starting to transmit")
            yield self.env.timeout(np.abs(self.rng.standard_normal()))
            print("Done transmitting")
            yield self.env.timeout(1)
            print("Opening receive windows")
            yield self.env.timeout(np.abs(self.rng.standard_normal()))
            print("Closing receive windows")

    def run(self):
        while True:
            yield self.env.process(self.auth())
            yield self.env.process(self.send())



