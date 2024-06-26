# Generated by Django 5.0.4 on 2024-05-22 04:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Organisation",
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
                ("website", models.URLField()),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="company_logos/"
                    ),
                ),
                ("contact_details", models.CharField(max_length=100, unique=True)),
                ("industry_type", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Job",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "work_location",
                    models.CharField(
                        choices=[
                            ("remote", "Remote"),
                            ("onsite", "Onsite"),
                            ("hybrid", "Hybrid"),
                        ],
                        default="onsite",
                        max_length=10,
                    ),
                ),
                (
                    "job_type",
                    models.CharField(
                        choices=[
                            ("part_time", "Part Time"),
                            ("full_time", "Full Time"),
                            ("internship", "Internship"),
                        ],
                        default="full_time",
                        max_length=10,
                    ),
                ),
                ("eligibility_criteria", models.TextField()),
                ("deadline", models.DateTimeField()),
                (
                    "stipend_salary",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("open", "Open"), ("closed", "Closed")],
                        default="open",
                        max_length=10,
                    ),
                ),
                ("openings", models.PositiveIntegerField(default=1)),
                ("custom_ques", models.JSONField(blank=True, null=True)),
                ("perks_benefits", models.TextField(blank=True, null=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="marketing.organisation",
                    ),
                ),
            ],
        ),
    ]
