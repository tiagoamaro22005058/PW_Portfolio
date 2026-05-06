from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver


@receiver(post_save, sender=User)
def adicionar_grupo_autores(sender, instance, created, **kwargs):
    if created:
        grupo, _ = Group.objects.get_or_create(name='autores')
        instance.groups.add(grupo)
