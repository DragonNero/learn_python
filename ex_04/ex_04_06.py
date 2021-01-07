def computepay(floatHoursInput, floatRateInput):
    #print("In computePay", floatHoursInput, floatRateInput)
    if floatHoursInput > 40:
        regularPay = floatRateInput * floatHoursInput
        overTimePay = (floatHoursInput - 40.0) * (floatRateInput * 0.5)
        pay = regularPay + overTimePay
    else:
            # print("Regular")
    	pay = floatHoursInput * floatRateInput
        #print("Returning", pay)
    return pay

hoursInput = input("Enter Hours: ")
rateInput = input("Enter Rate: ")
floatHoursInput = float(hoursInput)
floatRateInput = float(rateInput)

pay = computepay(floatHoursInput, floatRateInput)
print("Pay", pay)
