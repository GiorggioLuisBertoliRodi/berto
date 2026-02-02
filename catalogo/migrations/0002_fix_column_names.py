from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ("catalogo", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                ALTER TABLE catalogo_producto
                RENAME COLUMN categoria_id_id TO categoria_id;
            """,
            reverse_sql="""
                ALTER TABLE catalogo_producto
                RENAME COLUMN categoria_id TO categoria_id_id;
            """
        ),
    ]
