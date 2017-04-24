import flask
import sort
app = flask.Flask(__name__)

@app.route('/')
def render():
    return flask.render_template('index.html')

@app.route('/', methods=['POST'])
def formpost():

    text = flask.request.form['numbers']
    a = map(int, text.split(','))

    sort.sort(a)

    return flask.render_template('index.html', a=a)

if __name__ == "__main__":
    app.run()