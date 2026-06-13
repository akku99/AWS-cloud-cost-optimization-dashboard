import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/cleaned_costs.csv"
)

service_cost = (
    df.groupby('Service')
      ['Cost']
      .sum()
      .sort_values(
          ascending=False
      )
)

service_cost.head(10).plot(
    kind='bar'
)

plt.title(
    "Top AWS Services Cost"
)

plt.tight_layout()

plt.show()