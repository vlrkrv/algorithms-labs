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

def build_open_hash_table(words: list, m: int) -> list:
    """Будує хеш-таблицю з ланцюжками"""
    hash_table = [[] for _ in range(m)]
    for word in words:
        key = calculate_key(word)
        address = hash_multiplication(key)
        hash_table[address].append(word)
    return hash_table

def display_hash_table(table: list):
    """Виводить хеш-таблицю"""
    print(f"\n--- Метод множення (M={len(table)}) ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")

# Виконання:
hash_table = build_open_hash_table(WORDS, M)
display_hash_table(hash_table)
