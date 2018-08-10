# HOW TO HANDLE MISSING DATA
import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer

score_hg = pd.read_csv("Examination Result 2017/diem_thi_ha_giang.csv")
score_hg.head()

print("Shape of data:", score_hg.shape)
score_hg.describe()

# Missing at Random (MAR): propensity for a data point to be missing is not related to the missing data,but it is related to some of the observed data
# Missing Completely at Random (MCAR): certain value is missing has nothing to do with its hypothesis value and with the values of other variables
# Missing not at Random (MNAR): missing value depends on the hypothetical value

# MAR and MCAR: it's safe to delete the data
# Deletion
score_hg_drop_math = score_hg[pd.isnull(score_hg['TOAN']) == False]
print(score_hg_drop_math.shape)
# Dropping variable
score_hg_drop_hist = score_hg.drop('LICH SU', axis=1)
score_hg_drop_hist.head()

# MNAR: it's not allowed to delete the missing data
# Linear regression: missing data - dependent variables. Independent variables can be the score of other subjects
# Multiple imputation: impute data from a distribution to the missing datas and consolidate the results
# K nearest neighbors: requires a distance metric and selection of the number of nearest neighbors to impute the data
# Mean, Median and Mode
score_hg_math = score_hg
score_math = score_hg_math.TOAN
imputer = Imputer(missing_values=float('NaN'), strategy='mean')
# imputer = Imputer(missing_values=float('NaN'), strategy='median')
# imputer = Imputer(missing_values=float('NaN'), strategy='most_frequent')
score_math = score_math.values.reshape(-1, 1)
transformed_score_math = imputer.fit_transform(score_math)
score_hg_math.TOAN = pd.Series(transformed_score_math.tolist())
score_hg_math.TOAN = score_hg_math.TOAN.apply(lambda x: list(x)[0])

print(score_hg_math_mean.describe())

