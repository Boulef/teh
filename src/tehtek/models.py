# models.py

from django.db import models

# BaseProduct model represents the common attributes of all products
class BaseProduct(models.Model):
    SKU = models.CharField(max_length=50, unique=True, help_text="Product SKU, must be unique")
    serial_number = models.CharField(max_length=50, blank=True, null=True, unique=True, help_text="Product serial number if applicable")
    name = models.CharField(max_length=255, help_text="Product name")
    description = models.TextField(help_text="Product description")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Product price")

    class Meta:
        abstract = True

# Computer model represents a type of product (Computer)
class Computer(BaseProduct):
    # Additional fields specific to Computer
    cpu_manufacturer = models.CharField(max_length=100, help_text="CPU manufacturer, e.g., Intel, AMD")
    cpu_model = models.CharField(max_length=100, help_text="CPU model, e.g., Core i7, Ryzen 5")
    cpu_architecture = models.CharField(max_length=100, help_text="CPU architecture, e.g., x86_64")
    cpu_cores = models.IntegerField(help_text="Number of CPU cores")
    cpu_threads = models.IntegerField(help_text="Number of CPU threads")
    cpu_base_clock_speed = models.FloatField(help_text="Base CPU clock speed in GHz")
    cpu_max_clock_speed = models.FloatField(help_text="Maximum CPU clock speed in GHz")
    cpu_cache_size = models.IntegerField(help_text="CPU cache size in MB")  # in MB
    cpu_socket_type = models.CharField(max_length=50, help_text="CPU socket type, e.g., LGA1200")
    cpu_power_consumption = models.IntegerField(help_text="CPU power consumption in watts")  # in watts
    has_cpu = models.BooleanField(help_text="Whether the product has a CPU")
    ram_capacity = models.IntegerField(help_text="RAM capacity in gigabytes")  # in gigabytes
    ram_speed = models.IntegerField(help_text="RAM speed in megahertz")  # in megahertz
    ram_type = models.CharField(max_length=50, help_text="RAM type, e.g., DDR4")  # DDR3, DDR4, etc.
    has_ram = models.BooleanField(help_text="Whether the product has RAM")
    storage_capacity = models.IntegerField(help_text="Storage capacity in gigabytes")  # in gigabytes
    storage_interface = models.CharField(max_length=50, help_text="Storage interface, e.g., SATA, NVMe")  # SATA, NVMe, etc.
    storage_form_factor = models.CharField(max_length=50, help_text="Storage form factor, e.g., 2.5\", M.2")  # 2.5", 3.5", M.2, etc.
    power_supply_type = models.TextField(help_text="Type of power supply")
    has_power_supply = models.BooleanField(help_text="Whether the product has a power supply")
    operating_system = models.CharField(max_length=50, help_text="Installed operating system, e.g., Windows 10")

# TV model represents a type of product (TV)
class TV(BaseProduct):
    # Additional fields specific to TV
    manufacturer = models.CharField(max_length=100, help_text="TV manufacturer")
    model = models.CharField(max_length=100, help_text="TV model")
    screen_size = models.FloatField(help_text="TV screen size in inches")
    resolution = models.CharField(max_length=50, help_text="TV resolution, e.g., 4K, Full HD")
    display_technology = models.CharField(max_length=50, help_text="TV display technology, e.g., LED, OLED")
    is_smart_tv = models.BooleanField(default=False, help_text="Whether the TV is a smart TV")
    operating_system = models.CharField(max_length=50, null=True, blank=True, help_text="TV operating system")
    refresh_rate = models.FloatField(help_text="TV refresh rate in Hertz")
    connectivity = models.TextField(blank=True, null=True, help_text="TV connectivity features")
    ports = models.TextField(blank=True, null=True, help_text="TV ports")
    sound_system = models.CharField(max_length=50, null=True, blank=True, help_text="TV sound system")
    additional_features = models.TextField(blank=True, null=True, help_text="Additional TV features")

# Phone model represents a type of product (Phone)
class Phone(BaseProduct):
    # Additional fields specific to Phone
    manufacturer = models.CharField(max_length=100, help_text="Phone manufacturer")
    model = models.CharField(max_length=100, help_text="Phone model")
    display_size = models.FloatField(help_text="Phone display size in inches")
    resolution = models.CharField(max_length=50, help_text="Phone resolution")
    operating_system = models.CharField(max_length=50, help_text="Phone operating system")
    processor = models.CharField(max_length=100, help_text="Phone processor")
    memory = models.IntegerField(help_text="Phone memory in gigabytes")
    storage = models.IntegerField(help_text="Phone storage in gigabytes")
    rear_camera = models.CharField(max_length=100, help_text="Phone rear camera specification")
    front_camera = models.CharField(max_length=100, help_text="Phone front camera specification")
    battery_capacity = models.IntegerField(help_text="Phone battery capacity in milliampere-hours (mAh)")
    connectivity = models.TextField(blank=True, null=True, help_text="Phone connectivity features")
    ports = models.TextField(blank=True, null=True, help_text="Phone ports")
    biometric_security = models.TextField(blank=True, null=True, help_text="Phone biometric security features")
    additional_features = models.TextField(blank=True, null=True, help_text="Additional phone features")

# Accessory model represents a type of product (Accessory)
class Accessorie(BaseProduct):
    # Additional fields specific to Accessories
    category = models.CharField(max_length=100, help_text="Accessory category")
    manufacturer = models.CharField(max_length=100, help_text="Accessory manufacturer")
    model = models.CharField(max_length=100, help_text="Accessory model")
    description = models.TextField(help_text="Accessory description")
    compatibility = models.TextField(blank=True, null=True, help_text="Accessory compatibility")
    additional_features = models.TextField(blank=True, null=True, help_text="Additional accessory features")

# Part model represents a type of product (Part)
class Part(BaseProduct):
    # Additional fields specific to Parts
    category = models.CharField(max_length=100, help_text="Part category")
    manufacturer = models.CharField(max_length=100, help_text="Part manufacturer")
    model = models.CharField(max_length=100, help_text="Part model")
    description = models.TextField(help_text="Part description")
    compatibility = models.TextField(blank=True, null=True, help_text="Part compatibility")
    additional_features = models.TextField(blank=True, null=True, help_text="Additional part features")

# OtherProduct model represents a type of product (OtherProduct)
class OtherProduct(BaseProduct):
    # Additional fields specific to Others
    additional_info = models.TextField(help_text="Additional information about the product")

# Laptop model represents a type of computer (Laptop)
class Laptop(Computer):
    # Additional fields specific to Laptop
    screen_size = models.FloatField(help_text="Laptop screen size in inches")
    display_resolution = models.CharField(max_length=50, help_text="Laptop display resolution")
    battery_capacity = models.IntegerField(help_text="Laptop battery capacity in watt-hours (Wh)")
    weight = models.FloatField(help_text="Laptop weight in kilograms")
    graphics_card_manufacturer = models.CharField(max_length=100, help_text="Laptop graphics card manufacturer")
    graphics_card_model = models.CharField(max_length=100, help_text="Laptop graphics card model")
    graphics_card_memory = models.IntegerField(help_text="Laptop graphics card memory in gigabytes")
    has_touchscreen = models.BooleanField(help_text="Whether the laptop has a touchscreen")
    has_backlit_keyboard = models.BooleanField(help_text="Whether the laptop has a backlit keyboard")
    wireless_connectivity = models.TextField(blank=True, null=True, help_text="Laptop wireless connectivity features")
    ports = models.TextField(blank=True, null=True, help_text="Laptop ports")
    additional_features = models.TextField(blank=True, null=True, help_text="Additional laptop features")

# Desktop model represents a type of computer (Desktop)
class Desktop(Computer):
    # Additional fields specific to Desktop
    form_factor = models.CharField(max_length=50, help_text="Desktop form factor")
    power_supply_capacity = models.IntegerField(help_text="Desktop power supply capacity in watts")
    has_monitor = models.BooleanField(help_text="Whether the desktop comes with a monitor")
    has_speakers = models.BooleanField(help_text="Whether the desktop comes with speakers")

# AllInOne model represents a type of computer (AllInOne)
class AllInOne(Computer):
    # Additional fields specific to All in One
    integrated_display_size = models.FloatField(help_text="All-in-One integrated display size in inches")
    integrated_display_resolution = models.CharField(max_length=50, help_text="All-in-One integrated display resolution")
    has_touchscreen_display = models.BooleanField(help_text="Whether the All-in-One has a touchscreen display")
    has_integrated_webcam = models.BooleanField(help_text="Whether the All-in-One has an integrated webcam")
    has_integrated_speakers = models.BooleanField(help_text="Whether the All-in-One has integrated speakers")

# Tablet model represents a type of computer (Tablet)
class Tablet(Computer):
    # Additional fields specific to Tablet
    screen_size = models.FloatField(help_text="Tablet screen size in inches")
    display_resolution = models.CharField(max_length=50, help_text="Tablet display resolution")
    battery_capacity = models.IntegerField(help_text="Tablet battery capacity in milliampere-hours (mAh)")
    weight = models.FloatField(help_text="Tablet weight in grams")
    rear_camera = models.CharField(max_length=100, help_text="Tablet rear camera specification")
    front_camera = models.CharField(max_length=100, help_text="Tablet front camera specification")
    wireless_connectivity = models.TextField(blank=True, null=True, help_text="Tablet wireless connectivity features")
    ports = models.TextField(blank=True, null=True, help_text="Tablet ports")
    additional_features = models.TextField(blank=True, null=True, help_text="Additional tablet features")

# OtherComputer model represents a type of computer (OtherComputer)
class OtherComputer(Computer):
    # Additional fields specific to other types of computers
    additional_info = models.TextField(help_text="Additional information about other types of computers")
