from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingUser = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRating = self.post_set.aggregate(postRat=Sum('rating'))
        pRat = 0
        pRat += postRating.get('postRat')

        commentRating = self.authorUser.comment_set.aggregate(comRat=Sum('ratingComment'))
        cRat = 0
        cRat += commentRating.get('comRat')

        self.ratingUser = pRat*3 + cRat
        self.save()


class Category(models.Model):

    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )
    category_type = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)


    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:123]} ...'

    def __str__(self):
        return f'{self.author.authorUser.username}, {self.title}, {self.text[:20]}, {self.category_type}'

class PostCategory(models.Model):
    postConnected = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryConnected = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    textComment = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    ratingComment = models.SmallIntegerField(default=0)

    def like(self):
        self.ratingComment += 1
        self.save()

    def dislike(self):
        self.ratingComment -= 1
        self.save()

