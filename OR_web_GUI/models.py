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
    ACTIONS = (
        ('H', 'Set Output High'),
        ('L', 'Set Output Low'),
        ('T', 'Toggle Output'),
    )
    TIMES = (
        ('M', 'Momentary'),
        ('T', 'Timed'),
        ('L', 'Latched'),
        ('P', 'Permanent')
    )
    input = models.ForeignKey(Input, on_delete=models.CASCADE)
    output = models.ForeignKey(Output, on_delete=models.CASCADE)
    # what to do when triggered
    action = models.CharField(max_length=1, choices=ACTIONS, default='P')
    # how long to hold the action for in types
    #   momentary is just 10ms, Timed can be longer,
    #   Latched is until unlatched, Permanent is til next trigger
    times = models.CharField(max_length=1, choices=TIMES, default='L')
    # length of time for timed
    length = models.IntegerField(default=0)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return a string representation of the model."""
        return self.text


# Start of rules v2
# Currently unused


class EvalExpression(models.Model):
    # This should be a evaluable expression hopefully using basic if then logic and true false booleans
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
