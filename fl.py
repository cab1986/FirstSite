from flask import *
import os
#from flask_ngrok import run_with_ngrok

app = Flask(__name__)
#run_with_ngrok(app)

@app.route('/')
def index():
    user = "Андрей"
    return render_template('index.html', title='Домашняя страница', 
                           username=user)

@app.route('/first_page')
def first():
    name = url_for('static', filename='img/picture.jpg')
    return render_template('picture.html', title='Картинка', name=name)

@app.route('/news')
def news():
    with open("templates/news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('news.html', news=news_list, title='Новости')

@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('registration.html', title='Форма регистрации')
       
    elif request.method == 'POST':
        print(request.form.get('email'))
        print(request.form.get('password'))
        print(request.form.get('file'))
        print(request.form.get('about'))
        print(request.form.get('accept'))
        print(request.form.get('sex'))
        return render_template('registration1.html', title='Форма регистрации')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)