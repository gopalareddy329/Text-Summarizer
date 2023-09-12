from flask import Flask, render_template, request
from summarizer import Summarizer



app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    model=Summarizer()
    if request.method == 'POST':
        document = request.form['document']
        if document is not None:
            content = document
            summary = model(content)

    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
