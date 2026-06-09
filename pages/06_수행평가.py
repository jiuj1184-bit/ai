from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# 공공데이터 엑셀 파일 불러오기
df = pd.read_excel("식품의약품안전처_가공식품 품목별 영양성분 DB_20221231.xlsx")

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
        "허브": ["파슬리", "바질"],
        "플레이팅": ["감자퓌레", "파프리카"]
    },

    "새우": {
        "소스": ["비스크소스", "레몬크림소스"],
        "허브": ["바질", "딜"],
        "플레이팅": ["레몬", "오일파우더"]
    }
}


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        ingredient = request.form["ingredient"]

        if ingredient in pairing_data:
            result = pairing_data[ingredient]

        else:
            result = {
                "소스": ["추천 데이터 없음"],
                "허브": ["추천 데이터 없음"],
                "플레이팅": ["추천 데이터 없음"]
            }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
  <!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <title>소스 조합 추천 앱</title>

    <style>

        body{
            font-family: Arial;
            background-color: #f5f5f5;
            text-align: center;
            padding: 50px;
        }

        h1{
            color: #333;
        }

        input{
            padding: 10px;
            width: 250px;
        }

        button{
            padding: 10px 20px;
            cursor: pointer;
        }

        .box{
            background: white;
            padding: 20px;
            border-radius: 10px;
            width: 400px;
            margin: auto;
            margin-top: 30px;
        }

    </style>

</head>

<body>

    <h1>🍽 소스 조합 추천 앱</h1>

    <form method="POST">

        <input type="text" 
               name="ingredient" 
               placeholder="재료 입력 예: 연어">

        <button type="submit">추천 받기</button>

    </form>

    {% if result %}

    <div class="box">

        <h2>추천 소스</h2>

        <ul>
            {% for item in result["소스"] %}
            <li>{{ item }}</li>
            {% endfor %}
        </ul>

        <h2>추천 허브</h2>

        <ul>
            {% for item in result["허브"] %}
            <li>{{ item }}</li>
            {% endfor %}
        </ul>

        <h2>플레이팅 추천</h2>

        <ul>
            {% for item in result["플레이팅"] %}
            <li>{{ item }}</li>
            {% endfor %}
        </ul>

    </div>

    {% endif %}

</body>

</html>
