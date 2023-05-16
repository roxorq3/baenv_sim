import numpy as np


# 5g stand alone registration?

class Five_g:
    def __init__(self, env, rng, channels):
        self.env = env
        self.rng = rng
        self.channels = channels
        self.action = env.process(self.run())

    def nr_rcc_connection_setup(self):
        ## Should I include the preamble and Random Access Request/Response?
        # RCC setup request
        # RCC setup response (granted)
        # RCC setup complete (send message to 5g NodeB)
        return

    def registration(self):
        # Send registration message
        # Receive NAS identity request
        # Send NAS identity response
        # Receive NAS authentication request
        # Send Authentication response
        # call security_procedure()
        # Receive Reconfiguration message
        # Send Reconfiguration complete
        # Send NAS completed
        return

    def security_procedure(self):
        # Receive security mode Command
        # Send security mode complete
        return

    def send(self):
        print("Connection established")
        print("Starting to transmit")
        yield self.env.timeout(np.abs(self.rng.standard_normal()))
        print("Done transmitting")
        yield self.env.timeout(1)
        print("Opening receive window for download link")
        yield self.env.timeout(np.abs(self.rng.standard_normal()))
        print("Closing receive window for download link")

    def run(self):
        while True:
            yield self.env.process(self.nr_rcc_connection_setup())
            yield self.env.process(self.registration())
            yield self.env.process(self.send())
