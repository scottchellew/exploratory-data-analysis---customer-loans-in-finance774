# exploratory-data-analysis---customer-loans-in-finance774

The purpose of this task is to perform a data analysis on a set of data surrounding customer loans with a financial institution.
This will use various techniques to find meaning and patterns within the data.
I did find this project to be a challenge, but I was able to get through it and produce everything needed for the project.

Packages required:
pandas
numpy
missingno
seaborn
statsmodels.graphics.gofplots
matplotlib

db_utils.py is a file that extracts a database from the cloud and saves it locally.

view_data.py is a small view of the database, to get an idea of the variables and datatypes.

loan_payments.csv is the downloaded file from db_utils.py

new_loan_payments.csv is a copy of loan_payments.csv, before any data transformation has been applied to it.

credentials.yaml contains the credentials of the database stored in the cloud.

.gitignore contains credentials.yaml

Data_Analysis_Milestone3 is the file that contains all of the working out to complete the tasks of this milestone.
This shows histograms, qq plots, calculations of null values, heatmaps, transformation of data to remove nulls and fit the data to a normal distribution, removes outliers, creates a correlation matrix and drops unneeded rows.

Data_Analysis_Milestone4 is a file that contains all of the working out for this milestone. It contains a series of calculations relating to the amount of customers there are and the sum of loans taken.
This also contains some interpretation of the data, explaining what the loan company could do with these results.

Data_Transform.py converts some columns into a more appropriate data type.

DataFrameInfo.py has a class that converts the data type of some columns.

DataFrameTransformDoc.py has a class that creates qq plots, skews data and removes any outliers from a column.

PlotterDoc.py has a class that creates a heatmap.
