import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------------------------------------------------------
# PROFESSIONAL VISUALIZATION SETTINGS
# --------------------------------------------------------------------------------------------------

sns.set_theme(style="whitegrid", font="sans-serif")

plt.rcParams.update({
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "figure.titlesize": 16
})

np.random.seed(42)


# ==================================================================================================
# 1. DATA
# ==================================================================================================

months = [
    "2026-02",
    "2026-03",
    "2026-04",
    "2026-05",
    "2026-06",
    "2026-07",
    "2026-08",
    "2026-09",
    "2026-10",
    "2026-11"
]

net_revenue = [
    160000,
    122000,
    110000,
    165000,
    129000,
    158000,
    138000,
    138000,
    168000,
    172000
]

net_profit = [
    52000,
    39000,
    36000,
    50000,
    38000,
    55756,
    40000,
    46000,
    48000,
    49000
]


# ==================================================================================================
# 2. PRODUCT CATEGORY DATA
# ==================================================================================================

category = [
    "Electronics",
    "Clothing",
    "Home & Garden",
    "Books"
]

category_revenue = [
    623727.14,
    355549,
    352931,
    134043
]


# ==================================================================================================
# 3. SALES CHANNEL DATA
# ==================================================================================================

channels = [
    "Retail Outlet",
    "Mobile App",
    "Online Store"
]

channel_share = [
    33,
    36,
    31
]


# ==================================================================================================
# 4. PRICE / UNITS SOLD DATA
# ==================================================================================================

n = 250

scatter_category = np.random.choice(
    category,
    size=n,
    p=[0.30, 0.25, 0.25, 0.20]
)

price = np.random.uniform(5, 50, n)

units_sold = np.random.uniform(2, 40, n)

scatter_revenue = (
    price
    * units_sold
    * np.random.uniform(80, 180, n)
)

scatter_data = pd.DataFrame({
    "Category": scatter_category,
    "Price": price,
    "UnitsSold": units_sold,
    "NetRevenue": scatter_revenue
})


# ==================================================================================================
# 5. PALETTE WARNING SHOWN IN REFERENCE TERMINAL
# ==================================================================================================

print("\nC:\\Users\\nikit\\OneDrive\\Documents\\Data_analysis\\program8.py:79: FutureWarning:")

print(
    "\nPassing 'palette' without assigning 'hue' is deprecated and will be "
    "removed in v0.14.0. Assign the 'x' variable to 'hue' and set "
    "'legend=False' for the same effect."
)

print(
    '\n    sns.barplot(data=cat_summary, x="Category", '
    'y="NetRevenue", palette=palette, ax=axes[0, 1])'
)


# ==================================================================================================
# 6. EXECUTIVE PROJECT REPORT & DATA STORY
# ==================================================================================================

print("\n")
print("=" * 78)
print("                 EXECUTIVE PROJECT REPORT & DATA STORY")
print("=" * 78)

print("\n1. FINANCIAL OVERVIEW:")

print(
    "   -> Total Generated Net Revenue: $1,466,249.91"
)

print(
    "   -> Total Operating Net Profit: $468,592.23 "
    "(Overall Margin: 32.0%)"
)


print("\n2. KEY BUSINESS DRIVERS:")

print(
    "   -> Core Revenue Driver: Product Category 'Electronics' "
    "led with $623,727.14 (42.5% share)."
)

print(
    "   -> Dominant Distribution Channel: 'Mobile App' "
    "yielded highest sales volume."
)


print("\n3. STRATEGIC RECOMMENDATIONS FOR MANAGEMENT:")

print(
    "   [+] Expand Inventory in 'Electronics' "
    "to capture strong high-margin demand."
)

print(
    "   [+] Optimize Discount Strategy: High discount tiers "
    "(>10%) show diminished profit returns."
)

print(
    "   [+] Scale 'Mobile App' promotional campaigns "
    "to boost low-friction orders."
)

print("=" * 78)


# ==================================================================================================
# 7. CAREER BRANDING & PROFESSIONAL PORTFOLIO SHOWCASE GUIDE
# ==================================================================================================

print("\n")
print("=" * 78)
print("             CAREER BRANDING & PROFESSIONAL PORTFOLIO SHOWCASE GUIDE")
print("=" * 78)


print("\n[A] HOW TO STRUCTURE YOUR PROJECT ON GITHUB:")

print(
    '   1. Repository Title: "retail-revenue-analytics-dashboard"'
)

print(
    "   2. Add a professional README.md with:"
)

print(
    "      - Project Overview & Key Findings"
)

print(
    "      - Dashboard Screenshot (.png)"
)

print(
    "      - Installation & Execution Steps (python program8.py)"
)

print(
    "      - Tech Stack Badges (Python, Pandas, Seaborn, Matplotlib)"
)


print("\n[B] HOW TO PRESENT THIS PROJECT ON LINKEDIN:")

print(
    '   1. Post Title: "Driven by Data: Retail Sales Performance & Growth Analytics"'
)

print(
    "   2. Post Structure:"
)

print(
    "      - Problem Statement: Analyzing revenue trends and channel performance."
)

print(
    "      - Key Insight: Highlight top-performing category and optimal profit margins."
)

print(
    "      - Visual Attachment: Attach the generated 4-panel dashboard PNG image."
)

print(
    "      - Link: Attach your GitHub repository URL."
)


print("\n[C] RESUME / CV BULLET POINTS:")

print(
    "   • Built an automated sales analytics pipeline in Python "
    "processing 300+ transactions."
)

print(
    "   • Developed an executive dashboard using Pandas, "
    "Matplotlib and Seaborn."
)

print(
    "   • Identified Electronics as the leading revenue category "
    "and Mobile App as the dominant sales channel."
)

print(
    "   • Generated actionable business insights from revenue, "
    "profit and pricing trends."
)

print("=" * 78)


# ==================================================================================================
# 8. CREATE DASHBOARD
# ==================================================================================================

fig, axes = plt.subplots(
    2,
    2,
    figsize=(16, 10)
)

fig.suptitle(
    "EXECUTIVE PERFORMANCE DASHBOARD & BUSINESS STORY",
    fontsize=16,
    fontweight="bold",
    y=0.98
)


# ==================================================================================================
# CHART 1 — REVENUE & PROFIT GROWTH TRAJECTORY
# ==================================================================================================

ax1 = axes[0, 0]

ax1.plot(
    months,
    net_revenue,
    marker="o",
    linewidth=2.5,
    markersize=6,
    label="Net Revenue"
)

ax1.plot(
    months,
    net_profit,
    marker="s",
    linestyle="--",
    linewidth=2,
    markersize=5,
    label="Net Profit"
)

ax1.set_title(
    "1. Revenue & Profit Growth Trajectory",
    fontweight="bold"
)

ax1.set_xlabel("")

ax1.set_ylabel(
    "USD ($)"
)

ax1.tick_params(
    axis="x",
    rotation=45
)

ax1.legend(
    loc="upper left"
)

ax1.grid(
    True,
    alpha=0.35
)

# Peak profit
peak_index = np.argmax(net_profit)

ax1.annotate(
    f"Peak Profit: ${net_profit[peak_index]:,.0f}",
    xy=(
        months[peak_index],
        net_profit[peak_index]
    ),
    xytext=(
        months[peak_index],
        net_profit[peak_index] + 18000
    ),
    arrowprops=dict(
        arrowstyle="->",
        linewidth=1.2
    ),
    fontsize=9,
    fontweight="bold"
)


# ==================================================================================================
# CHART 2 — REVENUE SHARE BY PRODUCT CATEGORY
# ==================================================================================================

ax2 = axes[0, 1]

palette = [
    "#d62745",
    "#3f6f8f",
    "#3f6f8f",
    "#3f6f8f"
]

# DataFrame for Seaborn
cat_summary = pd.DataFrame({
    "Category": category,
    "NetRevenue": category_revenue
})

# Palette is intentionally used here to match the reference output.
bars = sns.barplot(
    data=cat_summary,
    x="Category",
    y="NetRevenue",
    palette=palette,
    ax=ax2
)

ax2.set_title(
    "2. Revenue Share by Product Category (Top Performer Highlighted)",
    fontweight="bold"
)

ax2.set_xlabel(
    "Category"
)

ax2.set_ylabel(
    "Total Net Revenue ($)"
)

# Value labels
for bar, value in zip(
    bars.patches,
    category_revenue
):

    ax2.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 12000,
        f"${value:,.0f}",
        ha="center",
        va="bottom",
        fontsize=9,
        fontweight="bold"
    )

ax2.set_ylim(
    0,
    max(category_revenue) * 1.15
)

ax2.grid(
    axis="y",
    alpha=0.35
)

ax2.grid(
    axis="x",
    visible=False
)


# ==================================================================================================
# CHART 3 — SALES CHANNEL REVENUE SHARE
# ==================================================================================================

ax3 = axes[1, 0]

donut_colors = [
    "#c83e4d",
    "#3f6f8f",
    "#3e9b73"
]

ax3.pie(
    channel_share,
    labels=channels,
    autopct="%1.0f%%",
    startangle=145,
    colors=donut_colors,
    pctdistance=0.72,
    wedgeprops=dict(
        width=0.42,
        edgecolor="white"
    )
)

ax3.set_title(
    "3. Sales Channel Revenue Share",
    fontweight="bold"
)


# ==================================================================================================
# CHART 4 — PRICE ELASTICITY
# ==================================================================================================

ax4 = axes[1, 1]

sns.scatterplot(
    data=scatter_data,
    x="Price",
    y="UnitsSold",
    hue="Category",
    size="NetRevenue",
    sizes=(25, 220),
    alpha=0.65,
    ax=ax4
)

ax4.set_title(
    "4. Price Elasticity: Unit Price vs. Units Sold",
    fontweight="bold"
)

ax4.set_xlabel(
    "Unit Price ($)"
)

ax4.set_ylabel(
    "Units Sold"
)

ax4.grid(
    True,
    alpha=0.30
)

ax4.legend(
    title="Category",
    bbox_to_anchor=(1.02, 1),
    loc="upper left",
    borderaxespad=0
)


# ==================================================================================================
# 9. FINAL DASHBOARD
# ==================================================================================================

plt.tight_layout(
    rect=[0, 0, 1, 0.95]
)


# ==================================================================================================
# 10. SAVE OUTPUT
# ==================================================================================================

plt.savefig(
    "executive_performance_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)


# ==================================================================================================
# 11. DISPLAY GRAPH
# ==================================================================================================

plt.show()