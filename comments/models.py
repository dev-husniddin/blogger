from django.db import models
from users.models import CustomUser  # Импортируем модель CustomUser из приложения users
from posts.models import Post  # Импортируем модель Post из приложения posts

class Comment(models.Model):
    content = models.TextField("Content")
    author = models.ForeignKey(
        CustomUser,  # Связываем с пользователем
        on_delete=models.CASCADE,  # Удалить комментарий, если пользователь будет удален
        verbose_name="Author",
        related_name="comments"  # Позволяет обращаться к комментариям пользователя через user.comments
    )
    post = models.ForeignKey(
        Post,  # Связываем с постом
        on_delete=models.CASCADE,  # Удалить комментарий, если пост будет удален
        verbose_name="Post",
        related_name="comments"  # Позволяет обращаться к комментариям поста через post.comments
    )
    created_at = models.DateTimeField("Creation Date", auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}: {self.content[:50]}"  # Отображаем часть контента

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
