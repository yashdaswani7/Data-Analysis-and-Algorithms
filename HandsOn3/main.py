import time
import numpy as np
import matplotlib.pyplot as plt

# Defined function g(m)
def g(m):
    counter = 1
    for i in range(m):
        for j in range(m):
            counter += 1
    return counter

# List of input sizes
m_values = list(range(1, 1000)) 
execution_times = []  

# Measuring the time for each input size
for m in m_values:
    start = time.time() 
    g(m)  
    stop = time.time()
    
    elapsed = stop - start  
    execution_times.append(elapsed)  

# Converting input sizes and execution times to numpy arrays for analysis
m_values_np = np.array(m_values)
execution_times_np = np.array(execution_times)

# Fitting a second-degree polynomial (quadratic) to the data
quad_coeffs = np.polyfit(m_values_np, execution_times_np, 2)
estimated_times = np.polyval(quad_coeffs, m_values)

# Plotting actual vs fitted execution times
plt.figure(figsize=(10, 6))
plt.plot(m_values, execution_times, label="Actual Execution Time")
plt.plot(m_values, estimated_times, label="Fitted Quadratic Curve", color='r')
plt.xlabel('m (Input Size)')
plt.ylabel('Time (Seconds)')
plt.title('Execution Time of g(m) vs Input Size m')
plt.legend()
plt.grid(True)
plt.show()

# Printing polynomial coefficients for verification
# print("Fitted quadratic polynomial coefficients:", quad_coeffs)

# Defining the Upper and Lower Bounds for the execution time
upper_bound = quad_coeffs[0] * m_values_np**2
lower_bound = quad_coeffs[0] * m_values_np**2 * 0.8  # Assuming lower bound as 80% of upper bound

# Plotting Upper and Lower Bounds along with actual times and fitted curve
plt.figure(figsize=(10, 6))
plt.plot(m_values, execution_times, label="Actual Execution Time")
plt.plot(m_values, estimated_times, label="Fitted Quadratic Curve", color='r')
plt.plot(m_values, upper_bound, label="Upper Bound", color='g')
plt.plot(m_values, lower_bound, label="Lower Bound", color='orange')
plt.xlabel('m (Input Size)')
plt.ylabel('Time (Seconds)')
plt.title('Upper and Lower Bounds for Execution Time of g(m)')
plt.legend()
plt.grid(True)
plt.show()

# Estimating the critical input size (m_0) where actual time exceeds the fitted curve
m_0_index = np.where(execution_times_np > estimated_times)[0][0]

# Plotting the point where the actual time starts to diverge from the estimated time
plt.figure(figsize=(10, 6))
plt.plot(m_values, execution_times, label="Actual Execution Time")
plt.plot(m_values, estimated_times, label="Fitted Quadratic Curve", color='r')
plt.axvline(x=m_values[m_0_index], color='k', linestyle='--', label=f"m_0 ~ {m_values[m_0_index]}")
plt.xlabel('m (Input Size)')
plt.ylabel('Time (Seconds)')
plt.title('Estimation of m_0 (Where Actual Time Diverges)')
plt.legend()

plt.grid(True)
plt.show()

print(f"Estimated m_0: {m_values[m_0_index]}")
