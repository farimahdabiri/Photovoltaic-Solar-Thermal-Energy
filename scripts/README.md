# Python Scripts for Solar & Energy Analysis

This directory contains Python scripts used to automate solar radiation processing and photovoltaic energy estimation for the project.

---

## 1. `radiation_processing.py`
Processes DSM-based solar radiation data:

- Loads daily/monthly solar radiation rasters using `rasterio`
- Computes monthly or annual statistical summaries
- Prepares radiation datasets for PV performance modeling

---

## 2. `pv_calculation.py`
Computes photovoltaic energy output:

- Applies PV performance equations
- Uses radiation inputs and system parameters (PR, efficiency, area, Wp)
- Generates energy output for each rooftop or cell

---

These scripts demonstrate **Python-based GIS automation** for renewable-energy modeling, integrating raster processing and PV system estimation.
