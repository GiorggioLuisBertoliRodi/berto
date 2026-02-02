from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ("catalogo", "0002_initial.py"),
    ]

    operations = [
        migrations.RunSQL(
            sql='''
            ALTER TABLE catalogo_producto RENAME COLUMN "Nombre" TO nombre;
            ALTER TABLE catalogo_categoria RENAME COLUMN "Nombre" TO nombre;
            ''',
            reverse_sql='''
            ALTER TABLE catalogo_producto RENAME COLUMN nombre TO "Nombre";
            ALTER TABLE catalogo_categoria RENAME COLUMN nombre TO "Nombre";
            '''
        )
    ]
