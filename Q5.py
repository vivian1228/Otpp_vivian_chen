import pandas as pd
from datetime import datetime

# series 1 to df
data_str1=['12/31/2019','01/02/2020','01/03/2020','01/06/2020']
date_obj1 = [datetime.strptime(date, "%m/%d/%Y") for date in data_str1]

data_1 = {
    'date': date_obj1,
    'close_1': [3230.78,3257.85,3234.85,3246.28]
}

#series 2 to df
data_str2 = ['12/31/2019','01/01/2020','01/02/2020','01/03/2020','01/06/2020']
date_obj2 = [datetime.strptime(date, "%m/%d/%Y") for date in data_str2]

data_2 = {
    'date': date_obj2,
    'close_2': [1.30606,1.3002,1.2973,1.2983,1.29866]
}

df1=pd.DataFrame(data_1)
df2=pd.DataFrame(data_2)

# join two series
joined_df=pd.merge(df1,df2, on='date', how='outer')


# Find rows where Column1 is NA
na_rows = joined_df['close_1'].isna()

#intepolate based on date & note on the
joined_df['note']='No change'
joined_df.loc[na_rows, 'note']='close_1 Interpolated'

joined_df.set_index('date', inplace=True)

joined_df['close_1'] = joined_df['close_1'].interpolate(method='time')

print(joined_df)

