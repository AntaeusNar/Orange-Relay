from django.db import models

# Create your models here.


class Inputs(models.Model):
    """Inputs from anything"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField()

    def __str__(self):
        """return a string representation of the model."""
        return self.text


class Outputs(models.Model):
    """outputs to pins/relays"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField()

    def __str__(self):
        """return a string representation of the model."""
        return self.text


class Rule(models.Model):
    """what when what"""
    input = models.ForeignKey(Inputs, on_delete=models.CASCADE)
    output = models.ForeignKey(Outputs, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField()

    def __str__(self):
        """return a string representation of the model."""
        return self.text