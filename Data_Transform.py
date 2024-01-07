import pandas as pd
import numpy as np
from datetime import datetime

database = pd.read_csv('loan_payments.csv')

class DataTransform():
    def __init__(self, grade, sub_grade, employment_length, term, issue_date, earliest_credit_line, next_payment_date, last_credit_pull_date, mths_since_last_delinq,):
         self.grade = grade
         self.sub_grade = sub_grade
         self.employment_length = employment_length
         self.term = term
         self.issue_date = issue_date
         self.earliest_credit_line = earliest_credit_line
         self.next_payment_date = next_payment_date
         self.last_credit_pull_date = last_credit_pull_date

    def transform_grade(self, grade):
         grade_map = {
              "A": 7,
              "B": 6,
              "C": 5,
              "D": 4,
              "E": 3,
              "F": 2,
              "G": 1  
        }
         database["grade"]= database["grade"].map(grade_map)
         return grade
    
    def transform_sub_grade(self, sub_grade):
         sub_grade_map = {
              "A1": 35,
              "A2": 34,
              "A3": 33,
              "A4": 32,
              "A5": 31,
              "B1": 30,
              "B2": 29,
              "B3": 28,
              "B4": 27,
              "B5": 26,
              "C1": 25,
              "C2": 24,
              "C3": 23,
              "C4": 22,
              "C5": 21,
              "D1": 20,
              "D2": 19,
              "D3": 18,
              "D4": 17,
              "D5": 16,
              "E1": 15,
              "E2": 14,
              "E3": 13,
              "E4": 12,
              "E5": 11,
              "F1": 10,
              "F2": 9,
              "F3": 8,
              "F4": 7,
              "F5": 6,
              "G1": 5,
              "G2": 4,
              "G3": 3,
              "G4": 2,
              "G5": 1
         }
         database["sub_grade"]= database["sub_grade"].map(sub_grade_map)
         return sub_grade
         
    def transform_employment_length(self, employment_length):
         employment_length_map = {
              "10+ years": 11,
              "9 years": 10,
              "8 years": 9,
              "7 years": 8,
              "6 years": 7,
              "5 years": 6,
              "4 years": 5,
              "3 years": 4,
              "2 years": 3,
              "1 year": 2,
              "<1 year": 1
         }
         database ["employment_length_ordinal"]= database["employment_length"].map(employment_length_map)
         return employment_length
    
    def tranform_term(self, term):
         database['term'] = database['term'].astype("string")
         database = database.term.str.extract('(^\d*)')
         return term
         
    def transform_issue_date(self, issue_date):
         database['issue_date'] = datetime.strptime(database['issue_date'],'%B, %Y')
         return issue_date

    
    def transform_earliest_credit_line(self, earliest_credit_line):
         database['earliest_credit_line'] = datetime.strptime(database['earliest_credit_line'], '%B, %Y')
         return earliest_credit_line

    def transform_next_payment_date(self, next_payment_date):
         database['next_payment_date'] = datetime.strptime(database['next_payment_date'], '%B, %Y')
         return next_payment_date

    def transform_last_credit_pull_date(self, last_credit_pull_date):
         database['last_credit_pull_date'] = datetime.strptime(database['last_credit_pull_date'], '%B, %Y')
         return last_credit_pull_date