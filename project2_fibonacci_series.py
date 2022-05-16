def fibonacci(num):
    num1 = 0
    num2 = 1
    series = 0
    #initially series is 0 captain
    for i in range(num):
        print(series, end=' ');
        num1 = num2;
        num2 = series;
        series = num1 + num2;
num = int(input('Enter number to print Fibonacci series- '))
fibonacci(num)
