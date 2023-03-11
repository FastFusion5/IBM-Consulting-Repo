inputData = open("")
allValid = True
errorCodes = []
for record in len(inputData.partition("\n")[0]):
    allValid = record.isValid
    if record.isValid is not True:
        errorMessage = record[-1]
        errorCodes.append(errorMessage)
        
if allValid is True:
    print("Yes")
else:
    print("No")
    result = " ".join(errorCodes)
    print(errorCodes)