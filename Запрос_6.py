from flask import Flask
from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# db/mars_explorer.db
def main():
    result = []
    global_init(input())
    db_sess = create_session()
    data = db_sess.query(Jobs).all()
    max_collaborators = max([max(job.collaborators.split(', ')) for job in data])
    for job in data:
        lst = job.collaborators.split(', ')
        if len(max(lst)) == max_collaborators:
            result.append((job.team_leader, lst))
    if len(result) == 1:
        for user in db_sess.query(User).all():
            if user.id == result[0]:
                print(user.surname, user.name)
    else:
        for user in db_sess.query(User).all():
            if user.id == result[0]:
                print(user.surname, user.name)
        for i in lst:
            for user in db_sess.query(User).all():
                if user.id == i:
                    print(user.surname, user.name)


if __name__ == '__main__':
    main()