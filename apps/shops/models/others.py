from django.db.models import CharField, Model, PositiveSmallIntegerField


class Country(Model):  # ✅
    name = CharField('Nomi', max_length=100)
    code = CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Davlat'
        verbose_name_plural = 'Davlatlar'


class Language(Model):  # ✅
    title = CharField('Nomi', max_length=50)
    code = CharField('Kodi', max_length=10)
    icon = CharField('Belgisi', max_length=10)


class Currency(Model):  # ✅
    name = CharField('Nomi', max_length=100)
    order = PositiveSmallIntegerField('Rangi', default=1, db_default=1)

    class Meta:
        verbose_name = 'Pul birligi'
        verbose_name_plural = 'Pul birliklari'

    def __str__(self):
        return self.name


class TemplateColor(Model):  # ✅
    name = CharField('Nomi', max_length=55)
    color = CharField('Rangi', max_length=55)

    class Meta:
        verbose_name = 'Shablon rangi'
        verbose_name_plural = 'Shablon ranglari'

    def __str__(self):
        return self.name


class Weight(Model):  # ✅
    name = CharField(max_length=10)


class Length(Model):  # ✅
    name = CharField(max_length=10)
