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
# rebuilding the rules models as follows:
#   One Linking statement can have many inputs(each with its own Condition),
#   one Logic command, and many Outputs(each with its own Condition)
# E.I. IF (Input #1 is HIGH & Input #3 is LOW)
#   set (Output # 4 HIGH LATCHED & Output #5 LOW TIMED 10sec & Output #1 Toggle)


class Conditions(models.Model):
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
    # what to do when triggered
    action = models.CharField(max_length=1, choices=ACTIONS, default='P')
    # how long to hold the action for in types
    #   momentary is just 10ms, Timed can be longer,
    #   Latched is until unlatched, Permanent is til next trigger
    times = models.CharField(max_length=1, choices=TIMES, default='L')
    # length of time for timed
    length = models.IntegerField(default=0)


class Linking(models.Model):
    # which input conditions trigger which logic tests to tirgger which output conditions
    description = models.CharField(max_length=50)
    logic_test = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now_add=True)


class InputConditions(models.Model):
    input = models.ForeignKey(Input, on_delete=models.CASCADE)
    condition = models.ForeignKey(Conditions, on_delete=models.CASCADE)
    link = models.ForeignKey(Linking, on_delete=models.CASCADE)


class OutputConditions(models.Model):
    output = models.ForeignKey(Output, on_delete=models.CASCADE)
    condition = models.ForeignKey(Conditions, on_delete=models.CASCADE)
    link = models.ForeignKey(Linking, on_delete=models.CASCADE)






