import matplotlib.pyplot as plt
import numpy as np
import VTOLParam as P
from signalGenerator import signalGenerator
from VTOLAnimation import VTOLAnimation
from dataPlotter import dataPlotter

# instantiate reference input classes for self, t, states, z_ref, h_ref, force, torque
reference = signalGenerator(amplitude=0.5, frequency=0.1)
zRef = signalGenerator(amplitude=0.5, frequency=0.1)
hRef = signalGenerator(amplitude=0.5, frequency=0.1)
thetaRef = signalGenerator(amplitude=.25, frequency=.5)
fRef = signalGenerator(amplitude=5, frequency=.5)
torqueRef = signalGenerator(amplitude=5, frequency=.5)

# instantiate the simulation plots and animation
dataPlot = dataPlotter()
animation = VTOLAnimation()

t = P.t_start  # time starts at t_start

while t < P.t_end:  # main simulation loop
    # set variables
    r = reference.square(t)
    z = zRef.sin(t)
    h = hRef.sin(t)
    theta = thetaRef.square(t)
    f = fRef.sawtooth(t)
    tau = torqueRef.sawtooth(t)
    # update animation for self, t, states, z_ref, h_ref, force, torque
    state = np.array([[z], [h], [theta], [0.0], [0.0], [0.0]])
    animation.update(state)
    dataPlot.update(t, state, z, h, f, tau)
    # advance time by t_plot
    t = t + P.t_plot
    plt.pause(0.05)  # allow time for animation to draw
    
# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()

