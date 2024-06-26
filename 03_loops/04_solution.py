inp_string = input("Enter the string: ")
reversed_str = ""
for i in inp_string:
    print(i)
    reversed_str = reversed_str+i
    
print(reversed_str)
print(inp_string[::-1])