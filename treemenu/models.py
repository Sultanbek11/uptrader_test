from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.title
