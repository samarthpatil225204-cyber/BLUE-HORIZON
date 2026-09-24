
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# DATA
# ==========================================

# Revenue trend data
dates = pd.date_range("2024-01-01", "2024-06-30", periods=100)

revenue = [
    500, 900, 2200, 300, 700, 600, 800, 1000, 700, 900,
    1200, 2100, 2300, 800, 900, 1100, 700, 600, 1500, 500,
    300, 700, 900, 1200, 1800, 500, 700, 1100, 1400, 1900,
    600, 900, 1700, 1000, 400, 700, 1200, 800, 600, 1000,
    1600, 2000, 500, 900, 1300, 600, 800, 1500, 300, 700,
    1000, 500, 900, 1800, 400, 700, 1100, 500, 900, 1300,
    200, 600, 1000, 700, 900, 1200, 500, 800, 1500, 600,
    900, 400, 700, 1200, 600, 1000, 500, 800, 1400, 700,
    1000, 500, 900, 1600, 600, 800, 1200, 400, 700, 1100,
    500, 900, 1300, 600, 800, 1500, 700, 1000, 600, 900
]

# Category revenue - SAME VALUES AS IMAGE
categories = [
    "Books",
    "Electronics",
    "Home & Kitchen",
    "Clothing"
]

category_revenue = [
    210000,
    150000,
    130000,
    110000
]

# Correlation values - SAME VALUES AS IMAGE
correlation = pd.DataFrame(
    [
        [1.00, 0.05, 0.68],
        [0.05, 1.00, 0.08],
        [0.68, 0.08, 1.00]
    ],
    columns=["Revenue", "Units Sold", "Discount"],
    index=["Revenue", "Units Sold", "Discount"]
)

# ==========================================
# DASHBOARD
# ==========================================

plt.figure(figsize=(14, 8))

plt.suptitle(
    "AI-Generated Analytics Dashboard",
    fontsize=17,
    fontweight="bold"
)

# ==========================================
# 1. REVENUE TREND
# ==========================================

plt.subplot(2, 2, 1)

plt.plot(
    dates,
    revenue,
    linewidth=1.5
)

plt.title(
    "1. Revenue Trend Over Time",
    fontsize=11,
    fontweight="bold"
)

plt.xlabel("Date")
plt.ylabel("Total Revenue ($)")

plt.xticks(rotation=35)

plt.grid(True, alpha=0.3)

plt.ylim(0, 2500)

# ==========================================
# 2. TOTAL REVENUE BY CATEGORY
# ==========================================

plt.subplot(2, 2, 2)

bars = plt.bar(
    categories,
    category_revenue
)

plt.title(
    "2. Total Revenue by Category",
    fontsize=11,
    fontweight="bold"
)

plt.xlabel("Category")
plt.ylabel("Total Revenue ($)")

plt.ylim(0, 220000)

# Values above bars
for bar, value in zip(bars, category_revenue):

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value + 4000,
        f"{value:,}",
        ha="center",
        fontsize=9
    )

# ==========================================
# 3. CORRELATION MATRIX
# ==========================================

plt.subplot(2, 2, 3)

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=1,
    vmin=-1,
    vmax=1
)

plt.title(
    "3. Correlation Matrix",
    fontsize=11,
    fontweight="bold"
)

# ==========================================
# FINAL LAYOUT
# ==========================================

plt.tight_layout(
    rect=[0, 0, 1, 0.95]
)

plt.show()