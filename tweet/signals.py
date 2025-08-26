from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.apps import apps


from .models import Tweet


@receiver(post_save, sender=Tweet)
def create_history_on_tweet(sender, instance, created, **kwargs):
    if created:
        History = apps.get_model('history', 'History')


        timestamp = instance.created_at.strftime('%Y-%m-%d %H:%M:%S')
        summary = f"User {instance.user.username} Created tweet with a content of {instance.content} at {timestamp}"


        History.objects.create(
            user=instance.user,
            method='POST',
            tweet=instance,
            date=timezone.now(),
            summary=summary,
        )