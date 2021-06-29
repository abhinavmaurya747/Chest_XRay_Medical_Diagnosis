import os
import pandas as pd
x = os.listdir('X-Ray Image DataSet/No_findings')

data = pd.DataFrame(x)
data.to_csv('2.csv')

