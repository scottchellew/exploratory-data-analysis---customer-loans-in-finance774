
import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot
from scipy import stats
dataframe = pd.read_csv('loan_payments.csv')

class DataFrameTransform():
    def __init__(self, dataframe):
        self.dataframe = dataframe
    def create_qq(self, column):
        qq_plot = qqplot(self.dataframe[column], scale=1, line='q')
    def create_skew(self, column):
        log_data = self.dataframe[column].map(lambda i: np.log(i) if i > 0 else 0)
    def remove_outliers(self, column):
        sorted_data = self.dataframe[column].sort_values()
        q1 = sorted_data.quantile(0.25)
        q3 = sorted_data.quantile(0.75)
        IQR = q3 - q1
        upper_bound = q1 - 1.5 * IQR
        lower_bound = q3 + 1.5 * IQR
        outliers = sorted_data[~((sorted_data<(upper_bound)) | (sorted_data>(lower_bound)))]