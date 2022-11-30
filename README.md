<p align="center">
<img title="Logo" src="https://img.hhcdn.ru/employer-logo/5500269.png">
</p>

## Демо-проект по автоматизации тестирования: WONE IT
:earth_americas: https://wone-it.ru/

## :watermelon: Реализованы следующие проверки:
:white_check_mark: API Статус-код страницы = 200    
:white_check_mark: API Статус-код страницы = 404    
:white_check_mark: UI Проверить актуальность контаков    
:white_check_mark: UI Заполнить форму данными    
:white_check_mark: UI Поиск через меню с выпадающим списком


## :watermelon: Запуск тестов
###### Локальный запуск (из терминала):
1. Перейти в директорию проекта.
2. Команда:
```
$ pytest .
```
Ожидаемый результат: На консоли выведется отчет о прохождении тестов (успешных и упавших)
###### Удаленный запуск: (IN WORK)
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
1. <i>Зарегистрированным</i> пользователем перейти на страницу сборки проекта по ссылке: 
   <a target="_blank" href="https://jenkins.autotests.cloud/job/C02_OlgaKos_python_demo_woneit/">our Jenkins project</a>
3. Перечисленные (ниже) параметры можно менять в графическом интерфейсе.
4. Запустить выполнение тестов кнопкой "Собрать" (внизу страницы)

Основные параметры сборки: (IN WORK)
- `BROWSER` – браузер, в котором будут выполняться тесты (по умолчанию - Chrome).
- `BROWSER_VERSION` версия браузера, в которой будут выполняться тесты (по умолчанию - 100.0). <i>В примере другие варианты не заданы.</i>.
- `BROWSER_SIZE` – размер окна браузера, в котором будут выполняться тесты (по умолчанию - 1920x1080).
- `REMOTE_BROWSER` - адрес (логин и пароль) удаленного сервера (Selenoid), на котором будут запускаться тесты.
- `THREADS` - кол-во потоков (в данном примере не задано)

Дополнительные параметры сборки, задействованные для выгрузки краткого отчета в Telegram: (IN WORK)
- `PROJECT_NAME`  название проекта
- `ENVIRONMENT` - тестовый стенд (prod, preprod, stage...), на котором запускались тесты. <i>В примере эти данные не заданы. Можно выставить любое значение из доступных в выпадающем списке</i>.
- `COMMENT` - ваш текстовой комментарий
- `BUILD_URL` - автоматическая ссылка на детализированный отчет о сборке


## :bellhop_bell: Allure отчет (....)
После того как тесты завершились, можно получить визуальный Allure отчет.
<br>Способ 1: Сформировать отчет средствами PyCharm (команда в терминале ... )
<br>Способ 2:
<br>1. Выполнить сборку в Jenkins
<br>2. Убедиться, что в блоке История сборок (напротив номера #) появился желтый значок Allure Report. (Если сборка запущена, но значок не виден, убедиться, что меню "История сброк" раскрыто)
<br>3. Кликнуть по значку Allure Report
<br>Ожидаемый результат: Откроется страница с графическими схемами Allure Report

###### Главная страница Allure-отчета содержит следующие информационные блоки:
- `ALLURE REPORT` отображает: Дату и время прохождения теста. Общее количество пройденных кейсов. Диаграмму с указанием процента и количества успешных, упавших и сломавшихся в процессе выполнения тестов
- `TREND` - отображает тренд прохождения тестов от сборки к сборке
- `SUITES` - отображает распределение результатов тестов по тестовым наборам
- `ENVIRONMENT` - отображает тестовое окружение (стенд), на котором запускались тесты. <i>В данном примере информация не задана.</i>
- `CATEGORIES` - отображает распределение неуспешно прошедших тестов по видам дефектов
- `FEATURES BY STORIES` - отображает распределение тестов по функционалу, который они проверяют
- `EXECUTORS` - отображает исполнителя текущей сборки (ссылка на сборку в Jenkins)

###### Главный экран отчета (Owerwiev)
<p align="center">
<img title="Allure Graphics" src="images/screens/ScreenshotAllure1.jpg" alt="Allure Graphics">
</p>

###### Страница с проведенными тестами (Suites)
<p align="center">
<img title="Allure Graphics" src="images/screens/ScreenshotAllure2.jpg" alt="Allure Graphics">
</p>

## :watermelon: Видео прохождения тестов
К каждому тесту (в отчете) прилагается автоматически сгенерированное Selenoid видео. Пример:
<p align="center">
  <img title="Selenoid Video" src="images/screens/VideoExample.gif" alt="Video">
</p>

## :bellhop_bell: Отчет в Telegram (IN WORK)
После завершения сборки специальный Telegram-бот отправляет сообщение с отчетом о прогоне тестов.
Чтобы видеть сообщения, вступите (временно) в телеграмм-группу `OlgaKos Bot_Group`

Пример поста от бота:
<p align="center">
<img title="Telegram Bot" src="images/screens/ScreenshotTelegram.jpg" alt="Telegram Bot">
</p>
----------
version 01 - add 5 easy tests
<br>version 02 - add Page Object Pattern
<br>version 03 - add local Allure. Some fix.
<br>version 04 - branch `jenkins_add`. Add Jenkins with remote Allure.
