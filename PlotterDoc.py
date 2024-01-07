import missingno as msno
import pandas as pd
import seaborn as sns
dataframe = pd.read_csv('loan_payments.csv')


class Plotter():
   def __init__(self, dataframe):
        self.dataframe = dataframe
        
   def create_heatmap(self):
       msno.heatmap(self.dataframe)
