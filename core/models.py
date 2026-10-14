from django.db import models

# Create your models here.


class TimeStampedMode(models.Model):
    """Guarda quando o registro foi criado e quando foi a alterado pela ultima vez."""
    
    created = models.DateTimeField('criado em', auto_now_add=True) 
    modified = models.DateTimeField('modificado em', auto_now=True)
    
    class Meta:
        astract = True
        
        
class ActiveMode(modeels.Model):
    """ Permite desativar um registro sem apaga-lo do banco."""
    
    active = models.BooleanField('ativo', default=true)
    
    class Meta:
        abstract = True

