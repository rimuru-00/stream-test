from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    video_url = request.form['video_url']
    return render_template('play.html', video_url=video_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
