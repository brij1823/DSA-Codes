#First Approach - Use an additional datastructure - SET
'''user_string = input()
set_string = set(user_string)

if(len(user_string) == len(set_string)):
    print("Is Unique")
else:
    print("Not Unique")'''
    
    
#Second Approach - Without using additional datastructure

'''user_string = input()
is_unique = {}
flag = 0
for i in user_string:
    if(i in list(is_unique.keys())):
        flag = 1
        print('Not Unique')
        break
    else:
        is_unique[i] = 1
if(flag == 0):
    print('Unique')'''
    
    
    

