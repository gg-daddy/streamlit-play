import streamlit as st
import pandas as pd
import numpy as np


st.header("Test session state / cache.")

left_column, right_column = st.columns(2)

with left_column:
    if "df" not in st.session_state:
        st.session_state.df = pd.DataFrame(
            np.random.randn(20, 2), columns=["x", "y"])

    st.header("Session State:", divider=True,
              help="The dataframe is stored in session state.")
    st.dataframe(st.session_state.df)
    color1 = st.color_picker("Color", "#FF0000", key="color1")
    st.divider()
    st.scatter_chart(st.session_state.df, x="x", y="y", color=color1)


@st.cache_data
def get_df():
    return pd.DataFrame(
        np.random.randn(20, 2), columns=["x", "y"])


with right_column:
    st.header("Cache:", divider=True, help="The dataframe is stored in cache.")
    st.dataframe(get_df())
    color2 = st.color_picker("Color", "#FFF000", key="color2")
    st.divider()
    st.scatter_chart(get_df(), x="x", y="y", color=color2)
