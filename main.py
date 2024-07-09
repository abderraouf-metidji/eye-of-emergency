import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class Node:
    def __init__(self, feature_index=None, threshold=None, left=None, right=None, value=None):
        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=float("inf")):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X, y):
        data = np.c_[X, y]
        self.tree = self._build_tree(data)

    def predict(self, X):
        return np.array([self._predict(sample, self.tree) for sample in X])

    def _build_tree(self, data, current_depth=0):
        X, y = data[:, :-1], data[:, -1]
        n_samples, n_features = X.shape

        if n_samples >= self.min_samples_split and current_depth <= self.max_depth:
            best_split = self._get_best_split(data, n_features)
            if best_split["info_gain"] > 0:
                left_subtree = self._build_tree(best_split["dataset_left"], current_depth + 1)
                right_subtree = self._build_tree(best_split["dataset_right"], current_depth + 1)
                return Node(best_split["feature_index"], best_split["threshold"], left_subtree, right_subtree)

        leaf_value = self._calculate_leaf_value(y)
        return Node(value=leaf_value)

    def _get_best_split(self, data, n_features):
        best_split = {}
        max_info_gain = -float("inf")

        for feature_index in range(n_features):
            feature_values = data[:, feature_index]
            if isinstance(feature_values[0], (int, float)):
                possible_thresholds = np.unique(feature_values)
                for threshold in possible_thresholds:
                    dataset_left, dataset_right = self._split(data, feature_index, threshold)
                    if len(dataset_left) > 0 and len(dataset_right) > 0:
                        y, left_y, right_y = data[:, -1], dataset_left[:, -1], dataset_right[:, -1]
                        curr_info_gain = self._information_gain(y, left_y, right_y)
                        if curr_info_gain > max_info_gain:
                            best_split["feature_index"] = feature_index
                            best_split["threshold"] = threshold
                            best_split["dataset_left"] = dataset_left
                            best_split["dataset_right"] = dataset_right
                            best_split["info_gain"] = curr_info_gain

        return best_split

    def _split(self, data, feature_index, threshold):
        data_left = np.array([row for row in data if row[feature_index] <= threshold])
        data_right = np.array([row for row in data if row[feature_index] > threshold])
        return data_left, data_right

    def _information_gain(self, parent, l_child, r_child):
        weight_l = len(l_child) / len(parent)
        weight_r = len(r_child) / len(parent)
        gain = self._entropy(parent) - (weight_l * self._entropy(l_child) + weight_r * self._entropy(r_child))
        return gain

    def _entropy(self, y):
        class_labels = np.unique(y)
        entropy = 0
        for cls in class_labels:
            p_cls = len(y[y == cls]) / len(y)
            entropy += -p_cls * np.log2(p_cls + 1e-10)  # Add a small epsilon to avoid log(0)
        return entropy

    def _calculate_leaf_value(self, y):
        y = list(y)
        return max(y, key=y.count)

    def _predict(self, sample, tree):
        if tree.value is not None:
            return tree.value
        feature_val = sample[tree.feature_index]
        if feature_val <= tree.threshold:
            return self._predict(sample, tree.left)
        else:
            return self._predict(sample, tree.right)

# Load the datasets
train_data = pd.read_csv('train_tweets_cleaned.csv')
test_data = pd.read_csv('test_tweets_cleaned.csv')

# Handle missing values in 'processed_text' column
train_data['processed_text'].fillna('', inplace=True)
test_data['processed_text'].fillna('', inplace=True)

# Vectorize text data using TfidfVectorizer
tfidf = TfidfVectorizer(max_features=1000)
tfidf.fit(train_data['processed_text'])

X_train_tfidf = tfidf.transform(train_data['processed_text']).toarray()
X_test_tfidf = tfidf.transform(test_data['processed_text']).toarray()

# Combine vectorized features with additional numerical features
X_train = np.hstack((X_train_tfidf, train_data[['text_length', 'word_count', 'unique_words', 'stopword_percentage', 'sentiment']].values))
X_test = np.hstack((X_test_tfidf, test_data[['text_length', 'word_count', 'unique_words', 'stopword_percentage', 'sentiment']].values))

# Separate target variable
y_train = train_data['target'].values
y_test = test_data['target'].values

# Train the decision tree
tree = DecisionTree(min_samples_split=5, max_depth=10)
tree.fit(X_train, y_train)

# Make predictions on the test set
predictions = tree.predict(X_test)

# Print the predictions
print("Predictions:", predictions)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
