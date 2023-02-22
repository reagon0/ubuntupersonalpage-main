# Generated by Django 4.1 on 2023-02-11 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0002_book_coverimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("born", models.DateField()),
                ("death", models.DateField(blank=True, null=True)),
                ("biography", models.TextField(blank=True)),
                ("image", models.ImageField(upload_to="images")),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="ISBN",
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AddField(
            model_name="book",
            name="date_published",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="date_read",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="genre",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="pages",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="rating",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="coverimage",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
        migrations.AlterField(
            model_name="book",
            name="read_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="summary",
            field=models.TextField(
                blank=True,
                help_text="Enter a brief description of the book",
                max_length=5000,
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main_app.author"
            ),
        ),
    ]
