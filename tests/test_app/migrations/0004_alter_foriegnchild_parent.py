# Generated by Django 4.1.5 on 2023-01-13 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("test_app", "0003_alter_foriegnchild_parent_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foriegnchild",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="foriegn_child",
                to="test_app.relationalparent",
            ),
        ),
    ]