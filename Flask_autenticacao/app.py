from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'SENHA-MUITO-SECRETA' 
#Colocar uma senha dificil, com letras maiusculas e numeros

@app.route('/exemplo_get')
def exemplo_get():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    if usuario and senha:
        return (f"Os dados recebidos são: usuário = {usuario} e senha = {senha}")
    else:
        return render_template("exemplo_get.html")

@app.route('/exemplo_post', methods=["GET", "POST"])
def exemplo_post():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario and senha:
        return (f"Os dados recebidos são: usuário = {usuario} e senha = {senha}")
    else:   
        return render_template("exemplo_post.html")
    
@app.route('/login', methods=["GET", "POST"])
def login():
    msg_erro = ''
    if request.method == "POST":
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        if usuario == 'João' and senha == '1234':
            session['usuario'] = 'João'
            return redirect('/area_logada')
        elif usuario == 'Camila' and senha == '4321':
            session['usuario'] = 'Camila'
            return redirect('/area_logada')
        else:
            msg_erro = 'Usuário ou senha incorretos'
    return render_template("login.html", erro=msg_erro)

@app.route('/area_logada')
def area_logada():
    if 'usuario' in session:
        nome_pessoa =''
        media_pessoa = 0.0
        if session['usuario'] == 'João':
            nome_pessoa = 'João Rafael'
            media_pessoa = 7.5
        elif session['usuario'] == 'Camila':
            nome_pessoa = 'Camila Maria'
            media_pessoa = 9.5
        return render_template('Area_logada.html', nome=nome_pessoa, media=media_pessoa)
    else:
        return redirect('/login')
    
@app.route('/sair')
def sair():
    session.clear()
    return redirect('/login')
    
if __name__ == '__main__':
    app.run(debug=True)