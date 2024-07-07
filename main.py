import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from decision_tree import DecisionTree  # Ensure the DecisionTree class is in decision_tree.py

# Load your datasets
train_tweets = pd.read_csv('train_tweets.csv')
test_tweets = pd.read_csv('test_tweets.csv')

# Check for missing data and handle it if necessary
if train_tweets.isnull().values.any() or test_tweets.isnull().values.any():
    print("Missing data found. Handling missing data...")
    train_tweets.dropna(inplace=True)
    test_tweets.dropna(inplace=True)

# Extract features and labels from training data
X_train_text = train_tweets['text']
y_train = train_tweets['target'].astype(int)  # Ensure the labels are integers

# Extract features from test data
X_test_text = test_tweets['text']

# Preprocess text data using TF-IDF
vectorizer = TfidfVectorizer()

# Fit and transform the training data
X_train = vectorizer.fit_transform(X_train_text).toarray()

# Transform the test data
X_test = vectorizer.transform(X_test_text).toarray()

# Create an instance of the DecisionTree
tree = DecisionTree(max_depth=5, min_samples_leaf=2)

# Train the decision tree classifier
tree.train(X_train, y_train)

# Predict on the test set
predictions = tree.predict(X_test)

# Evaluate the model
if 'target' in test_tweets.columns:
    y_test = test_tweets['target'].astype(int)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    print(f"Accuracy: {accuracy}")
    print("Classification Report:")
    print(report)

# Save the predictions
test_tweets['predicted_label'] = predictions
test_tweets.to_csv('test_tweets_with_predictions.csv', index=False)

print("Predictions have been saved to 'test_tweets_with_predictions.csv'")
