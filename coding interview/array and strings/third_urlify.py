user_input = input()
string1,length = user_input.split(',')
length = int(length)
reverse = len(string1) - length
string1 = string1[:length]
print(string1.replace(" ","%20"))