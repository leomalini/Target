import math

fib = [1,1]
i = 0
num = int(input("Digite um número: "))

while num > len(fib):
	fib.append(fib[i] + fib[i+1])
	i+=1

print ('Fibonacci(%d): %d' %(num,fib[num-1]))


def quadPerfeito(num):
    s = int(math.sqrt(num))
    return s*s == num

def fibonacci(num):
    return quadPerfeito(5*num*num + 4) or quadPerfeito(5*num*num - 4)

if(fibonacci(num) == True):
    print(num, "pertence a sequencia fibonacci")
else:
    print(num, "não pertence a sequencia fibonacci")
    