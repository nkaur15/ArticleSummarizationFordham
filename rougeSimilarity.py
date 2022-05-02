!pip install rouge

from rouge import Rouge
from google.colab import files
import pandas as pd

file = "summarized - summarized (1).csv"
df = pd.read_csv(file)

model_out = []
references = []
df.dropna()
vals = []

for i in range(len(df["Text"])):
  if (i != 103 and i != 117 and i != 547 and i != 632):
    #model_out.append(df["Summary"][i])
    #references.append(df["Text"][i])
    rouge = Rouge()
    vals.append(rouge.get_scores(df["Summary"][i], df["Text"][i]))
  else:
    vals.append("Empty")

new_df = df.copy()
new_df["Rouge_Eval"] = vals
new_df.to_csv("summaries.csv")
downloaded = files.download('summaries.csv')
