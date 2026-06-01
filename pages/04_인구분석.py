# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="행정구역 인구 분석", layout="wide")

st.title("📊 행정구역별 연령 인구 분석")

# CSV 불러오기
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

# 데이터 준비
ages = age_cols
population = [selected[col] for col in age_cols]

# 데이터 표시
chart_df = pd.DataFrame({
    "나이": ages,
    "인구수": population
})

st.subheader(f"📍 {region} 연령별 인구")

st.dataframe(chart_df)

# 그래프
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(ages, population, marker='o')

ax.set_xlabel("나이")
ax.set_ylabel("인구수")
ax.set_title(f"{region} 연령별 인구 그래프")

plt.xticks(rotation=45)

st.pyplot(fig)
