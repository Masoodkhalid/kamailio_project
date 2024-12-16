from django.db import models

class TrustedEntry(models.Model):
    id = models.AutoField(primary_key=True)
    src_ip = models.CharField(max_length=255)
    proto = models.CharField(max_length=50)
    from_pattern = models.CharField(max_length=255, null=True, blank=True)
    ruri_pattern = models.CharField(max_length=255, null=True, blank=True)
    tag = models.CharField(max_length=255, null=True, blank=True)
    priority = models.IntegerField()

    class Meta:
        db_table = 'trusted'  # Use the exact table name 'trusted'

    def __str__(self):
        return f"{self.src_ip} - {self.tag}"

