import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("기온 분석")

# CSV 읽기

df = pd.read_csv("seoul.csv", encoding="cp949")

# 날짜 변환

df['날짜'] = pd.to_datetime(df['날짜'])

# 날짜 선택

selected_date = st.date_input(
"날짜 선택",
value=df['날짜'].min()
)

# 선택한 날짜 데이터

filtered = df[df['날짜'].dt.date == selected_date]

if not filtered.empty:

```
max_temp = filtered['최고기온(℃)'].values[0]
min_temp = filtered['최저기온(℃)'].values[0]

st.write(f"최고기온: {max_temp}℃")
st.write(f"최저기온: {min_temp}℃")

# 그래프 생성
fig = go.Figure()

# 최고기온
fig.add_trace(
    go.Scatter(
        x=["최고기온"],
        y=[max_temp],
        mode='lines+markers',
        name='최고기온',
        line=dict(color='hotpink', width=4)
    )
)

# 최저기온
fig.add_trace(
    go.Scatter(
        x=["최저기온"],
        y=[min_temp],
        mode='lines+markers',
        name='최저기온',
        line=dict(color='skyblue', width=4)
    )
)

# 레이아웃
fig.update_layout(
    title="선택 날짜 기온 그래프",
    xaxis_title="기온 종류",
    yaxis_title="기온(℃)",
    legend_title="범례"
)

st.plotly_chart(fig)
```

else:
st.error("해당 날짜 데이터가 없습니다.")
