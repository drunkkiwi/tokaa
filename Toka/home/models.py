from django.db                           import models
from home                                import choices as ch
from django.template.defaultfilters      import slugify


class NewsArticle(models.Model):

    def __str__(self):
        return self.article_title

    article_author       = models.CharField(max_length=250)
    article_title        = models.CharField(max_length=250)
    article_body         = models.TextField(blank=False, null=False)
    article_category     = models.CharField(max_length=1, choices=ch.NEWS_CHOICE)
    article_slug         = models.SlugField(blank=True, max_length=300)
    article_image        = models.ImageField(upload_to='article_image')
    article_creation     = models.DateTimeField(auto_now_add=True)
    article_update       = models.DateTimeField(auto_now=True)
    article_created_at   = models.DateTimeField(auto_now_add=True)
    article_updated_at   = models.DateTimeField(auto_now=True)
    article_views        = models.IntegerField(default=0)


    def save(self, *args, **kwargs):
        if not self.id:

            # Newly created object, so set slug
            self.article_slug = slugify(self.article_title)

        super(NewsArticle, self).save(*args, **kwargs)
