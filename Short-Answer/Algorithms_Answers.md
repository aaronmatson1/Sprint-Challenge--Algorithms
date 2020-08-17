#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime of the first function is O(n).. The function is dependent on the input value of n, but it does't require nested loops and perfoms a single operation using the values of a and n.

```python
a)  a = 0 #this loop is 0(n)
    while (a < n * n * n): #this section is O(1)
      a = a + n * n
```


b) The runtime for the second function is O(2^n). This is also referred to as a quadratic function. This is because of a loop nested inside of another loop.

```python
b)  sum = 0
    for i in range(n): #This loop is O(n)
      j = 1
      while j < n: #this loop is O(n)
        j *= 2 #this is O(1)
        sum += 1 #this is O(1)
```
The first loop sets up the conditions for the second loop. The second loop will run a complete execution for every iteration **i** in range(n). **j** will continue to grow with each iteration of the inner loop until the value of j is greater than the value of n. At that point, the first loop will iterate to the next value and the cycle repeats.

c) The runtime of this function is O(n). This recursive function will be called from within the function as many times as the value we pass into the function as an argument.

```python
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0
      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

So I would choose to divide the total numbner of floors by 2, and start by seeing if the egg would break if it is dropped from the middle floor.

```python
start = 0
end = len(n)
middle = (start + end) // 2
```

So if the an egg is dropped from the middle floor and breaks, then we know that we are still too high. So then we need to reduce the height of our middle value, and get rid of all of the floors above the middle value as candidates fo a non-breaking floor, because we know that we are still breaking eggs at our current height.

```python
start = 0
end = middle-1
middle = (start + end) // 2
```

BUT, if an egg dropped from the middle of the building doesn't break, then we know that we can maybe go higher.

```python
start = middle + 1
end = len(f)
middle = (start + end // 2)
```

we can then repeat the process of narrowing dow the floor range until we find the floors where the egg WILL break and where the egg will NOT break

Then once we do that, we can then return the value of the floor where the eggs will not break.

This function runs in a O(log n) runtime. While the number of executions does increase in respect to the value of n, it does it  at a reduced rate because we are reducing the total amount of work required to complete every subsequent execution