import string
import flask

app = flask.Flask(__name__)

@app.route('/')
def myform():
    return flask.render_template('index.html')

@app.route('/', methods=['POST'])
def myformpost():

    text1 = flask.request.form['text1']
    text2 = flask.request.form['text2']
    plagiarism = checker(text1, text2)
    if plagiarism:
        return "<h1> Detected </h1>"
    else:
        return "<h1> Not Detected </h1>"


def checker(text1, text2):
    cleanchar = string.letters + string.digits + "- "
    cleanstring1 = filter(lambda c: c in cleanchar, text1)
    cleanstring2 = filter(lambda c: c in cleanchar, text2)

    cleanstring1 = cleanstring1.split()
    cleanstring2 = cleanstring2.split()

    if "is" in cleanstring1 : cleanstring1.remove("is")
    if "the" in cleanstring1 : cleanstring1.remove("the")
    if "a" in cleanstring1 : cleanstring1.remove("a")
    if "in" in cleanstring1 : cleanstring1.remove("in")

    if "is" in cleanstring2 : cleanstring2.remove("is")
    if "the" in cleanstring2 : cleanstring2.remove("the")
    if "a" in cleanstring2 : cleanstring2.remove("a")
    if "in" in cleanstring2 : cleanstring2.remove("in")

    wordsCopied = len(set(cleanstring1) & set(cleanstring2))
    smallerLength = 0

    if len(cleanstring1) <= len(cleanstring2):
        smallerLength = len(cleanstring1)
    else:
        smallerLength = len(cleanstring2)

    if wordsCopied >= (0.5 * smallerLength):
        return True

    return False



if __name__ == '__main__':
    app.run()