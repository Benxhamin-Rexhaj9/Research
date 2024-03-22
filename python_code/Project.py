import pandas as pd
from pandasql import sqldf

occupancy_PATH ="C:\\Users\\Benxhamin Rexhaj\\Desktop\\occupancy.parquet"
timeseries_PATH ="C:\\Users\\Benxhamin Rexhaj\\Desktop\\timeseries.parquet"


occ_df = pd.read_parquet(occupancy_PATH)
times_df = pd.read_parquet(timeseries_PATH)



query = '''
        SELECT * 
        FROM occ_df
        --WHERE condition
        '''
result = sqldf(query, globals())

print(result)
