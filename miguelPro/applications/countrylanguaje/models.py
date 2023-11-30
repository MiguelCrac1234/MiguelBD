from django import models

#create my model of countrylanguaje
class city(models.model):
    LANGUAJE = models.CharField('LANGUAJE', max_length=30)
    ISOFICIAL = models.Enum('ISOFICIAL', default=False)
    PERCENTAGE = models.Decimal('PERCENTAGE', max_length=4.0)
    VARIATIONS = models.CharField('VARIATIONS', max_length=20)
    DIALECTS = models.CHarField('DIALECTS', max_length=20)
    MORPHOLOGY = models.CharField('MORPHOLOGY', max_length=20)
    COUNTRYLANGUAJE = models.CharField('COUNTRYLANGUAJE', max_length=20)
    search_fields = ('COUNTRYLANGUAJE',)
    list_filter = ('COUNTRYLANGUAJE',)
    class Meta:
            verbose_name = 'LANGUAJE'
            verbose_name_plural = 'LANGUAJES'
            ordering = ['LANGUAJE']
            unique_together = ('LANGUAJE', 'COUNTRYLANGUAJE')
    def __str__(self):
        return self.LANGUAJE + ' - ' + self.COUNTRYLANGUAJE + ' - ' + self.ISOFICIAL + ' - ' + self.PERCENTAGE + str(self.COUNTRYCODE)