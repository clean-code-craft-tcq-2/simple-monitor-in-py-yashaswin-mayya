
class BMS_Parameter_Range:

    def __init__(self,min,max):
        self.min = min
        self.max = max

    def isValueInRange(self,parameterValue):
        return not(parameterValue < self.min or parameterValue > self.max)