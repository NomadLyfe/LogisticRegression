import numpy as np

class LogisticRegression:
    def __init__(self, lr=0.001, n_iters=1000) -> None:
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samps, n_feats = X.shape

        self.weights = np.zeros(n_feats)
        self.bias = 0

        for _ in range(self.n_iters):
            #y_pred = 1/(1 + e**(-w*x + b))
            y_pred = 1 / (1 + np.exp(-np.clip(np.dot(X, self.weights) + self.bias, -500, 500)))

            ddw = (1/n_samps) * np.dot(2*X.T, (y_pred-y))
            ddb = (1/n_samps) * np.sum(2*(y_pred-y))

            self.weights = self.weights - self.lr * ddw
            self.bias = self.bias - self.lr * ddb

    def predict(self, X):
        y_pred = 1 / (1 + np.exp(-np.clip(np.dot(X, self.weights) + self.bias, -500, 500)))
        class_pred = [0 if y<0.5 else 1 for y in y_pred]
        return class_pred