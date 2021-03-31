from typing import List
import numpy as np
def decipher_message(message):
    arr = list(message)
    number = 1
    while number*number != len(arr):
        number+=1
    for x in range(len(arr)):
        y= arr[x+number]
        arr[x] = y
    print(arr)
    pass



decipher_message('ArNran u rstm5twob  e ePb')#, 'Answer to Number 5 Part b')
#test.assert_equals(decipher_message('ArNran u rstm8twob  e ePc'), 'Answer to Number 8 Part c')