from django.db import models

# Create your models here.
class Blogpost(models.Model):
    catChoices = (
        ('1','General'),
        ('2','Technology'),
        ('3','Food'),
        ('4','Education and Facts'),
        ('5','GK'),
        ('6','News'),
        ('7','Gaming'),
        ('8','Entertainment and Movies'),
        ('9','Sports'),
        ('10','Lifestyle'),
        ('11','Travel'),
        ('12','Art and Design'),
        ('13','Music'),
        ('14','Finance'),
        ('15','Photography'),
        ('16','Health and Fitness'),
    )
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    cintrohead = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=500, default="")
    chead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500, default="")
    chead2 = models.CharField(max_length=5000, default="")
    con = models.CharField(max_length=500, default="")
    ccon = models.CharField(max_length=5000, default="")
    category =  models.CharField(max_length=100, default="1", choices=catChoices)
    pub_date = models.DateField()
    author_name = models.CharField(max_length=50, default="")
    author_info = models.CharField(max_length=200, default="")
    # thumbnail = models.ImageField(upload_to='', default="")

    def __str__(self):
        return self.title

