from django.db import migrations


def criar_grupo_autores(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Artigo = apps.get_model('artigos', 'Artigo')

    grupo, _ = Group.objects.get_or_create(name='autores')
    ct = ContentType.objects.get_for_model(Artigo)
    perms = Permission.objects.filter(content_type=ct, codename__in=['add_artigo', 'change_artigo', 'view_artigo'])
    grupo.permissions.set(perms)


def remover_grupo_autores(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name='autores').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.RunPython(criar_grupo_autores, remover_grupo_autores),
    ]
