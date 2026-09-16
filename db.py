import pickle
users=[]
def create_user(login, password):
    user=[login, password]
    users.append(user)
    h=saves()


def find_login(login):
    for u in users:
        if u[0]==login:
            return True
    return False


def check_user(login, password):
    for i in users:
        if i[0]==login and i[1]==password:
            return True
    return False

def saves():
    f=open("db", "wb")
    pickle.dump(users, f)
    f.close()


def load():
    global users
    g=open("db", "rb")
    users=pickle.load(g)
    g.close()
l=load()