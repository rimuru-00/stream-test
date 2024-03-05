from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/play', methods=['GET'])
def play():
    video_source = request.args.get('video_source')
    return render_template('play.html', video_source=video_source)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
