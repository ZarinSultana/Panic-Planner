from django.db import models


class Resource(models.Model):
    class Category(models.TextChoices):
        MENTAL_HEALTH = 'mental_health', 'Mental Health'
        EMERGENCY = 'emergency', 'Emergency Contacts'
        SELF_HELP = 'self_help', 'Self Help'
        ARTICLES = 'articles', 'Articles'
        HOTLINE = 'hotline', 'Hotlines'
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    category = models.CharField(
        max_length=50,
        choices=Category.choices,
        default=Category.MENTAL_HEALTH,
    )
    is_emergency = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-is_emergency', 'title']