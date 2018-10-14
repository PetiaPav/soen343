from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'pomoroad_soen09'
app.config['MYSQL_DATABASE_PASSWORD'] = 'discordApp343'
app.config['MYSQL_DATABASE_DB'] = 'pomoroad_soen343'
app.config['MYSQL_DATABASE_HOST'] = '108.167.160.63'
mysql.init_app(app)
connection = mysql.connect()
c = connection.cursor()

fd = open('../SQL/db_structure.sql', 'r')
sqlFile = fd.read()
fd.close()

fl = open('../SQL/db_data.sql', 'r')
sqlFile2 = fl.read()
fl.close()

# all SQL commands (split on ';')
sqlCommands = sqlFile.split(';')
sqlCommands2 = sqlFile2.split(';')

# Execute every command from the input file
print('Reseting table structures...')
for command in sqlCommands:
    # This will skip and report errors
    try:
        c.execute(command)
    except:
        if command != '':
            print(command)
            print('Command skipped')

print('Repopulating tables...')
for command in sqlCommands2:
    # This will skip and report errors
    try:
        c.execute(command)
    except:
        if command == '':
            print(command)
            print('Command skipped')

c.close()
print('All tables reset and repopulated')
        
