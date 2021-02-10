import sqlite3
from sqlite3 import Error


def createConnection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def getData(conn):
    """
    Query all enities in the Users table
    :param conn: the Connection object
    :return: rows
    """
    cur = conn.cursor()
    cur.execute("SELECT username, guildName, subLevel, inviteLink, description, lastShareTime FROM Users")

    rows = cur.fetchall()
    return rows


def updateSubLevel(conn, data):
    """
    update subLevel of a User
    :param conn:
    :param subLevel:
    :return: project id
    """
    sql = ''' UPDATE Users
              SET subLevel = ?
              WHERE username = ?'''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()

# def main():
#     database = r"bot"

#     # create a database connection
#     conn = createConnection(database)
#     # create a new project
#     # user = ('Admin', '3', 'google.com',"","9:19:52")
#     # userID = createUser(conn, user)
#     # test = getTime(conn, ["Sadeed"])[0]
#     # test = getData(conn)
#     # print(str(datetime.timedelta(seconds=test)).split(":"))
#     test = getAutoMsgData(conn)
#     print(test[0][0])


# if __name__ == '__main__':
#     main()
