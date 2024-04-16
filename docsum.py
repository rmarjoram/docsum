import os
import sqlite3

from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get(".env"),
)

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        UserName = request.form["UserName"]
        UserEmail = request.form["UserEmail"]
        document = request.form["document"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.6,
            messages=[
                {"role": "system","content": "You are a virtual assistant that provides summaries for text that users input. Your output summaries should be less than 500 words and should be provided in bullet points. The summary should include language and terms used within the text that was submitted by the user."},
                {"role": "user", "content": document}
            ]
        )
        docSum = response.choices[0].message.content
        conn = get_db_connection()
        conn.execute("INSERT INTO user (UserName, UserEmail) VALUES (?, ?)",
                     (UserName, UserEmail))
        conn.execute("INSERT INTO document (docInput, docSum) VALUES (?, ?)",
                     (document, docSum))
        conn.commit()
        conn.close()
        return redirect(url_for("index", result=docSum))

    result = request.args.get("result")
    return render_template("index.html", result=result)
