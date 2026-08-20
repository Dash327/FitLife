def main():
    """Главная функция программы."""
    # Обернула всё в фунцию, так как падал 6 тест, подсказал гптшник,
    # не одна столкнулась с такой проблемой,
    # что 6 тест ожидает строку
    print('Здравствуйте! Начнём путь к здоровью вместе')

    user_name = input('Как вас зовут?')
    # для обработки имени
    user_age = int(input('Cколько вам лет?'))

    print('Ещё немного данных :)')
    user_weight = float(input('Укажите свой вес в килограммах:'))
    user_height = float(input('Укажите ваш рост в метрах (например 1.60):'))
    print('Отлично, приступаем к рассчётам!')

    bmi = round((user_weight / (user_height ** 2)), 1)
    WATER_PER_LITER = 30  # мл воды на 1 кг веса
    CONVERT_ML_TO_L = 1000  # для перевода мл в л
    water_in_ml = user_name * WATER_PER_LITER
    water_needed = round((water_in_ml / CONVERT_ML_TO_L), 1)

    print('-' * 40)
    print(f'Отчёт для пользователя {user_name}, полных лет {user_age}')
    print(f"Ваш индекс массы тела: {bmi}")
    print(
        f"{user_name}, рекомендуемая норма воды для вас (л/день): "
        f"{water_needed}.",
    )


if __name__ == '__main__':
    main()
