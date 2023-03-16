from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from YouGotSpam.models import Email

# https://docs.djangoproject.com/en/4.1/topics/http/file-uploads/

class saveEmail(BaseCommand):
    help = 'Saves an email file to the database'
    def add_arguments(self, parser):
        parser.add_argument('email_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for email_id in options['email_id']:
            try:
                email = Email.objects.get(pk=email_id)
            except Email.DoesNotExist:
                raise CommandError('Email "%s" does not exist' % email_id)
            
            #https://docs.djangoproject.com/en/4.1/ref/files/file/#the-contentfile-class
            content_file = ContentFile(b'Hello world!', name='hello-world.txt')
            instance = email(file_field=content_file)
            instance.save()
            self.stdout.write(self.style.SUCCESS('Successfully saved email'))
