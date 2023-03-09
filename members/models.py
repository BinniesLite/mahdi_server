from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    position = models.CharField(max_length=100)
    image = models.URLField(default=None, null=True)
        
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(Member, related_name="projects")
    image = models.URLField(default=None, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    

class Image(models.Model):
    image = models.URLField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_images")
    
    def __str__(self) -> str:
        return self.project.name
