from flask import Flask, render_template
from classes.curso import Curso

app = Flask(__name__)

@app.route('/')
def index():
    titulo = 'Página inicial'
    conteudo = 'Criando páginas dinamicas'
    return render_template("index.html", titulo=titulo, conteudo=conteudo)

@app.route('/cursos')
def cursos():
    lista_de_cursos = ['Curso de HTML5 com CSS3', 'Programação Orientada a Objetos']
    return render_template("cursos.html", lista=lista_de_cursos)

@app.route('/curso/<nome>')
def curso_por_nome(nome):

    if nome == 'html':
        info = Curso("Curso de HTML e CSS3", "Disciplina que lida com devweb")
        habilidades = ['HTML', 'CSS', 'JAVASCRIPT']
        return render_template("info_curso.html", objeto=info, habilidades=habilidades, dificuldade=1)
    elif nome == 'poo':
        info = Curso("Programação Orientada a Objetos", "Disciplina que lida com o paradigma de objetos")
        habilidades = ['Dicionários', 'Tratamento de exceções', 'Classes', 'Herança']
        return render_template("info_curso.html", objeto=info, habilidades=habilidades, dificuldade=3)
    else:
        return "Curso inexistente"
    
if __name__ == '__main__':
    app.run(debug=True)