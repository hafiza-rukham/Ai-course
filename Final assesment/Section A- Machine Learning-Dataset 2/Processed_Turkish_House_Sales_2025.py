import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

#Load Data
df = pd.read_csv(r"C:\Users\Hajvery Technology\Documents\GitHub\Ai-course\Final assesment\Processed_Turkish_House_Sales_2025.csv",delimiter=",")

print(df.head())

print(df.info())
print(df.dtypes)
print(df.describe())
print(df.shape)

def price_class(price):
    if price < 3000000:
        return 0   # Low price
    elif price < 6000000:
        return 1   # Medium price
    else:
        return 2   # High price

df.loc[:, 'price_class'] = df['fiyat'].apply(price_class)

#Feature Engineering 
x = df.drop(['fiyat', 'price_class'], axis=1)
y = df['price_class']

import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(df['fiyat'], kde=True)   # Price distribution
sns.boxplot(x='satici_tip', y='fiyat', data=df)  # Brand-wise price
plt.show()

x = pd.get_dummies(x, drop_first=True)

#Split Dataset
SEED= 42
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Train Random Forest Regressor
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
print(x_train)
rf_classifier.fit(x_train, y_train)

#Predictions
y_pred = rf_classifier.predict(x_test)

#Metrics
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_rep)

#Confusion Matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
sample = x_test.iloc[0:1]
prediction = rf_classifier.predict(sample)

# Sample prediction / inference
sample = x_test.iloc[0:1]
prediction = rf_classifier.predict(sample)
prob = rf_classifier.predict_proba(sample)

sample_dict = sample.iloc[0].to_dict()
print(f"\nSample House Features: {sample_dict}")
print(f"Predicted Price Class: {prediction[0]}")
print(f"Probability Vector: {prob[0]}")
