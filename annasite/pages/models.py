from django.db import models


class AbstractPage(models.Model):
    slug = models.SlugField(
        max_length=255,
        null=False,
    )
    title = models.CharField(
        max_length=255,
    )
    meta_description = models.CharField(
        max_length=255,
    )
    meta_keywords = models.CharField(
        max_length=255,
    )

    def __unicode__(self):
        return self.title


class SiteNavigation(models.Model):
    link = models.CharField(
        max_length=255,
    )
    link_title = models.CharField(
        max_length=255,
    )

    def __unicode__(self):
        return 'Link item: {0}'.format(self.link_title)