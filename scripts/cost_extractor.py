import boto3
import pandas as pd

ce = boto3.client('ce')

response = ce.get_cost_and_usage(
    TimePeriod={
        'Start':'2026-01-01',
        'End':'2026-06-25'
    },
    Granularity='MONTHLY',
    Metrics=['UnblendedCost'],
    GroupBy=[
        {
            'Type':'DIMENSION',
            'Key':'SERVICE'
        }
    ]
)

rows=[]

for result in response['ResultsByTime']:
    month=result['TimePeriod']['Start']

    for group in result['Groups']:

        rows.append({
            'Month':month,
            'Service':group['Keys'][0],
            'Cost':float(
                group['Metrics']
                ['UnblendedCost']
                ['Amount']
            )
        })

df=pd.DataFrame(rows)

df.to_csv(
    'data/aws_costs.csv',
    index=False
)

print(df.head())