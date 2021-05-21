import streamlit as st
from streamlit.proto.TextInput_pb2 import TextInput
from stack import *
import time
import numpy as np
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
st.title('DATA STRUCTURE AND ALGORITHMS')

add_selectbox = st.sidebar.selectbox(
    "Which Algorithm you want to learn?",
    ("stack", "Queue", "Linked-list")
)
if add_selectbox=='stack':
  add_radio_left=st.sidebar.radio('Please select the more stuff',('push','pop','top element of stack'))
x=stack()
if add_radio_left=='push':
  st.write('your current stack is:',x.get_stack())
  
  for i in range(4):
    a=st.text_input('Enter the value',0)
    st.write('current stack:',x.push(a))
    pass
  #x.append(a)
  #ans=st.text_input('want to input more(y/n)')
  # 





# if add_radio_left=='pop':
#   st.write('current stack',x)
#   z=st.sidebar.radio('want to pop',('yes','no'))
#   if z=='yes':
#     try:
#       x.pop()
#       st.write('after pop stack is',x)
#     except:
#       st.write('Stack is Empty')
#   else:
#     pass
  
# code_show=st.sidebar.radio('want to look at code',('yes','no'))
# if code_show =='yes':
#   if add_selectbox=='stack':
#     if add_radio_left=='push' or 'pop' or 'top element of stack':
#       pass
      
  

#st.echo(code_location='above')
#type(add_selectbox)
#'Starting a long computation...'

# Add a placeholder
# latest_iteration = st.empty()

# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

# '...and now we\'re done!'

