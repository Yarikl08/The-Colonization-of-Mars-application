import datetime
from requests import get, post, delete, put

# выводит словарь всех работ из БД
print(get('http://localhost:5000/api/users').json())

# выводит работу с id = 1
print(get('http://localhost:5000/api/users/1').json())

# работы с id = 999 нет в базе
print(get('http://localhost:5000/api/users/999').json())

# ошибка (type(id) = int, а не str)
print(get('http://localhost:5000/api/users/q').json())

# ошибка (передан пустой словарь)
print(post('http://localhost:5000/api/users', json={}).json())

# ошибка (переданы не все поля в словаре)
print(post('http://localhost:5000/api/users',
           json={'id': 2}).json())

# добавит новую работу в БД
print(post('http://localhost:5000/api/users',
           json={'surname': 'Белов',
                 'name': 'Алексей',
                 'age': 26,
                 'position': 'colonist',
                 'speciality': 'pilot',
                 'address': 'module_1',
                 'email': '8@mars.org',
                 'hashed_password': 's45h3455'}).json())

# выводит словарь всех работ из БД
print(get('http://localhost:5000/api/users').json())

# ошибка (передан пустой словарь)
print(put('http://localhost:5000/api/users/edit/2', json={}).json())

# ошибка (type(id) = int, а не str)
print(put('http://localhost:5000/api/users/edit/q', json={'name': 'Фёдор', 'age': 16}).json())

# ошибка (нет в базе id = 999)
print(put('http://localhost:5000/api/users/edit/999', json={'name': 'Фёдор', 'age': 16}).json())

# изменит работу в БД
print(put('http://localhost:5000/api/users/edit/2', json={'name': 'Фёдор', 'age': 16}).json())

# выводит словарь всех работ из БД
print(get('http://localhost:5000/api/users').json())

# работы с id = 999 нет в базе
print(delete('http://localhost:5000/api/users/999').json())

# ошибка (type(id) = int, а не str)
print(delete('http://localhost:5000/api/users/q').json())

# удаляет работу из БД
print(delete('http://localhost:5000/api/users/1').json())

# выводит словарь всех работ из БД
print(get('http://localhost:5000/api/users').json())