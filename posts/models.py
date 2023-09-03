from django.db import models
from users.models import CustomUser  # Импортируем модель CustomUser из приложения users
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill

class Post(models.Model):
    title = models.CharField("Title", max_length=255)
    content = models.TextField("Content")
    author = models.ForeignKey(
        CustomUser,  # Связываем с пользователем
        on_delete=models.CASCADE,  # Удалить пост, если пользователь будет удален
        verbose_name="Author",
        related_name="posts"  # Позволяет обращаться к постам пользователя через user.posts
    )
    image = ProcessedImageField(
        upload_to="posts/images",
        processors=[ResizeToFill(800, 600)],  # Размер изображения
        format="JPEG",  # Формат изображения
        options={"quality": 90},  # Качество изображения
        blank=True,  # Поле может быть пустым
        null=True,
    )
    created_at = models.DateTimeField("Creation Date", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
