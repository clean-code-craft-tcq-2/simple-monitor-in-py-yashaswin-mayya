import range_check

class BMS_Range_Test:
  
  def Tester(self, BMS_Parameter, BMS_Parameter_value, expected_result):
    assert(BMS_Parameter.isValueInRange(BMS_Parameter_value) is expected_result)
  
if __name__ == '__main__':
  
  Battery_Parameter_Range_for_Temperature = range_check.BMS_Parameter_Range(0, 45)
  Battery_Parameter_Range_for_SOC = range_check.BMS_Parameter_Range(20, 80)
  Battery_Parameter_Range_for_Charge_Rate = range_check.BMS_Parameter_Range(0, 0.8)

  Battery_Tester_Object = BMS_Range_Test()

  #Test Cases for various conditions
  
  #Condition_1 - Values in Valid Range with Equivalence Class Partition(ECP)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_Temperature, 22.5, True)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_SOC, 50, True)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_Charge_Rate, 0.4, True)

  #Condition_2 - Values within range for Boundary Value Analysis(BVA) 
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_Temperature, 45-0.1, True)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_SOC, 80-0.1, True)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_Charge_Rate, 0.8-0.1, True)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_Temperature, 0+0.1, True)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_SOC, 20+0.1, True)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_Charge_Rate, 0+0.1, True)

  #Condition_3 - Values with bounday value for Boundary Value Analysis(BVA) 
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_Temperature, 45, True)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_SOC, 80, True)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_Charge_Rate, 0.8, True)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_Temperature, 0, True)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_SOC, 20, True)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_Charge_Rate, 0, True)

  #Condition_4 - Values outside range for Boundary Value Analysis(BVA) 
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_Temperature, 45+0.1, False)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_SOC, 80+0.1, False)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_Charge_Rate, 0.8+0.1, False)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_Temperature, 0-0.1, False)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_SOC, 20-0.1, False)
  Battery_Tester_Object.Tester(Battery_Parameter_Range_for_Charge_Rate, 0-0.1, False)

  print('All is Well!')
