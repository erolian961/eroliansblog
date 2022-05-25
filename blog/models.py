# modelでデータの項目属性を指定　migrationsで変更指示　テーブル作成
# データベースの内容
# setting app の所に作成したら表記

from django.db import models
from django.utils import timezone
from django_quill.fields import QuillField
from markdown import markdown

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_markdown_text_as_html(self):
        """MarkDown記法で書かれたtextをHTML形式に変換して返す"""
        return markdown(self.content)

class ContentImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    content_image = models.ImageField(upload_to='post_content_images/')

class QuillPost(models.Model):
    content = QuillField()
