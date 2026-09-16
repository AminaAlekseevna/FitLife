# Проект FitLife - MVP версия 1.0

# 1. Знакомство
print("Здравтвуйте! Я фитнес-бот для рассчета ИМТ! Давай знакомится!")
user_name = input("Как вас зовут?")
user_age = int(input("Сколько вам лет? Введите свой возраст цифрами:"))


# 2. Сбор данных
user_weight = float(input("А теперь давай узнеам твой вес, напиши его в кг:"))
user_height = float(input("Напиши еще свой рост в метрах пожалуйста:"))


# 3. Логика расчетов
bmi = user_weight / (user_height ** 2)
round_bmi = round(bmi, 1)

water_ml = user_weight * 30
water_l = water_ml / 1000


# 4. Вывод красивого результата
print(f"Отчет для пользователя: {user_name}, {user_age}")
print(f"Твой Индекс Массы Тела: {round_bmi}")
print(f"Рекомендуемая норма воды: {water_l} в день")
