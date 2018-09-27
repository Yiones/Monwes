from monwes.Beam import Beam
from monwes.Shape import BoundaryRectangle
import numpy as np
import matplotlib.pyplot as plt
from monwes.CompoundOpticalElement import CompoundOpticalElement
from monwes.Vector import Vector

do_plot = True
main = "__main__"


if main == "__main__":

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  example_montel_elliptical")

    beam = Beam(1e5)
    beam.set_flat_divergence(25*1e-6, 25*1e-6)
    #beam.set_rectangular_spot(xmax=25*1e-6, xmin=-25*1e-6, zmax=5*1e-6, zmin=-5*1e-6)
    beam.set_gaussian_divergence(25*1e-6, 25*1e-6)



    beam.flag *= 0

    p = 5.
    q = 15.
    #theta = np.pi/2 - 0.15
    theta = 85. * np.pi / 180

    xmax = 0.
    xmin = -0.3
    ymax =  0.1
    ymin = -0.1
    zmax =  0.3
    zmin = 0.

    bound1 = BoundaryRectangle(xmax, xmin, ymax, ymin, zmax, zmin)
    bound2 = BoundaryRectangle(xmax, xmin, ymax, ymin, zmax, zmin)


    montel = CompoundOpticalElement.initialize_as_montel_ellipsoid(p=p, q=q, theta_z=theta, bound1=bound1, bound2=bound2)
    beam1, beam2, beam03 = montel.trace_montel(beam, hitting_point=Vector(-0.0004, 0.004, 0.))

    beam03[2].plot_xz(0)
    plt.title("final plot of two reflection rays")

    print("No reflection = %d\nOne reflection = %d\nTwo reflection = %d" %(beam03[0].N, beam03[1].N, beam03[2].N))

    plt.show()