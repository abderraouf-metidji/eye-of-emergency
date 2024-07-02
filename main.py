import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from decision_tree import DecisionTree  # Ensure the DecisionTree class is in decision_tree.py

# Load your datasets
train_tweets = pd.read_csv('train_tweets.csv')
test_tweets = pd.read_csv('test_tweets.csv')

# Extract features and labels from training data
X_train_text = train_tweets['text']
y_train = train_tweets['target']

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

predictions = tree.predict(X_test)

test_tweets['predicted_label'] = predictions
test_tweets.to_csv('test_tweets_with_predictions.csv', index=False)

print("Predictions have been saved to 'test_tweets_with_predictions.csv'")
