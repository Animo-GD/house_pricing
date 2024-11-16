from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_absolute_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
import joblib

# Fetch Data
np.random.seed(0)
housing = fetch_california_housing()
X,y = housing.data,housing.target

# Split Data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

# Modeling
print("Training ......")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)
print("Finished Training")
# Testing
result = {
    "MAE":[mean_absolute_error(y_train,train_pred),mean_absolute_error(y_test,test_pred)],
    "R2 Score":[r2_score(y_train,train_pred),r2_score(y_test,test_pred)]
}

print(pd.DataFrame(result,["Training","Testing"]))

# Saving
print("Saving ....")
joblib.dump(model,"model.joblib")
print("Saved Successfully !")