from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Инициализация приложения Flask
app = Flask(__name__)

# Настройка подключения к базе данных SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # База данных будет храниться в файле users.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Отключаем отслеживание изменений

# Инициализация SQLAlchemy
db = SQLAlchemy(app)

# Разрешаем запросы с других источников (CORS)
CORS(app)

# Модель для таблицы Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    fio = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)  # Уникальность для номера телефона

    def __repr__(self):
        return f'<User {self.username}>'

# Роут для создания пользователей (например, через POST запрос)
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()  # Получаем данные из запроса
    username = data.get('username')
    password = data.get('password')
    fio = data.get('fio')
    phone = data.get('phone')

    # Проверка на пустые данные
    if not all([username, password, fio, phone]):
        return jsonify({'message': 'Недостаточно данных, все поля обязательны!'}), 400

    # Проверяем, существует ли уже пользователь с таким номером телефона
    existing_user = User.query.filter_by(phone=phone).first()
    if existing_user:
        return jsonify({'message': 'Пользователь с таким номером телефона уже существует!'}), 400

    # Создаем нового пользователя
    new_user = User(username=username, password=password, fio=fio, phone=phone)

    # Добавляем пользователя в базу данных
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Пользователь успешно создан!'}), 201

# Роут для получения всех пользователей
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{'id': user.id, 'username': user.username, 'fio': user.fio, 'phone': user.phone} for user in users]
    return jsonify(users_list)

# Точка входа
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
