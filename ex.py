x = int(input("Enter a number : "))
n = int(input("ENter number of terms : "))
sum = 0
for i in range(1,n+1):
    term = (x**i) / i
    sum += term

