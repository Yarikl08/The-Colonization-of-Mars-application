from requests import get, post, delete,put


# выводит словарь всех работ из БД
print(get('http://localhost:5000/api/v2/jobs').json())

# выводит работу с id = 1
print(get('http://localhost:5000/api/v2/jobs/1').json())

# работы с id = 999 нет в базе
print(get('http://localhost:5000/api/v2/jobs/999').json())

# ошибка (type(id) = int, а не str)
print(get('http://localhost:5000/api/v2/jobs/q').json())

# ошибка (передан пустой словарь)
print(post('http://localhost:5000/api/v2/jobs', json={}).json())

#ошибка (переданы не все поля в словаре)
print(post('http://localhost:5000/api/v2/jobs', json={'work_size': 150}).json())

# добавит новую работу в БД
print(post('http://localhost:5000/api/v2/jobs',
           json={'team_leader': 4, 'job': 'Исследование грунта', 'work_size': 150, 'collaborators': '2, 3',
                 'is_finished': False}).json())

# добавит новую работу в БД
print(put('http://localhost:5000/api/v2/jobs/1',
           json={'team_leader': 1, 'job': 'Исследование грунта', 'work_size': 150, 'collaborators': '2, 3',
                 'is_finished': False}).json())

# выводит словарь всех работ из БД
print(get('http://localhost:5000/api/v2/jobs').json())

# работы с id = 999 нет в базе
print(delete('http://localhost:5000/api/v2/jobs/999').json())

# ошибка (type(id) = int, а не str)
print(delete('http://localhost:5000/api/v2/jobs/q').json())

# удаляет работу из БД
print(delete('http://localhost:5000/api/v2/jobs/2').json())

# выводит словарь всех работ из БД
print(get('http://localhost:5000/api/v2/jobs').json())