import MySQLdb
import sys
import datetime

def update(name):
    connection = MySQLdb.connect(
    host='localhost', user='root', passwd='', db='mydb', charset='utf8')
    cursor = connection.cursor()
 
    try:
#        cursor.execute("""CREATE TABLE IF NOT EXISTS `iine` (
#        `id` int(11) AUTO_INCREMENT,
#        `name` varchar(128),
#        `first` varchar(128),
#        `second` varchar(128),
#        PRIMARY KEY (id)
#        )""")
        cursor.execute('select * from iine where name=%s', (name,))
        d1 = converter(cursor.fetchone()[2])
        t = datetime.datetime.now()
        h = t.strftime("%H")        
        h = 2
        if h > 0 and d1[h]==0:
          d1[h] += d1[h-1] 
        d1[h] += 1 
        cursor.execute('UPDATE `iine` SET `first`=%s WHERE `name`=%s;', (adapter(d1), name))
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
#    print(adapter([1,2,3]))
#    print(converter("1;2;3"))
