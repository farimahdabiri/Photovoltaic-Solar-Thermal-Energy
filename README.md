# Photovoltaic & Solar Thermal Energy Potential in Urban Districts (Portland, USA)

### GIS-based analysis of rooftop PV, solar thermal potential, energy consumption and retrofit strategies

This repository documents a GIS-based study evaluating solar radiation, rooftop photovoltaic (PV) potential, solar thermal production and energy retrofitting strategies for two residential districts in **Portland, Oregon**: **Cully Association** and **Cathedral Park**.

The project integrates:

- QGIS `r.sun` solar radiation modelling  
- PVGIS data for validation  
- PV energy production estimation  
- Urban building energy modelling  
- Economic and payback-time analysis of retrofit measures

---

## 1. Project Overview

The study investigates how much renewable energy can be produced from existing rooftops and how energy retrofits can reduce heating demand in Portland’s housing stock.

**Study area:**

- Two districts in Portland: Cully & Cathedral Park  
- Focus on residential buildings and their rooftop potential  
- Scale: urban district / neighbourhood

**Main research questions:**

1. How much PV electricity and solar thermal energy can be produced from rooftops?
2. How accurate are QGIS `r.sun` radiation results compared to PVGIS?
3. Which retrofit strategies (roof, wall, slab insulation, window substitution) give the best energy savings and payback times?
4. How do rooftop size, orientation and urban form affect renewable energy potential?

---

## 2. Data & Methods

### 2.1 Input Data

- **DSM (Digital Surface Model)** – terrain & shading
- **Aspect & Slope rasters**
- **Building footprints** – rooftop area & typology
- **Land use** – residential building stock
- **Solar radiation**: QGIS `r.sun` + PVGIS (for validation)
- **Climate data** – typical days per month
- **Energy consumption records** – residential sector in Portland

### 2.2 Solar Radiation Modelling (QGIS)

- Used **`r.sun`** to compute direct + diffuse solar radiation.
- Converted daily outputs to monthly radiation for seasonal analysis.
- Generated:
  - Global radiation per day (Wh/m²/day)
  - Global radiation per month (Wh/m²/month)
- Compared monthly profiles with **PVGIS** to validate model accuracy.

### 2.3 PV Energy Production

Two main equations were used:

- **E1 = PR × Hs × S × η**

  - *E1*: annual/monthly electrical energy produced (kWh/m²)  
  - *PR*: performance ratio  
  - *Hs*: solar radiation on the plane (kWh/m²)  
  - *S*: available rooftop area (m²)  
  - *η*: PV panel efficiency

- **E3 = PR × Hs × Wp / Istc**

  - *E3*: energy produced by 1 kWp of PV capacity  
  - *Wp*: peak system power for 6–8 m² PV surface  
  - *Istc*: solar irradiance under standard test conditions (1000 W/m²)

Results were compared between Cully & Cathedral Park for winter/summer and annual production.

---

## 3. Solar Thermal Potential & Optimization

Solar thermal analysis focused on domestic hot water demand in residential buildings.

### 3.1 Energy Consumption for Hot Water

Daily energy demand was estimated using:

- Water volume (V), density (ρ), specific heat (cₚ) and temperature difference (ΔT)  
- System efficiency (ε) for the heat exchanger

Daily demand per person was scaled to:

- Average household size  
- Number of days per month  
- Number of families per district

### 3.2 Solar Thermal Production

Thermal energy from collectors was calculated as:

- **Q_u = A_C × H_sol × η_coll,m**

  - *A_C*: collector area (m²)  
  - *H_sol*: monthly solar radiation on the collector (Wh/m²/month)  
  - *η_coll,m*: collector efficiency

Collector performance was corrected using **reduced temperature difference** (X), which accounts for the difference between fluid and air temperature and solar irradiance.

### 3.3 Collector Area Optimization (Step 5)

Initial designs produced more thermal energy than needed in summer.  
To avoid overproduction and reduce costs, the collector area was re-calculated to match **peak consumption (July)** instead of 30% of the rooftop area:

- **A_C,July = Q_u / (H_sol × η_coll,m)**

This optimization:

- Reduces installation and maintenance costs  
- Eliminates unnecessary energy surplus  
- Maintains sufficient production in winter months

---

## 4. Urban Building Energy Modelling & Retrofits

### 4.1 Factors Affecting Energy Use

- Construction period  
- Surface-to-volume ratio (S/V)  
- Building typology  
- Building height & shared surfaces between buildings  

Using GIS and field calculator, the following were computed for each building:

- Area & perimeter  
- Height (from stories or available attributes)  
- Shared surfaces (intersection of buffered footprints)  
- Real heat-loss surface (S1) and building volume (V1)

### 4.2 Retrofit Measures

Four retrofit options were evaluated:

1. Roof insulation  
2. Wall insulation  
3. Lower slab insulation  
4. Window substitution  

For each construction period and district:

- Energy savings (%)  
- Payback time (years)  
- Investment cost and total energy consumption after retrofit were calculated.

### 4.3 Key Findings

- **Roof insulation** is most effective for **older buildings** (pre-1960) with high heat losses through the roof.  
- **Wall insulation** is ideal for **newer buildings**, where walls dominate heat transfer.  
- **Lower slab insulation** has the **shortest payback time** (~5–7 years) but lower total savings.  
- **Window substitution** yields good comfort improvements but has higher costs.  
- **Combined retrofits (roof + wall + windows + slab)** provide the highest energy savings but require the largest investment and longest payback (>50 years).

---

## 5. District Comparison: Cully vs Cathedral Park

### PV & Solar Potential

- **Cully**:
  - Larger share of **industrial rooftops → higher total PV and solar output**
  - Best suited for large-scale rooftop PV deployment
- **Cathedral Park**:
  - Smaller rooftops but **more efficient orientation**
  - Stable PV performance despite lower total area

### Energy & Economy

- Both districts reach maximum solar radiation and energy production in **summer**; winter shows the lowest values.
- QGIS radiation estimates **closely match PVGIS** during high-sun periods; discrepancies increase in winter.
- Simple payback time for solar thermal collectors ranges from ~10–19 years depending on panel type and district.

**Policy implications:**

- Prioritize PV and solar thermal systems on well-oriented, large rooftops (industrial & multifamily).  
- Combine **retrofit policies** (roof & wall insulation subsidies) with **renewable incentives**.  
- Encourage comprehensive retrofit packages in older districts to reduce long-term heating demand.

---

## 6. Tools & Software

- **QGIS** (r.sun, raster & vector processing)
- **PVGIS** (EU JRC) for solar radiation data and validation
- **Excel** for energy and economic calculations
- **Illustrator / Inkscape** for cartography & layout

---

## 7. Repository Structure

```text
.
├── README.md                # Project description (this file)
└── images/                  # Project boards and figures
    ├── pv-01-overview.jpg
    ├── pv-02-solar-radiation.jpg
    ├── pv-03-economic-analysis.jpg
    ├── retrofit-01-intro.jpg
    ├── retrofit-02-methodology.jpg
    ├── retrofit-03-results.jpg
    ├── retrofit-04-policy.jpg
    ├── solar-thermal-01-method.jpg
    ├── solar-thermal-02-optimization.jpg
    └── solar-thermal-03-cost-benefit.jpg
