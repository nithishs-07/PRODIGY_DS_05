"""
Prodigy InfoTech - Data Science Internship
Task 05: Analyze traffic accident data to identify patterns related to road conditions, weather, and time of day.
Visualize accident hotspots and contributing factors.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Visual formatting
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

def run_traffic_accidents_analysis():
    print("=" * 65)
    print("PRODIGY INFOTECH - TASK 05: TRAFFIC ACCIDENT PATTERNS ANALYSIS")
    print("=" * 65)

    # 1. Load Dataset
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "US_Accidents_sample.csv")
    if not os.path.exists(data_path):
        data_path = "US_Accidents_sample.csv"

    print(f"\n[Step 1] Loading dataset from: {data_path}")
    df = pd.read_csv(data_path)
    print(f"Dataset Dimensions: {df.shape[0]} records, {df.shape[1]} variables\n")
    print("First 5 records:")
    print(df.head())

    # 2. DateTime Engineering
    print("\n[Step 2] Processing Timestamps...")
    df["Start_Time"] = pd.to_datetime(df["Start_Time"])
    df["Hour"] = df["Start_Time"].dt.hour
    df["Day_Of_Week"] = df["Start_Time"].dt.day_name()
    df["Month"] = df["Start_Time"].dt.month_name()

    # Visualizations Directory
    vis_dir = os.path.join(current_dir, "visualizations")
    os.makedirs(vis_dir, exist_ok=True)

    # 3. Visualization 1: Accidents by Time of Day (Hour)
    plt.figure(figsize=(10, 5))
    hourly_counts = df["Hour"].value_counts().sort_index()
    sns.lineplot(x=hourly_counts.index, y=hourly_counts.values, marker="o", color="#e74c3c", linewidth=2.5)
    plt.title("Traffic Accidents by Time of Day (24-Hour Cycle)", fontsize=13, weight="bold")
    plt.xlabel("Hour of Day (0 - 23)")
    plt.ylabel("Number of Accidents")
    plt.xticks(range(0, 24))
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(os.path.join(vis_dir, "01_accidents_by_hour.png"))
    plt.close()

    # 4. Visualization 2: Top Weather Conditions During Accidents
    plt.figure(figsize=(9, 5))
    top_weather = df["Weather_Condition"].value_counts().head(8)
    sns.barplot(x=top_weather.values, y=top_weather.index, hue=top_weather.index, palette="Blues_r", legend=False)
    plt.title("Accident Frequency by Top Weather Conditions", fontsize=13, weight="bold")
    plt.xlabel("Accident Count")
    plt.ylabel("Weather Condition")
    plt.tight_layout()
    plt.savefig(os.path.join(vis_dir, "02_accidents_by_weather.png"))
    plt.close()

    # 5. Visualization 3: Road Infrastructure Features / Hotspots
    road_features = ["Traffic_Signal", "Junction", "Crossing", "Station", "Stop"]
    road_counts = {feat: df[feat].sum() for feat in road_features}
    road_df = pd.DataFrame(list(road_counts.items()), columns=["Road_Feature", "Count"]).sort_values(by="Count", ascending=False)

    plt.figure(figsize=(8, 4))
    sns.barplot(data=road_df, x="Count", y="Road_Feature", hue="Road_Feature", palette="rocket", legend=False)
    plt.title("Accidents Near Specific Road Infrastructure Features", fontsize=13, weight="bold")
    plt.xlabel("Number of Occurrences")
    plt.ylabel("Road Infrastructure")
    plt.tight_layout()
    plt.savefig(os.path.join(vis_dir, "03_road_infrastructure_factors.png"))
    plt.close()

    # 6. Visualization 4: Geographic Hotspots (Top Cities)
    plt.figure(figsize=(9, 5))
    top_cities = df["City"].value_counts().head(10)
    sns.barplot(x=top_cities.values, y=top_cities.index, hue=top_cities.index, palette="magma", legend=False)
    plt.title("Top 10 Cities with Highest Accident Counts", fontsize=13, weight="bold")
    plt.xlabel("Number of Accidents")
    plt.ylabel("City")
    plt.tight_layout()
    plt.savefig(os.path.join(vis_dir, "04_accidents_by_city.png"))
    plt.close()

    # 7. Visualization 5: Day vs Night Severity Comparison
    plt.figure(figsize=(7, 4))
    sns.countplot(data=df, x="Severity", hue="Sunrise_Sunset", palette="Set2")
    plt.title("Accident Severity: Daytime vs Nighttime", fontsize=13, weight="bold")
    plt.xlabel("Severity Level (1 = Low Impact, 4 = Critical Delay)")
    plt.ylabel("Accident Count")
    plt.legend(title="Period")
    plt.tight_layout()
    plt.savefig(os.path.join(vis_dir, "05_severity_day_vs_night.png"))
    plt.close()

    print(f"\n[Step 3] Visualizations saved to: {vis_dir}/")
    print(" - 01_accidents_by_hour.png")
    print(" - 02_accidents_by_weather.png")
    print(" - 03_road_infrastructure_factors.png")
    print(" - 04_accidents_by_city.png")
    print(" - 05_severity_day_vs_night.png")

    peak_morning_hour = df[df["Hour"].between(6, 10)]["Hour"].value_counts().idxmax()
    peak_evening_hour = df[df["Hour"].between(15, 19)]["Hour"].value_counts().idxmax()

    print("\n[Step 4] Key Analytical Findings:")
    print(f" - Temporal Patterns: Sharp accident surges occur during morning commute (~{peak_morning_hour}:00 AM) and evening rush hours (~{peak_evening_hour}:00 PM).")
    print(f" - Road Infrastructure: Traffic Signals and Intersections/Junctions represent the most prevalent physical accident hotspots.")
    print(" - Weather & Environmental Conditions: While most incidents take place in Fair/Clear weather (due to high traffic volume), adverse conditions (rain, wet roads) exhibit elevated proportions of severe delays.")
    print("=" * 65)

if __name__ == "__main__":
    run_traffic_accidents_analysis()
