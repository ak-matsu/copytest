from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

def get_zodiac(year):
    zodiacs = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    return zodiacs[(year - 4) % 12]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    date_str = request.form['date']
    try:
        if len(date_str) == 8:
            date_obj = datetime.strptime(date_str, '%Y%m%d')
        else:
            date_obj = datetime.strptime(date_str, '%Y/%m/%d')
        weekday = date_obj.strftime('%A')
        zodiac = get_zodiac(date_obj.year)
        result_str = f"{date_str} ({weekday}) - 干支: {zodiac}"
        return jsonify(result=result_str)
    except ValueError:
        return jsonify(error="日付の形式が正しくありません。yyyy/mm/dd または yyyymmdd の形式で入力してください。")

if __name__ == '__main__':
    app.run(debug=True)
