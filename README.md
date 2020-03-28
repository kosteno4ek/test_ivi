# test_ivi


Для запуска необходимо выполнить команду:
pytest

При тестировании проверены следующие позитивне сценарии:

1. Получение списка всех персонажей (метод GET без параметров)
2. Полчучение информации о персонаже по имени (метод GET с указанием имени в параметрах)
3. Добавление нового персонажа (метод POST)
4. Обновление информации о персонаже (метод PUT)
5. Удаление персонажа (Метод DELETE)

Подробное описание тест-кейсов находится в файле smoke_scenarios.txt

Подробное описание тест-кейсов с использованием методологии BDD находится в файле features/test_smoke.feature


Проверены также следующие негативные сценарии:

1. Полчучение информации о персонаже с указанием неправильного поля в запросе
2. Обновление информации о персонаже, которого не существует в коллекции
3. Добавление нового персонажа в случае с заполненной коллекцией
4. Добавление нового персонажа без всех необходимых полей в запросе
5. Удаление персонажа, которого не существует в коллекции

Подробное описание тест-кейсов находится в файле negative_scenarios.txt

Подробное описание тест-кейсов с использованием методологии BDD находится в файле features/test_negative.feature
