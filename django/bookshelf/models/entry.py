from django.db import models

from .category import Category


class Entry(models.Model):

    category = models.ForeignKey(
        Category, related_name="entries", on_delete=models.CASCADE
    )

    content = models.FileField(upload_to="entries/%Y/%m/%d/")
