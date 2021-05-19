import streamlit as st
import time
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
st.title('DATA STRUCTURE AND ALGORITHMS')
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

add_selectbox = st.sidebar.selectbox(
    "Which Algorithm you want to visualise?",
    ("stack", "Queue", "Linked-list")
)

#st.echo(code_location='above')
#type(add_selectbox)
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
