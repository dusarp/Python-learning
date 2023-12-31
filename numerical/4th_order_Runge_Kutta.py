import numpy as np

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
#print("lefutott?")
#csinalok egy kis demot is vele:


#use it
import matplotlib.pyplot as plt 
#ez a diff egyenlet: y' = -y (dy/dt = - y)
def f(y, t):
    return -y

#initial condition 
y0 = 1.0
t = np.linspace(0, 10, 101)

y = rk4(f, y0, t)

plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y')
plt.show()

