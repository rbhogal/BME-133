import pandas as pd
import numpy as np

# init
df_init = pd.read_csv("space_missions.csv")
df_init = df_init.dropna(subset=["Rover_Data_GB"])
print(df_init)
df_init["Funding_Status"] = df_init["Rover_Data_GB"].apply(
    lambda x: "Continue Funding" if x >= 500 else "Terminate Funding"
)
print(df_init)


# Load datasets
df1 = df_init
df2 = pd.read_csv("life_support_payload.csv")

df1 = df1[df1["Rover_Data_GB"] >= 500]
print(df1)
print("")
print(df2)
print("")

# New column - Required Food
df_merged = pd.merge(df1, df2, on="Mission_Name")
# Required food
# each crew member = 5kg per day
# required_food_per_day = 5 * crew_size
# required_food_kg = required_food_per_day * duration_days
df_merged["Required_Food_kg"] = 5 * df_merged["Crew_Size"] * df_merged["Duration_Days"]
print("")
print(df_merged)
print("")

# New column - Max Allowable Food
# 10000 - (Water_kg + Equipment_kg)
df_merged["Max_Allowable_Food_kg"] = 10000 - (
    df_merged["Water_kg"] + df_merged["Equipment_kg"]
)
print("")
print(df_merged)
print("")

# New column - Launch Status
df_merged["Launch_Status"] = np.where(
    df_merged["Required_Food_kg"] <= df_merged["Max_Allowable_Food_kg"],
    "Successful Launch",
    "Failed Launch",
)

print("")
print(df_merged)
print("")

print(df_merged["Launch_Status"])
print(df_merged["Funding_Status"])
# df with only certain columns
df_final = df_merged[
    (df_merged["Launch_Status"] == "Successful Launch")
    & (df_merged["Funding_Status"] == "Continue Funding")
]

print("")
print(df_final)
print("")

print(
    "Conclusion: Areas-1, Ceres-Miner, and Mars-Delta missions should go to phase 2 based on rover data and launch feasibility."
)
