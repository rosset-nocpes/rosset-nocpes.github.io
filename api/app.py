from flask import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('soon.html')


@app.errorhandler(404)
def error(e):
    return render_template('error_404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
