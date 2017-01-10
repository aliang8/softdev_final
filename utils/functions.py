import sqlite3 as sql
import hashlib

#CONNECT DATABASE                                                                                                       
DATA = "../data/data.db"

def getUserID(user):
    db = sql.connect(DATA)
    c = db.cursor()
    data = c.execute("SELECT userID FROM accounts WHERE username = ?", (user,))
    userID = data.fetchone()[0]
    return userID

#retrieving all the user information outputted in a tuple
def getUserInfo(user):
    db = sql.connect(DATA)
    c = db.cursor()
    data = c.execute("SELECT money, level, exp FROM accounts WHERE username = ?", (user,))
    stats = data.fetchall()
    return stats[0]

#return the user's goals in a tuple
def getUserGoals(user):
    db = sql.connect(DATA)
    c = db.cursor()
    data = c.execute("SELECT * FROM events WHERE username = ?", (user,))
    goals = data.fetchall()
    ##return goals

#insert new user goal
def newGoal(user, goal):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    data = c.execute("INSERT INTO events VALUES (?,?)", (userID, goal,))
    db.commit()
    db.close()
 
#update and insert user info
def updateInfo(user,infoType,update):
    db = sql.connect(DATA)
    c = db.cursor()
    exists = c.execute("SELECT " + infoType + " from accounts WHERE username = ?", (user,))
    exist = exists.fetchall()
    print len(exist)
    if len(exist) != 0:
        data = c.execute("UPDATE accounts SET " + infoType + " = ? WHERE username = ?", (update, user,))
    else:
        data = c.execute("INSERT INTO accounts (" + infoType + ") VALUES (?) WHERE username = ?", (update,user,)) 
    db.commit()
    db.close()


newGoal('Anthony','eat fruits')
