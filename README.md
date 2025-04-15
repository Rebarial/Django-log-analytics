# Django-log-analytics

Консольное приложение для просмотра логов django проектов

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




![image](https://github.com/user-attachments/assets/73d6938c-727b-41d6-a0bf-6d072234aa14)


![image](https://github.com/user-attachments/assets/910969a7-3977-4d31-9b21-71ac59f8bfcc)

