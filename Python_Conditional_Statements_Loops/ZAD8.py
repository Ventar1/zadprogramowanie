#9. Write a Python program to get the Fibonacci series between 0 and 50.
#Note : The Fibonacci Sequence is the series of numbers :
#0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Every next number is found by adding up the two numbers before it.
#Expected Output : 1 1 2 3 5 8 13 21 34
a, b = 0, 1
fibonacci_series = []
while b < 50:
    fibonacci_series.append(b)
    a, b = b, a + b

print("Seria liczb Fibonacciego między 0 a 50:", fibonacci_series)
