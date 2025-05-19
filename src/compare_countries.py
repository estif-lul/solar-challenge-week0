import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

# Load datasets
df_benin = pd.read_csv("data/benin-cleaned.csv")
df_sierra = pd.read_csv("data/sierraleone-cleaned.csv")
df_togo = pd.read_csv("data/togo-cleaned.csv")

# Combine datasets with labels
df_benin["Country"] = "Benin"
df_sierra["Country"] = "Sierra Leone"
df_togo["Country"] = "Togo"
df_combined = pd.concat([df_benin, df_sierra, df_togo])

# List of metrics to compare
metrics = ["GHI", "DNI", "DHI"]

# Create one boxplot per metric, colored by country
fig, axes = plt.subplots(1, len(metrics), figsize=(18, 6))
for i, metric in enumerate(metrics):
    sns.boxplot(x="Country", y=metric, hue="Country", data=df_combined, palette="Set3", legend=False, ax=axes[i])
    axes[i].set_title(f"{metric} Distribution by Country")
    axes[i].set_xlabel("Country")
    axes[i].set_ylabel(metric)
plt.tight_layout()
plt.show()

# Compare key metrics: Mean, Median, Std Dev
summary_stats = pd.DataFrame({
    "Country": ["Benin", "Sierra Leone", "Togo"],
    "Mean GHI": [df_benin["GHI"].mean(), df_sierra["GHI"].mean(), df_togo["GHI"].mean()],
    "Mean DNI": [df_benin["DNI"].mean(), df_sierra["DNI"].mean(), df_togo["DNI"].mean()],
    "Mean DHI": [df_benin["DHI"].mean(), df_sierra["DHI"].mean(), df_togo["DHI"].mean()],
    "Median GHI": [df_benin["GHI"].median(), df_sierra["GHI"].median(), df_togo["GHI"].median()],
    "Median DNI": [df_benin["DNI"].median(), df_sierra["DNI"].median(), df_togo["DNI"].median()],
    "Median DHI": [df_benin["DHI"].median(), df_sierra["DHI"].median(), df_togo["DHI"].median()],
    "Std Dev GHI": [df_benin["GHI"].std(), df_sierra["GHI"].std(), df_togo["GHI"].std()],
    "Std Dev DNI": [df_benin["DNI"].std(), df_sierra["DNI"].std(), df_togo["DNI"].std()],
    "Std Dev DHI": [df_benin["DHI"].std(), df_sierra["DHI"].std(), df_togo["DHI"].std()],

})
print(summary_stats)

# Perform ANOVA test for each metric
f_statistic, p_value = f_oneway(df_benin["GHI"], df_sierra["GHI"], df_togo["GHI"])
print(f"P-value: {p_value}")

# Plotting the mean GHI for each country
plt.figure(figsize=(8, 6))
sns.barplot(
    x="Country", 
    y="Mean GHI", 
    data=summary_stats, 
    hue="Country",
    legend=False,
    palette="pastel", 
)
plt.title("Average GHI per Country", fontsize=16, fontweight='bold')
plt.xlabel("Country", fontsize=14)
plt.ylabel("Mean GHI", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
for i, v in enumerate(summary_stats["Mean GHI"]):
    plt.text(i, v + 5, f"{v:.1f}", ha='center', fontsize=12, fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()