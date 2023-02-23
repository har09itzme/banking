from django.db import models


# Create your models here.


# sub=(('option1-1',"Thamarassery"),
#      ('option1-2',"koyilandi"),
#      ('option1-3',"beypur"),
#       ('option1-4',"vadakara"))


class detail(models.Model):
    districtt = [("option1", "Calicut"),
                 ("option2", "Kannur"),
                 ("option3", "Ernakulam"),
                 ("option4", "Malappuram"),
                 ("option5", "Palakkad")]
    sub = [("option1-1", 'Thamarassery'),
           ("option1-2", 'Koyilandi'),
           ("option1-3", 'Beypur'),
           ('option1-4', 'Vadakara'),

           ("option2-1", 'Thalassery'),
           ('option2-2', 'Iritti'),
           ('option2-3', 'Payyanur'),
           ('option2-4', 'Thaliparamba'),

           ("option3-1", 'Cochin'),
           ('option3-2', 'Aluva'),
           ('option3-3', 'Edappalli'),
           ('option3-4', 'Vypin'),

           ("option4-1", 'Eranad'),
           ('option4-2', 'Kondotti'),
           ('option4-3', 'Nilambur'),
           ('option4-4', 'Ponnani'),

           ("option5-1", 'Chittur'),
           ('option5-2', 'Ottapalam'),
           ('option5-3', 'Mannarkad'),
           ('option5-4', 'Pattambi'),
           ]

    materialss = ("Debit card", "Debit card"), ("Credit card", "Credit card"), ("cheque book", "Cheque book")
    gender_choices = [("M", "MALE"), ("F", "FEMALE"),("O","OTHER")]
    name = models.CharField(max_length=250, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    account = models.CharField(max_length=250, blank=True, null=True)
    district = models.CharField(max_length=20, choices=districtt, blank=True, null=True)
    materials = models.CharField(max_length=20, choices=materialss, blank=True, null=True)
    subd = models.CharField(max_length=20, choices=sub, blank=True, null=True)

    def __str__(self):
        return str(self.id)
