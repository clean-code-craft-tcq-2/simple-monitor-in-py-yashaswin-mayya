import range_check

class BMS_range_test:
  
  def tester(self, BMS_parameter, BMS_parameter_value, expected_result):
    assert(BMS_parameter.isValueInRange(BMS_parameter_value) is expected_result)
  
if __name__ == '__main__':
  
  battery_parameter_range_for_temperature = range_check.BMS_parameter_range(0, 45)
  battery_parameter_range_for_SOC = range_check.BMS_parameter_range(20, 80)
  battery_parameter_range_for_charge_rate = range_check.BMS_parameter_range(0, 0.8)

  battery_tester_object = BMS_range_test()

  #Test Cases for various conditions
  
  #Condition_1 - Values in Valid Range with Equivalence Class Partition(ECP)
  battery_tester_object.tester(battery_parameter_range_for_temperature, 22.5, True)
  battery_tester_object.tester(battery_parameter_range_for_SOC, 50, True)
  battery_tester_object.tester(battery_parameter_range_for_charge_rate, 0.4, True)

  #Condition_2 - Values within range for Boundary Value Analysis(BVA) 
  battery_tester_object.tester(battery_parameter_range_for_temperature, 45-0.1, True)
  battery_tester_object.tester(battery_parameter_range_for_SOC, 80-0.1, True)
  battery_tester_object.tester(battery_parameter_range_for_charge_rate, 0.8-0.1, True)
  battery_tester_object.tester(battery_parameter_range_for_temperature, 0+0.1, True)
  battery_tester_object.tester(battery_parameter_range_for_SOC, 20+0.1, True)
  battery_tester_object.tester(battery_parameter_range_for_charge_rate, 0+0.1, True)

  #Condition_3 - Values with bounday value for Boundary Value Analysis(BVA) 
  battery_tester_object.tester(battery_parameter_range_for_temperature, 45, True)
  battery_tester_object.tester(battery_parameter_range_for_SOC, 80, True)
  battery_tester_object.tester(battery_parameter_range_for_charge_rate, 0.8, True)
  battery_tester_object.tester(battery_parameter_range_for_temperature, 0, True)
  battery_tester_object.tester(battery_parameter_range_for_SOC, 20, True)
  battery_tester_object.tester(battery_parameter_range_for_charge_rate, 0, True)

  #Condition_4 - Values outside range for Boundary Value Analysis(BVA) 
  battery_tester_object.tester(battery_parameter_range_for_temperature, 45+0.1, False)
  battery_tester_object.tester(battery_parameter_range_for_SOC, 80+0.1, False)
  battery_tester_object.tester(battery_parameter_range_for_charge_rate, 0.8+0.1, False)
  battery_tester_object.tester(battery_parameter_range_for_temperature, 0-0.1, False)
  battery_tester_object.tester(battery_parameter_range_for_SOC, 20-0.1, False)
  battery_tester_object.tester(battery_parameter_range_for_charge_rate, 0-0.1, False)

  print('All is Well!')
