import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Plotting Demo", page_icon="📈")
st.header("Page 1")

dataframe = pd.DataFrame(
    np.random.randn(5, 5),
    columns=('col %d' % i for i in range(5)))

st.dataframe(dataframe.style.highlight_max(axis=0))
