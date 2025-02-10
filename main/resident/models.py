from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Flat(models.Model):
    number = models.CharField("Номер квартири", max_length=3) # по принципу 101, 102, 103...
    floor = models.CharField("Поверх", max_length=9) # максимум 9 поверхів

    room_amount = models.CharField("Кількість кімнат", max_length=3) # одно-трьох кімнатні
    bought = models.BooleanField(verbose_name="Куплена (так/ні)") # або куплена, або орендована (так/ні)
    residents_amount = models.IntegerField("Кількість мешканців", default=0)

    def __str__(self):
        return self.number


class Resident(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, verbose_name="Квартира", related_name="residents")
    name = models.CharField("Ім'я", max_length=25)
    surname = models.CharField("Фамілія", max_length=50)
    phone_number = models.CharField("Номер телефону", max_length=19, unique=True)

    username = models.CharField("Username", max_length=50, blank=True, null=True)
    password = models.CharField("Пароль", max_length=19)

    has_pet = models.BooleanField(default=False, verbose_name="Маю улюбленця") # або має улюбленця, або не має улюбленця (так/ні)
    pet_type = models.CharField("Вид улюбленця", max_length=50, blank=True, null=True)
    has_car = models.BooleanField(default=False, verbose_name="Маю машину") # або є машина, або нема (так/ні)
    car_model = models.CharField("Модель машини", max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number', 'name', 'surname', 'flat']

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = f"{self.name} {self.surname}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.surname} ({self.flat})" # Ім'я Фамілія (№101)