from flask import *
from flask_socketio import SocketIO
import analyzer

app = Flask(__name__)
socketio = SocketIO(app, async_mode=None)

result = []

@app.route("/")
def init():
    # value_strをhtml側で使えるようにする
    return render_template('index.html', result=result)

#  action="/input"
@app.route("/input", methods=["GET", "POST"])
def get_form():
    global value_str
    global result
    result = []
    # フォームの値を受け取る
    try:
        value_str = request.form['str']  # name="str"のinputタグの値を取得
    # ページ読み込み時
    except:
        value_str = ""

    # tense_analyze関数の実行
    Analyzer = analyzer.Analyzer()
    value_str = Analyzer.tense_analyze(value_str)

    # 結果をresultに追加
    appendList = []
    if(value_str):
        appendList.append(value_str)
    result.append(appendList)

    # index.html内にて{{ result }}で挿入できる
    return render_template('index.html', result=result)


if __name__ == "__main__":
    # debugはデプロイ時にFalseにする
    socketio.run(app, host='127.0.0.1', port=5000, debug=False)
