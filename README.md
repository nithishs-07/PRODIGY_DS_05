# Task 05: Traffic Accident Data Analysis & Pattern Recognition

## Overview
This task examines traffic accident occurrences across the United States to detect patterns related to time of day, weather conditions, and road layout features. It identifies high-frequency accident hotspots and critical risk factors.

## Dataset
- `US_Accidents_sample.csv`: Sample of country-wide traffic accident events containing timestamps, weather metrics (Temperature, Humidity, Visibility, Weather Condition), infrastructure flags (Traffic Signals, Junctions, Crossings), geographic location, and severity ratings (1 to 4).

## Workflow
1. **Timestamp Decomposition**: Extracted temporal components including `Hour`, `Day_Of_Week`, and `Month` from accident start timestamps.
2. **Temporal Pattern Analysis**: Evaluated hourly accident distributions over 24-hour cycles.
3. **Environmental & Weather Profiling**: Aggregated accident counts by prevailing weather condition.
4. **Road Infrastructure Hotspots**: Quantified accident frequency near critical traffic markers (traffic signals, crossings, junctions).
5. **Severity Comparison**: Compared accident impact and severity levels during daylight vs night-time conditions.

## Key Insights
- **Commute Rush Hours**: Marked spikes in collision counts occur between 7:00 AM – 9:00 AM and 4:00 PM – 6:00 PM on weekdays.
- **Infrastructure Clustering**: Intersections and traffic signal junctions emerge as the most frequent physical accident hotspots.
- **Environmental Impact**: While clear weather sees higher incident volume due to heavy traffic density, reduced visibility and night driving raise relative accident severity.

## How to Run
Run the standalone Python script:
```bash
python traffic_accidents_analysis.py
```
Or open the interactive Jupyter Notebook:
```bash
jupyter notebook traffic_accidents_analysis.ipynb
```
