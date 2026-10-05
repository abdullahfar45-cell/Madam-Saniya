from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

PAGE_STYLE = """
<style>
    * {
        box-sizing: border-box;
    }

    body {
        margin: 0;
        min-height: 100vh;
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #667eea, #764ba2, #ff758c);
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
    }

    .card {
        background: rgba(255, 255, 255, 0.96);
        width: 100%;
        max-width: 450px;
        padding: 35px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0 15px 40px rgba(0,0,0,0.25);
    }

    h1 {
        color: #764ba2;
        margin-bottom: 10px;
    }

    h2 {
        color: #444;
    }

    .intro {
        color: #666;
        font-size: 17px;
        line-height: 1.5;
    }

    .question {
        font-weight: bold;
        color: #444;
        margin-top: 22px;
    }

    input, select, textarea {
        width: 100%;
        padding: 13px;
        border: 2px solid #ddd;
        border-radius: 12px;
        font-size: 16px;
        background: white;
    }

    input:focus, select:focus, textarea:focus {
        outline: none;
        border-color: #764ba2;
    }

    textarea {
        height: 90px;
        resize: none;
    }

    button {
        margin-top: 25px;
        padding: 14px 35px;
        border: none;
        border-radius: 30px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        color: white;
        font-size: 17px;
        font-weight: bold;
        cursor: pointer;
    }

    button:hover {
        transform: scale(1.05);
    }

    .back {
        display: inline-block;
        margin-top: 15px;
        text-decoration: none;
        background: #764ba2;
        color: white;
        padding: 13px 25px;
        border-radius: 25px;
    }

    .answer {
        background: #f5f2ff;
        padding: 12px;
        border-radius: 12px;
        margin: 10px 0;
    }

    .footer {
        margin-top: 25px;
        color: #999;
        font-size: 13px;
    }
</style>
"""


@app.route("/")
def home():
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Madam Saniya 💬</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {PAGE_STYLE}
</head>

<body>

<div class="card">

    <h1>💬 Madam Saniya 💬</h1>

    <h2>When do you wanna talk to me? 😊</h2>

    <p class="intro">
        Hey Madam Saniya! 👋
        <br>
        Pick a day and time when you're free to talk!
    </p>

    <form action="/submit" method="POST">

        <p class="question">📅 What day do you wanna talk?</p>
        <input type="date" name="date" required>

        <p class="question">⏰ What time are you free?</p>
        <input type="time" name="time" required>

        <p class="question">💬 Where do you wanna talk?</p>

        <select name="platform">
            <option>Snapchat</option>
            <option>Instagram</option>
            <option>Discord</option>
            <option>Phone Call</option>
            <option>Other</option>
        </select>

        <p class="question">✨ Anything you wanna tell me?</p>

        <textarea
            name="message"
            placeholder="Write something here..."
        ></textarea>

        <button type="submit">
            Send It 💙
        </button>

    </form>

    <p class="footer">
        Made for Madam Saniya ✨
    </p>

</div>

</body>
</html>
"""


@app.route("/submit", methods=["POST"])
def submit():

    date = escape(request.form.get("date", ""))
    time = escape(request.form.get("time", ""))
    platform = escape(request.form.get("platform", ""))
    message = escape(request.form.get("message", ""))

    return f"""
<!DOCTYPE html>
<html>

<head>
    <title>Madam Saniya 💙</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {PAGE_STYLE}
</head>

<body>

<div class="card">

    <h1>Got it, Madam Saniya! 🎉</h1>

    <h2>Thanks for letting me know 😊</h2>

    <div class="answer">
        📅 <b>Day:</b> {date}
    </div>

    <div class="answer">
        ⏰ <b>Time:</b> {time}
    </div>

    <div class="answer">
        💬 <b>Talk on:</b> {platform}
    </div>

    <div class="answer">
        ✨ <b>Your message:</b><br><br>
        {message if message else "No message"}
    </div>

    <h2>Talk to you soon! 👋</h2>

    <a class="back" href="/">
        ← Go Back
    </a>

</div>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)