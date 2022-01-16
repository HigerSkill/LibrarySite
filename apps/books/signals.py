from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.books.models import Book
from apps.subscribers.models import Subscriber


@receiver(post_save, sender=Book)
def send_emails_on_books_creation(instance, created, *args, **kwargs):
    """Send emails to subscribers on books creations.

    TODO: Don't send an email about books published in the future, if necessary
    """
    if not created:
        return

    # Send email to all subscribers about new book
    send_mail(
        subject='New book was added',
        message=f"New book {str(instance)} was added.",
        from_email='from@example.com',
        recipient_list=Subscriber.objects.values_list('email', flat=True),
        fail_silently=False,
    )
