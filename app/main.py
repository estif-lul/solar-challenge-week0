import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned datasets
df_benin = pd.read_csv("data/benin-cleaned.csv")
df_benin['Timestamp'] = pd.to_datetime(df_benin['Timestamp'])
df_sierra = pd.read_csv("data/sierraleone-cleaned.csv")
df_sierra['Timestamp'] = pd.to_datetime(df_sierra['Timestamp'])
df_togo = pd.read_csv("data/togo-cleaned.csv")
df_togo['Timestamp'] = pd.to_datetime(df_togo['Timestamp'])

# Country selection
st.title("Solar Data Dashboard")
country_selected = st.selectbox("Choose a country", ["Benin", "Sierra Leone", "Togo"])

# Dynamic data loading
if country_selected == "Benin":
    df = df_benin
elif country_selected == "Sierra Leone":
    df = df_sierra
else:
    df = df_togo


# Plot Solar Irradiance Over Time
st.subheader(f"Solar Irradiance Over Time for {country_selected}")
fig, ax = plt.subplots(figsize=(16, 8))
df[['GHI', 'DNI', 'DHI']].plot(ax=ax, linewidth=1)
ax.set_title(f"Solar Irradiance Over Time for {country_selected}", fontsize=16)
ax.set_ylabel("Values")
ax.set_xlabel("Timestamp")
ax.grid(True)
ax.legend(loc='upper right')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

# Boxplot comparison of solar metrics
st.subheader(f"Solar Irradiance Distribution in {country_selected}")
fig, ax = plt.subplots()
sns.boxplot(data=df[["GHI", "DNI", "DHI"]], ax=ax)
st.pyplot(fig)

# Heatmap for correlation between variables
st.subheader(f"Correlation Heatmap for {country_selected}")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df[["GHI", "DNI", "DHI", "Tamb", "RH"]].corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Wind speed distribution
st.subheader(f"Wind Speed Distribution for {country_selected}")
fig, ax = plt.subplots()
sns.histplot(df["WS"], bins=30, kde=True, ax=ax)
st.pyplot(fig)