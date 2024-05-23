import pandas as pd
import requests
from src.utils.models import Country
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Parsing Country data from restcountries.com'

    def handle(self, *args, **options):
        url = "https://restcountries.com/v3.1/all"

        r = requests.get(url).json()

        df = pd.DataFrame(r)
        name = df['name']
        country_code = df['cca3']
        flag = df['flags']
        try:
            for i in range(len(name)):
                country = Country.objects.create(title=name[i].get('common'), code=country_code[i],
                                                 flag=flag[i].get('png'))
                country.save()
            return 'zor'
        except Exception as e:
            return e
