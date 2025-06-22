import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, LabelEncoder

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


