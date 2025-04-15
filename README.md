# Django-log-analytics

Консольное приложение для просмотра логов

## Установка
~~~bash
git clone https://github.com/Rebarial/Django-log-analytics

cd Django-log-analytics

~~~

По желанию создайте виртуальное окружение

Windows:
~~~bash
python -m venv venv

venv\Scripts\activate
~~~
Linux/macOS:
~~~bash
python3 -m venv venv

source venv/bin/activate
~~~
Установите зависимости
~~~bash
pip install -r requirements.txt
~~~
Пример комманды для запуска на тестовых логах
~~~bash
python app/main.py --report handlers logs/app1.log logs/app2.log logs/app3.log
~~~




![image](https://github.com/user-attachments/assets/2cb889e9-264c-489a-af94-dd91a21d5958)

![image](https://github.com/user-attachments/assets/dff24139-838a-47ef-a04b-7241631493b2)
