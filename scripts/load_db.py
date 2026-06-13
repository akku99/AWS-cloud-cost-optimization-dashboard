import pandas as pd
from sqlalchemy import create_engine

df=pd.read_csv("data/cleaned_costs.csv")

engine = create_engine('sqlite:///data/aws_costs.db')

df.to_sql(
    'costs_data',
    engine,
    if_exists = 'replace',
    index=False
)
print("Data loaded into database successfully!")