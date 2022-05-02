#Second test, soft cosine similarity https://www.machinelearningplus.com/nlp/cosine-similarity/
#soft cosine similarity (higher scores from documents of the same topic and lower for those with different topics)

import gensim
from gensim.matutils import softcossim
from gensim import corpora
import gensim.downloader as api
from gensim.utils import simple_preprocess
import pandas as pd
import numpy as np

fasttext_model300 = api.load('fasttext-wiki-news-subwords-300')

!pip install preprocess
import numpy as np

#Similarity between multiple articles

#Define the summaries to be used
file = "summarized - summarized (1).csv"
df = pd.read_csv(file)

#df.dropna(subset = ["Summary"],inplace = True)
summaries = []
for i in range(len(df["Text"])):
  if (i != 103 and i != 117 and i != 547 and i != 632):
    summaries.append(df["Summary"][i])
  else:
    summaries.append("Empty")

# Prepare a dictionary and a corpus.
#dictionary = corpora.Dictionary([simple_preprocess(doc) for doc in summaries])
dictionary = corpora.Dictionary([simple_preprocess(doc) for doc in summaries])

# Prepare the similarity matrix
similarity_matrix = fasttext_model300.similarity_matrix(dictionary, tfidf=None, threshold=0.0, exponent=2.0, nonzero_limit=100)

def create_soft_cossim_matrix(values):
  len_array = np.arange(len(values))
  xx, yy = np.meshgrid(len_array, len_array)
  cossim_mat = pd.DataFrame([[round(softcossim(values[i],values[j], similarity_matrix) ,2) for i, j in zip(x,y)] for y, x in zip(xx, yy)])
  return cossim_mat

# Convert the sentences into bag-of-words vectors.
values = []
for i in summaries:
  val = dictionary.doc2bow(simple_preprocess(i))
  values.append(val)

sim_mat = create_soft_cossim_matrix(values)
a = np.array(sim_mat)
np.savetxt('sim_matrix.csv',a,delimeter=',')

#finding max_values (less than 1.00)
list_of_max = []
for i in range(731):
  column = sim_mat[i]
  max = 0
  for j in range(731):
    if (column[j] != 1.00 and column[j] > max):
      max = column[j]
      max_id = j
  list_of_max.append(max_id)

print(list_of_max)
print(len(list_of_max))

#add column in csv file for recommended article
rec_df = pd.read_csv("summaries_with_recommender (2).csv")
#rec_df = df.copy()
#uses renumbered column for recs
rec_df["Recommendation_Article_Num_Renumbered"] = list_of_max
rec_df.to_csv("summaries_with_recommender.csv")
downloaded = files.download('summaries_with_recommender.csv')

#outputing single recommendations for a single input summary
def recommendArticle(simMatrix, article_num):
  row = sim_mat[article_num]
  max = 0
  for j in range(len(df["Article_num"])):
    if (row[j] != 1.00 and row[j] > max):
      max = row[j]
      max_id = j
