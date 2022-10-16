import streamlit as st

# import pandas as pd
# import numpy as np


st.set_page_config(
    page_title="Personal template project",
    page_icon="👋",
)

st.header("Personal template project")

# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))

# st.dataframe(dataframe.style.highlight_max(axis=0))


st.sidebar.success("Select a demo above.")
