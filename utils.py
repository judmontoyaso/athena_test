import pandas as pd

def resp_to_df(resp):
 
    df = pd.read_json(resp)
    return df

def df_to_parquet(df):
 # df_otu_con_project es tu DataFrame
    parquet_buffer = df.to_parquet( engine='pyarrow', compression='snappy')
    return parquet_buffer