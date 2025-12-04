import os
from django.core.management import call_command
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_receitas.settings')
django.setup()

call_command('loaddata', 'fixtures/dump_clean.json')