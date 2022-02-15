import range_check

warning_indicator = {
    'Temperature' : True,
    'State_of_Charge' : True,
    'Charge_Rate' : True
}


def print_early_warnings(battery_parameter_object, BMS_parameter, BMS_parameter_value):
    
    isValueInWarningRange = battery_parameter_object.isValueWithinTolerance(BMS_parameter_value)
    console_print_string = BMS_parameter.replace('_', ' ') #To remove undrscore (_) while displaying on console

    if (warning_indicator.get(BMS_parameter)):
        if(isValueInWarningRange == True):
            print(f'Warning! {console_print_string} is approaching its limit value')



