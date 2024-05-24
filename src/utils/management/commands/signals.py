import pandas as pd
import requests
from utils.models import Country
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Parsing Country data from restcountries.com'

    def handle(self, *args, **options):
        url = "https://restcountries.com/v3.1/all"

        try:
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()

            df = pd.DataFrame(data)
            name = df['name']
            country_code = df['cca3']
            flag = df['flags']

            for i in range(len(name)):
                country = Country.objects.create(
                    title=name.iloc[i].get('common'),
                    code=country_code.iloc[i],
                    flag=flag.iloc[i].get('png')
                )
                country.save()
            self.stdout.write(self.style.SUCCESS('Successfully parsed country data'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))