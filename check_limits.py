import range_check

def Tester(BMS_Parameter, BMS_Parameter_value, expected_result):

    if (BMS_Parameter == 'Temperature'):
      range_check.BMS_Parameter_Range(0, 45)
    elif (BMS_Parameter == 'SOC'):
      range_check.BMS_Parameter_Range(20, 80)
    elif (BMS_Parameter == "Charge Rate"):
      range_check.BMS_Parameter_Range(0, 0.8)

    assert(range_check.isValueInRange(BMS_Parameter_value) is expected_result)
  


if __name__ == '__main__':
  Tester('Temperature', 30, True)
  print('All is Well!')
