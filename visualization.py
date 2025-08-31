import pandas as pd
import plotly.express as px

# ✅ 資料路徑
DATA_PATH = r"C:\Users\hanso\OneDrive\桌面\工作實習\AI與機器人學習\NETFLIX_data.csv"

# ✅ Rating 主頁：圓餅圖（固定前五類 + Other）
def generate_rating_pie():
    df = pd.read_csv(DATA_PATH)
    rating_counts = df['rating'].value_counts()

    top_ratings = rating_counts.head(5)
    other_count = rating_counts.iloc[5:].sum()

    pie_df = pd.concat([top_ratings, pd.Series({'Other': other_count})])
    fig = px.pie(
        pie_df,
        names=pie_df.index,
        values=pie_df.values,
        title="Distribution of Ratings"
    )
    fig.update_traces(
    textinfo='percent+label',
    textposition='outside',
    textfont=dict(size=14),
    insidetextorientation='radial'  # ✅ 避免文字被截斷或壓縮
    )
    fig.update_layout(width=700, height=500, font=dict(size=16))
    return fig.to_html(full_html=False)

def generate_genre_bar():
    df = pd.read_csv(DATA_PATH)

    # 🔍 拆解 listed_in 並統計 genre 數量（避免重複 label）
    df['listed_in'] = df['listed_in'].str.split(', ')
    genre_list = df.explode('listed_in')
    genre_counts = genre_list['listed_in'].value_counts().nlargest(15)

    # ✂️ 限制 label 長度，避免偏右排版
    short_labels = [label[:25] + '...' if len(label) > 25 else label for label in genre_counts.index]

    # 📊 建立 bar chart
    fig = px.bar(
        x=short_labels,
        y=genre_counts.values,
        color=short_labels,
        title="Top 15 Genres",
        color_discrete_sequence=px.colors.qualitative.Set3,
        text=genre_counts.values  # ✅ 直接在 px.bar 裡加 text，避免重複標示
    )

    # 🎨 視覺優化：居中排版、避免 label 重疊
    fig.update_layout(
        xaxis_title='Genre',
        yaxis_title='Number of Titles',
        width=1000,  # ✅ 稍微縮小寬度，讓圖表更居中
        height=600,
        font=dict(size=16),
        showlegend=False,
        xaxis_tickangle=-30,
        margin=dict(l=80, r=80, t=80, b=80)  # ✅ 左右邊界平衡
    )

    fig.update_traces(textposition='outside')  # ✅ 單一數字標示在 bar 外部

    return fig.to_html(full_html=False)

# ✅ Country 主頁：Top 15 製作地區 bar chart（加防呆）
def generate_country_bar():
    df = pd.read_csv(DATA_PATH)
    df = df.dropna(subset=['country'])
    country_counts = df['country'].value_counts().nlargest(15)

    fig = px.bar(
        country_counts,
        x=country_counts.values,
        y=country_counts.index,
        orientation='h',
        color=country_counts.index,  # ✅ 每個 country 不同顏色
        title="Top 15 Production Countries",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig.update_layout(
        xaxis_title='Number of Titles',
        yaxis_title='Country',
        width=900,
        height=600,
        font=dict(size=16),
        showlegend=False
    )
    return fig.to_html(full_html=False)