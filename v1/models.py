from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Contacts(models.Model):
    """
    up to 3 custom searches can be saved
    """

    uuid = models.CharField(max_length=36, unique=True, db_index=True)
    subject_pref = models.TextField()
    journal_pref = models.TextField()

    search1 = models.TextField()
    search1_date = models.DateTimeField()
    search2 = models.TextField()
    search2_date = models.DateTimeField()
    search3 = models.TextField()
    search3_date = models.DateTimeField()

    def __str__(self):
        return (self.uuid,
                self.subject_pref,
                self.journal_pref,
                self.search1,
                self.search1_date,
                self.search2,
                self.search2_date,
                self.search3,
                self.search3_date)


# probably will migrate this. no model creation for now
# @python_2_unicode_compatible
# class Journals(models.Model):
#
#     name = models.TextField()
#     minor_subject = models.TextField() # e.g. political science
#     major_subject = models.TextField() # e.g. science, humanities
#
#     def __str__(self):
#         return self.name, self.minor_subject, self.major_subject
