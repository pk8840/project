import streamlit as st
st.title('loan approval app')
st.write('check your eligibility')
c=st.number_input('enter your credit score')
s=st.number_input('enter your salry')
st.button('check')
if s>=50000 and c>=500:
    st.write('eligible for loan')
else:
    st.write('not eligible')