import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 한글 깨짐 방지
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

st.title("서울 기온 분석")

# CSV 불러오기
df = pd.read_csv("seoul.csv", encoding='cp949')

# 날짜 변환
df['날짜'] = pd.to_datetime(df['날짜'])

# 필요한 컬럼만 선택
df = df[['날짜', '최고기온(℃)', '최저기온(℃)']]

# 날짜 선택
selected_date = st.date_input(
    "날짜를 선택하세요",
    value=df['날짜'].min()
)

# 선택 날짜 데이터
filtered = df[df['날짜'].dt.date == selected_date]

if not filtered.empty:

    max_temp = filtered['최고기온(℃)'].values[0]
    min_temp = filtered['최저기온(℃)'].values[0]

    st.subheader(f"{selected_date} 기온 정보")
    st.write(f"최고기온: {max_temp}℃")
    st.write(f"최저기온: {min_temp}℃")

    # 그래프 데이터
    x = ['최고기온', '최저기온']
    y = [max_temp, min_temp]

    fig, ax = plt.subplots(figsize=(6,4))

    # 최고기온 그래프
    ax.plot(
        ['최고기온'],
        [max_temp],
        marker='o',
        linewidth=3,
        color='hotpink',
        label='최고기온'
    )

    # 최저기온 그래프
    ax.plot(
        ['최저기온'],
        [min_temp],
        marker='o',
        linewidth=3,
        color='skyblue',
        label='최저기온'
    )

    ax.set_ylabel("기온 (℃)")
    ax.set_title("선택 날짜 기온 그래프")

    # 범례
    ax.legend()

    st.pyplot(fig)

else:
    st.error("해당 날짜의 데이터가 없습니다.")
