import matplotlib.pyplot as plt
import numpy as np
import VTOLParam as P
from signalGenerator import signalGenerator
from VTOLAnimation import VTOLAnimation
from dataPlotter import dataPlotter

# instantiate reference input classes
z_fakeValueGenerator = signalGenerator(amplitude=2.0*np.pi, frequency=1)
h_fakeValueGenerator = signalGenerator(amplitude=0.5, frequency=1)
theta_fakeValueGenerator = signalGenerator(amplitude=5, frequency=.5)
force_fakeValueGenerator = signalGenerator(amplitude=5, frequency=1)

# instantiate the simulation plots and animation
dataPlot = dataPlotter()
animation = VTOLAnimation()

t = P.t_start  # time starts at t_start
while t < P.t_end:  # main simulation loop
    # set variables
    z = z_fakeValueGenerator.sin(t)
    h = h_fakeValueGenerator.sin(t)
    tau = h_fakeValueGenerator.sawtooth(t)
    theta = theta_fakeValueGenerator.sin(t)
    force = force_fakeValueGenerator.sin(t)
    # update animation
    state = np.array([[z], [h], [theta], [0.0], [0.0], [0.0]])
    animation.update(state)
    dataPlot.update(t, state, [[5,1]], z, h)
    # advance time by t_plot
    t += P.t_plot
    plt.pause(0.001)

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
