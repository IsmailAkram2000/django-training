from celery import shared_task
from django.core.mail import send_mail
from artists.models import Artist
from musicplatform import settings
from datetime import datetime, timezone 

@shared_task()
def send_mail_task(album_name, artist_id):
    artist = Artist.objects.get(id=artist_id)

    send_mail(subject='Congratulations!',
    message=f'Congratulations {artist.Stage_name} on your new album',
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=[artist.user.email, ],
    fail_silently=True,
    )

    print('Email sent successfully')
    return f'Email sent successfully' 

# check last time the artist was active
def lastActive(artist):
    if artist.albums.all().count() == 0:
        return False
    lastAlbum = artist.albums.all().latest('created')
    time = datetime.now(timezone.utc) - lastAlbum.created
    return time.days <= 30


@shared_task()
def send_mail_non_active_task():
    nonActiveArtist = []
    
    for artist in Artist.objects.all(): 
        if not lastActive(artist):
            nonActiveArtist.append(artist.user.email)
    
    send_mail(
        subject = "Warning",
        message= "You weren't active for more than 30 days.",
        from_email= settings.EMAIL_HOST_USER,
        recipient_list=nonActiveArtist,
        fail_silently= False,
    )

    return 'Emails were sent successfully'