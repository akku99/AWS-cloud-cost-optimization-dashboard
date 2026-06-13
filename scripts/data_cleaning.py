import pandas as pd

df = pd.read_csv(
    "data/aws_costs.csv"
)

df['Month'] = pd.to_datetime(
    df['Month']
)

df['Cost'] = df['Cost'].round(2)

df = df[df['Cost'] > 0]

df.to_csv(
    "data/cleaned_costs.csv",
    index=False
)