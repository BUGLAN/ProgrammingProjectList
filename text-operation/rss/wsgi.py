from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('rss.html')


@app.route('/rss-lists')
def rss_lists():
    return 'rss lists'


if __name__ == "__main__":
    app.run(debug=True)
