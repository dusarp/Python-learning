import numpy as np
import matplotlib.pyplot as plt

#logistic growth equation, models population growth with a carrying capacity
#Where y represents the population, t is the time, r: growth rate, K: carrying capacity of the environment. 

#dydt is the dy/dt, derivative of the population (y) with respect to time (t)



def rk4(f, y0, t):
    """Solve ODE using fourth-order Runge-Kutta method.

    Parameters:
        f: callable(y, t) -> dy/dt
            Function that returns the derivative of y with respect to t.
        y0: float or ndarray
            Initial value of y.
        t: ndarray
            Array of time points at which to solve for y.

    Returns:
        y: ndarray
            Array of y values corresponding to each time point in t.
    """
    dt = t[1] - t[0]  # Time step
    n = len(t)  # Number of time points
    y = np.zeros(n)  # Initialize output array
    y[0] = y0  # Set initial condition

    for i in range(1, n):
        k1 = f(y[i-1], t[i-1])
        k2 = f(y[i-1] + 0.5*dt*k1, t[i-1] + 0.5*dt)
        k3 = f(y[i-1] + 0.5*dt*k2, t[i-1] + 0.5*dt)
        k4 = f(y[i-1] + dt*k3, t[i-1] + dt)

        y[i] = y[i-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)*dt

    return y

def logistic_growth(y, t):
    r = 0.1
    K = 1000
    dydt = r * y * (1 - y / K)
    return dydt

y0 = 10.0  # Initial population
t = np.linspace(0, 50, 1001)  # Time points

y = rk4(logistic_growth, y0, t)

plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('Population')
plt.title('Logistic Growth')
plt.show()