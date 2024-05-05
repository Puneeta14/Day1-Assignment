## display fibonicii series of 10 numbers

def fibonacci(n):
    if n<=0:
        return
    elif n ==1:
        return 0
    elif n ==2:
        return 0,1
    else:
        series=[0,1] # initialize the series with the first two numbers 
        while len(series)<n:  # generate the fibonacci series
            next_number=series[-1]+series[-2]
            series.append(next_number)
        return series
    
# call the function to get the fibonacci series of 10 number

fib_series =fibonacci(10)

print("the fibonacci series of 10 numbers is :",fib_series)




























