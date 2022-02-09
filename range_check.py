
class BMS_Parameter_Range:

    def __init__(self,min,max):
        self.minimun_value = min
        self.maximun_value = max

    def isValueInRange(self, parameterValue):
        return ((parameterValue > self.minimum_value) and (parameterValue < self.maximum_value))