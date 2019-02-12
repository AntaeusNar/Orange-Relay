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
    # todo: remove from code and database
    """what when what"""
    input = models.ForeignKey(Input, on_delete=models.CASCADE)
    output = models.ForeignKey(Output, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return a string representation of the model."""
        return self.text


# Start of rules v2


class EvalExpression(models.Model):
    # This should be a evaluatalbe expession hopefully using basic if then logic and true false booleans
    descript = models.CharField(max_length=200)
    eval = models.CharField(max_length=200)
    input = models.ManyToManyField(Input, through='Relation', related_name='expressions')
    output = models.ManyToManyField(Output, through='Relation', related_name='expressions')
    date_added = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descript


class Relation(models.Model):
    # this is the many-to-many through table
    input = models.ForeignKey(Input, related_name='relation', on_delete=models.SET_NULL, null=True)
    output = models.ForeignKey(Output, related_name='relation', on_delete=models.SET_NULL, null=True)
    express = models.ForeignKey(EvalExpression, related_name='relation', on_delete=models.CASCADE)
