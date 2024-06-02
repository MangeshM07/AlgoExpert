def phoneNumberMnemonics(phoneNumber):
    dict_numbers = {"1":"1",
                   "0":"0",
                    "2":"abc",
                    "3":"def",
                    "4":"ghi",
                    "5":"jkl",
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz",
                    "10": " "
                   }

    result = [""]
    for digit in phoneNumber:
        lst = dict_numbers[digit]
        newresult = []
        for char in lst:
            for val in result:
                newresult.append(val+char)
        result = newresult
    return result


phoneNumber="1905"
print(phoneNumberMnemonics(phoneNumber))