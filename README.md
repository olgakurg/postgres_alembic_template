#### Async sqlalchemy and alembic dockerized

###### What is it
Creates postgres db from sqlalchemy model with some alembic migrations in docker containers. Hints to repository pattern and DI. 

###### Build
```bash 
docker compose up --build -d
```

###### Notes
1. There is no sense in data and operation, it's just a conversation starter.
2. Alembic doesn't do well with postgres index,  this is [known issue](https://github.com/sqlalchemy/alembic/issues/1390).
###### TODO
1. add logging
2. add many-to-many demo.
3. add backoff
