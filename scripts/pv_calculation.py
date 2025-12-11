import argparse
from pathlib import Path

import numpy as np
import rasterio


def load_radiation(radiation_path: str):
    """
    Load solar radiation raster.

    Parameters
    ----------
    radiation_path : str
        Path to the input radiation raster (kWh/m² over the analysis period).

    Returns
    -------
    radiation : np.ndarray
        2D array with solar irradiation values (kWh/m²).
    profile : dict
        Rasterio profile of the input raster, used to create the output raster.
    """
    radiation_path = Path(radiation_path)

    with rasterio.open(radiation_path) as src:
        # assuming a single-band raster
        radiation = src.read(1).astype("float32")
        profile = src.profile

        # replace nodata with NaN for safe math operations
        nodata = src.nodata
        if nodata is not None:
            radiation = np.where(radiation == nodata, np.nan, radiation)

    return radiation, profile


def compute_pv_energy(
    radiation: np.ndarray,
    panel_efficiency: float = 0.18,
    performance_ratio: float = 0.75,
    pixel_area: float = 1.0,
):
    """
    Compute PV energy output from solar radiation.

    Formula (per pixel):
        E = PR × Hs × S × η

        E  = PV energy (kWh over the period)
        PR = performance ratio (dimensionless, e.g. 0.75)
        Hs = solar irradiation (kWh/m² over the period)
        S  = pixel area (m²)
        η  = panel efficiency (dimensionless, e.g. 0.18)

    Parameters
    ----------
    radiation : np.ndarray
        Solar irradiation (kWh/m²).
    panel_efficiency : float
        PV panel efficiency η.
    performance_ratio : float
        System performance ratio PR.
    pixel_area : float
        Pixel area in m².

    Returns
    -------
    energy : np.ndarray
        PV energy output (kWh) for each pixel.
    """
    energy = radiation * pixel_area * panel_efficiency * performance_ratio

    # Preserve NaN where radiation was invalid
    return energy


def save_raster(output_path: str, data: np.ndarray, profile: dict):
    """
    Save a single-band raster with the given profile.

    Parameters
    ----------
    output_path : str
        Output file path.
    data : np.ndarray
        2D array with values to write.
    profile : dict
        Base rasterio profile to update.
    """
    output_path = Path(output_path)

    profile_out = profile.copy()
    profile_out.update(
        dtype=rasterio.float32,
        count=1,
        nodata=np.nan,
        compress="lzw",
    )

    with rasterio.open(output_path, "w", **profile_out) as dst:
        dst.write(data.astype("float32"), 1)


def main():
    parser = argparse.ArgumentParser(
        description="Compute PV energy output (kWh) from a solar-radiation raster (kWh/m²)."
    )

    parser.add_argument(
        "--radiation",
        required=True,
        help="Path to input solar-radiation raster (kWh/m²).",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Path to output PV energy raster (kWh).",
    )
    parser.add_argument(
        "--eta",
        type=float,
        default=0.18,
        help="PV panel efficiency η (default: 0.18).",
    )
    parser.add_argument(
        "--pr",
        type=float,
        default=0.75,
        help="Performance ratio PR (default: 0.75).",
    )
    parser.add_argument(
        "--pixel-area",
        type=float,
        default=None,
        help=(
            "Pixel area in m². If not provided, it will be derived "
            "from the raster resolution."
        ),
    )

    args = parser.parse_args()

    # 1) Load radiation raster
    radiation, profile = load_radiation(args.radiation)

    # 2) Derive pixel area (m²) if not given
    if args.pixel_area is None:
        # transform: a|b|c
        #            d|e|f
        # pixel size is |a| × |e|
        transform = profile["transform"]
        res_x = abs(transform[0])
        res_y = abs(transform[4])
        pixel_area = res_x * res_y
    else:
        pixel_area = args.pixel_area

    # 3) Compute PV energy
    energy = compute_pv_energy(
        radiation,
        panel_efficiency=args.eta,
        performance_ratio=args.pr,
        pixel_area=pixel_area,
    )

    # 4) Save result
    save_raster(args.output, energy, profile)

    print("---------------------------------------------------")
    print("PV energy computation finished.")
    print(f"Input radiation raster : {args.radiation}")
    print(f"Output PV energy raster: {args.output}")
    print(f"Panel efficiency (η)   : {args.eta}")
    print(f"Performance ratio (PR) : {args.pr}")
    print(f"Pixel area (m²)        : {pixel_area:.3f}")
    print("---------------------------------------------------")


if __name__ == "__main__":
    main()
