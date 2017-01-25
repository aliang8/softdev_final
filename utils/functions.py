import sqlite3 as sql
import hashlib

#CONNECT DATABASE                                                                                                       
DATA = "data/data.db"

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
    data = c.execute("SELECT username, money, level, exp FROM accounts WHERE username = ?", (user,))
    stats = data.fetchall()
    return stats[0]

def getUserEvents(user):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    data = c.execute("SELECT * FROM events WHERE userID = ?", (userID,))
    goals = data.fetchall()
    return goals
    
#return the user's goals in a tuple
def getUserToDos(user):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    data = c.execute("SELECT * FROM events WHERE userID = ? and todo = 1", (userID,))
    todos = data.fetchall()
    return todos
    
#return the user's goals in a tuple
def getUserHabits(user):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    data = c.execute("SELECT * FROM events WHERE userID = ? and habit = 1", (userID,))
    habits = data.fetchall()
    return habits

#return the user's goals in a tuple
def getUserGoals(user):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    data = c.execute("SELECT * FROM events WHERE userID = ? and goal = 1", (userID,))
    goals = data.fetchall()
    return goals
    


def insertToDo(user, goal):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    
    data = c.execute("INSERT INTO events VALUES (?,1,0,0,?)", (userID, goal,))
    
    db.commit()
    db.close()
    return goal

def insertHabit(user, goal):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    
    data = c.execute("INSERT INTO events VALUES (?,0,1,0,?)", (userID, goal,))
    
    db.commit()
    db.close()
    return goal

#one function for removing and inserting user goals
def insertGoal(user, goal):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)

    data = c.execute("INSERT INTO events VALUES (?,0,0,1,?)", (userID, goal,))

    db.commit()
    db.close()
    return goal
    
def deleteGoal(user, goalID):
    db = sql.connect(DATA)
    c = db.cursor()
    userID = getUserID(user)
    
    data = c.execute("DELETE FROM events WHERE goalID = ?", goalID)
    
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


