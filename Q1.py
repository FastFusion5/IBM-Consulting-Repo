inputList = []
while True:
    try:
       line = input()
    except EOFError:
        break
    inputList.append(line)
variables = inputList.split(",");
numberOfTShirts, TShirtSizes, numOfRequests, requestedSizes = variables
TShirtSizes = TShirtSizes.split(" ")
requestedSizes = requestedSizes.split(" ")
for i in range(len(requestedSizes)):
    if len(requestedSizes = 0):
        break
    else:
        if len(TShirtSizes) < len(requestedSizes):
            print("No")
        else:
            if requestedSizes[i] == "S" and TShirtSizes[i].contains("M"):
               TShirtSizes.pop(i)
               requestedSizes.pop(i)
            elif requestedSizes[i] == "M" and TShirtSizes[i].contains("L"):
               TShirtSizes.pop(i)
               requestedSizes.pop(i)
            elif (TShirtSizes[i].count("X") > requestedSizes[i].count("X") and TShirtSizes[i].contains("S")) or (TShirtSizes[i].count("X") > requestedSizes[i].count("X") and TShirtSizes[i].contains("L")):
               TShirtSizes.pop(i)
               requestedSizes.pop(i)
            else:
               print("No")
        print("Yes")