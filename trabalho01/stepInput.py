import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy import linalg

def quadcopter_pid(t, y, constants, pdy, pdz, pdΘ, refy, refz):
    Θc = (-1 / constants['g']) * (refy[2] + pdy[1] * (refy[1] - y[3]) + (refy[0] - y[0]) * pdy[0])
    u1 = constants['m']*(constants['g'] + refz[2] + pdz[1] * (refz[1] - y[4]) + (refz[0] - y[1])*pdz[0])
    u2 = (-pdΘ[1]*y[5] + pdΘ[0]*(Θc - y[2]))

    A = np.array([[1, 1], [constants['l'], -constants['l']]])
    A_inv = linalg.inv(A)

    f = A_inv.dot(np.array([[u1], [u2]]))
    f1 = f[0][0]
    f2 = f[1][0]

    x1dot = y[3]
    x2dot = y[4]
    x3dot = y[5]
    x4dot = -(f1+f2) * np.sin(y[2]) / constants['m']
    x5dot = ((f1+f2) / constants['m']) - constants['g']
    x6dot = (constants['l']*(f1-f2)) / constants['I']
    return [x1dot, x2dot, x3dot, x4dot, x5dot, x6dot]

def plot_all(title, t, z):
    plt.figure(figsize=(20, 12))

    plt.subplot(2, 3, 1)
    plt.plot(t, z.T[:,0], 'r')
    plt.xlabel('time (s)')
    plt.ylabel('Y position (m)')
    plt.title(title)
    plt.grid(True)

    plt.subplot(2, 3, 2)
    plt.plot(t, z.T[:,1], 'b')
    plt.xlabel('time (s)')
    plt.ylabel('Z position (m)')
    plt.grid(True)

    plt.subplot(2, 3, 3)
    plt.plot(t, z.T[:,2], 'g')
    plt.xlabel('time (s)')
    plt.ylabel('Θ angle (radians)')
    plt.grid(True)

    plt.subplot(2, 3, 4)
    plt.plot(t, z.T[:,3], 'y')
    plt.xlabel('time (s)')
    plt.ylabel('Y velocity (m/s)')
    plt.grid(True)

    plt.subplot(2, 3, 5)
    plt.plot(t, z.T[:,4], 'm')
    plt.xlabel('time (s)')
    plt.ylabel('Z velocity (m/s)')
    plt.grid(True)

    plt.subplot(2, 3, 6)
    plt.plot(t, z.T[:,5], 'c')
    plt.xlabel('time (s)')
    plt.ylabel('Θ angular velocity (radians/s)')
    plt.grid(True)

    plt.xlabel('time (s)')
    plt.show()

if __name__ == '__main__':
    y0 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    pdy, pdz, pdΘ, refy, refz = (6.0, 4.5), (12, 6.5), (3.5, 0.14), (1, 0, 0), (1, 0, 0)
    constants = dict(
        l=0.25,  # cm from CoM to rotor
        m=0.25,  # g
        I=0.001,  # kg*m^2
        g=9.81  # gravity, m/s^2
    )
    args = (constants, pdy, pdz, pdΘ, refy, refz)
    sol = solve_ivp(quadcopter_pid, [0, 10], y0, args=args, dense_output=True)
    t = np.linspace(0, 10, 100)
    z = sol.sol(t)
    plot_all(f'Quadcopter moving from (0,0) to ({(refy[0])},{refz[0]})', t, z)
