from flask import Flask
from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# db/mars_explorer.db
def main():
    global_init(input())
    db_sess = create_session()
    for job in db_sess.query(Jobs).all():
        if job.work_size < 20 and not job.is_finished:
            print(f"<Job> {job.job}")


if __name__ == '__main__':
    main()