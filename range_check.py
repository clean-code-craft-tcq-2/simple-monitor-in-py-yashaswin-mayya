
class BMS_Parameter_Range:

    minimum_value = 0
    maximum_value = 0

    def __init__(self,min,max):
        self.minimun_value = min
        self.maximun_value = max

    def isValueInRange(self, parameterValue):
        return not(parameterValue < self.minimum_value or parameterValue > self.maximum_value)