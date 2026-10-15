# Machine Learning Algorithms and Their Principles

Machine learning algorithms learn patterns from data to predict outcomes, classify observations, group similar data points, reduce dimensionality, or detect anomalies.

## 1. Supervised Learning Algorithms

Supervised learning uses labelled data: the training dataset contains input features `X` and known target values `y`.

### Core Classification and Regression Algorithms

| Algorithm | Type | Fundamental Principle |
|---|---|---|
| Linear Regression | Regression | Fits a linear equation that minimizes the sum of squared prediction errors. |
| Logistic Regression | Classification | Uses the sigmoid function to estimate the probability of a class. |
| Decision Tree | Classification / Regression | Recursively splits data using a criterion such as Gini impurity, information gain, or variance reduction. |
| Random Forest | Classification / Regression | Combines predictions from many decision trees to reduce variance and improve generalization. |
| Support Vector Machine (SVM) | Classification / Regression | Finds a decision boundary with the maximum margin between classes; kernels can model nonlinear boundaries. |
| K-Nearest Neighbours (KNN) | Classification / Regression | Predicts using the labels or values of the closest training observations. |
| Naive Bayes | Classification | Applies Bayes' theorem while assuming features are conditionally independent given the class. |
| Gradient Boosting | Classification / Regression | Builds models sequentially, with each new model reducing the current loss. |
| AdaBoost | Classification / Regression | Combines weak learners while increasing emphasis on observations misclassified by earlier learners. |
| Linear Discriminant Analysis (LDA) | Classification | Separates classes using their means and within-class covariance assumptions. |
| Ridge Regression | Regression | Minimizes squared error with an L2 penalty on coefficients to reduce overfitting. |
| Lasso Regression | Regression | Uses an L1 penalty that can shrink some coefficients to zero. |
| Elastic Net | Regression | Combines L1 and L2 regularization. |

### Key Supervised Algorithms Explained

#### 1. Linear Regression
**Principle:** Finds a line or hyperplane that minimizes squared residuals.

`ŷ = wᵀX + b`

Use it to predict continuous values, such as house prices or stock prices. It assumes a linear relationship in the model's features.

#### 2. Logistic Regression
**Principle:** Converts a linear score into a probability using the sigmoid function.

`P(y = 1 | x) = 1 / (1 + e^(-z))`, where `z = wᵀx + b`.

It is used for binary classification and can be extended to multiclass classification.

#### 3. Decision Tree
**Principle:** Selects a feature and threshold that best separate target classes, then repeats this process recursively.

- Classification: Gini impurity or entropy/information gain.
- Regression: Often variance reduction or squared-error reduction.

The final leaf provides a class prediction or numerical prediction.

#### 4. Random Forest
**Principle:** Trains many decision trees on bootstrap samples and considers random subsets of features at splits.

- Classification generally uses majority voting.
- Regression averages tree predictions.

This often reduces the variance of a single tree.

#### 5. Support Vector Machine (SVM)
**Principle:** Maximizes the margin between classes. Support vectors are the observations that determine the boundary.

Kernel functions, such as the RBF kernel, allow nonlinear decision boundaries. Feature scaling is usually important.

#### 6. K-Nearest Neighbours (KNN)
**Principle:** Finds the `k` closest training observations using a distance measure.

- Classification uses majority voting.
- Regression commonly averages neighbours' target values.

The choice of `k`, distance measure, and feature scaling matters.

#### 7. Naive Bayes
**Principle:** Uses Bayes' theorem to estimate the probability of each class given the features.

It assumes conditional independence of features given the class. It is often efficient for text classification and other high-dimensional problems.

#### 8. Gradient Boosting and AdaBoost
**Principle:** Combine several weak learners into a stronger model.

- Gradient boosting fits new learners to reduce the current loss.
- AdaBoost reweights observations to emphasize difficult examples.

Both can overfit if not appropriately tuned.

## 2. Unsupervised Learning Algorithms

Unsupervised learning uses data without target labels. The algorithm tries to discover structure, groups, patterns, or lower-dimensional representations.

### Clustering Algorithms

| Algorithm | Fundamental Principle | Main Use |
|---|---|---|
| K-Means | Assigns observations to the nearest centroid and updates centroids to minimize within-cluster squared distances. | Grouping similar observations. |
| Hierarchical Clustering | Builds a hierarchy of clusters by repeatedly merging clusters (agglomerative) or splitting them (divisive). | Exploring nested groups. |
| DBSCAN | Groups closely packed observations based on density and labels sparse observations as noise. | Irregular-shaped clusters and outliers. |
| OPTICS | Orders observations to represent clustering structure across different density levels. | Data with varying cluster densities. |
| Gaussian Mixture Model (GMM) | Models data as a mixture of Gaussian probability distributions and estimates membership probabilities. | Soft clustering and overlapping groups. |
| Mean Shift | Moves candidate cluster centres toward regions of higher estimated data density. | Discovering clusters without specifying their number in advance. |

### 9. K-Means Clustering
**Principle:** Minimizes the sum of squared distances between data points and their assigned cluster centroids.

Steps:
1. Initialize `K` centroids.
2. Assign each point to its nearest centroid.
3. Recalculate each centroid as the mean of its assigned points.
4. Repeat assignment and update until convergence.

You must choose `K`. Scaling is often important when features use different units.

### 10. DBSCAN
**Principle:** Forms clusters from dense neighbourhoods using two parameters:

- `eps`: neighbourhood radius.
- `min_samples`: minimum number of observations required in a neighbourhood for a core point.

It can find irregular-shaped clusters and identify noise. It may struggle when clusters have substantially different densities.

### 11. Hierarchical Clustering
**Principle:** Builds a tree of clusters called a **dendrogram**.

The choice of linkage—single, complete, average, or Ward's method—determines how clusters are merged. A cut through the dendrogram determines the final groups.

## 3. Dimensionality Reduction Algorithms

Dimensionality reduction reduces the number of features while attempting to preserve useful information or structure.

| Algorithm | Fundamental Principle | Main Use |
|---|---|---|
| PCA (Principal Component Analysis) | Finds orthogonal directions that capture maximum variance in the data. | Compression, visualization, reducing correlated features. |
| t-SNE | Preserves local neighbourhood similarities when mapping high-dimensional data into fewer dimensions. | Visualizing high-dimensional data. |
| UMAP | Constructs a neighbourhood graph and optimizes a lower-dimensional representation that preserves much of its structure. | Visualization and exploratory analysis. |
| ICA (Independent Component Analysis) | Finds components that are as statistically independent as possible. | Signal separation. |
| Feature Selection | Selects a subset of original features based on relevance or importance. | Removing redundant or irrelevant features. |

### 12. PCA — Principal Component Analysis
**Principle:** PCA transforms original features into new, mutually orthogonal variables called principal components. The first component captures the greatest possible variance, the second captures the greatest remaining variance subject to orthogonality, and so on.

Typical steps:
1. Standardize features when their scales differ.
2. Calculate the covariance matrix or use singular value decomposition (SVD).
3. Find the principal component directions.
4. Rank components by explained variance.
5. Retain the desired number of components.

**Explained variance ratio** tells you the proportion of variance represented by each component.

**Important:** PCA does not directly tell you the percentage contribution of each original feature to the target. Component loadings describe how original features contribute to each component.

### 13. t-SNE and UMAP

- **t-SNE:** Attempts to preserve local neighbourhood relationships. It is mainly useful for visualization; distances between widely separated groups and cluster sizes may be misleading.
- **UMAP:** Also preserves neighbourhood structure and can often retain more global structure than t-SNE, although results depend on parameter choices.

Neither method should automatically be treated as a predictive model or proof that genuine clusters exist.

## 4. Robust Estimation and Anomaly Detection

| Algorithm | Fundamental Principle | Main Use |
|---|---|---|
| RANSAC | Repeatedly fits a model to random subsets and selects a model supported by the greatest number of inliers. | Robust line fitting, geometric estimation, noisy data. |
| Isolation Forest | Randomly partitions data; anomalous observations tend to be isolated in fewer splits. | Detecting unusual observations. |
| Local Outlier Factor (LOF) | Compares local density around an observation with density around its neighbours. | Finding local anomalies. |
| One-Class SVM | Learns a boundary around typical training observations and identifies observations outside that boundary. | Novelty detection. |
| Huber Regression | Uses squared loss for small residuals and linear loss for large residuals. | Regression less sensitive to outliers. |
| Theil–Sen Regression | Estimates a robust regression slope using the median of slopes from pairs of observations. | Robust linear trend estimation. |

### 14. RANSAC
**Principle:** Random Sample Consensus estimates a model despite substantial numbers of outliers.

The algorithm:
1. Randomly selects a minimal subset of observations.
2. Fits a model to that subset.
3. Counts observations that agree with the model (inliers).
4. Repeats the process.
5. Selects the best-supported model and may refit it using the inliers.

RANSAC is useful in computer vision, robotics, line fitting, and geometric estimation.

## 5. Neural Network and Deep Learning Algorithms

| Algorithm | Fundamental Principle | Main Use |
|---|---|---|
| Artificial Neural Network (ANN) | Learns weights and biases through forward propagation and backpropagation with gradient-based optimization. | General nonlinear prediction. |
| Convolutional Neural Network (CNN) | Uses learned convolutional filters to detect spatial patterns and hierarchical features. | Images and spatial data. |
| Recurrent Neural Network (RNN) | Processes sequences while maintaining a hidden state that carries information from earlier steps. | Sequential data. |
| LSTM | Uses gated memory cells to retain or discard information over longer sequences. | Time series and sequence modelling. |
| Transformer | Uses attention mechanisms to model relationships between elements in a sequence or input. | Language, images, and multimodal tasks. |
| Autoencoder | Learns to encode data into a compressed representation and reconstruct the original input. | Representation learning and anomaly detection. |

### 15. ANN — Artificial Neural Network
**Principle:** A neural network learns a function by adjusting weights and biases to minimize a loss function.

The main steps are:
1. Forward propagation computes predictions.
2. A loss function measures prediction error.
3. Backpropagation calculates gradients.
4. An optimizer updates the weights.
5. The process repeats over training iterations.

Networks with nonlinear activation functions can learn complex relationships.

## 6. Quick Revision: Which Algorithm Should You Choose?

| Problem | Suitable Starting Algorithm | Why |
|---|---|---|
| Predict a continuous number | Linear Regression | Simple, interpretable baseline. |
| Predict a category | Logistic Regression or Decision Tree | Straightforward classification baselines. |
| Understand decision rules | Decision Tree | Provides explicit feature-based splits. |
| Improve tree-based prediction | Random Forest | Combines multiple trees. |
| Find groups when `K` is known | K-Means | Simple centroid-based clustering. |
| Find dense, irregular-shaped groups | DBSCAN | Uses density rather than centroids. |
| Visualize high-dimensional data | PCA, t-SNE, or UMAP | Provides lower-dimensional representations. |
| Reduce correlated numerical features | PCA | Creates orthogonal components. |
| Detect outliers | Isolation Forest or LOF | Identifies unusual observations. |
| Fit a model with many outliers | RANSAC | Selects models supported by inliers. |
| Classify using nearby observations | KNN | Uses local similarity. |
| Model complex image patterns | CNN | Learns spatial features. |
| Model long sequences | LSTM or Transformer | Learns sequence dependencies. |

## 7. Essential Principles to Remember for Task 6

Focus first on these eight algorithms:

| Algorithm | Learning Type | Core Principle |
|---|---|---|
| Decision Tree | Supervised | Selects feature splits using impurity reduction and builds branches recursively. |
| Random Forest | Supervised | Combines many randomized decision trees to improve generalization. |
| SVM | Supervised | Finds a maximum-margin decision boundary. |
| KNN | Supervised | Predicts from the nearest training examples. |
| K-Means | Unsupervised | Assigns observations to the nearest centroid and updates centroids. |
| DBSCAN | Unsupervised | Forms clusters from dense neighbourhoods and identifies noise. |
| PCA | Dimensionality reduction | Finds orthogonal components that capture maximum variance. |
| RANSAC | Robust estimation | Fits models using random subsets and selects the model with strongest inlier support. |

### Final Distinction

- **Supervised learning** predicts a known target.
- **Unsupervised learning** discovers structure without a target.
- **Dimensionality reduction** compresses features while preserving selected information.
- **Robust estimation and anomaly detection** address outliers and unusual observations.

These categories serve different purposes, so not every algorithm is a direct substitute for another.
