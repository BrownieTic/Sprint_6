# Sprint 6 — автотесты сервиса «Самокат»

Проект содержит UI-автотесты сервиса аренды самокатов на Selenium и pytest. Тесты проверяют переходы между страницами, работу блока «Вопросы о важном», оформление заказа и переходы по логотипам в шапке.

## Структура проекта

```text
Sprint_6/
├── locators/       # Локаторы элементов страниц
├── page/           # Page Object-классы
├── tests/          # Тесты главной страницы и страницы заказа
├── data.py         # Тестовые данные и ожидаемые тексты
├── conftest.py     # Фикстуры
└── urls.py         # URL тестируемых страниц
```

## Требования
Выписаны в requirements.txt

- Python 3.10 или новее
- Mozilla Firefox
- установленный браузерный драйвер, совместимый с браузером
- pytest
- Selenium
- allure-pytest
- Java и Allure Commandline для формирования HTML-отчёта

## Установка

Перейдите в каталог проекта и установите зависимости:

```powershell
cd ..\Sprint_6
py -m pip install pytest selenium allure-pytest
```

Проверьте, что Java доступна в PATH:

```powershell
java -version
```

Allure Commandline можно установить через npm:

```powershell
npm install -g allure-commandline
```

## Запуск тестов

Запустить все тесты:

```powershell
py -m pytest
```

Запустить тесты с сохранением результатов для Allure:

```powershell
py -m pytest --alluredir=allure-results
```

Запустить отдельный набор тестов:

```powershell
py -m pytest tests\test_main_page.py --alluredir=allure-results
py -m pytest tests\test_order_page.py --alluredir=allure-results
```

## Allure-отчёт

После выполнения тестов открыть временный отчёт в браузере:

```powershell
allure serve allure-results
```

Или создать отчёт в отдельной папке:

```powershell
allure generate allure-results -o allure-report --clean
allure open allure-report
```

Папки `allure-results` и `allure-report` создаются автоматически и не являются исходным кодом проекта.

## Важные замечания

- Тесты используют реальные URL тестового стенда `qa-scooter.praktikum-services.ru`, поэтому требуется доступ к интернету.
- Перед запуском убедитесь, что браузер и его драйвер установлены и совместимы.
- В тестах используется Firefox `webdriver.Chrome()`.
- Каждый тестовый класс самостоятельно создаёт и закрывает экземпляр браузера.
