import pandas as pd

df = pd.read_csv("../data/processed/jobs_scrapy.csv")

print("Total Jobs:", len(df))
print("\nTop Companies:")
print(df["company"].value_counts().head(10))

print("\nTop Locations:")
print(df["location"].value_counts().head(10))

# Optional: simple chart
import matplotlib.pyplot as plt

df["company"].value_counts().head(5).plot(kind="bar", title="Top Companies")
plt.tight_layout()
plt.savefig("top_companies.png")
plt.show()