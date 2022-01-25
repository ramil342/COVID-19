from covid import Covid

covid = Covid(source="worldometers")
covid.get_data()
countries = covid.list_countries()

place = input("Введите название страны: ")

location = covid.get_status_by_country_name(place)

answer = "Активные больные: " + str(location['active']) + "\n" "Всего заболело: " + str(location['confirmed']) + "\n" "Страна: " + str(location['country']) + "\n" "Вылечено: " + str(location['recovered']) + "\n" "Умерло всего: " + str(location['deaths']) + "\n" "Новых зараженных: " + str(location['new_cases']) + "\n" "Новых смертей: " + str(location['new_deaths']) + "\n" "Кол-во тестов: " + str(location['total_tests'])

print(answer)