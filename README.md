# Solar Challenge Week 0 - Benin Solar Data EDA

This project performs exploratory data analysis (EDA) on solar and meteorological data collected from Benin (Malanville). The analysis aims to understand the relationships between solar irradiance, weather variables, and module performance, and to prepare the data for further modeling or reporting.

## Project Structure

```
.
├── data/
│   ├── benin-malanville.csv
│   └── benin-cleaned.csv
├── src/
│   ├── notebooks/
│   │   └── benin_eda.ipynb
│   └── benin_eda.py
└── README.md
```

## Features

- Data cleaning and outlier removal
- Correlation and relationship analysis (heatmaps, scatter plots)
- Wind distribution analysis (wind rose, histograms)
- Visualization of time series and variable distributions
- Bubble charts for multi-variable relationships

## Requirements

- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- windrose

Install dependencies with:
```
pip install pandas numpy matplotlib seaborn scipy windrose
```

## Usage

1. **Data Preparation:**  
   Place your raw data file (e.g `benin-malanville.csv`) in the `data/` directory.

2. **Run the Notebook:**  
   Open `src/notebooks/[country]_eda.ipynb` in Jupyter or VS Code and run the cells to perform EDA and generate plots.

3. **Run the Script:**  
   Alternatively, run `src/[country]_eda.py` for a script-based analysis:
   ```
   python src/[country]_eda.py
   ```

4. **Outputs:**  
   - Cleaned data is saved as `[country]-cleaned.csv` in the `data/` directory.
   - Plots are displayed inline in the notebook or as output from the script.

## Key Analyses

- **Correlation Heatmap:**  
  Visualizes relationships between GHI, DNI, DHI, TModA, and TModB.

- **Scatter Plots:**  
  Explore relationships such as WS, WSgust, WD vs. GHI, and RH vs. Tamb/GHI.

- **Wind Rose:**  
  Shows wind speed and direction distribution.

- **Histograms:**  
  Distribution of GHI and wind speed.

- **Bubble Chart:**  
  GHI vs. Tamb with bubble size representing RH.

---

**Author:**  
Estifanos Lulseged  
Solar Challenge Week 0
