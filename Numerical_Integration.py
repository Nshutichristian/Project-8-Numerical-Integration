"""
Riemann Sum Visualizations for Numerical Integration
Programmer: Christian Nshuti Manzi
Institution: Grand Canyon University
Course: CST-305
Professor: Ricardo Citro

This program implements numerical calculation of Riemann integrals for three functions:
1. f(x) = sin(x) + 1 on [-π, π]
2. f(x) = 3x + 2x² on [0, 1]
3. f(x) = ln(x) on [1, e]

The program generates visualizations of Left, Right, and Midpoint Riemann sums along with
their combined views, and calculates the approximate integral values.

Packages Used:
- numpy (for numerical operations)
- matplotlib (for visualization)
- math (for mathematical constants)

Approach:
1. For each function, divide the interval into n subintervals
2. Calculate rectangle heights using specified method (left/right/midpoint)
3. Compute the Riemann sum as sum of rectangle areas
4. Plot the function curve with Riemann rectangles
5. Display the approximate integral value
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Set consistent figure size for all plots
plt.rcParams['figure.figsize'] = [10, 6]

def calculate_riemann_sum(f, a, b, n, method='left'):
    """Calculate Riemann sum for given function and parameters
    
    Args:
        f (function): The function to integrate
        a (float): Lower bound of integration
        b (float): Upper bound of integration
        n (int): Number of subintervals
        method (str): 'left', 'right', or 'midpoint'
    
    Returns:
        tuple: (riemann_sum, rectangles) where rectangles are (x_left, height, width)
    """
    dx = (b - a)/n
    rectangles = []
    riemann_sum = 0.0
    
    for i in range(n):
        x_left = a + i*dx
        x_right = x_left + dx
        
        if method == 'left':
            x_point = x_left
        elif method == 'right':
            x_point = x_right
        else:  # midpoint
            x_point = (x_left + x_right)/2
        
        height = f(x_point)
        area = height * dx
        riemann_sum += area
        rectangles.append((x_left, height, dx))
    
    return riemann_sum, rectangles

def plot_riemann(f, a, b, n, method, color, title):
    """Plot Riemann sum visualization for a function
    
    Args:
        f (function): The function to plot
        a (float): Lower bound
        b (float): Upper bound
        n (int): Number of subintervals
        method (str): 'left', 'right', or 'midpoint'
        color (str): Color for rectangles
        title (str): Plot title
    """
    # Calculate Riemann sum and get rectangle data
    riemann_sum, rectangles = calculate_riemann_sum(f, a, b, n, method)
    
    # Create plot
    plt.figure()
    x_fine = np.linspace(a, b, 1000)
    
    # Plot rectangles
    for x_left, height, width in rectangles:
        plt.bar(x_left, height, width=width, alpha=0.3, 
                edgecolor=color, align='edge')
    
    # Plot function curve
    plt.plot(x_fine, f(x_fine), 'b-', linewidth=2)
    
    # Add title and labels
    plt.title(f"{title}\nRiemann Sum: {riemann_sum:.6f}")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()

# ====================== PART 1a: sin(x) + 1 ======================
def plot_sin_riemann():
    """Generate Riemann sum plots for sin(x) + 1 on [-π, π]"""
    def f(x):
        return np.sin(x) + 1
    
    a, b = -np.pi, np.pi
    n = 4
    
    # Individual methods
    plot_riemann(f, a, b, n, 'left', 'red', "sin(x) + 1 - Left Riemann Sum")
    plot_riemann(f, a, b, n, 'right', 'green', "sin(x) + 1 - Right Riemann Sum")
    plot_riemann(f, a, b, n, 'midpoint', 'purple', "sin(x) + 1 - Midpoint Riemann Sum")
    
    # Combined view
    plt.figure()
    x_fine = np.linspace(a, b, 1000)
    dx = (b - a)/n
    
    # Plot all methods together
    methods = ['left', 'right', 'midpoint']
    colors = ['red', 'green', 'purple']
    labels = ['Left', 'Right', 'Midpoint']
    
    for method, color, label in zip(methods, colors, labels):
        _, rectangles = calculate_riemann_sum(f, a, b, n, method)
        for x_left, height, width in rectangles:
            plt.bar(x_left, height, width=width, alpha=0.2, 
                    edgecolor=color, align='edge', label=label)
            # Only show label once
            label = None
    
    plt.plot(x_fine, f(x_fine), 'b-', linewidth=2)
    plt.title(f"sin(x) + 1 - All Riemann Methods (n={n})")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# ====================== PART 1b: 3x + 2x² ======================
def plot_quadratic_riemann():
    """Generate Riemann sum plots for 3x + 2x² on [0, 1]"""
    def f(x):
        return 3*x + 2*x**2
    
    a, b = 0, 1
    n = 10
    
    # Individual methods
    plot_riemann(f, a, b, n, 'left', 'red', "3x + 2x² - Left Riemann Sum")
    plot_riemann(f, a, b, n, 'right', 'green', "3x + 2x² - Right Riemann Sum")
    plot_riemann(f, a, b, n, 'midpoint', 'purple', "3x + 2x² - Midpoint Riemann Sum")
    
    # Combined view
    plt.figure()
    x_fine = np.linspace(a, b, 1000)
    dx = (b - a)/n
    
    # Plot all methods together
    methods = ['left', 'right', 'midpoint']
    colors = ['red', 'green', 'purple']
    labels = ['Left', 'Right', 'Midpoint']
    
    for method, color, label in zip(methods, colors, labels):
        _, rectangles = calculate_riemann_sum(f, a, b, n, method)
        for x_left, height, width in rectangles:
            plt.bar(x_left, height, width=width, alpha=0.2, 
                    edgecolor=color, align='edge', label=label)
            label = None
    
    plt.plot(x_fine, f(x_fine), 'b-', linewidth=2)
    plt.title(f"3x + 2x² - All Riemann Methods (n={n})")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# ====================== PART 1b4a: ln(x) ======================
def plot_ln_riemann():
    """Generate Riemann sum plots for ln(x) on [1, e]"""
    def f(x):
        return np.log(x)
    
    a, b = 1, math.e
    n = 8
    
    # Individual methods
    plot_riemann(f, a, b, n, 'left', 'red', "ln(x) - Left Riemann Sum")
    plot_riemann(f, a, b, n, 'right', 'green', "ln(x) - Right Riemann Sum")
    plot_riemann(f, a, b, n, 'midpoint', 'purple', "ln(x) - Midpoint Riemann Sum")
    
    # Combined view
    plt.figure()
    x_fine = np.linspace(a, b, 1000)
    dx = (b - a)/n
    
    # Plot all methods together
    methods = ['left', 'right', 'midpoint']
    colors = ['red', 'green', 'purple']
    labels = ['Left', 'Right', 'Midpoint']
    
    for method, color, label in zip(methods, colors, labels):
        _, rectangles = calculate_riemann_sum(f, a, b, n, method)
        for x_left, height, width in rectangles:
            plt.bar(x_left, height, width=width, alpha=0.2, 
                    edgecolor=color, align='edge', label=label)
            label = None
    
    plt.plot(x_fine, f(x_fine), 'b-', linewidth=2)
    plt.title(f"ln(x) - All Riemann Methods (n={n})")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# ====================== MAIN EXECUTION ======================
if __name__ == "__main__":
    print("Generating all Riemann sum visualizations...")
    
    print("\n=== Part 1a: sin(x) + 1 on [-π, π] ===")
    plot_sin_riemann()
    
    print("\n=== Part 1b: 3x + 2x² on [0, 1] ===")
    plot_quadratic_riemann()
    
    print("\n=== Part 1b4a: ln(x) on [1, e] ===")
    plot_ln_riemann()
    
    print("\nAll plots generated successfully!")