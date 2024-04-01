from requests import get, post, delete, put


# выводит словарь всех работ из БД
print(get('http://localhost:5000/api/jobs').json())

# выводит работу с id = 1
print(get('http://localhost:5000/api/jobs/1').json())

# работы с id = 999 нет в базе
print(get('http://localhost:5000/api/jobs/999').json())

# ошибка (type(id) = int, а не str)
print(get('http://localhost:5000/api/jobs/q').json())

# ошибка (передан пустой словарь)
print(post('http://localhost:5000/api/jobs', json={}).json())

# ошибка (переданы не все поля в словаре)
print(post('http://localhost:5000/api/jobs',
           json={'title': 'Заголовок'}).json())

# добавит новую работу в БД
print(post('http://localhost:5000/api/jobs',
           json={'job': 'Исследование грунта',
                 'team_leader': 1,
                 'work_size': 150, 'collaborators': '2, 3',
                 'is_finished': False}).json())

# выводит словарь всех работ из БД
print(get('http://localhost:5000/api/jobs').json())

# ошибка (передан пустой словарь)
print(put('http://localhost:5000/api/jobs/edit/2', json={}).json())

# ошибка (type(id) = int, а не str)
print(put('http://localhost:5000/api/jobs/edit/q', json={'job': 'Исследование грунта измененное', 'team_leader': 1,
                                                         'work_size': 16, 'collaborators': '2, 3, 4'}).json())

# ошибка (нет в базе id = 999)
print(put('http://localhost:5000/api/jobs/edit/999', json={'job': 'Исследование грунта измененное', 'team_leader': 1,
                                                           'work_size': 16, 'collaborators': '2, 3, 4'}).json())

# изменит работу в БД
print(put('http://localhost:5000/api/jobs/edit/2', json={'job': 'Исследование грунта измененное', 'team_leader': 1,
                                                         'work_size': 16, 'collaborators': '2, 3, 4'}).json())

# выводит словарь всех работ из БД
print(get('http://localhost:5000/api/jobs').json())

# работы с id = 999 нет в базе
print(delete('http://localhost:5000/api/jobs/999').json())

# ошибка (type(id) = int, а не str)
print(delete('http://localhost:5000/api/jobs/q').json())

# удаляет работу из БД
print(delete('http://localhost:5000/api/jobs/1').json())

# выводит словарь всех работ из БД
print(get('http://localhost:5000/api/jobs').json())