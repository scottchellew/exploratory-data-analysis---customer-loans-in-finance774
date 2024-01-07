import pandas as pd

dataframe = pd.read_csv('loan_payments.csv')
pd.set_option('display.max_columns', None)
dataframe.tail()

#datatypes = dataframe.dtypes
#print(datatypes)
#loan_type = dataframe['loan_status'].unique()
#print(loan_type)
#sub = dataframe['sub_grade'].unique()
#sub.sort()
#print(sub)
#employment = dataframe['employment_length'].unique()
#print(employment)
#verify = dataframe['verification_status'].unique()
#print(verify)
#app = dataframe['application_type'].unique()
#print(app)
#policy = dataframe['policy_code'].unique()
#print(policy)