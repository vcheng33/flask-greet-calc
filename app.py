from flask import Flask, request

app = Flask(__name__)

@app.get("/welcome")
def welcome_message():
    """ Returns "welcome" html """
    return """
    <html>
        <title>Welcome Message</title>
        <body>
            <h1>Welcome</h1>
        </body>
    </html>
    """