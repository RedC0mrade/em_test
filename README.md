# Тестовый проек Effective_mobile

## Для развертывания проекта необходимо выполнить команды

- сборку проекта docker-compose up -d
- войти в контейнер docker exec -it fastapi_app /bin/bash 
- выполнить команду для миграций alembic revision --autogenerate -m "init db" и alembic upgrade head
- Для удобства работы с базой использован pgAdmin

P.S В связи с очень плотным графиком и некоторыми семейными обстоятельствами, я не смог уделить проекту достаточно времени. 
Я хотел связаться и попросить немного времени для дороботки, но профиль на HH был заблокирован. 
Все функции, валидация и бизнес логика работают, но хотелось бы уделить больше времени тестам

P.P.S Так как это тестовый проект я не стал убирать данные, которые должны быть в .env
