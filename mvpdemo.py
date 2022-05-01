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
def fit_characters(summ):
	#disabledRuleIds configuration change rule id to stop correcting
	#tool = language_tool_python.LanguageTool('en-US', config={ 'maxSpellingSuggestions': 0})
	if (summ[len(summ)-1] == '.' and len(summ) <= 280):
		#return tool.correct(summ)
		return summ
	summ = summ[:280]
	sentences = summ.split(".")
	sentences.pop()
	for newsum in sentences:
		if newsum[-1] == ' ':
			newsum = newsum[:(len(newsum)-1)]
	newsum = '.'.join(sentences)
	if newsum[-1] == ' ':
		newsum = newsum[:(len(newsum)-1)]+"."
	return newsum
	#return tool.correct(newsum)

def fit_tokens(tx):
	words = tx.split(" ")
	words = words[:350]
	tx = " ".join(words)
	return tx

def run_model(text):
	text = fit_tokens(text)
	summary = summarizer(text, max_length=55, min_length = 15, do_sample = False)[0]['summary_text']
	summary = fit_characters(summary)
	return summary

def app():
	header = st.container()
	runmodel = st.container()
	quality = st.container()
	#rec = st.container()
	
	with header:
		st.title("Article Summarization Demo")

	with runmodel:
		st.header("Let's run the model")
		article_choice = st.slider("Which article would you like to summarize?", min_value = 0, max_value = 730, value = 395, step = 1)
		num = article_choice
		article_col,summary_col, recommender_col = st.columns(3)
		article_col.subheader("Chosen article")
		articledf = pd.read_csv('data/new_article_data.csv')
		recdf = pd.read_csv('data/newest.csv')
		# use astype look up syntax
		# try transforming string data see what happens
		article_col.write(str(articledf['Text'][article_choice]))
		summary_col.subheader("Summary")
		summary_col.write(run_model(articledf['Text'][article_choice]))
		recommender_col.subheader("Recommendation")
		recommender_col.write(str(recdf['Text'][recdf['Recommendation_Article_Num_Renumbered'][num]]))


	with quality:
		st.header("Summary quality")

	#with rec:
		#st.header("Recommended article")
		#st.write("The article with the below summary has been recommended: - ")
		#articledf = pd.read_csv('data/newest.csv')
		#st.write(str(articledf['Text'][articledf['Recommendation_Article_Num_Renumbered'][num]]))
