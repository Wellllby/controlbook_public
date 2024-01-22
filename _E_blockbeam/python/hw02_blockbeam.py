import matplotlib.pyplot as plt
import numpy as np
import blockbeamParam as Parameter
from signalGenerator import signalGenerator
from blockbeamAnimation import blockbeamAnimation
from dataPlotter import dataPlotter

# instantiate reference input classes
reference = signalGenerator(amplitude=a_r, frequency=f_r)


# instantiate the simulation plots and animation
dataPlot = dataPlotter()
animation = blockbeamAnimation()

t = Parameter.t_start  # time starts at t_start
while t < Parameter.t_end:  # main simulation loop
    # set variables
    r = reference.square(t)
    z = zRef.sin(t)
    f = fRef.sawtooth(t)
    # update animation
    state = np.array([[z], [0.0]])
    animation.update(state)
    dataPlot.update(t, r, state, f)
    # advance time by t_plot    
    t = t + Parameter.t_plot  
    plt.pause(0.05)  # allow time for animation to draw
    
# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
