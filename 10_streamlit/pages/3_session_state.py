import streamlit as st

st.title('Counter')

# streamlit은 화면을 생성할 때마다 처음부터 코드를 렌더링하는 방식이다.
# 따라서 저장이 되지 않기 때문에 초기 설정을 아래와 같이 잡아주는 것이 좋다.
if 'customer_count' not in st.session_state:
    st.session_state.customer_count = 0

if st.button('손님 한 명 추가요~!'):
    st.session_state.customer_count += 1

if st.button('오늘 장사 끝! 손님 수 초기화!'):
    st.session_state.customer_count = 0

st.write(f'지금까지 온 손님 수: {st.session_state.customer_count}')
