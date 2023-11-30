from django import models

#create my model of city
class city(models.model):
    NAME = models.CharField('NAME', max_length=35)
    COUNTRYCODE = models.CharField(
        'siglaDepartamento', max_length=2, unique=True)
    DISTRICT = models.Int('DISTRICT', default=False)
    POPULATION = models.BigInt('POPULATION', max_length=20)
    DIRECTION = models.CharField('DIRECTION', max_length=35)
    POSTALCODE = models.BigInt('POSTALCODE', max_length=10)
    NEIGHBORHOOD = models.CharField('NEIGHBORHOOD', max_length=35)
    search_fields = ('nombreDepartamento', 'siglaDepartamento',)
    list_filter = ('nombreDepartamento',)
    class Meta:
            verbose_name = 'NAME'
            verbose_name_plural = 'NAMES'
            ordering = ['NAME']
            unique_together = ('NAME', 'COUNTRYCODE')
    def __str__(self):
        return self.NAME + ' - ' + self.COUNTRYCODE + ' - ' + self.DISTRICT + ' - ' + self.POPULATION + str(self.id)