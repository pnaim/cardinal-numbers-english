Ones= ("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")  #standard numbers
Tens= ("ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")  #multiplication of ten
Tens2= (10, 20, 30, 40, 50, 60, 70, 80, 90)
Exceptions= ("eleven", "twelve", "thirteen", "fifteen")  #unique structures
x = int(input("Input a 1-3 digit number:\n"))  #input for 1-3 digits
y = str(x)  #change the numbers to strings
if len(y) == 3:  #if the number has three digits
    print(Ones[int(y[0])], "hundred", end=" and ")
    if y[1:3] == "11":
        print(Exceptions[0])  #to make the string "eleven"
    elif y[1:3] == "12":
        print(Exceptions[1])  #to make the string "twelve"
    elif y[1:3] == "13":
        print(Exceptions[2])  #to make the string "thirteen"
    elif y[1:3] == "15":
        print(Exceptions[3])  #to make the string "fifteen"
    elif int(y[1:3])>10 and int(y[1:3])<20:
        print(Ones[int(y[len(y)-1])], end="")
        print("teen") #14 to 19 except 15
    elif y[1:3] == Tens2[0:9]:
        print(Tens[0:9])

elif len(y) == 2:
    if y[0:2] == "11": #for number eleven
        print(Exceptions[0])
    elif y[0:2] == "12":   #for number twelve
        print(Exceptions[1])
    elif y[0:2] == "13":   #for number thirteen
        print(Exceptions[2])
    elif y[0:2] == "15":   #for number fifteen
        print(Exceptions[3])
    elif int(y[0:2])>10 and int(y[0:2])<20:  #for number 14-19 except 15
        print(Ones[int(y[len(y)-1])], end="")
        print("teen")
    elif y[0:2] == Tens2[0:9]:
        print(Tens[0:10])

elif len(y) == 1:
    if x == 0:
        print("Zero")
    else:
        print(Ones[x])