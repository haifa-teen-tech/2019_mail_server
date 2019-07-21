from flask import Flask, request
import smtplib, ssl


username = "bottorobotto1337"
password = "IAmBottoRobotto" # It's fine because we just use a dumb shit account. No one really cares about it

port = 465
url = "smtp.gmail.com"

sender = "bottorobotto1337@gmail.com"


app = Flask(__name__)


@app.route("/send/<to>/<title>", methods=["POST"])
def _send(to, title):
    try:
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(url, port, context=context) as server:
            server.login(username, password)

            server.sendmail(sender, to, request.data)

        return "ok"
    except:
        return "error"

app.run(port=8080)
