# Generated by Django 5.0.6 on 2024-06-20 17:28

import django.db.models.deletion
import taggit.managers
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.models.media
import wagtail.search.index
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_create_homepage"),
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
        ("wagtailcore", "0093_uploadedfile"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("doc", wagtail.documents.blocks.DocumentChooserBlock()),
                    ("text", wagtail.blocks.RichTextBlock()),
                ],
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="rich",
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="CustomDocument",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                ("file", models.FileField(upload_to="documents", verbose_name="file")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                ("file_size", models.PositiveIntegerField(editable=False, null=True)),
                (
                    "file_hash",
                    models.CharField(blank=True, editable=False, max_length=40),
                ),
                ("my", wagtail.fields.RichTextField()),
                (
                    "collection",
                    models.ForeignKey(
                        default=wagtail.models.media.get_root_collection_id,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailcore.collection",
                        verbose_name="collection",
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text=None,
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="tags",
                    ),
                ),
                (
                    "uploaded_by_user",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="uploaded by user",
                    ),
                ),
            ],
            options={
                "verbose_name": "document",
                "verbose_name_plural": "documents",
                "abstract": False,
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
    ]
