# Hi hello how are you

def primary_num(num):
    for i in range(2,int(num/2)):
        if num%2==0:
            print("not prime")
            break
    else:
        print("prime")

primary_num(7)

