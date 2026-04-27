import pandas as pd

# init
df_init = pd.read_csv("space_missions.csv")
df_init = df_init.dropna(subset=["Rover_Data_GB"])
print(df_init)
df_init["Funding_Status"] = df_init["Rover_Data_GB"].apply(
    lambda x: "Continue Funding" if x >= 500 else "Terminate Funding"
)
print(df_init)
