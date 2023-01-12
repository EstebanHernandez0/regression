import pandas as pd
import numpy as np
import os
from env import get_connection



def get_telco_data():
    file_csv = 'telco_churn.csv'
    
    if os.path.isfile(file_csv):
        return pd.read_csv(file_csv)
    else: telco_churn=pd.read_sql('''SELECT * FROM contract_types
    JOIN customers USING (contract_type_id)
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN payment_types USING (payment_type_id)''', telco_connnect)
    telco_churn.to_csv('telco_churn.csv',index=False)
    return telco_churn


def get_telco_data():
    
    if os.path.isfile('telco.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('telco.csv', index_col=0)
        
    else:
        
        df = new_telco_data()

        df.to_csv('telco.csv')
        
    return df