from requests import get, post, delete

# выводит словарь всех работ из БД
print(get('http://localhost:5000/api/v2/users').json())

# выводит работу с id = 1
print(get('http://localhost:5000/api/v2/users/1').json())

# работы с id = 999 нет в базе
print(get('http://localhost:5000/api/v2/users/999').json())

# ошибка (type(id) = int, а не str)
print(get('http://localhost:5000/api/v2/users/q').json())

# ошибка (передан пустой словарь)
print(post('http://localhost:5000/api/v2/users', json={}).json())

# ошибка (переданы не все поля в словаре)
print(post('http://localhost:5000/api/v2/users',
           json={'id': 2}).json())

# добавит новую работу в БД
print(post('http://localhost:5000/api/v2/users',
           json={'surname': 'Белов',
                 'name': 'Алексей',
                 'age': 26,
                 'position': 'colonist',
                 'speciality': 'pilot',
                 'address': 'module_1',
                 'email': '8@mars.org',
                 'hashed_password': 's45h3455'}).json())

# выводит словарь всех работ из БД
print(get('http://localhost:5000/api/v2/users').json())

# работы с id = 999 нет в базе
print(delete('http://localhost:5000/api/v2/users/999').json())

# ошибка (type(id) = int, а не str)
print(delete('http://localhost:5000/api/v2/users/q').json())

# удаляет работу из БД
print(delete('http://localhost:5000/api/v2/users/1').json())

# выводит словарь всех работ из БД
print(get('http://localhost:5000/api/v2/users').json())