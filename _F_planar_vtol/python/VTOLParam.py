# VTOL Parameter File
import numpy as np

# Physical parameters of the  VTOL known to the controller
mc = 10 # kg
mr = 10 # kg
Jc = 10 # kg m^2
d  = 10  # m
mu = 10 # kg/s
g  = 10  # m/s^2
F_wind = 0 # wind disturbance force is zero in initial homeworks

# parameters for animation
length = 10.0

# Initial Conditions
z0        = 0  # initial lateral position
h0        = 0  # initial altitude
theta0    = 0  # initial roll angle
zdot0     = 0  # initial lateral velocity
hdot0     = 0  # initial climb rate
thetadot0 = 0  # initial roll rate
target0   = 0.0  # initial target

# Simulation Parameters
t_start = 0 # Start time of simulation
t_end =30  # End time of simulation
Ts = 30 # sample time for simulation
t_plot = .5 # the plotting and animation is updated at this rate

# saturation limits
fmax = 100  # Max Force, N

# dirty derivative parameters
# sigma =   # cutoff freq for dirty derivative
# beta =  # dirty derivative gain

# equilibrium force
# Fe =

# mixing matrix
unmixing = np.array([[1.0, 1.0], [d, -d]]) # converts fl and fr (LR) to force and torque (FT)
mixing = np.linalg.inv(unmixing) # converts force and torque (FT) to fl and fr (LR) 

