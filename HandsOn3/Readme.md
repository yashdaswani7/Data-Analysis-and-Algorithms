### Name : Yash Daswani  
### Student ID: `1002257766`

## Code

```
function result = g(m)
   result = 1;
   for i = 1:m
       for j = 1:m
           result = result + 1;
```

### Runtime of algorithm (Math approach)

![WhatsApp Image 2024-09-10 at 6 29 16 PM](https://github.com/user-attachments/assets/046c7ded-df45-4eab-854e-092e40771e1b)

### Plot : time vs n

![time vs n](https://github.com/user-attachments/assets/1524f218-15b8-491b-8ef8-20ebf5eeb190)

### Upper bound vs Lower Bound 

![lowe upper bound](https://github.com/user-attachments/assets/c891ccf9-57fd-444d-8482-10fdb507b70d)

## Results

### Big-O Notation (O)
The function `g(m)` is \( O(m^2) \) because the runtime grows quadratically with \( m \).

### Big-Omega Notation (Ω)
The function `g(m)` is \( \Omega(m^2) \) because the runtime has a lower bound that grows quadratically with \( m \).

### Big-Theta Notation (Θ)
The function `g(m)` is \( \Theta(m^2) \) because the runtime grows quadratically with \( m \), and both the upper and lower bounds are \( m^2 \).

### Approx location of m_0

![N_0_zoomed](https://github.com/user-attachments/assets/14444eaf-b404-4dfb-b3b6-b0e45fa453b9)

![N_0](https://github.com/user-attachments/assets/91c490f6-8602-4334-a6ee-bd5f06312f37)



### Time Complexity:
Even with the additional operation `temp = i + j`, this does not affect the number of iterations of the nested loops.

Each loop still runs \( m \times m \) times, and the added operation inside the loop does not increase the overall time complexity. Hence, the time complexity of the modified function remains \( O(m^2) \).

However, the constant factor in execution time might increase slightly due to the extra computation of `temp`.

### Effect on Original Results
In the original function analysis, the runtime was determined to be \( O(m^2) \) based on the number of iterations in the nested loops.

The additional operation in the modified function does not change this result:
- The time complexity remains \( O(m^2) \) since the number of iterations remains the same.
- The extra computation inside the loop causes a slight increase in the actual runtime, although this is a constant factor and does not affect the asymptotic complexity.






