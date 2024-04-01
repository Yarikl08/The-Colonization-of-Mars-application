import datetime
from flask import Flask, render_template, redirect, request, abort, make_response, jsonify
from data import db_session, jobs_api, users_api
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from forms.loginform import LoginForm
from forms.jobs import JobsForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                      Jobs.user == current_user
                                      ).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = JobsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          Jobs.user == current_user
                                          ).first()
        if jobs:
            form.job.data = jobs.job
            form.team_leader.data = jobs.team_leader
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.is_finished.data = jobs.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          Jobs.user == current_user
                                          ).first()
        if jobs:
            jobs.job = form.job.data
            jobs.team_leader = form.team_leader.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            jobs.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('jobs.html',
                           title='Works log',
                           form=form
                           )


@app.route('/jobs',  methods=['GET', 'POST'])
@login_required
def add_jobs():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = Jobs()
        jobs.team_leader = form.team_leader.data
        jobs.job = form.job.data
        jobs.work_size = form.work_size.data
        jobs.collaborators = form.collaborators.data
        jobs.is_finished = form.is_finished.data
        current_user.jobs.append(jobs)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('jobs.html', title='Adding a Job', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    # jobs = db_sess.query(Jobs)
    if current_user.is_authenticated:
        jobs = db_sess.query(Jobs).filter(Jobs.user == current_user)
    else:
        jobs = db_sess.query(Jobs)
    return render_template("index.html", title='Works log', jobs=jobs)


@app.route("/login_1")
def login_1():
    return render_template("login_1.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Authorization', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.repeat_password.data:
            return render_template('register.html', title='Register', form=form, message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.login_email.data).first():
            return render_template('register.html', title='Register', form=form, message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.login_email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)


# Добавляем капитана, Первая работа
def main():
    db_session.global_init("db/mars_explorer.db")
    app.register_blueprint(jobs_api.blueprint)
    app.register_blueprint(users_api.blueprint)

    session = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    session.add(user)

    user = User()
    user.surname = "Weir"
    user.name = "Andy"
    user.age = 40
    user.position = "colonist"
    user.speciality = "cook"
    user.address = "module_2"
    user.email = "weir_chief@mars.org"
    session.add(user)

    user = User()
    user.surname = "Watney"
    user.name = "Mark"
    user.age = 23
    user.position = "colonist"
    user.speciality = "pilot"
    user.address = "module_1"
    user.email = "watney_chief@mars.org"
    session.add(user)

    user = User()
    user.surname = "Sanders"
    user.name = "Teddy"
    user.age = 29
    user.position = "colonist"
    user.speciality = "programmer"
    user.address = "module_3"
    user.email = "sanders_chief@mars.org"
    session.add(user)

    job = Jobs()
    job.team_leader = 1
    job.job = 'Deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.start_date = datetime.datetime.now()
    job.is_finished = False
    session.add(job)

    job = Jobs()
    job.team_leader = 2
    job.job = 'Exploration of mineral resources'
    job.work_size = 15
    job.collaborators = '4, 3'
    job.start_date = datetime.datetime.now()
    job.is_finished = False
    session.add(job)

    job = Jobs()
    job.team_leader = 3
    job.job = 'Development of a management system'
    job.work_size = 25
    job.collaborators = '5'
    job.start_date = datetime.datetime.now()
    job.is_finished = False
    session.add(job)

    session.commit()

    for job in session.query(Jobs).all():
        print(job)

    app.run()


if __name__ == '__main__':
    main()