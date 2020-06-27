# koshelec_testForAPI
Tests API Site

В данном репозитории 3 файла .py:
  1) getData - получение данных о 10 тикерах, просчет времени ответа от сервера, просчет размера полученных данных, нахождение информации об актуальности данных;
  2) test1 - cравнивание полученных данных с заданными условиями (ответ от ресурса < 500 мс, информация о валюте актуальна, размер пакета данных < 10 кб);
  3) test2. К сожалению, не совсем понял как сделать вторую часть задания.
  
Для запуска теста необходимо в командной строке (или аналог) перейти в каталог с файлами (вместо перехода в необходимый каталог можно указать путь к файлу) и запустить его с помощью написания одной из следующих строк:
   1) python -m unittest test1.TestAPI (Запуск отдельного класса с тестами. Таким же образом можно запускать отдельные методы)
   2) python -m unittest test1 (Запуск модуля с тестами)
   3) python -m unittest -v test1 (С помощью флага -v можно получить более детальный отчёт)
   4) python test1.py
  
В коде присутствуют разъяснительные комментарии.
