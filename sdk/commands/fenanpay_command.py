from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'My command'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('All done'))
        return 0
