from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/saudacao')
def saudacao():
    return render_template("saudacao.html")

@app.route('/cursos')
def curso():
    return render_template("cursos.html")

@app.route('/cursos/<nome>')
def curso_com_nome(nome):
    if nome == 'devweb':
        return render_template("curso_devweb.html")
    elif nome == 'poo':
        return render_template("curso_poo.html")
    else:
        return "Curso inexistente"

@app.route('/curso/<nome>/<ano>')
def curso_com_dois_paramentros(nome, ano):
    return (f'Rota de demosnração que receebe dois valores: nome={nome} e ano={ano}')

if __name__ == '__main__':
    app.run(debug=True)