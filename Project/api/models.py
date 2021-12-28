from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Snippet(models.Model):
    """Model definition for Snippet."""

    # TODO: Define fields here
    text = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    UserInfo = models.ForeignKey(User, on_delete=models.CASCADE)
    TagInfo = models.ForeignKey('api.Tag', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Snippet."""

        verbose_name = 'Snippet'
        verbose_name_plural = 'Snippets'

    def __str__(self):
        """Unicode representation of Snippet."""
        return "{}".format(self.TagInfo.title)


class Tag(models.Model):
    """Model definition for Tag."""

    title = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return "{}".format(self.title)

    def get_absolute_url(self):
        return "/api/v1/snippet/{}".format(self.id)