import numpy as np

class PD_Controller:
    # Use default values from specification
    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        self.kp = kp
        self.kd = kd
        self.errors = []

    def control(self, error: float, t: int) -> float:
        self.errors.append(error)
        prev_error = self.errors[t - 1] if t > 0 else 0

        return self.kp * error + self.kd * (error - prev_error)