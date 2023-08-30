import numpy as np
import matplotlib.pyplot as plt

def rk4_system(f, y0, t):
    """Solve a system of ODEs using fourth-order Runge-Kutta method.

    Parameters:
        f: callable(y, t) -> dy/dt
            Function that returns the derivatives of y with respect to t.
        y0: ndarray
            Initial values of y.
        t: ndarray
            Array of time points at which to solve for y.

    Returns:
        y: ndarray
            Array of y values corresponding to each time point in t.
    """
    dt = t[1] - t[0]  # Time step
    n = len(t)  # Number of time points
    m = len(y0)  # Number of variables
    y = np.zeros((n, m))  # Initialize output array
    y[0] = y0  # Set initial conditions

    for i in range(1, n):
        k1 = f(y[i-1], t[i-1])
        k2 = f(y[i-1] + 0.5*dt*k1, t[i-1] + 0.5*dt)
        k3 = f(y[i-1] + 0.5*dt*k2, t[i-1] + 0.5*dt)
        k4 = f(y[i-1] + dt*k3, t[i-1] + dt)

        y[i] = y[i-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)*dt

    return y

def harmonic_oscillator(y, t):
    omega_n = 2
    zeta = 0.25 #ez a zeta a dumping factor
    dydt = np.zeros(2)
    dydt[0] = y[1] # dy/dt = v
    #dv/dt = -2*zeta*omega_n*v - omega_n^2*y
    dydt[1] = -2*zeta*omega_n*y[1] - omega_n**2*y[0] #ez a dydt valojaban a dy/dt lenne a papiron
    return dydt

y0 = np.array([1.0, 0.0])  # Initial values for y and y'
t = np.linspace(0, 20, 1001)  # Time points

y = rk4_system(harmonic_oscillator, y0, t)

plt.plot(t, y[:, 0])
plt.xlabel('t')
plt.ylabel('y')
plt.title('Harmonic Oscillator')
plt.show()