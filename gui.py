import streamlit as st
st.title('MY FIRST APP')
st.balloons()
st.write('hello all')
x=st.radio('are you working',options=['yes','no'])
if x=='yes':
    st.write('ok you can take our weekend batch')
else:
    st.write('ok you can take weekdays batch')
a=st.text_input('enter you  branch')
b=st.number_input('percentage')
c=st.sidebar.checkbox('test cleared')
if c==True:
    st.sidebar.write('20%off')
