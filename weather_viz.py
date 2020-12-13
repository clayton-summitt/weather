import pandas as pd
url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/us-weather-history/KCLT.csv"
clt_df = pd.read_csv( url, sep = ",", parse_date= True)

clt_df.head()