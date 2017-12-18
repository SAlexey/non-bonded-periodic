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


def propose_simulate():
    """The proposal technique for simulation."""
    pass


def accept_simulate():
    """The acceptance technique for simulation."""
    pass


def show_frame(coordinates):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(coordinates[:, 0],
               coordinates[:, 1],
               coordinates[:, 2], )
    plt.show()