# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_extensions.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Conference",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last Modified At"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Conference Name"),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        editable=False,
                        populate_from=("name",),
                        max_length=255,
                        blank=True,
                        unique=True,
                    ),
                ),
                ("description", models.TextField(default="")),
                ("start_date", models.DateField(verbose_name="Start Date")),
                ("end_date", models.DateField(verbose_name="End Date")),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        verbose_name="Current Status",
                        choices=[
                            (1, b"Accepting Call for Proposals"),
                            (2, b"Closed for Proposals"),
                            (3, b"Accepting Votes"),
                            (4, b"Schedule Published"),
                        ],
                    ),
                ),
                (
                    "deleted",
                    models.BooleanField(default=False, verbose_name="Is Deleted?"),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        related_name="created_conference_set",
                        verbose_name="Created By",
                        blank=True,
                        on_delete=models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        null=True,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        related_name="updated_conference_set",
                        verbose_name="Modified By",
                        blank=True,
                        on_delete=models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        null=True,
                    ),
                ),
            ],
            options={"abstract": False},
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="ConferenceModerator",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last Modified At"
                    ),
                ),
                (
                    "active",
                    models.BooleanField(default=True, verbose_name="Is Active?"),
                ),
                (
                    "conference",
                    models.ForeignKey(
                        to="conferences.Conference", on_delete=models.deletion.CASCADE,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        related_name="created_conferencemoderator_set",
                        verbose_name="Created By",
                        blank=True,
                        on_delete=models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        null=True,
                    ),
                ),
                (
                    "moderator",
                    models.ForeignKey(
                        to=settings.AUTH_USER_MODEL, on_delete=models.deletion.CASCADE,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        related_name="updated_conferencemoderator_set",
                        verbose_name="Modified By",
                        blank=True,
                        on_delete=models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        null=True,
                    ),
                ),
            ],
            options={"abstract": False},
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="ConferenceProposalReviewer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last Modified At"
                    ),
                ),
                (
                    "active",
                    models.BooleanField(default=True, verbose_name="Is Active?"),
                ),
                (
                    "conference",
                    models.ForeignKey(
                        to="conferences.Conference", on_delete=models.deletion.CASCADE,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        related_name="created_conferenceproposalreviewer_set",
                        verbose_name="Created By",
                        blank=True,
                        on_delete=models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        null=True,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        related_name="updated_conferenceproposalreviewer_set",
                        verbose_name="Modified By",
                        blank=True,
                        on_delete=models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        null=True,
                    ),
                ),
                (
                    "reviewer",
                    models.ForeignKey(
                        to=settings.AUTH_USER_MODEL, on_delete=models.deletion.CASCADE,
                    ),
                ),
            ],
            options={},
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name="conferenceproposalreviewer",
            unique_together=set([("conference", "reviewer")]),
        ),
    ]
