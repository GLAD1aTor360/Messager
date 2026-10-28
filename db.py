import pickle
users=[]
chats={}
def create_chat(chatname, login):
     chat_id=len(chats)
     chats[chat_id]={
         "name":chatname,
         "users":[login],
         "id":chat_id
     }
     g=saves()


def find_chats_by_login(login):
    userchats=[]
    for chat_id in chats:
        chat_info=chats[chat_id]
        chat_users=chat_info["users"]
        if login in chat_users:
            userchats.append(chat_info)
    return(userchats)


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
    pickle.dump([users, chats], f)
    f.close()


def load():
    global users, chats
    g=open("db", "rb")
    users, chats=pickle.load(g)
    g.close()
l=load()