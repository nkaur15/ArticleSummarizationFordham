import pandas as pd
import streamlit as st

def app():
	summs = st.container()

	with summs:
		sumdf = pd.DataFrame()
		st.header("Dataframe with all summaries and recommendations")
		articledf = pd.read_csv('data/bigdf.csv')
		sumdf['ARTICLE'] = [articledf['Text'][i] for i in range(730)]
		sumdf['SUMMARY'] = [articledf['Summary'][i] for i in range(730)]
		sumdf['RECOMMENDATION'] = [articledf['Text'][articledf['Recommendation_Article_Num_Renumbered'][i]] for i in range(730)]
		#sumdf['ARTICLE'] = articledf['Text']
		st.write(sumdf)
