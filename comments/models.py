from django.db import models
from users.models import CustomUser  
from posts.models import Post  

class Comment(models.Model):
    content = models.TextField("Content")
    author = models.ForeignKey(
        CustomUser,  
        on_delete=models.CASCADE,  
        verbose_name="Author",
        related_name="comments"  
    )
    post = models.ForeignKey(
        Post,  
        on_delete=models.CASCADE,  
        verbose_name="Post",
        related_name="comments"  
    )
    created_at = models.DateTimeField("Creation Date", auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}: {self.content[:50]}" 

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
