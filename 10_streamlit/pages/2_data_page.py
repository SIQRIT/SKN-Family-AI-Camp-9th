import streamlit as st
import pandas as pd

st.title('게임 캐릭터의 인지도')

data = pd.DataFrame({
    '역할군': ['딜러', '탱커', '컨트롤러'],
    '선택 횟수': [120, 150, 111],
    '승률 (%)': [52, 56, 49],
    '인지도 (%)': [25, 30, 22]
})

st.dataframe(data, use_container_width=True) # 데이터프레임을 보여만 주기

# edited_data = st.data_editor(data) # 데이터프레임을 수정도 가능하게 하기
# st.write(edited_data)

st.bar_chart(data.set_index('역할군')['선택 횟수'])
st.line_chart(data.set_index('역할군')['승률 (%)'])
fig  = data.plot.pie(
    y = '인지도 (%)',
    labels = data['역할군'],
    autopct = '%1.1f%%', # 소수점 첫째 자리까지 나타내기기
    figsize = (6, 6),
    legend = False, # 범례
    title = '역할군 별 인지도'
).get_figure()
st.pyplot(fig)
