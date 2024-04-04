# myapp/models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField(upload_to='files/')
    file_path_field = models.FilePathField(path='/path/to/files/')
    float_field = models.FloatField()
    # foreign_key = models.ForeignKey(OtherModel, on_delete=models.CASCADE)
    generic_ip_address_field = models.GenericIPAddressField()
    json_field = models.JSONField()
    # positive_big_integer_field = models PositiveBigIntegerField()
    # positive_integer_field = models PositiveIntegerField()
    text_field = models.TextField()
    url_field = models.URLField()