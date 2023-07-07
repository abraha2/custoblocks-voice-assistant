num_dict = {"zero": "0",
            "one": "1",
            "two": "2",
            "to": "2",
            "three": "3",
            "four": "4",
            "for": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
            }

def str_to_num(string):
    result = []
    str_list = string.split()
    for each_word in str_list:
        if each_word in num_dict:
            Number = num_dict.get(each_word)
            if result[-1].isdigit():
                result[-1] += Number
            else:
                result.append(Number)
        else:
            result.append(each_word)
    return " ".join(result)
    
if __name__ == '__main__':
    while True:
        string = input("type: ")
        output = str_to_num(string)
        print(output)