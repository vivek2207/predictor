import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import training

# Expand displayed data rows and columns
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

# Load data
output = 'impressions'
data = training.load_data_from_csv(output + '.csv')

# Show data shape (size), columns and first 10 rows
print(data.shape)
print(data.columns)
data.head(10)

# View metrics summary
data.describe()

# Visualize distributions of numerical features with histograms
quan = list(data.loc[:, data.dtypes != 'object'].columns.values)
grid = sns.FacetGrid(pd.melt(data, value_vars=quan),
                     col='variable', col_wrap=4, height=3, aspect=1,
                     sharex=False, sharey=False)
grid.map(plt.hist, 'value', color="steelblue")
plt.show()

# Visualize feature correlations
sns.heatmap(data._get_numeric_data().astype(float).corr(),
            square=True, cmap='RdBu_r', linewidths=.5,
            annot=True, fmt='.2f').figure.tight_layout()
plt.show()

# Investigate correlations between dependent and independent variables
data.corr(method='pearson').iloc[0].sort_values(ascending=False)

# Investigate missing values
# Columns with NaN
data.isnull().sum()
# Rows with NaN
rows_with_nan = 0
for i in range(len(data)):
    rows_with_nan += data.iloc[i].isnull().sum()
print(rows_with_nan)

####

# Visualize tree results
import graphviz
from sklearn import tree
dot_data = tree.export_graphviz(tree_regressor, out_file='tree.dot',
                                feature_names=X_train.columns)
# dot -Tpng tree.dot -o tree.png
