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

<p align="center">
  <img src="images/1.studyarea.png" width="350">
</p>

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

<p align="center">
  <img src="images/2.inputdata.png" width="150">
</p>---

## 2.3 Solar Radiation Modeling

The radiation modeling process included:

- Computation of direct, diffuse, and reflected radiation  
- Conversion of daily → monthly outputs  
- Extraction of radiation values per rooftop polygon  
- Validation against PVGIS (strong correlation in summer periods, higher error in winter)

---

## 2.4 PV Energy Estimation

### Energy per rooftop area:E1 = PR × Hs × S × η

### Energy per kWp capacity:E3 = PR × Hs × Wp / Istc

Where:  
- PR — Performance ratio  
- Hs — Solar radiation (kWh/m²)  
- S — Rooftop area  
- η — Panel efficiency  
- Wp — System peak power  
- Istc — Standard irradiance  

---

## 2.5 Key Findings

### Cully Association
- Larger rooftops → higher annual PV output  
- Best suited for large-scale PV installations  
- Payback period: **~17.3 years**

### Cathedral Park
- Smaller rooftops but consistent efficiency  
- Payback period: **~16.8 years**

---

# 3. Solar Thermal Potential Analysis

Solar thermal modeling focuses on domestic hot water (DHW) heating potential and collector sizing.

---

## 3.1 Energy Consumption Calculation

Daily DHW energy demand per person:Q_u,d = (V × ρ × c_p × ΔT) / ε

Using:  
- V = 0.06 m³/day  
- ρ = 1000 kg/m³  
- c_p = 1.163×10⁻³ kWh/kg·K  
- ΔT = 30 K  
- ε = 0.9  

**Result: 2.326 kWh/day per person**  
Scaled using district-level household sizes and days/month.

---

## 3.2 Thermal Production Equation
Q_u = A_C × H_sol × η_coll

Where:  
- A_C — Collector area  
- H_sol — Monthly radiation  
- η_coll — Collector efficiency  

---

## 3.3 Optimization of Collector Area

Initial design (30% rooftop coverage) → excessive summer production.  
To improve system performance:

### Adjust collector area so that **July demand = July production**:
A_C,July = Q_u / (H_sol × η_coll)

Benefits:
- Eliminates excess summer heat  
- Reduces installation cost  
- Improves annual energy balance  

---

## 3.4 Economic Results (Solar Thermal)

### Best collector options:
- **Cathedral Park → Vaillant Panels (~10.5 years payback)**  
- **Cully Association → Beretta Panels (~18.9 years payback)**  

---

# 4. Urban Building Energy Modeling & Retrofit Strategies

This section analyzes heating energy demand based on:

- Building typology  
- Construction period  
- Surface-to-volume ratio (S/V)  
- Shared wall conditions  
- Height differences  

---

## 4.1 Envelope Heat Loss Calculation

### Real Heat Loss Surface:
S1 = [(Perimeter × Height) + (Area × 2)] − Shared_Surface

### Building Volume:
V1 = (Area × Height) − (Shared_Surface × 0.4)
Outputs classify buildings into efficiency classes and reveal how form and age influence energy performance.

---

# 5. Retrofit Strategies & Energy Savings

Retrofit measures evaluated:

- Roof insulation  
- Wall insulation  
- Lower slab insulation  
- Window substitution  
- Combined retrofits  

### Key insights:
- Up to **42% energy reduction** for the combined retrofit  
- Roof insulation → best for older buildings  
- Wall insulation → best for post-1960 buildings  
- Lower slab insulation → shortest payback (5–7 years)  
- Window substitution → improves comfort but with higher cost  

---

# 6. General Conclusions

### PV Systems
- Cully: highest overall production  
- Cathedral Park: more consistent seasonal performance  

### Solar Thermal
- Optimized collector area prevents overproduction  
- Best collector type varies by district  

### Retrofit Strategy
- Roof insulation: optimal for older buildings  
- Wall insulation: effective for modern structures  
- Lower slab insulation: fastest economic return  

### Main Takeaway
**GIS-based solar modeling combined with energy retrofitting provides a powerful framework for sustainable urban energy planning and decarbonization.**

---



