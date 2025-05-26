# web_app.py
# Web interface using Flask.
# Perfect for interplanetary browser-based translations.
from flask import Flask, request, render_template_string
from translator import lettersToMorseCode, morseCodeToLetters

app = Flask(__name__)
#  Simple HTML for encode/decode interface
HTML = """
<!DOCTYPE html>
<html>
<head><title>R2-D2 Translator</title></head>
<body style="font-family:sans-serif;">
  <h2>🛰️ Morse Code Translator</h2>
  <form method="post">
    <input name="text" placeholder="Enter message" size="40">
    <button name="action" value="encode">Encode</button>
    <button name="action" value="decode">Decode</button>
  </form>
  {% if result %}
  <h3>🔎 Result:</h3>
  <p>{{ result }}</p>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        action = request.form["action"]
        if action == "encode":
            result = lettersToMorseCode(text)
        elif action == "decode":
            result = morseCodeToLetters(text)
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
