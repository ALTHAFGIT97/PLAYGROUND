f = int (input("enter the mark"))
b = int (input("enter the mark"))
y = int (input("enter the mark"))

total=f+b+y
average=total/3.0
print("Total : ",total)
print("Average : ",average)
if f>=35 and b>=35 and y>=35:
    print("Result : pass")
else:
    print("Result : fail")
