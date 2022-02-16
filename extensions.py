import range_check

warning_indicator = {
    'Temperature' : True,
    'State of Charge' : True,
    'Charge Rate' : True
}

language_support_select ={
        'English' : True,
        'German' : True
    }

def print_on_console_main(range_specifier, battery_parameter_object, BMS_parameter_name, BMS_parameter_value):

        BMS_parameter_without_underscore = BMS_parameter_name.replace('_', ' ') #To remove undrscore (_) while displaying on console

        if(language_support_select.get('English')):
            print_on_console_english(range_specifier, battery_parameter_object, BMS_parameter_without_underscore, BMS_parameter_value)
        if(language_support_select.get('German')):
            print_on_console_german(range_specifier, battery_parameter_object, BMS_parameter_without_underscore, BMS_parameter_value)



    
def print_on_console_english(range_specifier, battery_parameter_object, BMS_parameter_name, BMS_parameter_value):
    
    if(range_specifier == 'NORMAL'):
        print(f'\nEN: {BMS_parameter_name}: {BMS_parameter_value} is within defined range')
        print_early_warnings_english(battery_parameter_object, BMS_parameter_name, BMS_parameter_value)
    elif(range_specifier == 'LOW_BREACH'):
        print(f'\nEN: {BMS_parameter_name}: {BMS_parameter_value} is below the lower limit')
    else:
        print(f'\nEN: {BMS_parameter_name}: {BMS_parameter_value} is above the upper limit')



def print_on_console_german(range_specifier, battery_parameter_object, BMS_parameter_name_english, BMS_parameter_value):
    
    BMS_parameter_name_translator_to_german = {
        'Temperature' : 'Temperatur',
        'State of Charge' : 'Ladezustand',
        'Charge Rate' : 'Laderate'
    }

    BMS_parameter_name_german = BMS_parameter_name_translator_to_german.get(BMS_parameter_name_english)

    
    if(range_specifier == 'NORMAL'):
        print(f'\nDE: {BMS_parameter_name_german}: {BMS_parameter_value} liegt im definierten bereich')
        print_early_warnings_german(battery_parameter_object, BMS_parameter_name_german, BMS_parameter_value)
    elif(range_specifier == 'LOW_BREACH'):
        print(f'\nDE: {BMS_parameter_name_german}: {BMS_parameter_value} liegt unter dem unteren brenzwert')
    else:
        print(f'\nDE: {BMS_parameter_name_german}: {BMS_parameter_value} liegt über der obergrenze')




def print_early_warnings_english(battery_parameter_object, BMS_parameter_name, BMS_parameter_value):
    
    #if (warning_indicator.get(BMS_parameter_name) == False):
        #return

    tolerance_specifier_function = battery_parameter_object.tolerance_specifier_function(BMS_parameter_value)

    warning_range_specifier = {
        'LOW_WARNING' : 'is approaching the lower limit',
        'HIGH_WARNING' : 'is approaching the upper limit'
    }
    
    
    if(tolerance_specifier_function == 'LOW_WARNING' or tolerance_specifier_function == 'HIGH_WARNING'):
        print(f'EN: Warning! {BMS_parameter_name} {warning_range_specifier.get(tolerance_specifier_function)}')



def print_early_warnings_german(battery_parameter_object, BMS_parameter_name, BMS_parameter_value):
    
    tolerance_specifier_function = battery_parameter_object.tolerance_specifier_function(BMS_parameter_value)
    
    if (warning_indicator.get(BMS_parameter_name)):
        if(tolerance_specifier_function == 'LOW_WARNING'):
            print(f'DE: Warnung! {BMS_parameter_name} nähert sich der untergrenze')
        elif(tolerance_specifier_function == 'HIGH_WARNING'):
            print(f'DE: Warnung! {BMS_parameter_name} nähert sich der oberen grenze')




# Temperatur liegt im definierten Bereich
# Temperatur liegt unter dem unteren Grenzwert
# Temperatur liegt über der Obergrenze


# Ladezustand liegt im definierten Bereich
# Ladezustand liegt unter dem unteren Grenzwert
# Ladezustand liegt über der Obergrenze

# Laderate liegt im definierten Bereich
# Laderate liegt unter dem unteren Grenzwert
# Laderate liegt über der Obergrenze


# Warning = Warnung
# is approaching the lower limit = nähert sich der Untergrenze
# is approaching the upper limit = nähert sich der oberen Grenze
