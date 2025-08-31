from flask import Flask, render_template
from visualization import (
    generate_rating_pie,
    generate_genre_bar,
    generate_country_bar
)

app = Flask(__name__)

# ✅ 首頁
@app.route('/')
def home():
    return render_template('index.html')

# ✅ Rating 主頁：只顯示前五類 + Other 的圓餅圖
@app.route('/rating')
def rating():
    chart_html = generate_rating_pie()
    return render_template('rating.html', chart=chart_html)

# ✅ Genre 主頁：Top 15 長條圖
@app.route('/genre')
def genre():
    chart_html = generate_genre_bar()
    return render_template('genre.html', chart=chart_html)

# ✅ Country 主頁：Top 15 製作地區 bar chart
@app.route('/country')
def country():
    chart_html = generate_country_bar()
    return render_template('country.html', chart=chart_html)

# ✅ 啟動 Flask
if __name__ == '__main__':
    app.run(debug=True)