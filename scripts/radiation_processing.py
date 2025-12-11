import rasterio
import numpy as np
import os

def load_radiation(path):
    """Load daily/monthly solar radiation raster (Wh/m2)."""
    with rasterio.open(path) as src:
        return src.read(1), src.profile

def compute_monthly_avg(radiation):
    """Return average radiation for statistics or visualization."""
    return np.mean(radiation)

def main():
    data_path = "../data/solar_radiation_monthly.tif"

    if not os.path.exists(data_path):
        print("⚠️ ERROR: Radiation file not found:", data_path)
        return

    radiation, profile = load_radiation(data_path)
    avg_value = compute_monthly_avg(radiation)

    print(f"Average monthly solar radiation: {avg_value:.2f} Wh/m²")

if __name__ == "__main__":
    main()
