'''
Program Name: Dollars to Euros
Programmer: me (not using real name here.)
Version: Alpha v0.0.1
For COMP-PROG W/PYTHON 1...

'''
while True:
    uInp = input("Would you like to convert dollars to euros?: ")
    uInpNReg = ["no", "nope", "No", "Nope", "no thanks", "false", "False"]
    if not uInp in uInpNReg:
        dVal = float("Enter dollar amount to be converted: ")
        erVal = round(dVal, 2)
        print("$" + str(dVal) + " equates to €" + str(erVal))
    else:
        break
