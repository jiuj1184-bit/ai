import streamlit as st

# 제목
st.title("🍽 소스 조합 추천 앱")

# 소스 조합 데이터
pairing_data = {

    "연어": {
        "소스": ["레몬버터소스", "피치소스"],
        "허브": ["딜", "차이브"],
        "플레이팅": ["레몬", "허브오일"]
    },

    "관자": {
        "소스": ["버터소스", "크림소스"],
        "허브": ["차이브", "파슬리"],
        "플레이팅": ["콜리플라워 퓌레", "허브오일"]
    },

    "문어": {
        "소스": ["먹물소스", "토마토소스"],
        "허브": ["바질", "파슬리"],
        "플레이팅": ["감자퓌레", "파프리카"]
    },

    "새우": {
        "소스": ["비스크소스", "레몬크림소스"],
        "허브": ["딜", "바질"],
        "플레이팅": ["레몬", "오일파우더"]
    }
}

# 사용자 입력
ingredient = st.text_input("재료를 입력하세요")

# 버튼
if st.button("추천 받기"):

    if ingredient in pairing_data:

        st.subheader("추천 소스")

        for sauce in pairing_data[ingredient]["소스"]:
            st.write("•", sauce)

        st.subheader("추천 허브")

        for herb in pairing_data[ingredient]["허브"]:
            st.write("•", herb)

        st.subheader("플레이팅 추천")

        for plating in pairing_data[ingredient]["플레이팅"]:
            st.write("•", plating)

    else:
        st.error("추천 데이터가 없습니다.")
