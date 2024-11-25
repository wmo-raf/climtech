# Generated by Django 5.0.9 on 2024-11-25 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
        ("images", "0001_initial"),
        ("wagtailcore", "0094_alter_page_locale"),
        ("wagtailmedia", "0004_duration_optional_floatfield"),
    ]

    operations = [
        migrations.AddField(
            model_name="contentpage",
            name="listing_image",
            field=models.ForeignKey(
                blank=True,
                help_text="Image to display along with summary, when this page is linked from elsewhere in the site.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.climtechimage",
            ),
        ),
        migrations.AddField(
            model_name="contentpage",
            name="social_image",
            field=models.ForeignKey(
                blank=True,
                help_text="Image to appear alongside 'Meta description', particularly for sharing on social networks",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.climtechimage",
                verbose_name="Meta image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="listing_image",
            field=models.ForeignKey(
                blank=True,
                help_text="Image to display along with summary, when this page is linked from elsewhere in the site.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.climtechimage",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="social_image",
            field=models.ForeignKey(
                blank=True,
                help_text="Image to appear alongside 'Meta description', particularly for sharing on social networks",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.climtechimage",
                verbose_name="Meta image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="video",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailmedia.media",
            ),
        ),
        migrations.AddField(
            model_name="themesetting",
            name="site",
            field=models.OneToOneField(
                editable=False,
                on_delete=django.db.models.deletion.CASCADE,
                to="wagtailcore.site",
            ),
        ),
    ]
