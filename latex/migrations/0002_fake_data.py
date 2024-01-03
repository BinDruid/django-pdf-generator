from django.db import migrations


def add_sample_data(apps, schema_editor):
    Staff = apps.get_model("latex", "Staff")
    db_alias = schema_editor.connection.alias
    Staff.objects.using(db_alias).bulk_create(
        [
            Staff(first_name="علی", last_name="محمدی", salary=2500, role="C"),
            Staff(first_name="حسن", last_name="طاهری", salary=1200, role="E"),
            Staff(first_name="محمد", last_name="اصغری", salary=1800, role="M"),
        ]
    )


def remove_sample_data(apps, schema_editor):
    Staff = apps.get_model("latex", "Staff")
    db_alias = schema_editor.connection.alias
    Staff.objects.using(db_alias).all().delete()

class Migration(migrations.Migration):
    dependencies = [("latex", "0001_initial"),]

    operations = [
        migrations.RunPython(add_sample_data, remove_sample_data),
    ]
