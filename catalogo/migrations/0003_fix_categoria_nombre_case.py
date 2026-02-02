from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ("catalogo", "0002_fix_column_names"),
    ]

    operations = [
        migrations.RunSQL(
            sql='''
                ALTER TABLE catalogo_categoria
                RENAME COLUMN "Nombre" TO nombre;
            ''',
            reverse_sql='''
                ALTER TABLE catalogo_categoria
                RENAME COLUMN nombre TO "Nombre";
            '''
        ),
    ]
