call_stack = []

def fibonacci(n):
    # Debugging: storing call stack
    call_stack.append(f'fibonacci{n}')
    
    # Base conditions
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive calls
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    print(fibonacci(5))
    
    print("Recursive call stack:", call_stack)
    # Output: Recursive call stack : ['fibonacci5', 'fibonacci4', 'fibonacci3', 'fibonacci2', 'fibonacci1', 'fibonacci0', 'fibonacci1', 'fibonacci2', 'fibonacci1', 'fibonacci0', 'fibonacci3', 'fibonacci2', 'fibonacci1', 'fibonacci0', 'fibonacci1']

if __name__ == "__main__":
    main()
