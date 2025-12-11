import numpy as np

def pv_energy(radiation, efficiency=0.18, performance_ratio=0.75, panel_area=1.6):
    """
    Estimate PV output using rooftop solar radiation.
    radiation: Wh/m2
    """
    return radiation * efficiency * performance_ratio * panel_area

def main():
    # Example values
    example_radiation = 120000  # Wh/m2 per month
    energy_output = pv_energy(example_radiation)

    print("Estimated PV energy (Wh):", energy_output)

if __name__ == "__main__":
    main()
