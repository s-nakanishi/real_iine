from flask import Flask, render_template
import MySQLdb

app = Flask(__name__)

@app.route('/')
def index():
    d = data()
    return render_template('index.html', names=d['name'], datas=d['data'])

def data():
    connection = MySQLdb.connect(
    host='localhost', user='root', passwd='', db='mydb', charset='utf8')
    cursor = connection.cursor()
    cursor.execute('select * from iine')
    names = []
    datas = []
    for result in cursor.fetchall():
        print(result)
        names.append(result[1])
        datas.append(converter(result[2].replace(';0', '')))
    return {'name':names, 'data':datas}

def converter(str):
    ret = [int(i) for i in str.split(';')]
    return ret

if __name__ == "__main__":
    app.run(debug=True)
