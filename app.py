from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def inicial():
    return render_template('index.html')


@app.route('/soma')
def somar():
    numero1 = request.form['num']
    numero2 = request.form['nu']
    soma = numero1 + numero2
    return render_template('index.html', resultado = soma)
        
app.run(debug=True)
