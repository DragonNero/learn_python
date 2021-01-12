largest = None
smallest = None
while True :
    numberInput = input('Enter a number: ')
    if numberInput == 'Done':
        break

    try:
        intNumberInput = int(numberInput)
    except:
        print('Invalid input')
        continue

    if largest is None :
        largest = intNumberInput
    elif largest < intNumberInput :
        largest = intNumberInput

    if smallest is None :
        smallest = intNumberInput
    elif smallest > intNumberInput :
        smallest = intNumberInput

print("Maximum is", largest)
print("Minimum is", smallest)
