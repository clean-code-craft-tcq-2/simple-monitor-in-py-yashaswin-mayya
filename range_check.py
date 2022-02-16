
class BMS_parameter_range:

    def __init__(self, min, max):
        self.minimum_value = min
        self.maximum_value = max

    def range_specifier_function(self, parameterValue):
        if(parameterValue<self.minimum_value):
            return 'LOW_BREACH'
        elif(parameterValue>self.maximum_value):
            return 'HIGH_BREACH'
        else:
            BMS_parameter_range.tolerance_specifier_function(parameterValue)

    
    def tolerance_specifier_function(self, parameterValue):
        self.tolerance = 0.05 * self.maximum_value
        if(parameterValue<(self.minimum_value+self.tolerance)):
            return 'LOW_WARNING'
        elif(parameterValue>(self.maximum_value-self.tolerance)):
            return 'HIGH_WARNING'
        else:
            return 'NORMAL'