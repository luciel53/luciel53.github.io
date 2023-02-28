from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.core.validators import (MinLengthValidator)
from django.urls import reverse


race_choices = (('1', 'Abyssin'),
                ('2', 'Bengal'),
                ('3', 'Bleu Russe'),
                ('4', 'Bombay'),
                ('5', 'British Shorthair'),
                ('6', 'Chartreux'),
                ('7', 'Maine Coon'),
                ('8', 'Persan'),
                ('9', 'Ragdoll'),
                ('10', 'Sacré de Birmanie'),
                ('11', 'Savannah'),
                ('12', 'Scottish Fold'),
                ('13', 'Siamois'),
                ('14', 'Sibérien'),
                ('15', 'Sphynx'),
                ('16', 'Toyger'),
                )

localisation_choices = (
                        ('1', 'Alsace'),
                        ('2', 'Aquitaine'),
                        ('3', 'Auvergne'),
                        ('4', 'Basse-Normandie'),
                        ('5', 'Bourgogne'),
                        ('6', 'Bretagne'),
                        ('7', 'Centre'),
                        ('8', 'Champagne-Ardennes'),
                        ('9', 'Corse'),
                        ('10', 'Franche-Comté'),
                        ('11', 'Haute-Normandie'),
                        ('12', 'Ile-de-France'),
                        ('13', 'Languedoc-Roussillon'),
                        ('14', 'Limousin'),
                        ('15', 'Lorraine'),
                        ('16', 'Midi-Pyrénées'),
                        ('17', 'Nord-Pas-de-Calais'),
                        ('18', 'Pays de la loire'),
                        ('19', 'Picardie'),
                        ('20', 'Poitou-Charentes'),
                        ('21', 'Provence-Alpes-Cotes d\'Azur'),
                        ('22', 'Rhône-Alpes'),
                        )
bloodtype_choices = (
                    ('1', 'A'),
                    ('2', 'B'),
                    ('3', 'AB'),
                    ('', ''),
                    )

eyecolor_choices = (
                    ('1', 'Bleus'),
                    ('2', 'Verts'),
                    ('3', 'Or'),
                    ('4', 'Vairons'),
                    ('', ''),
                    )

age_choices = (
                    ('1', '6 mois - 1 an'),
                    ('2', '1 an - 2 ans'),
                    ('3', '2 ans - 3 ans'),
                    ('4', '3 ans - 4 ans'),
                    ('5', '4 ans - 5 ans'),
                    ('6', '5 ans - 6 ans'),
                    ('7', '6 ans - 7 ans'),
                    ('8', '7 ans - 8 ans'),
                    ('9', '8 ans - 9 ans'),
                    )
sex_choices = (('1', 'mâle'), ('2', 'femelle'),)

class annimal_post(models.Model):
    #essential
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = "Prix de la saillie:")
    localisation = models.CharField(choices=localisation_choices, max_length=100)

    name = models.CharField(max_length=100, verbose_name = "Nom")
    photo = models.ImageField(upload_to="animal.pics")

    sexe = models.CharField(choices=sex_choices, max_length=100, verbose_name = "Sexe")
    race = models.CharField(choices=race_choices, max_length=100)
    identification = models.CharField(validators=[MinLengthValidator(15)], max_length=15, unique=True, verbose_name = "N° d'identification")

    #optional admin checks
    bloodtype = models.CharField(choices=bloodtype_choices, max_length=10,default=None, blank=True, verbose_name = "Groupe sanguin")
    viral_disease_tests = models.CharField(max_length=1000,default=None, blank=True, verbose_name = "Tests maladies")

    # optional phisical description of the cat:
    eye_color = models.CharField(choices=eyecolor_choices, max_length=100,default=None, blank=True, verbose_name = "Couleur des yeux")
    age = models.CharField(choices=age_choices, max_length=10)

    fur_color = models.CharField(max_length=100,default=None, blank=True, verbose_name = "Couleur du poil")
    qualities = models.TextField(max_length=350, default=None, blank=True, null=True, verbose_name = "Qualités")
    flaws = models.TextField(max_length=350, default=None, blank=True, null=True, verbose_name = "Défauts")
    free_descriptive_text = models.TextField(max_length=2000,default=None, blank=True, verbose_name = "Autre")

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.photo.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

