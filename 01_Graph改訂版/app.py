# 参考: https://www.python.ambitious-engineer.com/archives/1630
# 参考: https://note.com/kamakiriphysics/n/n2aec5611af2a
# 参考:  https://qiita.com/Gen6/items/2979b84797c702c858b1

import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, g, flash
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

SAVE_DIR = "graph"
if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

@app.route('/graph/<path:filepath>')
def send_js(filepath):
    return send_from_directory(SAVE_DIR, filepath)

@app.route("/", methods=["GET","POST"])
def upload_file():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":

        # csv ファイルを DataFrame に読み込み
        csv = request.files['csv']
        if csv:
            df = pd.read_csv(csv)
        else: # エラー処理
            return render_template("index.html", err_message_1="ファイルを選択してください！")

        kind = request.form.get('kind')
        if kind:
            if kind == "other":
                return render_template("index.html", err_message_2="グラフの種類を選択してください！")
            else:
                if kind == "pairplot":
                    # sns で描画
                    sns_plot_1 = sns.pairplot(df, hue ="label")
                    # ユニークなグラフ画像名を生成
                    filepath_1 = "./graph/" + datetime.now().strftime("%Y%m%d%H%M%S_") + "graph1.png"
                    # グラフ画像を保存
                    sns_plot_1.savefig(filepath_1)
                    return render_template("index.html", csv=csv, filepath_1=filepath_1)
                
                elif kind == "lmplot":
                    sns_plot_2 = sns.lmplot(x="a1", y="a4", data=df, hue="label")
                    filepath_2 = "./graph/" + datetime.now().strftime("%Y%m%d%H%M%S_") + "graph2.png"
                    sns_plot_2.savefig(filepath_2)
                    return render_template("index.html", csv=csv, filepath_2=filepath_2)
                
                elif kind == "violin":
                    plt.figure(figsize=(10, 6))
                    sns.violinplot(x="label", y="a3", data=df)
                    filepath_3 = "./graph/" + datetime.now().strftime("%Y%m%d%H%M%S_") + "graph3.png"
                    plt.savefig(filepath_3)
                    return render_template("index.html", csv=csv, filepath_3=filepath_3)

                
        else: # エラー処理
            return render_template("index.html", err_message_2="グラフの種類を選択してください！")

if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0', port=5554) # ポートの変更
