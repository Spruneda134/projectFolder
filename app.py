from flask import Flask, render_template, request
#flask run <<< this is to run in terminal

app = Flask(__name__)

def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]


@app.route("/")
def homePage():
    name = "Salvador Pruneda"
    details = readDetails('static/details.txt')
    return render_template('base.html', name= name, aboutMe= details)

@app.route('/user/<name>')
def greet(name):
    return f'<p>Hello, {name}!</p>'

@app.route("/another")
def anotherPage():
    return render_template('another.html')



@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        if request.form['name']:
            name = request.form['name']
            return render_template('base.html', name=name)
    return render_template('form.html', name=name)

#When running this file directly...
if __name__ == "__main__":
    app.run(debug=True, port=2000)