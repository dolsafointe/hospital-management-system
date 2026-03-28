from django.db import models

class Exam(models.Model):
    EXAM_TYPE_CHOICES = [
        ('blood_test', 'Blood Test'),
        ('x_ray', 'X-Ray'),
        ('ultrasound', 'Ultrasound'),
        ('ct_scan', 'CT Scan'),
        ('mri', 'MRI'),
        ('ecg', 'ECG'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    ordered_by = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES)
    exam_date = models.DateTimeField()
    result_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    result_description = models.TextField(null=True, blank=True)
    result_file = models.FileField(upload_to='results/', null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']