
class BMS_parameter_range:

    def __init__(self, min, max):
        self.minimum_value = min
        self.maximum_value = max

    def range_specifier_function(self, parameterValue):
        #return not(parameterValue<self.minimum_value or parameterValue>self.maximum_value)
        if(parameterValue<self.minimum_value):
            return 'LOW_BREACH'
        elif(parameterValue>self.maximum_value):
            return 'HIGH_BREACH'
        else:
            return 'NORMAL'

    
    def tolerance_specifier_function(self, parameterValue):
        self.tolerance = 0.05 * self.maximum_value
        #return (parameterValue<(self.minimum_value+self.tolerance) or parameterValue>(self.maximum_value-self.tolerance))
        if(parameterValue<(self.minimum_value+self.tolerance)):
            return 'LOW_WARNING'
        elif(parameterValue>(self.maximum_value-self.tolerance)):
            return 'HIGH_WARNING'
        else:
            return 'NORMAL'