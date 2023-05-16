import numpy as np


class Wifi:
    def __init__(self, env, rng, channels):
        self.env = env
        self.rng = rng
        self.channels = channels
        self.action = env.process(self.run())

    # In case I should include the Wifi scanning process.
    # def scanning(self):
    #     return

    # Shared key?
    def auth(self):
        print("Starting authentication")
        yield self.env.timeout(np.abs(self.rng.standard_normal()))
        print("Done with authentication")

    def association(self):
        print("Sending association request")
        yield self.env.timeout(np.abs(self.rng.standard_normal()))
        print("Association approved")

    def send(self):
        print("Requesting channel")
        with self.channels.request() as rq:
            yield rq
            print("Channel received")
            print("Starting to transmit")
            yield self.env.timeout(np.abs(self.rng.standard_normal()))
            print("Done transmitting")
            yield self.env.timeout(1)
            print("Connection teardown - disassociation")

        #  Wifi doesn't have a receiving window like LoRa?
        #  print("Opening receive windows")
        #  yield self.env.timeout(np.abs(self.rng.standard_normal()))
        #  print("Closing receive windows")

    def run(self):
        while True:
            yield self.env.process(self.auth())
            yield self.env.process(self.association())
            yield self.env.process(self.send())
