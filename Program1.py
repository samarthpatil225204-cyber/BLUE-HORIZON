import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n_samples = 100
dates = pd.date_range(start="2026-01-01", periods=n_samples, freq="D")
categories = np.random.choice(["Electronics", "Clothing", "Home & Garden"], size=n_samples)
unit_prices = np.random.uniform(10, 100, size=n_samples)
units_sold = np.random.randint(50, 200, size=n_samples)
unit_prices = np.round(np.random.uniform(5, 50, size=n_samples), 2)

df = pd.DataFrame({
    "Date": dates,  
    "Category": categories,
    "UnitsSold": units_sold,
    "UnitPrice": unit_prices
})

df["TotalRevenue"] = df["UnitsSold"] * df["UnitPrice"]

cat_summary = df.groupby("Category").agg(
    TotalRevenueSum=("TotalRevenue","sum"),
    AverageRevenue=("UnitsSold","mean")
).reset_index()

fig, axes = plt.subplots(3, 3, figsize=(16, 12))
fig.suptitle("All Major Data Visualization Plot Types", fontsize=16, fontweight='bold')

axes[0,0].plot(df["Date"], df["TotalRevenue"], color='#1f77b4', linestyle=1.5)
axes[0,0].set_title("1. Line Plot: Total Revenue Over Time")
axes[0,0].tick_params(axis='x', rotation=30)
axes[0,0].grid(True, linestyle='--', alpha=0.5)

axes[0,1].bar(cat_summary["Category"], cat_summary["TotalRevenueSum"], color=['#2b5c8a', '#d95f02', "#5ff042"])
axes[0,1].set_title("2. Vertical Bar Chart (Category Revenue)")
axes[0,1].grid(axis='y', linestyle='--', alpha=0.5)

axes[0,2].barh(cat_summary["Category"], cat_summary["AverageRevenue"], color=['#2b5c8a', '#d95f02', '#7570b3'])
axes[0,2].set_title("3. Horizontal Bar Chart (Average Units Sold)")
axes[0,2].grid(axis='x', linestyle='--', alpha=0.5)

scatter = axes[1,0].scatter(df["UnitPrice"], df["UnitsSold"], c=df["TotalRevenue"], cmap='viridis', alpha=0.7)
