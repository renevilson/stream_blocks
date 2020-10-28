# stream blocks
Бот для отслеживания статуса ресурса. Изначально, проект задумывался как сервис для отслеживания блокировки зеркал. 
Написан на python3.8. В качестве инструмента для создания бота используется асинхронная библиотека aiogram. Данные о 
пользователях, доменах, чатах хранятся в postgres. Для работы с базой данных используется ORM SQLAlchemy. На данный
момент бот доступен @streamblocks_bot

### Технологии
1. python3.8
2. База данных postgres.
3. ORM SQLAlchemy
4. Aiogram

### Возможности
- [x] Для старта: ```/start```
- [x] Для добавления домена: ```/add domain```
- [x] Для просмотра списка отслеживаемых доменов: ```/all```
- [x] Для удаления из списка отслеживаемых доменов: ```/remove domain```

### Запуск проекта
> Приложение использует Docker, docker-compose.
>
> Образ находится в публичном registry https://hub.docker.com/repository/docker/renevilson/stream_blocks
> 
> Для получения образа ```docker pull renevilson/stream_blocks```. 
>
> Для запуска приложения ```docker-compose -f docker-compose.yml up -d```.
>
> Для сборки приложения ```docker-compose build```.
>
> Для того чтобы запушить в репозиторий ```docker-compose push```.
