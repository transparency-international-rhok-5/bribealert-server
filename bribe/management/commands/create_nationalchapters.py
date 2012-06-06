from django.core.management.base import BaseCommand

from bribe.models import NationalChapter, Country

class Command(BaseCommand):
    def handle(self, *args, **options):
        for country in Country.objects.all():
            chapter = NationalChapter()
            chapter.country = country
            chapter.name = country.name
            chapter.save()
