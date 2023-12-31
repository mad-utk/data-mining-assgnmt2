# -*- coding: utf-8 -*-
"""Assignment2A3_Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WzB5MjHpLsT1OKUMnU9vrZZwkC5KbD0T
"""

# install pycaret
!pip install pycaret

# check installed version
import pycaret
pycaret.__version__

# mount google drive
from google.colab import drive
drive.mount("/content/gdrive")
crab_age_path = '/content/gdrive/MyDrive/Sem-I/CMPE-255 Data Mining/Assignments2/CrabAgePrediction.csv'

# read data
import pandas as pd
crab_age_regression = pd.read_csv(crab_age_path)

# check data
crab_age_regression.shape

crab_age_regression.head()

crab_age_regression.columns

crab_age_regression.describe

# create train data
data_train = crab_age_regression.sample(frac=0.9)
data_train.shape

data_train.head()

data_test = crab_age_regression.drop(data_train.index)
data_test.shape

data_test.head()

data_train.reset_index(drop=True, inplace=True)
data_train.head()

data_test.reset_index(drop=True, inplace=True)
data_test.head()

# import pycaret classification
from pycaret.regression import *
reg = setup(data=data_train, target = 'Age')

# compare baseline models
best = compare_models()

gbr_regressor = create_model('gbr')

print(gbr_regressor)

tuned_gbr_regressor = tune_model(gbr_regressor)

plot_model(gbr_regressor)

plot_model(tuned_gbr_regressor, plot="error")

plot_model(tuned_gbr_regressor, plot="feature")

# save pipeline
final_gbr = finalize_model(tuned_gbr_regressor)
test_prediction = predict_model(final_gbr, data=data_test)
test_prediction.head()

save_model(tuned_gbr_regressor, "my_regression_model")

# gradio app
!pip install gradio
!pip install pycaret[mlops]

dt = create_model('gbr_regressor')

create_app(gbr_regressor)