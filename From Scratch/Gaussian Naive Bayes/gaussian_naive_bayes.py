import numpy as np

class GaussianNB:
    def fit(self, x, y):
        X, y = np.asarray(x), np.asarray(y)
        self.classes = np.unique(y)
        n_classes, n_features = len(self.classes), X.shape[1]
        
        self.means_ = np.zeros((n_classes, n_features), dtype=np.float64)
        self.vars_ = np.zeros((n_classes, n_features), dtype=np.float64)
        self.priors = np.zeros(n_classes, dtype=np.float64)
        
        for idx, k in enumerate(self.classes):
            X_k = X[y == k]
            
            self.means_[idx, :] = X_k.mean(axis=0)
            self.vars_[idx, :] = X_k.var(axis=0)
            self.priors[idx] = X_k.shape[0] / float(X.shape[0])
        return self
    
    def _log_gaussian(self, X):
        num = -0.5 * (X[:, None, :] - self.means_) ** 2 / self.vars_
        log_prob = num - 0.5 * np.log(2 * np.pi * self.vars_, axis = 1)
        return log_prob.sum(axis=2)
    
    def predict(self, X):
        X = np.asarray(X)
        log_probs = self._log_gaussian(X)
        log_prior = np.log(self.priors)
        return self.classes[np.argmax(log_probs + log_prior, axis=1)]