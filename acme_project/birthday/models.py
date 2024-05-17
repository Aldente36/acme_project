from django.db import models


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    birthday = models.DateField('Дата рождения')
    
# class Contest(models.Model):
#     title = models.TextField('Название', max_length=20)
#     description = models.TextField('Описание', max_length=20)
#     price = models.IntegerField(
#         'Цена', validators=[MinValueValidator(1), MaxValueValidator(9)], help_text='Рекомендованная розничная цена'
#     )
#     comment = models.TextField(
#         'Комментарий', blank = False
#     )