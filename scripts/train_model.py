import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv('../data/hardware_specs.csv')
features = data[['clock_speed', 'cores', 'logical_cores', 'memory', 'total_storage']]
labels = data['brand']

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, '../models/model.h5')
print("Model trained and saved!")