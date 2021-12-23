import sqlite3


def create_user():
    query = ''' 
        CREATE TABLE "usuarios" (
            "ID" INTEGER, 
            "CPF" TEXT, 
            "NOME" TEXT, 
            "DATA_DE_NASCIMENTO" TEXT, 
            "DATA_DE_CRIACAO" TEXT, 
            "DATA_DE_ATUALIZACAO" TEXT, 
            PRIMARY KEY("ID" AUTOINCREMENT) )
    '''.replace('    ', '')

    print(query)

    with sqlite3.connect('user.db') as database:
        cursor = database.cursor()
        cursor.execute(query)

#rotaGet
def select_users():
    query = '''SELECT * FROM usuarios'''
    users = []
    with sqlite3.connect('user.db') as database:
        for user in database.cursor.execute(query):
            user = dict({user[0]: user[1]})
            users.append(user)

    return users


# create_user()
print(select_users())