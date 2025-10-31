# Константа розміру таблиці
M = 16
# Список вхідних слів
WORDS = ["Хто", "грошима", "величається", "той", "без", "душі", "зостачається"]

# Словник позицій українських букв
LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8, 'Ж': 9, 'З': 10,
    'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19,
    'П': 20, 'Р': 21, 'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28,
    'Ш': 29, 'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}

# Константа A для методу множення
A = 0.6180339887

def calculate_key(word: str) -> int:
    """Обчислює числовий ключ K для слова"""
    sum_of_positions = 0
    for char in word.upper():
        position = LETTER_POSITIONS.get(char, 0)
        sum_of_positions += position
    return sum_of_positions

def hash_multiplication(key: int) -> int:
    """Хеш-функція методом множення: h(k) = floor(16 * (k * A mod 1))"""
    fractional_part = (key * A) % 1
    return int(M * fractional_part)

def build_closed_hash_table(words: list, m: int) -> list:
    """Будує закриту хеш-таблицю з відкритою адресацією"""
    # 1. Ініціалізація таблиці: M порожніх слогів (використовуємо None як "порожній")
    hash_table = [None] * m
    
    # 2. Обробка кожного слова
    for word in words:
        # Крок 2a: Обчислення початкової адреси
        key = calculate_key(word)
        start_address = hash_multiplication(key)
        address = start_address
        
        # Крок 2b: Лінійне дослідження (Linear Probing)
        # Цикл гарантує, що ми не будемо шукати нескінченно довго у повній таблиці
        for i in range(m):
            # h(k, i) = (h(k) + i) mod M
            address = (start_address + i) % m
            
            # Перевірка, чи комірка вільна
            if hash_table[address] is None:
                # Вставлення ключа
                hash_table[address] = word
                break
        else:
            # Цей блок виконується, якщо цикл завершився без 'break' (таблиця повна)
            print(f"Помилка: Таблиця заповнена. Не вдалося додати слово: {word}")
    
    return hash_table

def display_hash_table(table: list):
    """Виводить хеш-таблицю у зручному форматі."""
    print(f"\n--- Закрита хеш-таблиця методом множення (M={len(table)}) ---")
    print("Індекс | Слово")
    print("-------|-------")
    for i, item in enumerate(table):
        # Виводимо ключі або позначку, що комірка порожня
        value = item if item is not None else "(NULL)"
        print(f"{i:02d}     | {value}")

# Виконання:
hash_table = build_closed_hash_table(WORDS, M)
display_hash_table(hash_table)
