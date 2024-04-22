
#METHOD --1

def add(num):
    count=0
    for fa in range(1,num+1):
        if num%fa==0:
            count+=1
    return count
def prime(n):
    if n==2:
        return 'prime'
    else:
        return 'not prime'
num=int(input('Enter a Number : '))
print(prime(add(num)))






#METHOD  --2

def add(num,count=0):
    for fa in range(1,num+1):
        if num%fa==0:
            count+=1
    if count==2:
        return 'prime'
    else:
        return 'not prime'
num=int(input('Enter a Number : '))
    
print(add(num))



