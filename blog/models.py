#FEATURES:
    #Create/Edit blog post(admin)
    #View blog post(public)
    # Comment on a blog post(anonymous)
    # Store anonymoues user details in session
    # Show month based blog archives
    # Generate RSS Feed

##MODELS USED
    #POST
        #title
        # Text content
        # slug
        # Created date
        # Author
    #COMMENT
        #name
        #website
        #Email
        #text Content
        #Post Related
        # Created Date

from django.db import models
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    text=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        retunr ('blog_post_detail',(),
                {
                    'slug':self.slug,
                })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    name=models.CharField(max_length=42)
    email=models.EmailField(max_length=75)
    website=models.URLField(max_length=200, null=True)
    text=models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.text

