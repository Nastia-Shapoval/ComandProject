# Оригінальний текст для обробки
text = "Learning Python is an essential skill for developers in today's tech-driven world. The language is versatile, easy to learn, and widely used across industries."

# 1. Перетворення всього тексту на великі літери (функція upper())
text_upper = text.upper()

# 2. Заміняємо всі коми на крапки з комою (функція replace())
text_replace_commas = text_upper.replace(',', ';')

# 3. Підрахунок кількості слів у тексті (функція split() та len())
word_count = len(text_replace_commas.split())

# Виведення результатів
print("Текст з великими літерами:\n", text_upper)
print("\nТекст із заміненими комами:\n", text_replace_commas)
print("\nКількість слів у тексті:", word_count)

