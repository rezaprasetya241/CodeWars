def life_path_number(birthdate):
    li = birthdate.replace("-", "")
    res = 0
    for x in li:
        res += int(x)
        
        if(res>9):
            res = res%10 + res //10
    return res

print(life_path_number("1971-06-28")) #result = 7
#best practice
def life_path_number(s):
    return int(s.replace("-", "")) % 9 or 9