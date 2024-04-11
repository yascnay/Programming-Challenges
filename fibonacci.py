# Determine a Fibonacci sequence to generate n numbers
def gen_fibonacci(n):
     list_fib=[0,1]
    for i in range(1, n + 1):
        list_fib.append(list_fib[-1]+list_fib[-2])
    return list_fib

#Example of use
list_result=gen_fibonacci(10)
print(list_result)