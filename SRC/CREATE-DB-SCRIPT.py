from sshtunnel import SSHTunnelForwarder
import mysql.connector


tunnel = SSHTunnelForwarder(('nova.cs.tau.ac.il', 22),
                            ssh_username=input("insert your moodle username: "),
                            ssh_password=input("insert your moodle password: "),
                            remote_bind_address=('mysqlsrv1.cs.tau.ac.il', 3306))
tunnel.start()

details = {
    'user': 'DbMysql02',
    'password': 'DbMysql02',
    'host': '127.0.0.1',
    'database': 'DbMysql02',
    'port': tunnel.local_bind_port,
    'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**details)

cursor = cnx.cursor()

add_employee = ("INSERT INTO example (id, name) values (88, 'sahar')")

# Insert new employee
cursor.execute(add_employee)
emp_no = cursor.lastrowid

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()

print('done')
