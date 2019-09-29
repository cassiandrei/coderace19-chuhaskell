#!/bin/bash

# Script utilizado para criar o banco de dados
# O banco de dados atual sera removido!!!

# Cria a pasta para armazenar o repositorio
mkdir /var/lib/fende
chmod -R 777 /var/lib/fende

#Logs
mkdir ../logs
touch ../logs/main.log
chmod 777 ../logs/main.log

# inicia Repository Manager
python ../repository/manager/server.py &

# remove os repositorios locais
rm -rf /var/lib/fende/*

# remove todos os arquivos de migração
echo -n "Removendo arquivos de migração... "
find . -path "../*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "../*/migrations/*.pyc" -delete
echo "OK"

# remove o banco de dados atual
echo -n "Removendo banco de dados... "
rm "../db.sqlite3"
echo "OK"

# cria novamente o banco de dados
echo "Recriando banco de dados... "
python ../manage.py makemigrations
python ../manage.py migrate

# popula o banco de dados
echo "Populando o banco de dados... "
python ../manage.py shell < populator.py
echo "OK"

# corrige as permissões do banco de dados
chmod uog+w ../db.sqlite3 

pkill -f ../repository/manager/server.py

echo "\nBanco de dados recriado com sucesso."

# atualizando aplicativo watson
python ../manage.py installwatson
python ../manage.py buildwatson