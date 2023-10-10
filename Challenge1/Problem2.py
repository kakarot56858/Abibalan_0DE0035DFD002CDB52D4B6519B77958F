#leap year

def leap(n):
       if(n%4==0):
            print(n," is leap year")
       else:
            print(n," is not leap year")

n=int(input(" Enter the year "))
leap(n)
