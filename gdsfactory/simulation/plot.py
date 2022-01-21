from pathlib import Path
from typing import Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame

import gdsfactory as gf


def plot_sparameters(
    df: DataFrame,
    logscale: bool = True,
    keys: Optional[Tuple[str, ...]] = None,
    dirpath: Path = gf.CONFIG["sparameters"],
    **sim_settings,
):
    """Plots Sparameters from a pandas DataFrame.

    Args:
        df: Sparameters pandas DataFrame
        logscale: plots 20*log10(S)
        keys: list of keys to plot, plots all by default.
        dirpath: where to store/read the simulations.

    Keyword Args:
        sim_settings: simulation settings for the write_sparameters_function

    """

    w = df["wavelengths"] * 1e3
    keys = keys or [
        key for key in df.keys() if key.lower().startswith("s") and key.endswith("m")
    ]

    for key in keys:
        if key in df:
            y = df[key]
            y = 20 * np.log10(y) if logscale else y
            plt.plot(w, y, label=key[:-1])
        else:
            raise ValueError(f"{key} not in {df.keys()}")
    plt.legend()
    plt.xlabel("wavelength (nm)")
    plt.ylabel("|S| (dB)") if logscale else plt.ylabel("|S|")


def plot_imbalance2x2(df: DataFrame, port1: str = "s13m", port2: str = "s14m") -> None:
    """Plots imbalance in % for 2x2 coupler"""
    y1 = df[port1].values
    y2 = df[port2].values
    imbalance = y1 / y2
    plt.plot(df.wavelength_nm, 100 * abs(imbalance))
    plt.xlabel("wavelength (nm)")
    plt.ylabel("imbalance (%)")
    plt.grid()


def plot_loss2x2(df: DataFrame, port1: str = "s13m", port2: str = "s14m") -> None:
    """Plots imbalance in % for 2x2 coupler"""
    y1 = df[port1].values
    y2 = df[port2].values
    plt.plot(df.wavelength_nm, abs(10 * np.log10(y1 ** 2 + y2 ** 2)))
    plt.xlabel("wavelength")
    plt.ylabel("excess loss (dB)")


plot_loss1x2 = gf.partial(plot_loss2x2, port1="S13m", port2="S12m")
plot_imbalance1x2 = gf.partial(plot_imbalance2x2, port1="S13m", port2="S12m")


if __name__ == "__main__":
    import gdsfactory.simulation as sim

    d = sim.get_sparameters_data(component=gf.c.mmi1x2)
    plot_sparameters(d, logscale=True)
    plt.show()
