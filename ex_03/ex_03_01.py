hoursInput = input("Enter Hours: ")
rateInput = input("Enter Rate: ")
floatHoursInput = float(hoursInput)
floatRateInput = float(rateInput)
# print(floatHoursInput, floatRateInput)
if floatHoursInput > 40:
    # print("Overtime")
    regularPay = floatRateInput * floatHoursInput
    overTimePay = (floatHoursInput - 40.0) * (floatRateInput * 0.5)
    # print(regularPay, overTimePay)
    pay = regularPay + overTimePay
else:
        # print("Regular")
        pay = floatHoursInput * floatRateInput
print("Pay: ", pay)
