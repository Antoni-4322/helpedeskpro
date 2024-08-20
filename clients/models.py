from django.db import models


class Clients(models.Model):
    name = models.CharField(max_length=65)
    status = models.CharField(
        default='I',
        max_length=1,
        choices=(
            ('I', 'Inativo'),
            ('A', 'Ativo'),
            ('P', 'Pendente'),
        ),

    )
    telephone = models.IntegerField(null=True)
    sub_id = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)        

    def __str__(self): 
        full_path = [self.name]                  
        k = self.sub_id

       
     
        while k is not None:
            full_path.append(k.name)
            
            k = k.sub_id
            print(full_path)
        
        return ' -> '.join(full_path[::-1])  
        

   
           
    
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'