import os
import json
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pickle

data = pd.read_csv('Laptop_price.csv')

label_encoder = LabelEncoder()
data['Brand'] = label_encoder.fit_transform(data['Brand'])

X = data[['Processor_Speed', 'RAM_Size', 'Storage_Capacity', 'Brand']]
y = data['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

rf_model = RandomForestRegressor()
param_grid = {
    'max_depth': [2, 5, 10, 15, 20, 25],
    'n_estimators': [2, 4, 6, 8, 10, 12],
    'max_features': ['sqrt', 'log2']
}

gridfr = GridSearchCV(rf_model, param_grid, cv=5)
gridfr.fit(X_train_scaled, y_train)

print(f"The best params are: {gridfr.best_params_}")

best_model = gridfr.best_estimator_

predictions = best_model.predict(X_test_scaled)
predictions_train = best_model.predict(X_train_scaled)

r2_score_test = r2_score(y_test, predictions)
r2_score_train = r2_score(y_train, predictions_train)

metrics = {
    'r2_score_test': r2_score_test,
    'r2_score_train': r2_score_train
}

output_dir = 'model_outputs'
os.makedirs(output_dir, exist_ok=True)

model_path = os.path.join(output_dir, 'finalized_model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(best_model, f)

scaler_path = os.path.join(output_dir, 'scaler.pkl')
with open(scaler_path, 'wb') as f:
    pickle.dump(scaler, f)

encoder_path = os.path.join(output_dir, 'label_encoder.pkl')
with open(encoder_path, 'wb') as f:
    pickle.dump(label_encoder, f)

metrics_path = os.path.join(output_dir, 'metric.json')
with open(metrics_path, 'w') as f:
    json.dump(metrics, f, indent=2)
