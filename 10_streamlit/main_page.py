import streamlit as st

st.title('오늘은 불금입니다~')
st.header('불타는 마음으로 Streamlit을 다루죠....')
st.subheader('크아아악, Streamlit이 날 죽인다!!!!')

my_site = st.text_input('오늘 내가 만들어야 하는 사이트는 ?')
st.write(my_site)

if st.button(f'{my_site} 접속하기'): # bool type
    st.success(f'{my_site}로 접속 중', icon='❤️')
