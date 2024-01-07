import pandas as pd
dataframe = pd.read_csv('loan_payments.csv')

class DataFrameInfo():
    def __init__(self, term, application_type):
        self.term = term
        self.application_type = application_type

    def convert_dictionary(self, term, application_type):
        conversion = {'term': int,
                'application_type': str
                }
        dataframe = dataframe.astype(conversion)
        return term, application_type