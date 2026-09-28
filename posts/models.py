from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

class ImagePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="post_images")
    caption = models.CharField(max_length=200, blank=True)


# class Comments(models.Model):
#     post = models.ForeignKey(Post, models.CASCADE, related_name='comments')
#     # authorid = models.ForeignKey()
#     content = models.TextField()
#     date_created = models.DateTimeField()