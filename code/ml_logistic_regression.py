#!/usr/bin/env python
"""Use sklearn to do logistic regression."""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Create a 2D dataset
X = np.array([ [1.4, 0.2],
               [1.4, 0.2],
               [1.3, 0.2],
               [1.5, 0.2],
               [1.4, 0.2],
               [1.7, 0.4],
               [1.4, 0.3],
               [1.5, 0.2],
               [1.4, 0.2],
               [1.5, 0.1],
               [1.5, 0.2],
               [1.6, 0.2],
               [1.4, 0.1],
               [1.1, 0.1],
               [1.2, 0.2],
               [1.5, 0.4],
               [1.3, 0.4],
               [1.4, 0.3],
               [1.7, 0.3],
               [1.5, 0.3],
               [1.7, 0.2],
               [1.5, 0.4],
               [1. , 0.2],
               [1.7, 0.5],
               [1.9, 0.2],
               [1.6, 0.2],
               [1.6, 0.4],
               [1.5, 0.2],
               [1.4, 0.2],
               [1.6, 0.2],
               [1.6, 0.2],
               [1.5, 0.4],
               [1.5, 0.1],
               [1.4, 0.2],
               [1.5, 0.2],
               [1.2, 0.2],
               [1.3, 0.2],
               [1.4, 0.1],
               [1.3, 0.2],
               [1.5, 0.2],
               [1.3, 0.3],
               [1.3, 0.3],
               [1.3, 0.2],
               [1.6, 0.6],
               [1.9, 0.4],
               [1.4, 0.3],
               [1.6, 0.2],
               [1.4, 0.2],
               [1.5, 0.2],
               [1.4, 0.2],
               [4.7, 1.4],
               [4.5, 1.5],
               [4.9, 1.5],
               [4. , 1.3],
               [4.6, 1.5],
               [4.5, 1.3],
               [4.7, 1.6],
               [3.3, 1. ],
               [4.6, 1.3],
               [3.9, 1.4],
               [3.5, 1. ],
               [4.2, 1.5],
               [4. , 1. ],
               [4.7, 1.4],
               [3.6, 1.3],
               [4.4, 1.4],
               [4.5, 1.5],
               [4.1, 1. ],
               [4.5, 1.5],
               [3.9, 1.1],
               [4.8, 1.8],
               [4. , 1.3],
               [4.9, 1.5],
               [4.7, 1.2],
               [4.3, 1.3],
               [4.4, 1.4],
               [4.8, 1.4],
               [5. , 1.7],
               [4.5, 1.5],
               [3.5, 1. ],
               [3.8, 1.1],
               [3.7, 1. ],
               [3.9, 1.2],
               [5.1, 1.6],
               [4.5, 1.5],
               [4.5, 1.6],
               [4.7, 1.5],
               [4.4, 1.3],
               [4.1, 1.3],
               [4. , 1.3],
               [4.4, 1.2],
               [4.6, 1.4],
               [4. , 1.2],
               [3.3, 1. ],
               [4.2, 1.3],
               [4.2, 1.2],
               [4.2, 1.3],
               [4.3, 1.3],
               [3. , 1.1],
               [4.1, 1.3],
               [6. , 2.5],
               [5.1, 1.9],
               [5.9, 2.1],
               [5.6, 1.8],
               [5.8, 2.2],
               [6.6, 2.1],
               [4.5, 1.7],
               [6.3, 1.8],
               [5.8, 1.8],
               [6.1, 2.5],
               [5.1, 2. ],
               [5.3, 1.9],
               [5.5, 2.1],
               [5. , 2. ],
               [5.1, 2.4],
               [5.3, 2.3],
               [5.5, 1.8],
               [6.7, 2.2],
               [6.9, 2.3],
               [5. , 1.5],
               [5.7, 2.3],
               [4.9, 2. ],
               [6.7, 2. ],
               [4.9, 1.8],
               [5.7, 2.1],
               [6. , 1.8],
               [4.8, 1.8],
               [4.9, 1.8],
               [5.6, 2.1],
               [5.8, 1.6],
               [6.1, 1.9],
               [6.4, 2. ],
               [5.6, 2.2],
               [5.1, 1.5],
               [5.6, 1.4],
               [6.1, 2.3],
               [5.6, 2.4],
               [5.5, 1.8],
               [4.8, 1.8],
               [5.4, 2.1],
               [5.6, 2.4],
               [5.1, 2.3],
               [5.1, 1.9],
               [5.9, 2.3],
               [5.7, 2.5],
               [5.2, 2.3],
               [5. , 1.9],
               [5.2, 2. ],
               [5.4, 2.3],
               [5.1, 1.8]])

# Create 1D label data per 2D datapoint
y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
              2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

# Split the data into test and train
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1, stratify=y)

#  Perform logistic regression on the training data
lr = LogisticRegression(C=100.0, solver='lbfgs', multi_class='ovr')
lr.fit(X_train, y_train)

# Use model on one datapoint of the test dataset
test_predictions = lr.predict_proba(X_test[:1, :])
for x in test_predictions:
    print("Chance of it being class 1:", "%.2f%%" % round(test_predictions[0][0]*100, 2))
    print("Chance of it being class 2:", "%.2f%%" % round(test_predictions[0][1]*100, 2))
    print("Chance of it being class 3:", "%.2f%%" % round(test_predictions[0][2]*100, 2))