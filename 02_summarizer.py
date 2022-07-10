import streamlit as st
import pandas as pd
from gingerit.gingerit import GingerIt
import os
from transformers import pipeline
import language_tool_python
import json

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
summarizer = pipeline("summarization")
num = 0
tool = language_tool_python.LanguageTool('en-US', config={ 'disabledRuleIds': 'MORFOLOGIK_RULE_EN_US'})
similaritydf = pd.read_csv('data/sim_matrix.csv')

def fit_characters(summ):
	#disabledRuleIds configuration change rule id to stop correcting
	if (summ[len(summ)-1] == '.' and len(summ) <= 280):
		return tool.correct(summ)
		#return summ
	summ = summ[:280]
	sentences = summ.split(".")
	sentences.pop()
	newsum = '.'.join(sentences)	
	if newsum[-1] == ' ':
		newsum = newsum[:(len(newsum)-1)]+"."
	#return newsum
	return tool.correct(newsum)

def fit_tokens(tx):
	words = tx.split(" ")
	words = words[:350]
	tx = " ".join(words)
	return tx

def run_model(text):
	text = fit_tokens(text)
	summary = summarizer(text, max_length=55, min_length = 15)[0]['summary_text']
	summary = fit_characters(summary)
	return summary

def recommendArticle(sim_mat, article_num, df):
	row = sim_mat[article_num]
	max = 0
	for j in range(len(df["Article_num"])):
		if (row[j] != 1.00 and row[j] > max):
			max = row[j]
			max_id = j
	print("Source: ", df["Source"][max_id])
	print("Article Number: ",df["Renumbered"][max_id])
	print("Recommended Article: ", df["Text"][max_id])

def app():
	header = st.container()
	runmodel = st.container()
	quality = st.container()
	#rec = st.container()
	
	with header:
		st.title("Article Summarization Demo")

	with runmodel:
		st.header("Let's run the model")
		article_choice = st.slider("Which article would you like to summarize?", min_value = 0, max_value = 730, value = 360, step = 1)
		num = article_choice
		article_col,summary_col, recommender_col,similarity_col = st.columns(4)
		article_col.subheader("Chosen article")
		articledf = pd.read_csv('data/new_article_data.csv')
		recdf = pd.read_csv('data/bigdf.csv')
		# use astype look up syntax
		# try transforming string data see what happens
		article_col.write(str(articledf['Text'][article_choice]))
		summary_col.subheader("Summary")
		recommender_col.subheader("Recommended Article")
		similarity_col.subheader("\tRouge Similarity")
		summary_col.write("\n" + run_model(articledf['Text'][article_choice]))
		recommender_col.write(str(recdf['Text'][recdf['Recommendation_Article_Num_Renumbered'][num]]))
		similarity_col.write(recdf['Rouge_Eval'][num])
		#recommender_col.write(recommendArticle(similaritydf, article_choice, articledf))
