def likes(names):
    if(len(names) == 0):
        return "no one likes this"
    # your code here
    else:
        if(len(names) == 1):
            return names[0] + " likes this"
        elif(len(names)==2):
            strRes = str(names[0]) + " and " + str(names[1]) + " like this"
        elif(len(names)==3):
            strRes = str(names[0:2]) + " and " + str(names[-1]) + " like this"
        elif(len(names)>3):
            strRes = str(names[0:2]) + " and " +str(len(names)-2) + " others" + " like this"
    for x in "[]'":
        strRes = strRes.replace(x,"")    
    return strRes
#print(likes(["Alex", "Jacob","Mark", "Max"]))

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
print(likes(["Alex", "Jacob", "Mark", "Max"])) # must be "Alex, Jacob and 2 others like this"
