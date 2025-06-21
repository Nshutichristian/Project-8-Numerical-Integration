# 📊 Numerical Integration Using Riemann Sums and Real-World Data Modeling

**Course**: CST-305  
**Institution**: Grand Canyon University  
**Professor**: Ricardo Citro  
**Student**: Christian Nshuti Manzi  

---

## 📘 Project Overview

This project implements numerical integration using **Riemann Sums** to approximate definite integrals and analyze real-world data. The work is divided into two main parts:

- **Part 1**: Develop and visualize Riemann sums for three mathematical functions.
- **Part 2**: Use polynomial modeling and integration to estimate total data downloaded from a media server using real-world-like rate data.

---

## ✅ Objectives

- Implement Riemann sum approximations (Left, Right, Midpoint)
- Visualize numerical integration using Python and Matplotlib
- Apply polynomial curve fitting to real-world rate data
- Calculate total quantities using definite integrals

---

## 🔢 Part 1: Riemann Sum Visualization Tool

### Functions Evaluated

1. `f(x) = sin(x) + 1` over `[-π, π]`
2. `f(x) = 3x + 2x²` over `[0, 1]`
3. `f(x) = ln(x)` over `[1, e]`

### Features

- Computes Left, Right, and Midpoint Riemann sums
- Generates bar graphs showing area under each approximation
- Includes combined visualizations for method comparison

---

## 🌐 Part 2: Real-World Data Application – Download Rate Modeling

### Data Collected

Download rates (in Mbps) were recorded each minute for 30 minutes:

| Minute | R(t) Mbps |
|--------|-----------|
| 0      | 46.15     |
| 1      | 47.969    |
| 2      | 49.376    |
| 3      | 50.421    |
| 4      | 51.154    |
| 5      | 51.621    |
| 6      | 51.865    |
| 7      | 51.926    |
| 8      | 51.841    |
| 9      | 51.644    |
| 10     | 51.366    |
| 11     | 51.036    |
| 12     | 50.678    |
| 13     | 50.315    |
| 14     | 49.965    |
| 15     | 49.645    |
| 16     | 49.368    |
| 17     | 49.144    |
| 18     | 48.980    |
| 19     | 48.881    |
| 20     | 48.847    |
| 21     | 48.877    |
| 22     | 48.966    |
| 23     | 49.106    |
| 24     | 49.287    |
| 25     | 49.495    |
| 26     | 49.712    |
| 27     | 49.919    |
| 28     | 50.095    |
| 29     | 50.211    |
| 30     | 50.241    |

---

### Polynomial Fit

A 4th-degree polynomial was fit to the above data to define a smooth function R(t):

R(t) = -0.0001t⁴ + 0.0094t³ - 0.2339t² + 2.0441t + 46.15


---

### Integration to Find Total Data

To estimate the total amount of data downloaded:

1. Multiply `R(t)` by 60 (convert rate from Mbps to megabits per minute)
2. Integrate this function over the interval `[0, 30]` minutes
3. Divide the result by 8 to convert **Megabits → Megabytes**

---

### Output

4th-Degree Polynomial R(t) (download rate in Mbps):
R(t) = -0.0001t⁴ + 0.0094t³ - 0.2339t² + 2.0441t + 46.15

Total data downloaded over 30 minutes:
≈ 90,004.67 Megabits
≈ 11,250.58 Megabytes


---

## 💻 How to Run

### Requirements

- Python 3.x
- NumPy
- SciPy
- Matplotlib

### Installation

```bash
pip install numpy scipy matplotlib
