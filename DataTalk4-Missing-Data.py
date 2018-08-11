# HOW TO HANDLE MISSING DATA
import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer

score_hg = pd.read_csv("Examination Result 2017/diem_thi_ha_giang.csv")
score_hg.head()

print("Shape of data:", score_hg.shape)
print(score_hg.describe())

# Missing at Random (MAR): propensity for a data point to be missing is not related to the missing data,but it is related to some of the observed data
# Missing Completely at Random (MCAR): certain value is missing has nothing to do with its hypothesis value and with the values of other variables
# Missing not at Random (MNAR): missing value depends on the hypothetical value

# Remove all rows with missing maths score
score_hg_drop_math = score_hg[pd.isnull(score_hg['TOAN']) == False]
print("Length of the data now:", len(score_hg_drop_math))
# Dropping variable
score_hg_drop_hist = score_hg.drop('LICH SU', axis=1)
print("List of columns now:", score_hg_drop_hist.columns)

# Impute missing data with mean
score_math = score_hg.TOAN
imputer = Imputer(missing_values=float('NaN'), strategy='mean')
# imputer = Imputer(missing_values=float('NaN'), strategy='median')
# imputer = Imputer(missing_values=float('NaN'), strategy='most_frequent')
score_math = score_math.values.reshape(-1, 1)
# Transform the data with filled value for missing data
transformed_score_math = imputer.fit_transform(score_math)
score_hg.TOAN = pd.Series(transformed_score_math.tolist())
score_hg.TOAN = score_hg.TOAN.apply(lambda x: list(x)[0])

print(score_hg.describe())

# First quantile
Q1 = score_hg['GDCD'].quantile(0.25)
# Third quantile
Q3 = score_hg['GDCD'].quantile(0.75)
# Interquantile Range
IQR = Q3 - Q1
score_hg = score_hg[(score_hg['GDCD']<=Q3+1.5*IQR) & (score_hg['GDCD']>=Q1-1.5*IQR)]

print(score_hg.describe())

# Remove all duplicates in the data set
score_hg.drop_duplicates(keep="first", inplace=True)

print(score_hg.describe())
