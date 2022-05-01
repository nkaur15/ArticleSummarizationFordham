import streamlit as st
import mvpdemo
import pandas as pd

def app():
	header = st.container()
	dataset = st.container()
	method = st.container()

	with header:
		st.title("Article Summarization Project")

	with dataset:
		st.header("Red Ventures Article Dataset")
		st.write("The project we worked on is about summarizing a dataset of articles and generating article recommendations from the same dataset. This dataset was provided in the problem statement. Originally, the dataset consisted of 1176 articles, many of which were mainly comprised of special characters, so through data preprocessing we have trimmed the dataset considerably into 731 articles. Below is a dataframe with the articles numbered, along with other information like sources and text length.")
		articledf = pd.read_csv('data/new_article_data.csv')
		st.write(articledf)

	with method:
		st.header("Summarization method")
		st.markdown("We used the summarizer from the pipeline imported through the transformers library to generate summaries for each article. After looking at open-source projects on GitHub, we thought this was a great abstractive text summarization model. The below line with the specified parameters generates summaries in the ballpark of 280 characters.")
		st.text("summary = summarizer(text, max_length=55, min_length = 15, do_sample = False)[0][\'summary_text\']")
		st.markdown("fit_characters() is a function we wrote to ensure that the summaries fit the 280 character maximum, while also ensuring that they end on a complete sentence.")
		st.text("fit_characters(summ):\n\ttool = language_tool_python.LanguageTool('en-US')\n\tif (summ[len(summ)-1] == '.' and len(summ) <= 280):\n\t\treturn tool.correct(summ)\n\tsumm = summ[:280]\n\tsentences = summ.split(\".\")\n\tsentences.pop()\n\tnewsum = \'.\'.join(sentences)\n\tif newsum[-1] == \' \':\n\t\tnewsum = newsum[:(len(newsum)-1)]+\".\"\n\treturn tool.correct(newsum)")

	