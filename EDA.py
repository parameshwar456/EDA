# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
# (You can replace this with your own CSV file)
data = pd.read_csv("data.csv")

# -----------------------------
# Basic Information
# -----------------------------
print("First 5 rows:\n", data.head())
print("\nDataset Info:\n")
print(data.info())

print("\nStatistical Summary:\n", data.describe())

# -----------------------------
# Check Missing Values
# -----------------------------
print("\nMissing Values:\n", data.isnull().sum())

# -----------------------------
# Data Visualization
# -----------------------------

# Histogram (for numeric columns)
data.hist(figsize=(10, 8))
plt.suptitle("Histograms")
plt.show()

# Scatter Plot (example: first two columns)
plt.scatter(data.iloc[:, 0], data.iloc[:, 1])
plt.xlabel(data.columns[0])
plt.ylabel(data.columns[1])
plt.title("Scatter Plot")
plt.show()

# Boxplot (to detect outliers)
data.plot(kind='box', figsize=(10, 6))
plt.title("Box Plot")
plt.show()

# -----------------------------
# Correlation Analysis
# -----------------------------
correlation = data.corr(numeric_only=True)
print("\nCorrelation Matrix:\n", correlation)

# Heatmap (simple)
plt.imshow(correlation, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Heatmap")
plt.show()

# -----------------------------
# Key Insights (basic example)
# -----------------------------
print("\nInsights:")
print("- Check which variables have high correlation.")
print("- Look for outliers in boxplots.")
print("- Observe distribution in histograms.")