from SiPANN.scee import Standard
from SiPANN.scee_int import SimphonyWrapper


def coupler(
    width: float = 0.5,
    thickness: float = 0.22,
    gap: float = 0.22,
    length: float = 10.0,
    sw_angle: float = 90.0,
    dx: float = 1.5,
    dy: float = 5.0,
    **kwargs,
):
    r"""Return simphony Directional coupler model.

    Args:
        width: Width of the straight in um (Valid for 0.4-0.6)
        thickness: Thickness of straight in um (Valid for 0.18-0.24)
        gap: Minimum distance between the two straights edge in um. (Must be > 0.1)
        length: float or ndarray Length of the straight portion of both straights in um.
        dx: Horizontal distance between end of coupler until straight portion in nm.
        dy: Vertical distance between end of coupler until straight portion in um.
        sw_angle: Sidewall angle from horizontal in degrees

    This is what most people think of when they think directional coupler.
    Ports are named as

    .. code::

                                                   H
               dx                                 dx
            |------|                           |------|
         o2 ________                           _______o3       _ _
                    \                         /           |     |
                     \        length         /            |    _|_V
                      ======================= gap         | dy
                     /                       \            |
            ________/                         \_______    |
         o1                                           o4


    .. plot::
        :include-source:

        import gdsfactory as gf

        c = gf.components.coupler(gap=0.2, length=10)
        c.plot()

    .. plot::
        :include-source:

        import gdsfactory.simulation.simphony.components as gc
        import gdsfactory.simulation simphony as gs

        c = gc.coupler()
        gs.plot_model(c)

    """

    # SiPANN units are in nm
    width = width * 1e3
    thickness = thickness * 1e3
    gap = gap * 1e3
    length = length * 1e3
    H = dx * 1e3
    V = dy * 1e3 / 2

    s = Standard(
        width=width,
        thickness=thickness,
        gap=gap,
        length=length,
        H=H,
        V=V,
        sw_angle=sw_angle,
    )
    model = SimphonyWrapper(s)
    model.pins = ("o1", "o2", "o4", "o3")
    model.sipann = s
    return model


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    from gdsfactory.simulation.simphony.plot_model import plot_model

    c = coupler()
    print(c)
    plot_model(c)
    plt.show()
