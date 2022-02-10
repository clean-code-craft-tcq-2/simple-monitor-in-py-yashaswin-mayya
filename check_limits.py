import range_check

class BMS_range_test:
  
  def tester(self, BMS_parameter, BMS_parameter_value, expected_result):

    self.obtained_result = parameters_dict.get(BMS_parameter).isValueInRange(BMS_parameter_value)
    assert(self.obtained_result is expected_result)


    console_print_string = BMS_parameter.replace('_',' ') #TO remove undrscore (_) while displaying on console

    if (self.obtained_result == True):
      print(f'{console_print_string} is within defined range\n')
    else:
      print(f'{console_print_string} is out of defined range\n')

      
  
if __name__ == '__main__':
  
  
  parameters_dict = {}
  parameters_dict.update({'Temperature' : range_check.BMS_parameter_range(0, 45)})
  parameters_dict.update({'State_of_Charge' : range_check.BMS_parameter_range(20, 80)})
  parameters_dict.update({'Charge_Rate' : range_check.BMS_parameter_range(0, 0.8)})
  #new parameters can be added here with range without disturbing other code



  battery_tester_object = BMS_range_test()



  #Test Cases for various conditions
  
  #Condition_1 - Values in Valid Range with Equivalence Class Partition(ECP)
  battery_tester_object.tester('Temperature', 22.5, True)
  battery_tester_object.tester('State_of_Charge', 50, True)
  battery_tester_object.tester('Charge_Rate', 0.4, True)

  #Condition_2 - Values within range for Boundary Value Analysis(BVA) 
  battery_tester_object.tester('Temperature', 45-0.1, True)
  battery_tester_object.tester('State_of_Charge', 80-0.1, True)
  battery_tester_object.tester('Charge_Rate', 0.8-0.1, True)
  battery_tester_object.tester('Temperature', 0+0.1, True)
  battery_tester_object.tester('State_of_Charge', 20+0.1, True)
  battery_tester_object.tester('Charge_Rate', 0+0.1, True)

  #Condition_3 - Values with bounday value for Boundary Value Analysis(BVA) 
  battery_tester_object.tester('Temperature', 45, True)
  battery_tester_object.tester('State_of_Charge', 80, True)
  battery_tester_object.tester('Charge_Rate', 0.8, True)
  battery_tester_object.tester('Temperature', 0, True)
  battery_tester_object.tester('State_of_Charge', 20, True)
  battery_tester_object.tester('Charge_Rate', 0, True)

  #Condition_4 - Values outside range for Boundary Value Analysis(BVA) 
  battery_tester_object.tester('Temperature', 45+0.1, False)
  battery_tester_object.tester('State_of_Charge', 80+0.1, False)
  battery_tester_object.tester('Charge_Rate', 0.8+0.1, False)
  battery_tester_object.tester('Temperature', 0-0.1, False)
  battery_tester_object.tester('State_of_Charge', 20-0.1, False)
  battery_tester_object.tester('Charge_Rate', 0-0.1, False)

  print('All is Well!')
