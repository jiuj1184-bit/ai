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

# 숫자형 변환
mbti_data = pd.to_numeric(mbti_data)

# 내림차순 정렬
mbti_data = mbti_data.sort_values(ascending=False)

# 색상 설정
colors = []

for i in range(len(mbti_data)):
    if i == 0:
        colors.append("yellow")
    else:
        green = 0.9 - (i * 0.04)

        if green < 0.2:
            green = 0.2

        colors.append((0.2, green, 0.2))

# 그래프 생성
fig, ax = plt.subplots(figsize=(11, 5))

ax.bar(
    mbti_data.index,
    mbti_data.values,
    color=colors
)

# 제목
ax.set_title(f"{country}의 MBTI 비율")

# 축
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

# 출력
st.pyplot(fig)

# 가장 높은 MBTI
top_mbti = mbti_data.index[0]

st.subheader("🏆 가장 높은 MBTI")
st.success(f"{country}에서 가장 높은 MBTI는 {top_mbti} 입니다!")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="MBTI 국가 순위 분석",
    layout="centered"
)

st.title("🌍 MBTI 유형별 국가 TOP 10")

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# MBTI 목록
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI 선택
selected_mbti = st.selectbox(
    "MBTI 유형을 선택하세요",
    mbti_list
)

# 선택한 MBTI 기준 정렬
top10 = df[["Country", selected_mbti]].sort_values(
    by=selected_mbti,
    ascending=False
).head(10)

# 색상 설정
colors = []

for i in range(len(top10)):
    # 1등 → 노랑
    if i == 0:
        colors.append("yellow")
    else:
        # 초록 그라데이션
        green = 0.9 - (i * 0.07)

        if green < 0.2:
            green = 0.2

        colors.append((0.2, green, 0.2))

# 그래프 생성
fig, ax = plt.subplots(figsize=(11, 6))

bars = ax.bar(
    top10["Country"],
    top10[selected_mbti],
    color=colors
)

# 제목
ax.set_title(
    f"{selected_mbti} 비율이 높은 나라 TOP 10",
    fontsize=18
)

# 축 이름
ax.set_xlabel("국가")
ax.set_ylabel("비율")

# x축 회전
plt.xticks(rotation=45)

# 값 표시
for i, value in enumerate(top10[selected_mbti]):
    ax.text(
        i,
        value + 0.002,
        f"{value:.2%}",
        ha="center",
        fontsize=9
    )

# 출력
st.pyplot(fig)

# 1위 국가 표시
top_country = top10.iloc[0]["Country"]

st.subheader("🏆 1위 국가")
st.success(
    f"{selected_mbti} 비율이 가장 높은 나라는 {top_country} 입니다!"
)
