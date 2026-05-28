# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="국가별 MBTI 분석",
    layout="centered"
)

st.title("🌍 국가별 MBTI 비율 분석기")

# CSV 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# 국가 선택
country = st.selectbox(
    "국가를 선택하세요",
    df["Country"]
)

# 선택한 국가 데이터
selected_row = df[df["Country"] == country].iloc[0]

# MBTI 데이터만 추출
mbti_data = selected_row.drop("Country")

# 내림차순 정렬
mbti_data = mbti_data.sort_values(ascending=False)

# 색상 만들기
colors = []

for i in range(len(mbti_data)):
    # 1등 MBTI → 노란색
    if i == 0:
        colors.append("yellow")
    else:
        # 초록색 그라데이션
        green_value = 0.9 - (i * 0.04)

        if green_value < 0.2:
            green_value = 0.2

        colors.append((0.2, green_value, 0.2))

# 그래프 생성
fig, ax = plt.subplots(figsize=(11, 5))

bars = ax.bar(
    mbti_data.index,
    mbti_data.values,
    color=colors
)

# 제목
ax.set_title(
    f"{country}의 MBTI 비율",
    fontsize=18
)

# 축 이름
ax.set_xlabel("MBTI 유형")
ax.set_ylabel("비율")

# x축 회전
plt.xticks(rotation=45)

# 값 표시
for i, value in enumerate(mbti_data.values):
    ax.text(
        i,
        value + 0.002,
        f"{value:.2%}",
        ha="center",
        fontsize=8
    )

# 스트림릿 출력
st.pyplot(fig)

# 가장 높은 MBTI 표시
top_mbti = mbti_data.index[0]

st.subheader("🏆 가장 높은 MBTI")
st.success(f"{country}에서 가장 높은 MBTI는 {top_mbti} 입니다!")
