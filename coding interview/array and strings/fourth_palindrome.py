'''#Approach 1
string1 = input()
length = len(string1)
hash_table = {}
#dict.setdefault(hash_table, default=0)
for i in string1:
    if(i in hash_table.keys()):
        hash_table[i]=hash_table[i]+1
    else:
        hash_table[i]=1

flag = 0

for i in string1:
    if(hash_table[i]%2!=0):
        flag=flag+1
if(length%2 and flag == 1):
    print('Yes')

elif(length%2 == 0 and flag == 0):
    print('Yes')

else:
    print('No')
    
        
'''

'''
#Approach 2 - not need to check
string1 = input()
length = len(string1)
hash_table = {}
#dict.setdefault(hash_table, default=0)
for i in string1:
    try:
        if(hash_table[i] >= 1):
            hash_table[i] = hash_table[i]+1
    except:
        hash_table[i] = 1
flag = 0

for i in string1:
    if(hash_table[i]%2!=0):
        flag=flag+1
if(length%2 and flag == 1):
    print('Yes')

elif(length%2 == 0 and flag == 0):
    print('Yes')

else:
    print('No')'''
    
    
#Approach 3 : Just check whether ever or odd. Not need to maintain the counter
    
        
