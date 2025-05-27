# web_app.py
# 🛰️ Web interface using Flask to translate to/from Morse code.
# 🕵️‍♂️ Includes theme switcher and audio playback for encoding messages.

from flask import Flask, request, render_template_string
from translator import lettersToMorseCode, morseCodeToLetters

app = Flask(__name__)

# ⚠️ HTML template with theme switcher, star background, and sound player
HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>R2-D2 Morse Code Translator</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');

    :root {
      --bg-color: #000;
      --text-color: #FFE81F;
      --btn-bg: #222;
      --btn-text: #FFE81F;
      --btn-border: #FFE81F;
      --result-bg: rgba(255, 255, 255, 0.05);
      --footer-color: #888;
    }

    body.light {
      --bg-color: #f4f4f4;
      --text-color: #111;
      --btn-bg: #fff;
      --btn-text: #111;
      --btn-border: #111;
      --result-bg: rgba(0, 0, 0, 0.05);
      --footer-color: #333;
    }

    body {
      font-family: 'Orbitron', sans-serif;
      background: var(--bg-color);
      color: var(--text-color);
      margin: 0;
      padding: 0;
      overflow: hidden;
    }

    canvas#stars {
      position: fixed;
      top: 0;
      left: 0;
      z-index: -1;
    }

    .container {
      text-align: center;
      padding: 4em 2em;
      position: relative;
      z-index: 1;
    }

    h2 {
      font-size: 2.2em;
      margin-bottom: 0.5em;
      text-shadow: 0 0 10px var(--text-color);
    }

    input[type="text"] {
      width: 60%;
      padding: 10px;
      font-size: 1em;
      margin-bottom: 1em;
      border: none;
      border-radius: 5px;
    }

    button {
      background-color: var(--btn-bg);
      color: var(--btn-text);
      border: 2px solid var(--btn-border);
      padding: 10px 20px;
      margin: 5px;
      font-size: 1em;
      cursor: pointer;
      border-radius: 4px;
    }

    button:hover {
      background-color: var(--btn-text);
      color: var(--btn-bg);
    }

    .result {
      margin-top: 2em;
      padding: 1em;
      border: 1px dashed var(--text-color);
      background-color: var(--result-bg);
      width: 80%;
      margin-left: auto;
      margin-right: auto;
    }

    .theme-switcher {
      position: absolute;
      top: 20px;
      right: 20px;
    }

    footer {
      margin-top: 3em;
      font-size: 0.9em;
      color: var(--footer-color);
    }
  </style>
</head>
<body>
  <canvas id="stars"></canvas>

  <div class="theme-switcher">
    <button id="theme-toggle" type="button">🌓 Switch Theme</button>
  </div>

  <div class="container">
    <h2>🛰️ R2-D2 Morse Code Translator</h2>
    <form method="post">
      <input type="text" name="text" placeholder="Enter your secret message here..." required>
      <br>
      <button type="submit" name="action" value="encode">Encode</button>
      <button type="submit" name="action" value="decode">Decode</button>
    </form>

    {% if result %}
    <div class="result">
      <h3>🔎 Translation:</h3>
      <p id="morse">{{ result }}</p>
    </div>
    {% endif %}

    <footer>
      Made for the Resistance • May the Code be with you ✨
    </footer>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // ⭐ Animated stars
      const canvas = document.getElementById('stars');
      const ctx = canvas.getContext('2d');
      let stars = [], numStars = 100;

      function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
      }

      function createStars() {
        stars = [];
        for (let i = 0; i < numStars; i++) {
          stars.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            size: Math.random() * 1.5,
            speed: Math.random() * 0.5 + 0.2
          });
        }
      }

      function drawStars() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = 'white';
        stars.forEach(star => {
          ctx.beginPath();
          ctx.arc(star.x, star.y, star.size, 0, 2 * Math.PI);
          ctx.fill();
          star.y += star.speed;
          if (star.y > canvas.height) {
            star.y = 0;
            star.x = Math.random() * canvas.width;
          }
        });
      }

      function animate() {
        drawStars();
        requestAnimationFrame(animate);
      }

      resize();
      createStars();
      animate();
      window.addEventListener('resize', () => {
        resize();
        createStars();
      });

      // 🌓 Theme toggle
      const themeButton = document.querySelector('#theme-toggle');
      const body = document.body;
      const savedTheme = localStorage.getItem('theme');
      if (savedTheme === 'light') {
        body.classList.add('light');
      }

      themeButton.addEventListener('click', () => {
        body.classList.toggle('light');
        const isLight = body.classList.contains('light');
        localStorage.setItem('theme', isLight ? 'light' : 'dark');
      });

      // 🔊 Sound player for Morse code
      const encodeBtn = document.querySelector('button[name="action"][value="encode"]');
      encodeBtn.addEventListener('click', () => {
        setTimeout(() => {
          const text = document.querySelector('#morse')?.innerText;
          if (!text) return;
          const context = new (window.AudioContext || window.webkitAudioContext)();
          let t = context.currentTime;

          for (const c of text) {
            if (c === '.') {
              beep(context, t, 0.1);
              t += 0.2;
            } else if (c === '-') {
              beep(context, t, 0.3);
              t += 0.4;
            } else {
              t += 0.2;
            }
          }
        }, 200);
      });

      function beep(context, time, duration) {
        const oscillator = context.createOscillator();
        const gainNode = context.createGain();
        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(700, time);
        gainNode.gain.setValueAtTime(0.5, time);
        oscillator.connect(gainNode);
        gainNode.connect(context.destination);
        oscillator.start(time);
        oscillator.stop(time + duration);
      }
    });
  </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    # 🧠 Decode incoming request
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        action = request.form["action"]
        # 📨 Handle encode or decode
        if action == "encode":
            result = lettersToMorseCode(text)
        elif action == "decode":
            result = morseCodeToLetters(text)
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    # 🧪 Fire up Flask locally
    app.run(debug=True)
