import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class MCMC:
    """An class which applies actor to a System instance and updates it to the next step in MCMC."""
    pass


class Actor:
    """Methods wrapper for the proposal and acceptance steps in MCMC."""
    pass


def propose_optimize():
    """The proposal technique for optimization."""
    pass


def accept_optimize():
    """The acceptance technique for optimization."""
    pass


def propose_simulate(r, temp, timestep):
    """The proposal technique for simulation.
   
    :param r: (list, ndarray)
        initial positions

    :param temp: (int)
        simulation temperature

    :param timestep: (float)
        simulation timestep

    returns: (list, ndarray)
        new positions of the particles (same shape as <r>)
    """
    v_avg = #TODO: calculate average velocity of a particle according to MaxBoltz Distribution
    s_avg = #TODO: calculate average travel distace of a particle based on the v_avg and the timestep
    #<s_avg> can be used to change the positions of the particles. Travel distances will be normally distributed around the <s_avg> 
    r_new = np.copy(r) 
    
    indices = np.random.randint(0, len(r), size=np.random.randint(5, np.floor(len(r)*0.5))
    #creates an array of random indices of particles in a simulation box whose positions will be changed
    
    r_new[indices] += [np.reshape(np.random.randn((1,3))+s_avg, (3)) for _ in range(len(indices))]
    #changes the positions of selected particles 
    e_new = 
    if accept_simulate(r_new):
        trajectory.append(r_new) 
        energies.append(e_new)
    else:
        trajectory.append(r)
        energies.append(e)

def accept_simulate(r_new):
    """The acceptance technique for simulation."""

    pass


def show_frame(coordinates):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(coordinates[:, 0],
               coordinates[:, 1],
               coordinates[:, 2], )
    plt.show()
