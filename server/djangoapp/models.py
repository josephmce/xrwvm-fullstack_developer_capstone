from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country_of_origin = models.CharField(
        max_length=100,
        blank=True
    )
    logo = models.ImageField(
        upload_to='car_makes/logos/',
        blank=True,
        null=True
    )
    is_premium = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SALOON', 'Saloon'),
        ('HATCHBACK', 'Hatchback'),
        ('ESTATE', 'Estate'),
        ('SUV', 'SUV'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('MPV', 'MPV'),
        ('CROSSOVER', 'Crossover'),
        ('PICKUP', 'Pickup'),
        ('VAN', 'Van'),
        ('MINIBUS', 'Minibus'),
        ('ROADSTER', 'Roadster'),
        ('FASTBACK', 'Fastback'),
    ]

    type = models.CharField(
        max_length=11,
        choices=CAR_TYPES,
        default='SALOON'
    )
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015),
        ]
    )
    engine_size = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True
    )
    fuel_type = models.CharField(
        max_length=20,
        choices=[
            ('PETROL', 'Petrol'),
            ('DIESEL', 'Diesel'),
            ('HYBRID', 'Hybrid'),
            ('ELECTRIC', 'Electric'),
        ],
        blank=True
    )
    gearbox = models.CharField(
        max_length=20,
        choices=[
            ('MANUAL', 'Manual'),
            ('AUTOMATIC', 'Automatic'),
        ],
        blank=True
    )
    doors = models.PositiveSmallIntegerField(
        blank=True,
        null=True
    )
    seats = models.PositiveSmallIntegerField(
        blank=True,
        null=True
    )
    colour = models.CharField(
        max_length=30,
        blank=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    mileage = models.PositiveIntegerField(
        blank=True,
        null=True
    )  # In miles or km
    is_available = models.BooleanField(default=True)
    main_image = models.ImageField(
        upload_to='car_models/',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
