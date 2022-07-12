from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=80)
    status = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


