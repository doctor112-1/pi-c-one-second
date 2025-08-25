import matplotlib.pyplot as plt
import numpy as np
import subprocess
import resource
import time
import math
import statistics

i = 0
y_points = np.array([])
x_points = np.array([])

def check_pi(pi_number):
    pi_to_check_against = str(math.pi)
    matches = 0
    for pi_digit1, pi_digit2 in zip(pi_number, pi_to_check_against):
        if pi_digit1 == pi_digit2:
            matches += 1
        else:
            break
    return matches - 1

while True:
    usage_start = resource.getrusage(resource.RUSAGE_CHILDREN)
    pi = subprocess.run(["./a.out", f"{i}"], capture_output=True, text=True)
    usage_end = resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu_time = usage_end.ru_utime - usage_start.ru_utime
    pi = str(pi.stdout).strip()
    result_check_pi = check_pi(pi)
    y_points = np.append(y_points, cpu_time)
    x_points = np.append(x_points, result_check_pi)
    plt.plot(result_check_pi, cpu_time, 'ro')
    i += 500
    if cpu_time > 0.1:
        break

# what does this do? no idea
trend = np.polyfit(x_points, y_points, 100)
trendpoly = np.poly1d(trend)
plt.plot(x_points, trendpoly(x_points))
plt.xlabel = "Digits"
plt.ylaber = "Runtime"
plt.show()
