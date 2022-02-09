import range_check

def Tester(BMS_Parameter,BMS_Parameter_value,expected_result):
  
  assert(BMS_Parameter.isValueInRange(BMS_Parameter_value) is expected_result)
  
if __name__ == '__main__':
  
  Battery_parameter_Range_Temperature = range_check.BMS_Parameter_Range(0,45)
  Battery_parameter_Range_SOC = range_check.BMS_Parameter_Range(20,80)
  Battery_parameter_Range_Charge_Rate = range_check.BMS_Parameter_Range(0,0.8)

  Tester(Battery_parameter_Range_Temperature,30,True)
  print('All is Well!')
