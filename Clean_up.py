import pandas as pd

df = pd.read_csv('CleanData.csv', index_col='FAC_STREET')

df.drop(['UNKNOWN'], inplace=True)

df.to_csv('Clean_Facilities_Data.csv')
