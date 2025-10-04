import random
import string
from datetime import datetime


def generate_email():
    """Генерирует уникальный email для регистрации"""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    rand_digits = ''.join(random.choices(string.digits, k=3))

    return f"test_s5_{timestamp}_{rand_digits}@yandex.ru"


def generate_password(length=8):
    """Генерирует случайный пароль"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))
