#!/bin/bash
sleep 20
alembic revision --autogenerate -m "initial migration"
alembic upgrade head

python3 main.py
