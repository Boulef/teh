# Generated by Django 5.0.1 on 2024-01-16 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(help_text='Product SKU, must be unique', max_length=50, unique=True)),
                ('serial_number', models.CharField(blank=True, help_text='Product serial number if applicable', max_length=50, null=True, unique=True)),
                ('name', models.CharField(help_text='Product name', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, help_text='Product price', max_digits=10)),
                ('category', models.CharField(help_text='Accessory category', max_length=100)),
                ('manufacturer', models.CharField(help_text='Accessory manufacturer', max_length=100)),
                ('model', models.CharField(help_text='Accessory model', max_length=100)),
                ('description', models.TextField(help_text='Accessory description')),
                ('compatibility', models.TextField(blank=True, help_text='Accessory compatibility', null=True)),
                ('additional_features', models.TextField(blank=True, help_text='Additional accessory features', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(help_text='Product SKU, must be unique', max_length=50, unique=True)),
                ('serial_number', models.CharField(blank=True, help_text='Product serial number if applicable', max_length=50, null=True, unique=True)),
                ('name', models.CharField(help_text='Product name', max_length=255)),
                ('description', models.TextField(help_text='Product description')),
                ('price', models.DecimalField(decimal_places=2, help_text='Product price', max_digits=10)),
                ('cpu_manufacturer', models.CharField(help_text='CPU manufacturer, e.g., Intel, AMD', max_length=100)),
                ('cpu_model', models.CharField(help_text='CPU model, e.g., Core i7, Ryzen 5', max_length=100)),
                ('cpu_architecture', models.CharField(help_text='CPU architecture, e.g., x86_64', max_length=100)),
                ('cpu_cores', models.IntegerField(help_text='Number of CPU cores')),
                ('cpu_threads', models.IntegerField(help_text='Number of CPU threads')),
                ('cpu_base_clock_speed', models.FloatField(help_text='Base CPU clock speed in GHz')),
                ('cpu_max_clock_speed', models.FloatField(help_text='Maximum CPU clock speed in GHz')),
                ('cpu_cache_size', models.IntegerField(help_text='CPU cache size in MB')),
                ('cpu_socket_type', models.CharField(help_text='CPU socket type, e.g., LGA1200', max_length=50)),
                ('cpu_power_consumption', models.IntegerField(help_text='CPU power consumption in watts')),
                ('has_cpu', models.BooleanField(help_text='Whether the product has a CPU')),
                ('ram_capacity', models.IntegerField(help_text='RAM capacity in gigabytes')),
                ('ram_speed', models.IntegerField(help_text='RAM speed in megahertz')),
                ('ram_type', models.CharField(help_text='RAM type, e.g., DDR4', max_length=50)),
                ('has_ram', models.BooleanField(help_text='Whether the product has RAM')),
                ('storage_capacity', models.IntegerField(help_text='Storage capacity in gigabytes')),
                ('storage_interface', models.CharField(help_text='Storage interface, e.g., SATA, NVMe', max_length=50)),
                ('storage_form_factor', models.CharField(help_text='Storage form factor, e.g., 2.5", M.2', max_length=50)),
                ('power_supply_type', models.TextField(help_text='Type of power supply')),
                ('has_power_supply', models.BooleanField(help_text='Whether the product has a power supply')),
                ('operating_system', models.CharField(help_text='Installed operating system, e.g., Windows 10', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OtherProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(help_text='Product SKU, must be unique', max_length=50, unique=True)),
                ('serial_number', models.CharField(blank=True, help_text='Product serial number if applicable', max_length=50, null=True, unique=True)),
                ('name', models.CharField(help_text='Product name', max_length=255)),
                ('description', models.TextField(help_text='Product description')),
                ('price', models.DecimalField(decimal_places=2, help_text='Product price', max_digits=10)),
                ('additional_info', models.TextField(help_text='Additional information about the product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(help_text='Product SKU, must be unique', max_length=50, unique=True)),
                ('serial_number', models.CharField(blank=True, help_text='Product serial number if applicable', max_length=50, null=True, unique=True)),
                ('name', models.CharField(help_text='Product name', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, help_text='Product price', max_digits=10)),
                ('category', models.CharField(help_text='Part category', max_length=100)),
                ('manufacturer', models.CharField(help_text='Part manufacturer', max_length=100)),
                ('model', models.CharField(help_text='Part model', max_length=100)),
                ('description', models.TextField(help_text='Part description')),
                ('compatibility', models.TextField(blank=True, help_text='Part compatibility', null=True)),
                ('additional_features', models.TextField(blank=True, help_text='Additional part features', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(help_text='Product SKU, must be unique', max_length=50, unique=True)),
                ('serial_number', models.CharField(blank=True, help_text='Product serial number if applicable', max_length=50, null=True, unique=True)),
                ('name', models.CharField(help_text='Product name', max_length=255)),
                ('description', models.TextField(help_text='Product description')),
                ('price', models.DecimalField(decimal_places=2, help_text='Product price', max_digits=10)),
                ('manufacturer', models.CharField(help_text='Phone manufacturer', max_length=100)),
                ('model', models.CharField(help_text='Phone model', max_length=100)),
                ('display_size', models.FloatField(help_text='Phone display size in inches')),
                ('resolution', models.CharField(help_text='Phone resolution', max_length=50)),
                ('operating_system', models.CharField(help_text='Phone operating system', max_length=50)),
                ('processor', models.CharField(help_text='Phone processor', max_length=100)),
                ('memory', models.IntegerField(help_text='Phone memory in gigabytes')),
                ('storage', models.IntegerField(help_text='Phone storage in gigabytes')),
                ('rear_camera', models.CharField(help_text='Phone rear camera specification', max_length=100)),
                ('front_camera', models.CharField(help_text='Phone front camera specification', max_length=100)),
                ('battery_capacity', models.IntegerField(help_text='Phone battery capacity in milliampere-hours (mAh)')),
                ('connectivity', models.TextField(blank=True, help_text='Phone connectivity features', null=True)),
                ('ports', models.TextField(blank=True, help_text='Phone ports', null=True)),
                ('biometric_security', models.TextField(blank=True, help_text='Phone biometric security features', null=True)),
                ('additional_features', models.TextField(blank=True, help_text='Additional phone features', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(help_text='Product SKU, must be unique', max_length=50, unique=True)),
                ('serial_number', models.CharField(blank=True, help_text='Product serial number if applicable', max_length=50, null=True, unique=True)),
                ('name', models.CharField(help_text='Product name', max_length=255)),
                ('description', models.TextField(help_text='Product description')),
                ('price', models.DecimalField(decimal_places=2, help_text='Product price', max_digits=10)),
                ('manufacturer', models.CharField(help_text='TV manufacturer', max_length=100)),
                ('model', models.CharField(help_text='TV model', max_length=100)),
                ('screen_size', models.FloatField(help_text='TV screen size in inches')),
                ('resolution', models.CharField(help_text='TV resolution, e.g., 4K, Full HD', max_length=50)),
                ('display_technology', models.CharField(help_text='TV display technology, e.g., LED, OLED', max_length=50)),
                ('is_smart_tv', models.BooleanField(default=False, help_text='Whether the TV is a smart TV')),
                ('operating_system', models.CharField(blank=True, help_text='TV operating system', max_length=50, null=True)),
                ('refresh_rate', models.FloatField(help_text='TV refresh rate in Hertz')),
                ('connectivity', models.TextField(blank=True, help_text='TV connectivity features', null=True)),
                ('ports', models.TextField(blank=True, help_text='TV ports', null=True)),
                ('sound_system', models.CharField(blank=True, help_text='TV sound system', max_length=50, null=True)),
                ('additional_features', models.TextField(blank=True, help_text='Additional TV features', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AllInOne',
            fields=[
                ('computer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tehtek.computer')),
                ('integrated_display_size', models.FloatField(help_text='All-in-One integrated display size in inches')),
                ('integrated_display_resolution', models.CharField(help_text='All-in-One integrated display resolution', max_length=50)),
                ('has_touchscreen_display', models.BooleanField(help_text='Whether the All-in-One has a touchscreen display')),
                ('has_integrated_webcam', models.BooleanField(help_text='Whether the All-in-One has an integrated webcam')),
                ('has_integrated_speakers', models.BooleanField(help_text='Whether the All-in-One has integrated speakers')),
            ],
            options={
                'abstract': False,
            },
            bases=('tehtek.computer',),
        ),
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('computer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tehtek.computer')),
                ('form_factor', models.CharField(help_text='Desktop form factor', max_length=50)),
                ('power_supply_capacity', models.IntegerField(help_text='Desktop power supply capacity in watts')),
                ('has_monitor', models.BooleanField(help_text='Whether the desktop comes with a monitor')),
                ('has_speakers', models.BooleanField(help_text='Whether the desktop comes with speakers')),
            ],
            options={
                'abstract': False,
            },
            bases=('tehtek.computer',),
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('computer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tehtek.computer')),
                ('screen_size', models.FloatField(help_text='Laptop screen size in inches')),
                ('display_resolution', models.CharField(help_text='Laptop display resolution', max_length=50)),
                ('battery_capacity', models.IntegerField(help_text='Laptop battery capacity in watt-hours (Wh)')),
                ('weight', models.FloatField(help_text='Laptop weight in kilograms')),
                ('graphics_card_manufacturer', models.CharField(help_text='Laptop graphics card manufacturer', max_length=100)),
                ('graphics_card_model', models.CharField(help_text='Laptop graphics card model', max_length=100)),
                ('graphics_card_memory', models.IntegerField(help_text='Laptop graphics card memory in gigabytes')),
                ('has_touchscreen', models.BooleanField(help_text='Whether the laptop has a touchscreen')),
                ('has_backlit_keyboard', models.BooleanField(help_text='Whether the laptop has a backlit keyboard')),
                ('wireless_connectivity', models.TextField(blank=True, help_text='Laptop wireless connectivity features', null=True)),
                ('ports', models.TextField(blank=True, help_text='Laptop ports', null=True)),
                ('additional_features', models.TextField(blank=True, help_text='Additional laptop features', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('tehtek.computer',),
        ),
        migrations.CreateModel(
            name='OtherComputer',
            fields=[
                ('computer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tehtek.computer')),
                ('additional_info', models.TextField(help_text='Additional information about other types of computers')),
            ],
            options={
                'abstract': False,
            },
            bases=('tehtek.computer',),
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('computer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tehtek.computer')),
                ('screen_size', models.FloatField(help_text='Tablet screen size in inches')),
                ('display_resolution', models.CharField(help_text='Tablet display resolution', max_length=50)),
                ('battery_capacity', models.IntegerField(help_text='Tablet battery capacity in milliampere-hours (mAh)')),
                ('weight', models.FloatField(help_text='Tablet weight in grams')),
                ('rear_camera', models.CharField(help_text='Tablet rear camera specification', max_length=100)),
                ('front_camera', models.CharField(help_text='Tablet front camera specification', max_length=100)),
                ('wireless_connectivity', models.TextField(blank=True, help_text='Tablet wireless connectivity features', null=True)),
                ('ports', models.TextField(blank=True, help_text='Tablet ports', null=True)),
                ('additional_features', models.TextField(blank=True, help_text='Additional tablet features', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('tehtek.computer',),
        ),
    ]
