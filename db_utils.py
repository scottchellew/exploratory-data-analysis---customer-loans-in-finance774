import yaml
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

creds_file = "credentials.yaml"

class RDSDatabaseConnector(): 
   def __init__(self, creds_file):
      self.creds_file = creds_file

   def open_data(self, creds_file):
    with open(creds_file, "r") as file:
      yaml_dict = yaml.safe_load(file)
    return yaml_dict
   
   def load_yaml(self):
      DATABASE_TYPE = 'postgresql'
      DBAPI = 'psycopg2'
      USER = 'loansanalyst'
      PASSWORD = 'EDAloananalyst'
      HOST = 'eda-projects.cq2e8zno855e.eu-west-1.rds.amazonaws.com'
      PORT = '5432'
      DATABASE = 'payments'
      engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
      return engine

   def extract():
      RDS_Connector = RDSDatabaseConnector(creds_file)
      opened = RDS_Connector.load_yaml()
      query = 'SELECT * FROM loan_payments'
      open_database = pd.read_sql_query(query, con=opened)
      ##loan_payments = pd.DataFrame(open_database)
      return open_database

def save(loan_payments):
   saved_database = loan_payments.to_csv('loan_payments.csv')
   return saved_database

extracted = RDSDatabaseConnector.extract()
save(extracted)

