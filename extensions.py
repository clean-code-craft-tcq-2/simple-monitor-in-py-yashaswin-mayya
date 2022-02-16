import range_check

warning_indicator = {
    'Temperature' : True,
    'State of Charge' : True,
    'Charge Rate' : True
    #Warning for any parameter can be turned on/off by setting the respective ones to True/False
    #Also, new parameters, if added in future can be added here without code change
}

language_support_select = {
        'English' : True,
        'German'  : True
        #Alert print language can be slected/deselected by setting respective language as True/False
        #Also, new language can be added here later. A function for the same has to be added in the end of this file for that
    }

def print_on_console_main(range_specifier, battery_parameter_object, BMS_parameter_name, BMS_parameter_value):

        BMS_parameter_without_underscore = BMS_parameter_name.replace('_', ' ') #To remove undrscore (_) while displaying on console

        if(language_support_select.get('English')):
            print_on_console_english(range_specifier, battery_parameter_object, BMS_parameter_without_underscore, BMS_parameter_value)
        if(language_support_select.get('German')):
            print_on_console_german(range_specifier, battery_parameter_object, BMS_parameter_without_underscore, BMS_parameter_value)



    
def print_on_console_english(range_specifier, battery_parameter_object, BMS_parameter_name, BMS_parameter_value):
    
    range_specifier_to_print = {
        'LOW_BREACH' : 'is below lower limit',
        'HIGH_BREACH' : 'is above upper limit',
        'LOW_WARNING' : 'is approaching the lower limit',
        'HIGH_WARNING' : 'is approaching the upper limit',
        'NORMAL' : 'is within defined range'
    }

    if not(warning_indicator.get(BMS_parameter_name)):
        range_specifier_to_print.update({'LOW_WARNING' : 'is within defined range'})
        range_specifier_to_print.update({'HIGH_WARNING' : 'is within defined range'})
        print(f'EN: {BMS_parameter_name}: {BMS_parameter_value} {range_specifier_to_print.get(range_specifier)}')
    
    else:
        print(f'EN: {BMS_parameter_name}: {BMS_parameter_value} {range_specifier_to_print.get(range_specifier)}')





def print_on_console_german(range_specifier, battery_parameter_object, BMS_parameter_name_english, BMS_parameter_value):
    
    BMS_parameter_name_translator_to_german = {
        'Temperature' : 'Temperatur',
        'State of Charge' : 'Ladezustand',
        'Charge Rate' : 'Laderate'
    }


    range_specifier_to_print = {
        'LOW_BREACH' : 'liegt unter dem unteren brenzwert',
        'HIGH_BREACH' : 'liegt über der obergrenze',
        'LOW_WARNING' : 'nähert sich der untergrenze',
        'HIGH_WARNING' : 'nähert sich der oberen grenze',
        'NORMAL' : 'liegt im definierten bereich'
    }

    BMS_parameter_name_german = BMS_parameter_name_translator_to_german.get(BMS_parameter_name_english)


    if not(warning_indicator.get(BMS_parameter_name_english)):
        range_specifier_to_print.update({'LOW_WARNING' : 'liegt im definierten bereich'})
        range_specifier_to_print.update({'HIGH_WARNING' : 'liegt im definierten bereich'})
        print(f'DE: {BMS_parameter_name_german}: {BMS_parameter_value} {range_specifier_to_print.get(range_specifier)}')
    
    else:
        print(f'DE: {BMS_parameter_name_german}: {BMS_parameter_value} {range_specifier_to_print.get(range_specifier)}')
