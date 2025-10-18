import numpy as np

class PD_Controller:
    # Use default values from specification
    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        self.kp = kp
        self.kd = kd
        self.last_error = 0
    
    def reset(self):
        self.last_error = 0

    def control(self, error: float, t: int) -> float:
        last_error = self.last_error
        self.last_error = error

        return self.kp * error + self.kd * (error - last_error)
    