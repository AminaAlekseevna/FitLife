# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_IN_LITER = 1000
DECIMAL_PLACES = 1


# 1. Знакомство
def main():
    """Запускает бота:собирает данные, считает ИМТ и норму воды,отчет."""
    print("Здравствуйте! Я фитнес-бот для расчета ИМТ")
    user_name = input("Как вас зовут? ")
    user_age = input("Сколько вам лет? ")


    weight_input = input("Ваш вес в кг: ")
    user_weight = float(weight_input.replace(',', '.'))
    height_input = input("Ваш рост в метрах: ")
    user_height = float(height_input.replace(',', '.'))


    bmi = user_weight / (user_height ** 2)
    round_bmi = round(bmi, DECIMAL_PLACES)
    water_ml = user_weight * WATER_PER_KG
    water_l = water_ml / ML_IN_LITER


    return user_name, user_age, round_bmi, water_l


if __name__ == '__main__':
    name, age, bmi_val, water_val = main()
    print(
        f"Отчет для пользователя: {name}, {age} лет\n"
        f"Твой Индекс Массы Тела: {bmi_val}\n"
        f"Рекомендуемая норма воды: {water_val} л в день" )
