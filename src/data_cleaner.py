import pandas as pd
import numpy as np

from scipy.stats import zscore

class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()
        self.cleaned_df = None

    def clean(self):
        # Drop rows with missing values in key columns
        self.df = self.df.dropna(subset=['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']).copy()
        self.df = self.df.reindex().copy()

        # remove incorrect entries for GHI, the possible values for Global Horizontal Irradiance (GHI) are between 0 and 1000 W/m²
        self.df = self.df[(self.df['GHI'] >= 0) & (self.df['GHI'] <= 1000)]
        # remove incorrect entries for DNI, the possible values for Direct Normal Irradiance (DNI) are between 0 and 1000 W/m²
        self.df = self.df[(self.df['DNI'] >= 0) & (self.df['DNI'] <= 1000)]
        # remove incorrect entries for DHI, the possible values for Diffuse Horizontal Irradiance (DHI) are between 0 and 1000 W/m²
        self.df = self.df[(self.df['DHI'] >= 0) & (self.df['DHI'] <= 1000)]
        return self.df
    
    def remove_outliers(self):
        cols = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']
        z_scores = zscore(self.df[cols])
        # Create a DataFrame for Z-scores to align indices
        z_scores_df = pd.DataFrame(z_scores, columns=cols, index=self.df.index)

        # Identify outliers using Z-scores
        # A Z-score greater than 3 or less than -3 is typically considered an outlier
        # Filter the DataFrame to get the outliers
        outliers = self.df[np.abs(z_scores_df) > 3].any(axis=1)

        # Drop rows with outliers
        self.cleaned_df = self.df.loc[~outliers].reset_index(drop=True).copy()
        return self.cleaned_df
    