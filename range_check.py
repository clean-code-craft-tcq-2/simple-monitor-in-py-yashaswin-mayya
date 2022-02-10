
class BMS_parameter_range:

    def __init__(self, min, max):
        self.minimum_value = min
        self.maximum_value = max

    def isValueInRange(self, parameterValue):
        return not((parameterValue < self.minimum_value) or (parameterValue > self.maximum_value))