hoursInput = input("Enter Hours: ")
rateInput = input("Enter Rate: ")
try:
    floatHoursInput = float(hoursInput)
    floatRateInput = float(rateInput)
except:
    print("Error, please enter numerical input")
    quit()

print(floatHoursInput, floatRateInput)
if floatHoursInput > 40:
    regularPay = floatRateInput * floatHoursInput
    overTimePay = (floatHoursInput - 40.0) * (floatRateInput * 0.5)
    pay = regularPay + overTimePay
else:
        pay = floatHoursInput * floatRateInput
print("Pay: ", pay)
