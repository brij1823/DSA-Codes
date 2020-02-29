
#Approach 1 : Works but this is a O(n^2) approach

'''string1 = input()
string2 = input()

common_list = {}

for i in string1:
    if(i in common_list.keys()):
        common_list[i] = common_list[i]+1
    else:
        common_list[i] = 1
flag = 0
for i in string2:
    if(i in common_list.keys()):
        if(common_list[i]!=0):
            common_list[i] = common_list[i]-1
        else:
            flag = 1
            print('Not')
            break
    else:
        flag = 1
        print('Not')
        break
    
if(flag  == 0):
    print('Yes')'''
        

#Approach 2 : Sorting the strings
    
string1 = input()
string2 = input()


string1 = sorted(string1)
string2 = sorted(string2)

if(string1 == string2):
    print('Yes')
else:
    print('Not')
