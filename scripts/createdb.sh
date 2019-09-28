#!/bin/bash

# Script utilizado para criar o banco de dados
# O banco de dados atual sera removido!!!

# remove todos os arquivos de migração
echo -n "Removendo arquivos de migração... "
for f in `find .. -name migrations`; do ls $f/0*py; done
for f in `find .. -name migrations`; do ls $f/0*pyc; done
echo "OK"

# remove o banco de dados atual
echo -n "Removendo banco de dados... "
rm -f "../db.sqlite3"
echo "OK"

# cria novamente o banco de dados
echo "Recriando banco de dados... "
python3 ../manage.py makemigrations
python3 ../manage.py migrate

# popula o banco de dados
echo "Populando o banco de dados... "
python3 ../manage.py shell < populate_database.py
echo "OK"

# corrige as permissões do banco de dados
chmod uog+w ../db.sqlite3 

pkill -f ../repository/manager/server.py

echo "\nBanco de dados recriado com sucesso."
