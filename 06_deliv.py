import mvp
import mvpdemo
import fulldf
import streamlit as st
from multiapp import MultiApp

app = MultiApp()
app.add_app("Project", mvp.app)
app.add_app("Demo", mvpdemo.app)
app.add_app("Full Dataframe", fulldf.app)
app.run()
