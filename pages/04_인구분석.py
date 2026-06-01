import streamlit as st
import pandas as pd

st.set_page_config(page_title="인구 분석", layout="wide")

st.title("📊 행정구역별 연령 인구 분석")

# CSV 읽기

df = pd.read_csv("population.csv", encoding="euc-kr")

# 숫자 변환

for col in df.columns[1:]:
df[col] = (
df[col]
.astype(str)
.str.replace(",", "", regex=False)
.astype(int)
)

# 연령 컬럼

age_cols = [
'0~9세',
'_10~19세',
'20~29세',
'30~39세',
'40~49세',
'50~59세',
'60~69세',
'70~79세',
'0~89세',
'100세 이상'
]

# 행정구역 선택

region = st.selectbox(
"행정구역 선택",
df["행정구역"]
)

# 선택 데이터

selected = df[df["행정구역"] == region].iloc[0]

# 그래프용 데이터

chart_df = pd.DataFrame({
"나이": age_cols,
"인구수": [selected[col] for col in age_cols]
})

st.subheader(f"{region} 연령별 인구수")

# 표 출력

st.dataframe(chart_df)

# 꺾은선 그래프

st.line_chart(
chart_df,
x="나이",
y="인구수"
)
