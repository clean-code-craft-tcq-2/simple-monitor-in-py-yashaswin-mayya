import range_check

# def battery_is_ok(temperature, soc, charge_rate):
#   if temperature < 0 or temperature > 45:
#     print('Temperature is out of range!')
#     return False
#   elif soc < 20 or soc > 80:
#     print('State of Charge is out of range!')
#     return False
#   elif charge_rate > 0.8:
#     print('Charge rate is out of range!')
#     return False

#   return True


# if __name__ == '__main__':
#   assert(battery_is_ok(25, 70, 0.7) is True)
#   assert(battery_is_ok(50, 85, 0) is False)

class BMS_Parameters_Range_Test():

  def Tester(self, BMS_Parameter, BMS_Parameter_value, expected_result):
    assert(range_check.BMS_Parameter_Range.isValueInRange(BMS_Parameter_value) is expected_result)
  
if __name__ == '__main__':
  Battery_Parameter_Range_Set_Temprature = range_check.BMS_Parameter_Range(0, 45)
  Battery_Parameter_Range_Set_Temprature = range_check
  Battery_Parameter_Range_Set_SOC = range_check.BMS_Parameter_Range(20, 80)
  Battery_Parameter_Range_Set_ChargeRate = range_check.BMS_Parameter_Range(0, 0.8)

  Battery_Test_Object = BMS_Parameters_Range_Test()

  Battery_Test_Object.Tester(Battery_Parameter_Range_Set_Temprature, 30, True)

