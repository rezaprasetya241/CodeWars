#buatan sendiri
'''def loose_change(cents):
    nickles = 5
    pennies = 1
    dimes = 10
    quarterz = 25
    if(cents <= 0 ):
        nickles = 0
        pennies = 0
        quarterz = 0
        dimes = 0
        change_dict = {'Nickels':nickles, 'Pennies': pennies, 'Dimes': dimes, 'Quarters': quarterz}
    else:
        quarterz=int(cents/25)
        cents=cents-(quarterz*25)
        if(cents%25 != 0):
            dimes=int(cents/dimes)
            cents-=dimes*10
            if(cents%10 != 0):
                nickles=int(cents/nickles)
                cents-=nickles*5
                if(cents%5 != 0):
                    pennies=int(cents/pennies)
                    change_dict = {'Nickels':nickles, 'Pennies': pennies, 'Dimes': dimes, 'Quarters': quarterz}
                else:
                    pennies = 0
                    change_dict = {'Nickels':nickles, 'Pennies': pennies, 'Dimes': dimes, 'Quarters': quarterz}

            else:
                nickles = 0
                pennies = 0
                change_dict = {'Nickels':nickles, 'Pennies': pennies, 'Dimes': dimes, 'Quarters': quarterz}
                

        else:
            nickles = 0
            pennies = 0
            dimes = 0
            change_dict = {'Nickels':nickles, 'Pennies': pennies, 'Dimes': dimes, 'Quarters': quarterz}
    return change_dict
'''
#best practice
import math
def loose_change(cents):
    if cents < 0:
        cents = 0
    cents = int(cents)
    
    change = {}

    change['Quarters'] = cents // 25
    cents = cents % 25

    change['Dimes'] = cents // 10
    cents = cents % 10

    change['Nickels'] = cents // 5
    cents = cents % 5
    
    change['Pennies'] = cents
    
    return change
print(loose_change(390))