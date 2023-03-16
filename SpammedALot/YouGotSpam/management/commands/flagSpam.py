from django.core.management.base import BaseCommand, CommandError
from YouGotSpam.models import Email

class flagSpam(BaseCommand):
    help = 'Flags an email as spam'

    def add_arguments(self, parser):
        parser.add_argument('email_id', nargs='+', type=int)

    # THIS IS WHERE THE MAGIC HAPPENS!
    def handle(self, *args, **options):
        for email_id in options['email_id']:
            # GRAB AN EMAIL
            try:
                email = Email.objects.get(pk=email_id)
            except Email.DoesNotExist:
                raise CommandError('Email "%s" does not exist' % email_id)
            email.isSpam = True
            email.save()
            self.stdout.write(self.style.SUCCESS('Successfully flagged email as spam'))


# https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/
# from polls.models import Question as Poll

# class Command(BaseCommand):
#     help = 'Closes the specified poll for voting'

#     def add_arguments(self, parser):
#         parser.add_argument('poll_ids', nargs='+', type=int)

#     def handle(self, *args, **options):
#         for poll_id in options['poll_ids']:
#             try:
#                 poll = Poll.objects.get(pk=poll_id)
#             except Poll.DoesNotExist:
#                 raise CommandError('Poll "%s" does not exist' % poll_id)

#             poll.opened = False
#             poll.save()

#             self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))