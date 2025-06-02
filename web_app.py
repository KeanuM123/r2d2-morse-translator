# web_app.py
# 🛰️ Web interface using Flask to translate to/from Morse code.
# 🕵️‍♂️ Includes theme switcher and audio playback for encoding messages.

from flask import Flask, request, render_template_string
from translator import lettersToMorseCode, morseCodeToLetters

app = Flask(__name__)

# ⚠️ HTML template with theme switcher, star background, and sound player
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>R2-D2 Morse Code Translator</title>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap" rel="stylesheet">
  <style>
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
    <button id="theme-toggle">🌓 Switch Theme</button>
  </div>

  <div class="container">
    <h2>🛰️ R2-D2 Morse Code Translator</h2>
    <form method="post">
      <input type="text" name="text" placeholder="Enter your secret message here..." required>
      <br>
      <button name="action" value="encode">Encode</button>
      <button name="action" value="decode">Decode</button>
      <button type="button" id="play-sound">🔊 Play Sound</button>
    </form>

    {% if result %}
    <div class="result">
      <h3>🔎 Translation:</h3>
      <p>{{ result }}</p>
    </div>
    {% endif %}

    <footer>
      Made for the Resistance • May the Code be with you ✨
    </footer>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
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

      window.addEventListener('resize', () => {
        resize();
        createStars();
      });

      resize();
      createStars();
      animate();

      // Theme Toggle
      const themeButton = document.getElementById('theme-toggle');
      const body = document.body;
      const savedTheme = localStorage.getItem('theme');
      if (savedTheme === 'light') body.classList.add('light');

      themeButton.addEventListener('click', () => {
        body.classList.toggle('light');
        localStorage.setItem('theme', body.classList.contains('light') ? 'light' : 'dark');
      });

      // Play Sound
      const playButton = document.getElementById('play-sound');
      const resultElement = document.querySelector('.result p');

      playButton.addEventListener('click', () => {
        if (!resultElement) return;
        const morseCode = resultElement.textContent.trim();
        playMorseCode(morseCode);
      });

      function playMorseCode(morse) {
        const unit = 100;
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        let time = audioCtx.currentTime;

        for (let char of morse) {
          switch (char) {
            case '.':
              beep(audioCtx, time, unit);
              time += unit / 1000 + 0.1;
              break;
            case '-':
              beep(audioCtx, time, unit * 3);
              time += (unit * 3) / 1000 + 0.1;
              break;
            case ' ':
              time += (unit * 3) / 1000;
              break;
            case '/':
              time += (unit * 7) / 1000;
              break;
          }
        }
      }

      function beep(audioCtx, time, duration) {
        const oscillator = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();
        oscillator.connect(gainNode);
        gainNode.connect(audioCtx.destination);
        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(600, time);
        gainNode.gain.setValueAtTime(1, time);
        gainNode.gain.exponentialRampToValueAtTime(0.0001, time + duration / 1000);
        oscillator.start(time);
        oscillator.stop(time + duration / 1000);
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
