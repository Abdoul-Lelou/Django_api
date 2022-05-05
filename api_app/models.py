from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

    username = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique = True)
    tel = models.CharField( max_length=9, unique= True)
    is_archive = models.BooleanField()
    last_login = models.DateTimeField(auto_now= True)
    is_superuser = models.BooleanField(default= False)
    image = models.ImageField(upload_to ='uploads/', default='')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name','tel','role']

    def __str__(self):
      return "{}".format(self.email)

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})



    
class Cour(models.Model):

    nom = models.CharField(max_length=50, unique= True)
    created_at = models.DateTimeField( auto_now_add=True)
    description = models.CharField( max_length=500)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='user')
    date_cour = models.DateField( auto_now=False, auto_now_add=False)
    status = models.BooleanField(default= False)

    class Meta:
        unique_together = ('nom', 'description')
       

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("Cours_detail", kwargs={"pk": self.pk})

    def __unicode__(self):
        return '%d: %s' % (self.nom, self.description)    







class ArchiveUser(models.Model):

    created_at=models.DateTimeField( auto_now_add=True)
    user=models.ForeignKey('User', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("Archiveuser_detail", kwargs={"pk": self.pk})
    class Meta:
        unique_together = ('user',)


class ArchiveCour(models.Model):

    created_at=models.DateTimeField( auto_now_add=True)
    cour=models.ForeignKey("Cour", on_delete=models.CASCADE, related_name='cour')

    def get_absolute_url(self):
        return reverse("Archivecour_detail", kwargs={"pk": self.pk})

    class Meta:
        unique_together = ('cour',)

