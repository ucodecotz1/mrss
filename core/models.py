from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

PROBLEM_TYPE = (
    ('H', 'Hardware problem'),
    ('S', 'Software problem'),
    ('N', 'Network problem'),
)


class Problems(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='Pro_image', null=True, blank=True)
    # Problem_code = models.CharField(max_length=200, null=True, blank=True)
    problem_type = models.CharField(max_length=200,
                                    choices=PROBLEM_TYPE, null=True, blank=True)
    # solution = models.TextField(null=True, blank=True)
    slug = models.SlugField()
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Problems'

    def __str__(self):
        return self.title


class Solution(models.Model):
    problem_id = models.ForeignKey(Problems,
                                   on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Solutions'

    def __str__(self):
        return self.user.username


class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.TextField(null=True,blank=True)
    solution_id = models.ForeignKey(Solution, on_delete=models.CASCADE,
                                    null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.user.username
