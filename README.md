<p align="center">
<img title="Logo" src="https://img.hhcdn.ru/employer-logo/5500269.png">
</p>

## Демо-проект по автоматизации тестирования: WONE IT
:earth_americas: https://wone-it.ru/

### :watermelon: Реализованы следующие проверки:
:white_check_mark: API Статус-код страницы = 200    
:white_check_mark: API Статус-код страницы = 404    
:white_check_mark: UI Проверить актуальность контаков    
:white_check_mark: UI Заполнить форму данными    
:white_check_mark: UI Поиск через меню с выпадающим списком


## :watermelon: Запуск тестов из терминала
###### Локальный запуск:
```
pytest .
```
###### Удаленный запуск:
```
clean
test
-Dbrowser=${BROWSER}
-DbrowserVersion=${BROWSER_VERSION}
-DbrowserSize=${BROWSER_SIZE}
-DremoteDriverUrl=https://user1:1234@${REMOTE_BROWSER}/wd/hub/
-DvideoStorage=https://${REMOTE_BROWSER}/video/
```

## :watermelon: Запуск тестов в Jenkins
Шаги:
1. <i>Зарегистрированным</i> пользователем перейти на страницу сборки проекта по ссылке: <a target="_blank" href="hhttps://jenkins.autotests.cloud/job/C02_OlgaKos_python_demo_woneit/">our Jenkins project</a>
2. Перечисленные (ниже) параметры можно менять в графическом интерфейсе.
3. Запустить выполнение тестов кнопкой "Собрать" (внизу страницы)

Основные параметры сборки:
- `BROWSER` – браузер, в котором будут выполняться тесты (по умолчанию - Chrome).
- `BROWSER_VERSION` версия браузера, в которой будут выполняться тесты (по умолчанию - 91.0). <i>В примере другие варианты не заданы.</i>.
- `BROWSER_SIZE` – размер окна браузера, в котором будут выполняться тесты (по умолчанию - 1920x1080).
- `REMOTE_BROWSER` - адрес (логин и пароль) удаленного сервера (Selenoid), на котором будут запускаться тесты.
- `THREADS` - кол-во потоков (в данном примере не задано)

Дополнительные параметры сборки, задействованные для выгрузки краткого отчета в Telegram:
- `PROJECT_NAME`  название проекта
- `ENVIRONMENT` - тестовый стенд (prod, preprod, stage...), на котором запускались тесты. <i>В примере эти данные не заданы. Можно выставить любое значение из доступных в выпадающем списке</i>.
- `COMMENT` - ваш текстовой комментарий
- `BUILD_URL` - автоматическая ссылка на детализированный отчет о сборке

------------
version 01 - add 5 easy tests
<br>version 02 - add Page Object Pattern
<br>version 03 - add local Allure. Some fix.
<br>version 04 - branch 'jenkins_add'. Add Jenkins with remote Allure.
