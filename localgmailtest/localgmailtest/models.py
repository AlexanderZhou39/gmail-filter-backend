from django.db import models

# College model contains attributes for gmail filter. SAT score, ACT score, etc.
class College(models.Model):
    school_name = models.CharField(max_length=50)
    slug = models.CharField(null=True, blank=True, max_length=50) # Unsure.
    acceptance = models.FloatField(null=True, blank=True)
    city = models.CharField(null=True, blank=True, max_length=25)
    state = models.CharField(null=True, blank=True, max_length=2)
    grad_rate = models.FloatField(null=True, blank=True)
    desirability = models.IntegerField(null=True, blank=True)
    influence = models.IntegerField(null=True, blank=True)
    overall_rank = models.IntegerField(null=True, blank=True)
    sat = models.IntegerField(null=True, blank=True)
    act = models.IntegerField(null=True, blank=True)
    student_body = models.IntegerField(null=True, blank=True)
    undergrad_student_body = models.IntegerField(null=True, blank=True)
    tuition = models.IntegerField(null=True, blank=True)
    domain = models.URLField(max_length=25)

    def __str__(self):
        return self.school_name