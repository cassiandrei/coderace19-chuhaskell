import names
from random import shuffle, randint, random, randrange
from datetime import datetime
from django.core.files import File  # you need this somewhere
from user.models import User, Guia, Turista, Especialidade, Avaliacao, Pais, Estado, Cidade


SPECIALITIES = ("Tradução","Direção","Assistência a Pessoas com Deficiência","Cultura","Aventura","Ecoturismo","Praia","Baladas")
GENDERS = ("male","female")

LOCAIS = {
    "Brazil" : {
        "RS" : ["Santa Maria", "Porto Alegre"],
        "SP" : ["São Paulo", "Campinas"],
        "RJ" : ["Rio de Janeiro", "Petrópolis"],
        "SC" : ["Florianópolis", "Chapecó"]
    }
}

print("Criando Locais...")
locais = []
for pais, estados in LOCAIS.items():
    pais_obj = Pais.objects.create(nome=pais)
    pais_obj.save()
    for estado, cidades in estados.items():
        estado_obj = Estado.objects.create(nome=estado, pais=pais_obj)
        estado_obj.save()
        for cidade in cidades:
            cidade_obj = Cidade.objects.create(
                nome   = cidade, 
                estado = estado_obj,
                image  = "cidades/{p}_{e}_{c}.jpg".format(p=pais,e=estado,c=cidade).replace(" ", "_"),
                descricao = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            )
            cidade_obj.save()
            locais.append(cidade_obj)


print("Criando especialidades...")
espec_list = []
for espec in SPECIALITIES:
    espec_obj = Especialidade.objects.create(descricao=espec, tipo='chat')
    espec_obj.save()
    espec_list.append(espec_obj)

print("Criando Super Usuário...")
User.objects.create_superuser(
    first_name = "Chuhaskell",
    last_name = "Endgame",
    email = "jvlima@inf.ufsm.br",
    password = "teste1234"
).save()

print("Criando guias e associando com especialidades...")
guia_list = []
for i in range(20):
    genero = GENDERS[randrange(2)]
    name = names.get_full_name(gender=genero)
    first_name = name.split()[0]
    last_name  = name.split()[1]

    guia_obj = Guia.objects.create(
        user = User.objects.create(
            first_name  = first_name,
            last_name   = last_name,
            email       = first_name.lower() + "_" + last_name.lower() + "@gmail.com", 
            password    = "123",
            telefone    = "+55559" + str(randint(0,99999999)).rjust(8, "0"),
            nascimento  = datetime(randint(1940, 2000), randint(1, 12), randint(1, 28)),
            genero      = genero,
            cidade      = locais[randrange(len(locais))],
            image       = "users/{g}{i}.jpg".format(
                g = "w" if genero == "female" else "m",
                i = randrange(8)
            )
        ), 
        preco = 20 + random() * 30
    )

    # associa com especialidade
    shuffle(espec_list)
    random_especs = espec_list[:randint(1,5)]
    for espec_obj in random_especs:
        guia_obj.especialidades.add(espec_obj)
    
    guia_obj.save()
    guia_list.append(guia_obj)

print("Criando turistas e avaliações...")
for i in range(20):
    genero = GENDERS[randrange(2)]
    name = names.get_full_name(gender=genero)
    first_name = name.split()[0]
    last_name  = name.split()[1]

    turista_obj = Turista.objects.create(
        user = User.objects.create(
            first_name  = first_name,
            last_name   = last_name,
            email       = first_name.lower() + "_" + last_name.lower() + "@gmail.com", 
            password    = "123",
            telefone    = "+55559" + str(randint(0,99999999)).rjust(8, "0"),
            nascimento  = datetime(randint(1940, 2000), randint(1, 12), randint(1, 28)),
            genero      = genero,
            cidade      = locais[randrange(len(locais))],
            image       = "users/{g}{i}.jpg".format(
                g = "w" if genero == "female" else "m",
                i = randrange(8)
            )
        )
    )
    turista_obj.save()
        
    shuffle(guia_list)
    random_guias = guia_list[:randint(1,5)]
    for guia_obj in random_guias:
        rate_obj = Avaliacao.objects.create(
            guia        = guia_obj,
            turista     = turista_obj,
            nota        = randint(1, 5),
            comentario  = "Pessoa muito atenciosa, porém pouca atenção aos detalhes."
        )
        rate_obj.save()