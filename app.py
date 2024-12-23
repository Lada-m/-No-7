import database.connection as conn
import database.DAO.newsDAO as news

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/news')
def get_news():
  try:
    xconn=conn.initConnection()
    data_news = news.getNewsAll(pconnection=xconn)

    return render_template('news.html', data_news=data_news)
  except Exception as e:
    return '<font color="red"><h1> Ошибка: '+str(e)+'</h1></font>'
  finally:
    conn.closeConnection(pconnection=xconn)

@app.route('/')
def index():
  return '<h1>Hello World!</h1>'

@app.route('/hello')
def hello():
  return '<h1> Hello my friend!</h1>'

@app.route('/user', defaults={'name': 'azat'})
@app.route('/user/<name>')
def hello_user(name):
  return '<h1>Hello, %s ! </h1>' % name

if __name__ == '__main__':
  app.run(host='0.0.0.0')