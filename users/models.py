from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    picture = models.ImageField('Аватар', upload_to='profile_pics/', blank=True, null=True)
    description = models.TextField('Описание', max_length=500, blank=True, null=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')

    class Meta:
        db_table = 'profiles'

    def __str__(self) -> str:
        return self.user.username
