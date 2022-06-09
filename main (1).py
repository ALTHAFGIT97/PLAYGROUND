para=[]


while True:
    line=input("enter the name")
    
    if line:
        para.append(line)
    else:
        break
print(para)
output='\n'.join(para)
print(output)