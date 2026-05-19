# MBTI 기반 책·영화·진로 추천 Streamlit 코드

```python
import streamlit as st

st.set_page_config(page_title="MBTI 추천 앱", page_icon="📚")

st.title("📚 MBTI 기반 추천 앱")
st.write("MBTI를 선택하면 책, 영화, 진로 정보를 추천해줍니다.")

mbti_data = {
    "INTJ": {
        "books": ["아몬드", "사피엔스"],
        "movies": ["인터스텔라", "이미테이션 게임"],
        "careers": [
            {
                "job": "데이터 분석가",
                "major": "컴퓨터공학과, 통계학과",
                "personality": "논리적이고 분석적인 성격",
                "salary": "평균 연봉 약 5,000만원"
            },
            {
                "job": "연구원",
                "major": "자연과학계열",
                "personality": "집중력이 높고 탐구심이 강함",
                "salary": "평균 연봉 약 4,800만원"
            }
        ]
    },

    "INTP": {
        "books": ["코스모스", "데미안"],
        "movies": ["매트릭스", "인셉션"],
        "careers": [
            {
                "job": "프로그래머",
                "major": "소프트웨어학과",
                "personality": "창의적이고 호기심이 많음",
                "salary": "평균 연봉 약 5,200만원"
            },
            {
                "job": "교수",
                "major": "교육학과",
                "personality": "탐구와 분석을 좋아함",
                "salary": "평균 연봉 약 6,000만원"
            }
        ]
    },

    "ENTJ": {
        "books": ["부의 추월차선", "자기혁명"],
        "movies": ["소셜 네트워크", "아이언맨"],
        "careers": [
            {
                "job": "CEO",
                "major": "경영학과",
                "personality": "리더십이 강하고 목표 지향적",
                "salary": "평균 연봉 약 7,000만원"
            },
            {
                "job": "마케팅 기획자",
                "major": "광고홍보학과",
                "personality": "도전적이고 추진력이 강함",
                "salary": "평균 연봉 약 4,500만원"
            }
        ]
    },

    "ENTP": {
        "books": ["트렌드 코리아", "넛지"],
        "movies": ["업", "레디 플레이어 원"],
        "careers": [
            {
                "job": "광고 기획자",
                "major": "광고홍보학과",
                "personality": "아이디어가 많고 창의적",
                "salary": "평균 연봉 약 4,300만원"
            },
            {
                "job": "창업가",
                "major": "경영학과",
                "personality": "새로운 도전을 즐김",
                "salary": "평균 연봉 약 6,000만원"
            }
        ]
    },

    "INFJ": {
        "books": ["미드나잇 라이브러리", "어린 왕자"],
        "movies": ["코코", "인사이드 아웃"],
        "careers": [
            {
                "job": "상담사",
                "major": "심리학과",
                "personality": "공감 능력이 뛰어남",
                "salary": "평균 연봉 약 4,000만원"
            },
            {
                "job": "작가",
                "major": "문예창작과",
                "personality": "감수성이 풍부함",
                "salary": "평균 연봉 약 3,800만원"
            }
        ]
    },

    "INFP": {
        "books": ["죽고 싶지만 떡볶이는 먹고 싶어", "나미야 잡화점의 기적"],
        "movies": ["라라랜드", "월터의 상상은 현실이 된다"],
        "careers": [
            {
                "job": "디자이너",
                "major": "시각디자인과",
                "personality": "감성적이고 창의적",
                "salary": "평균 연봉 약 4,000만원"
            },
            {
                "job": "작곡가",
                "major": "실용음악과",
                "personality": "예술적 감각이 뛰어남",
                "salary": "평균 연봉 약 4,200만원"
            }
        ]
    },

    "ENFJ": {
        "books": ["미움받을 용기", "리더는 마지막에 먹는다"],
        "movies": ["굿 윌 헌팅", "위대한 쇼맨"],
        "careers": [
            {
                "job": "교사",
                "major": "교육학과",
                "personality": "사람을 이끄는 능력이 좋음",
                "salary": "평균 연봉 약 4,500만원"
            },
            {
                "job": "HR 담당자",
                "major": "경영학과",
                "personality": "소통 능력이 뛰어남",
                "salary": "평균 연봉 약 4,300만원"
            }
        ]
    },

    "ENFP": {
        "books": ["아주 작은 습관의 힘", "역행자"],
        "movies": ["주토피아", "이터널 선샤인"],
        "careers": [
            {
                "job": "유튜버",
                "major": "미디어학과",
                "personality": "활발하고 창의적",
                "salary": "평균 연봉 약 4,500만원"
            },
            {
                "job": "여행 기획자",
                "major": "관광경영학과",
                "personality": "사람 만나는 것을 좋아함",
                "salary": "평균 연봉 약 4,000만원"
            }
        ]
    },

    "ISTJ": {
        "books": ["넛지", "돈의 속성"],
        "movies": ["포레스트 검프", "머니볼"],
        "careers": [
            {
                "job": "공무원",
                "major": "행정학과",
                "personality": "책임감이 강함",
                "salary": "평균 연봉 약 4,200만원"
            },
            {
                "job": "회계사",
                "major": "회계학과",
                "personality": "꼼꼼하고 체계적",
                "salary": "평균 연봉 약 6,000만원"
            }
        ]
    },

    "ISFJ": {
        "books": ["아낌없이 주는 나무", "행복의 기원"],
        "movies": ["원더", "업"],
        "careers": [
            {
                "job": "간호사",
                "major": "간호학과",
                "personality": "배려심이 깊음",
                "salary": "평균 연봉 약 4,500만원"
            },
            {
                "job": "사회복지사",
                "major": "사회복지학과",
                "personality": "도움을 주는 것을 좋아함",
                "salary": "평균 연봉 약 3,500만원"
            }
        ]
    },

    "ESTJ": {
        "books": ["원칙", "성공하는 사람들의 7가지 습관"],
        "movies": ["탑건", "국가대표"],
        "careers": [
            {
                "job": "경영 관리자",
                "major": "경영학과",
                "personality": "리더십과 책임감이 강함",
                "salary": "평균 연봉 약 5,500만원"
            },
            {
                "job": "경찰",
                "major": "경찰행정학과",
                "personality": "원칙을 중요하게 생각함",
                "salary": "평균 연봉 약 4,700만원"
            }
        ]
    },

    "ESFJ": {
        "books": ["관계를 읽는 시간", "타인의 해석"],
        "movies": ["인턴", "겨울왕국"],
        "careers": [
            {
                "job": "승무원",
                "major": "항공서비스학과",
                "personality": "친절하고 사교적",
                "salary": "평균 연봉 약 4,800만원"
            },
            {
                "job": "호텔리어",
                "major": "호텔관광학과",
                "personality": "서비스 정신이 뛰어남",
                "salary": "평균 연봉 약 4,300만원"
            }
        ]
    },

    "ISTP": {
        "books": ["팩트풀니스", "왜 일하는가"],
        "movies": ["분노의 질주", "존 윅"],
        "careers": [
            {
                "job": "정비사",
                "major": "자동차공학과",
                "personality": "손재주가 좋고 실용적",
                "salary": "평균 연봉 약 4,200만원"
            },
            {
                "job": "파일럿",
                "major": "항공운항학과",
                "personality": "침착하고 판단력이 좋음",
                "salary": "평균 연봉 약 7,000만원"
            }
        ]
    },

    "ISFP": {
        "books": ["모모", "달러구트 꿈 백화점"],
        "movies": ["알라딘", "소울"],
        "careers": [
            {
                "job": "플로리스트",
                "major": "원예학과",
                "personality": "감성이 풍부함",
                "salary": "평균 연봉 약 3,500만원"
            },
            {
                "job": "사진작가",
                "major": "사진영상학과",
                "personality": "예술적 감각이 뛰어남",
                "salary": "평균 연봉 약 4,000만원"
            }
        ]
    },

    "ESTP": {
        "books": ["그릿", "부자 아빠 가난한 아빠"],
        "movies": ["베이비 드라이버", "스파이더맨"],
        "careers": [
            {
                "job": "영업 전문가",
                "major": "경영학과",
                "personality": "도전적이고 활동적",
                "salary": "평균 연봉 약 5,000만원"
            },
            {
                "job": "스포츠 코치",
                "major": "체육학과",
                "personality": "에너지가 넘침",
                "salary": "평균 연봉 약 4,200만원"
            }
        ]
    },

    "ESFP": {
        "books": ["멈추면 비로소 보이는 것들", "나는 나로 살기로 했다"],
        "movies": ["맘마미아", "씽"],
        "careers": [
            {
                "job": "방송인",
                "major": "방송연예과",
                "personality": "사람들과 어울리는 것을 좋아함",
                "salary": "평균 연봉 약 5,000만원"
            },
            {
                "job": "이벤트 플래너",
                "major": "관광이벤트학과",
                "personality": "밝고 적극적",
                "salary": "평균 연봉 약 4,000만원"
            }
        ]
    }
}

mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_list)

if selected_mbti:
    data = mbti_data[selected_mbti]

    st.subheader("📖 추천 책")
    for book in data["books"]:
        st.write(f"- {book}")

    st.subheader("🎬 추천 영화")
    for movie in data["movies"]:
        st.write(f"- {movie}")

    st.subheader("💼 추천 진로")

    for career in data["careers"]:
        st.markdown(f"### {career['job']}")
        st.write(f"✔ 적합한 학과: {career['major']}")
        st.write(f"✔ 적합한 성격: {career['personality']}")
        st.write(f"✔ 평균 연봉: {career['salary']}")
        st.write("---")
```

## 실행 방법

1. 파일 이름을 `app.py`로 저장
2. 터미널에서 아래 명령어 실행

```bash
streamlit run app.py
```

## Streamlit Cloud 업로드 방법

1. GitHub에 `app.py` 업로드
2. urlStreamlit Community Cloud[https://share.streamlit.io](https://share.streamlit.io) 접속
3. GitHub 저장소 연결
4. `app.py` 선택 후 Deploy 클릭
