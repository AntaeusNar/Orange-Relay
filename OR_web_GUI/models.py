from django.db import models

# Create your models here.


class Input(models.Model):
    """Inputs from anything"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return a string representation of the model."""
        return self.text


class Output(models.Model):
    """outputs to pins/relays"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now_add=True)
    channel = models.IntegerField()

    def __str__(self):
        """return a string representation of the model."""
        return self.text+" channel: "+str(self.channel)


class Rule(models.Model):
    """what when what"""
    input = models.ForeignKey(Input, on_delete=models.CASCADE)
    output = models.ForeignKey(Output, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return a string representation of the model."""
        return self.text
