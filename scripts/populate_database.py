import names, random
from django.utils import timezone
# from accounts.models import Guia, Turista

GENDERS = ("male","female")
SPECIALITIES = ("translation","driving","disable-assistance","culture","adventure","ecotourism","beach","night-life")

class RandomUser:
    def __init__(self):
        self.genero = GENDERS[random.randint(0, 1)]
        self.name = names.get_full_name(genero=self.genero)
        self.data_nascimento = timezone()
        # self.birth_day = random.randint(1, 28)
        # self.birth_month = random.randint(1, 12)
        # self.birth_year = random.randint(1940, 2000)
        self.country = "Brazil"
        self.state = "RS"
        self.city = "Santa Maria"
        self.email = self.name.split()[0].lower() + "_" + self.name.split()[-1].lower() + "@gmail.com"
        self.phone = "+55559" + str(random.randint(0,99999999)).rjust(8, "0")
        self.password = "123"

class RandomGuide(RandomUser):
    def __init__(self):
        RandomUser.__init__(self)
        self.price = 20 + random.random() * 30
        self.social_number = str(random.randint(0,99999999999)).rjust(11, "0")

class RandomTourist(RandomUser):
    pass

# cria guias
for i in range(20):
    RandomGuide()
    new_user = User.objects.create_user(user['username'], password=user['password'], email=user['email'])
    guia = Guia.objects.create(user=new_user, preco=5.00)
    guia.save()