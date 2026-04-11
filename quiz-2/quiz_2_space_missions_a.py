import pandas as pd

# Load dataset
print("--- Load & Show First 5 Rows ---")
print("")
df = pd.read_csv("space_missions.csv")
print(df.head())

# Removed rows with missing values
print("")
print("--- Removed rows with missing values ---")
print("")
df = df.dropna(subset=["Rover_Data_GB"])
df["Funding_Status"] = df["Rover_Data_GB"].apply(
    lambda x: "Continue Funding" if x >= 500 else "Terminate Funding"
)
print(df)

# New dataframe including only missions with "Continue Funding"
print("")
print("--- Dataframe with only continue funding ---")
print("")
df_continue_funding = df[df["Funding_Status"] == "Continue Funding"]
print(df_continue_funding)
print("--")

# Sort new df by Rover_Data_GB from high to low (desc)
print("")
print("--- Sort df by rover data (desc) ---")
print("")
df_sorted = df_continue_funding.sort_values("Rover_Data_GB", ascending=False)
print(df_sorted)

# Print only certain columns
print("")
print("-- Print only certain columns using sorted df---")
print("")
print(df_sorted[["Mission_Name", "Planet", "Rover_Data_GB", "Funding_Status"]])

# Conclusion
print("")
print(
    "Conclusion: Based on the largest amount of data collected the Neptune-Observer Mission appears to be the strongest for continued funding."
)
