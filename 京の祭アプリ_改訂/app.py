# 参考: https://stackoverflow.com/questions/37379374/insert-the-folium-maps-into-the-jinja-template
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, g, flash

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def main():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        matsuri = request.form['matsuri']

        if matsuri == "祇園祭先祭":
            url = "https://www.youtube.com/embed/8-P2_i1A1vc"
            url2 = "https://youtu.be/8-P2_i1A1vc"
        elif matsuri == "祇園祭後祭":
            url = "https://www.youtube.com/embed/bJApl-iKEvE"
            url2 = "https://youtu.be/bJApl-iKEvE"
        elif matsuri == "時代祭":
            url = "https://www.youtube.com/embed/0mUEP6J-320"
            url2 = "https://youtu.be/0mUEP6J-320"
        elif matsuri == "葵祭":
            url = "https://www.youtube.com/embed/vM-usKjMAhE"
            url2 = "https://youtu.be/vM-usKjMAhE"
        elif matsuri == "鞍馬の火祭":
            url = "https://www.youtube.com/embed/wvD9bfcmC8M"
            url2 = "https://youtu.be/wvD9bfcmC8M"
        elif matsuri == "曲水の宴":
            url = "https://www.youtube.com/embed/cDS6mgnOzvw"
            url2 = "https://youtu.be/cDS6mgnOzvw"
        elif matsuri == "送り火":
            url = "https://www.youtube.com/embed/qJpnGplnI4o"
            url2 = "https://youtu.be/qJpnGplnI4o"
        elif matsuri == "みたらし祭":
            url = "https://www.youtube.com/embed/IBQMdLQJUF0"
            url2 = "https://youtu.be/IBQMdLQJUF0"
        else:
            url = "https://e-shoei.com"
            url2 = "https://youtu.be/"

        return  render_template("index.html", 
            matsuri=matsuri, 
            url=url,
            url2=url2
            )
    
if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0', port=7777) # ポートの変更
