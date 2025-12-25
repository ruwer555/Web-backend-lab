from app import app
from db.models import RgzUser
from werkzeug.security import check_password_hash

with app.app_context():
    print("🔍 ПОДКЛЮЧЕНИЕ К БАЗЕ...")
    
    # Ищем пользователя
    user = RgzUser.query.filter_by(login='kladovshik').first()
    
    if not user:
        print("❌ ОШИБКА: Пользователь 'kladovshik' НЕ НАЙДЕН в базе!")
    else:
        print(f"✅ Пользователь найден: ID {user.id}")
        print(f"💾 Хеш в базе (первые 50 символов): {user.password_hash[:50]}...")
        print(f"📏 Длина хеша: {len(user.password_hash)}")
        
        # Проверяем пароль
        password = "password"
        is_valid = check_password_hash(user.password_hash, password)
        
        print("-" * 30)
        if is_valid:
            print(f"✅ ПАРОЛЬ '{password}' ПОДХОДИТ! Проблема в браузере/кэше.")
        else:
            print(f"❌ ПАРОЛЬ '{password}' НЕ ПОДХОДИТ! Хеш в базе неправильный.")
            print("💡 Возможно, хеш обрезался или вставился с пробелом.")
