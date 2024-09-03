from django.db import migrations, models
from django.db.models import F


def import_data_to_new_fields(apps, schema_editor):
    Person = apps.get_model('people', 'Person')

    Person.objects.update(first_name=F('fullname').split(';')[0].split(':')[-1])
    Person.objects.update(last_name=F('fullname').split(';')[-1].split(':')[-1])
    Person.objects.update(id_code=sorted(F('information').split(';'))[2].split(':')[-1])
    Person.objects.update(born_in=sorted(F('information').split(';'))[1].split(':')[-1])
    Person.objects.update(birth_year=int(sorted(F('information').split(';'))[0].split(':')[-1]))


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birth_year',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='born_in',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='id_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.RunPython(
            import_data_to_new_fields,
            reverse_code=migrations.RunPython.noop
        ),
        migrations.RemoveField('Person', 'fullname'),
        migrations.RemoveField('Person', 'information'),
        migrations.AlterField('Person',
                              'first_name',
                              models.CharField(max_length=30)),
        migrations.AlterField('Person',
                              'last_name',
                              models.CharField(max_length=50)),
        migrations.AlterField('Person',
                              'id_code',
                              models.CharField(max_length=10)),
        migrations.AlterField('Person',
                              'born_in',
                              models.CharField(max_length=30)),
        migrations.AlterField('Person',
                              'birth_year',
                              models.PositiveSmallIntegerField())
    ]
