from django.db import models
from django.conf import settings
from django.urls import reverse
from cms.models.pluginmodel import CMSPlugin
from tinymce_4.fields import TinyMCEModelField

class Presentation(CMSPlugin):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=100)
    description = models.CharField('Descrição', max_length=300)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('presentations-list', kwargs={'pk': self.pk})

    def get_author(self):
        name = self.author.first_name + " " + self.author.last_name
        return name

    def __str__(self):
        return self.title

class Slide(CMSPlugin):
    presentation = models.ForeignKey(Presentation, related_name='presentation', on_delete=models.CASCADE)
    content = TinyMCEModelField('Conteúdo')

    def get_content(self):
        return self.content

    def get_title(self):
        return self.presentation.title
    
    def __str__(self):
        return self.presentation.title

