# GIS-Based Urban Energy Assessment: Solar Potential, Thermal Systems, and Retrofit Strategies in Portland, USA

This repository presents a comprehensive GIS-based urban energy assessment conducted for two districts in Portland, Oregon — **Cully Association** and **Cathedral Park**.  
The study integrates spatial analysis, solar modeling, and building energy evaluation to quantify renewable energy potential and identify effective retrofit strategies for reducing energy consumption in residential areas.

The work includes:

- Photovoltaic (PV) Energy Potential Analysis  
- Solar Thermal Domestic Hot Water (DHW) Assessment  
- Urban Building Energy Modeling & Retrofit Strategy Evaluation  
- Economic and Payback Analysis for Renewable Installations  

---

## 1. Study Area

Two districts were selected due to their contrasting morphological and rooftop characteristics:

- **Cully Association** — larger industrial rooftops, high PV suitability  
- **Cathedral Park** — compact residential forms, stable solar performance  

Both districts offer valuable insights into how urban form influences renewable energy potential.

---

# 2. Photovoltaic (PV) Energy Potential

## 2.1 Objectives
1. Model rooftop solar radiation using GIS-based tools.  
2. Validate radiation outputs with PVGIS data.  
3. Estimate PV energy production at building scale.  
4. Evaluate economic feasibility and payback periods.

---

## 2.2 Data Inputs

- Digital Surface Model (DSM)  
- Slope & Aspect rasters  
- Diffuse-to-global radiation ratio  
- Linke turbidity values  
- Typical radiation days (12 per year)  
- Building footprints and rooftop areas  
- Performance ratio and panel efficiency  

Solar radiation was simulated using **QGIS r.sun**, producing daily and monthly radiation maps, later validated with **PVGIS**.

---

## 2.3 Solar Radiation Modeling

The radiation modeling process included:

- Computation of direct, diffuse, and reflected radiation  
- Conversion of daily → monthly outputs  
- Extraction of radiation values per rooftop polygon  
- Validation against PVGIS (strong correlation in summer periods, higher error in winter)

---

## 2.4 PV Energy Estimation

### Energy per rooftop area:
