from django import models

#create my model of countrylanguaje
class city(models.model):
    NAME = models.CharField('NAME', max_length=30)
    CONTINENT = models.Enum('CONTINENT', default=False)
    REGION = models.Decimal('REGION', max_length=4.0)
    SURFACEAREA = models.CharField('SURFACEAREA', max_length=20)
    INDEPYEAR = models.CHarField('INDEPYEAR', max_length=20)
    POPULATION = models.CharField('POPULATION', max_length=20)
    LIFEEXPECTANCY = models.CharField('LIFEEXPECTANCY', max_length=20)
    GNP = models.CharField('GNP', max_length=20)
    GNPOLD = models.CharField('GNOPOLD', max_length=20)
    LOCALNAME = models.CharField('LOCALNAME', max_length=20)
    GOVERNMENTFORM = models.CharField('GOVERNMENTFORM', max_length=20)
    HEADOFSTATE = models.CharField('HEADOFSTATE', max_length=20)
    CAPITAL = models.CharField('CAPITAL', max_length=20)
    CODE2 = models.CharField('CODE2', max_length=20)
    INFRAESTRUCTURE = models.CharField('INFRAESTRUCTURE', max_length=20)
    DEMOGRAPHY = models.CharField('DEMOGRAPHY', max_length=20)
    CULTURE = models.CharField('CULTURE', max_length=20)
    ID_IBFK = models.CharField('ID_IBFK', max_length=20)
    search_fields = ('NAME', 'CONTINENT','ID_IBFK',)
    list_filter = ('ID_IBFK',)
    class Meta:
            verbose_name = 'NAME'
            verbose_name_plural = 'NAMES'
            ordering = ['NAME']
            unique_together = ('NAME', 'ID_IBFK')
    def __str__(self):
        return self.NAME + ' - ' + self.CONTINENT + ' - ' + self.REGION + ' - ' + self.SURFACEAREA + str(self.COUNTRYLANGUAJE)