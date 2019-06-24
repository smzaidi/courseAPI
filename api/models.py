from django.db import models
import csv

# path = '/Users/samizaidi/Desktop/FA2019.csv'
# cl = open(path, 'r')
# csv_reader = csv.reader(cl)
#
# for line in csv_reader:
#     print(str(line[3]))

class CourseNumber(models.Model):

    number = models.CharField(max_length=200)

    def load_csv(self):

        path = '/app/FA2019.csv'
        cl = open(path, 'r')
        csv_reader = csv.reader(cl)

        for line in csv_reader:
            print(str(line[3]))
            c = CourseNumber.objects.create(number=str(line[3]))
            c.save()
