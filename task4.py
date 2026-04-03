import pandas as pd

try:
    df = pd.read_csv("weather_data_export.csv")
    print("[SUCCESS] Dataset loaded into memory.\n")
except FileNotFoundError:
    print("[ERROR] CSV artifact not found. Run Task 3 first.")
    exit()

print("--- Executive Summary: Weather KPIs ---")

avg_temp = df['Temperature_C'].mean()
print(f"-> Average Temperature across all monitored nodes: {avg_temp:.2f}°C")

condition_distribution = df['Condition'].value_counts()
most_common_condition = condition_distribution.index[0]
occurrences = condition_distribution.iloc[0]

print(f"-> Predominant Weather Condition: {most_common_condition} (Occurrences: {occurrences})")

insight_matrix = df.groupby('Condition')['Temperature_C'].mean().reset_index()
insight_matrix.rename(columns={'Temperature_C': 'Avg_Temp_C'}, inplace=True)

print("\n--- Insight Matrix: Average Temp by Condition ---")
print(insight_matrix.to_string(index=False))