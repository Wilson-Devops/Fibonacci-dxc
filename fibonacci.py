# Fibonacci numbers module
def fibo(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(a)
        temp, a = a, b
        b=temp+a
        
    return result

def main():
    print(fibo(int(input("enter the number to check the sequence\n"))))

if __name__ == '__main__' : main()
