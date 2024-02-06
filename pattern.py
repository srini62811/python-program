def triangle_pattern(john):
    for i in range(1,len(john)+1):

        print(john[:i])
user=input("enter the string")
triangle_pattern(user)
