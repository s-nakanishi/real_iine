import MySQLdb
import sys
 
def update(name):
    connection = MySQLdb.connect(
    host='localhost', user='root', passwd='', db='mydb', charset='utf8')
    cursor = connection.cursor()
 
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS `iine` (
        `id` int(11) AUTO_INCREMENT,
        `name` varchar(128),
        `first` varchar(128),
        `second` varchar(128),
        PRIMARY KEY (id)
        )""")
        cursor.execute('select * from iine')
        for result in cursor.fetchall():
            if result[1]==name:
                cursor.execute('DELETE FROM iine WHERE name=%s', (name,))
                connection.commit()

        cursor.execute('INSERT INTO iine (name, first, second) values (%s, %s, %s)', (name, "0;0;0;0;0;0;0;0", "0;0;0;0;0;0;0;0"))
        connection.commit()

        cursor.execute('select * from iine')
        print(cursor.fetchall())
        connection.close()

    except MySQLdb.Error as e:
        print('MySQLdb.Error: ', e)

def adapter(list):
    ret = ';'.join([str(i) for i in list])
    return ret

def converter(str):
    ret = [int(i) for i in str.split(';')]
    return ret

if __name__ == '__main__':
    update(sys.argv[1])
