import os
import json
from sklearn.metrics import r2_score
import pickle
from model_development.model import label_encoder, scaler, X_train_scaled, X_test_scaled, y_train, y_test
from model_development.model import gridfr

best_model = gridfr.best_estimator_



predictions = best_model.predict(X_test_scaled)
predictions_train = best_model.predict(X_train_scaled)

r2_score_test = r2_score(y_test, predictions)
r2_score_train = r2_score(y_train, predictions_train)

metrics = {
    'r2_score_test': r2_score_test,
    'r2_score_train': r2_score_train
}

output_dir = 'artifacts'
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
 
print(f"Model, scaler, and label encoder saved to {output_dir}")    