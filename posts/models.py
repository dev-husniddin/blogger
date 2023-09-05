from django.db import models
from users.models import CustomUser  
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill

class Post(models.Model):
    title = models.CharField("Title", max_length=255)
    content = models.TextField("Content")
    author = models.ForeignKey(
        CustomUser,  
        on_delete=models.CASCADE,  
        verbose_name="Author",
        related_name="posts"  
    )
    image = ProcessedImageField(
        upload_to="posts/images",
        processors=[ResizeToFill(800, 600)],  
        format="JPEG",  
        options={"quality": 90},  
        blank=True,  
        null=True,
    )
    created_at = models.DateTimeField("Creation Date", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
