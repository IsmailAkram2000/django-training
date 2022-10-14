# import Models and timezone

- from artists.models import Artist
- from albums.models import Albums
- from django.utils import timezone

# Create some artists

- Artist(Stage_name="Amr Diab", Social_link="https://www.facebook.com/Amr_Diab").save()
- Artist(Stage_name="Asala", Social_link="https://www.facebook.com/Asala").save()
- Artist(Stage_name="Nancy Ajram", Social_link="https://www.facebook.com/Nancy_Ajram").save()
- Artist(Stage_name="Om Kalthoum", Social_link="https://www.facebook.com/Om_Kalthoum").save()
- Artist(Stage_name="Tamer Hosney", Social_link="https://www.facebook.com/Tamer_Hosney").save()

# list down all artists

## Artist.objects.all()

- <QuerySet [

  <Artist: Stage_name: Amr Diab, Social_link: https://www.facebook.com/Amr_Diab>,

  <Artist: Stage_name: Asala, Social_link: https://www.facebook.com/Asala>,

  <Artist: Stage_name: Nancy Ajram, Social_link: https://www.facebook.com/Nancy_Ajram>,

  <Artist: Stage_name: Om Kalthoum, Social_link: https://www.facebook.com/Om_Kalthoum>,

  <Artist: Stage_name: Tamer Hosney, Social_link: https://www.facebook.com/Tamer_Hosney>

  ]>

# list down all artists sorted by name

## Artist.objects.all().order_by("Stage_name")

- <QuerySet [

  <Artist: Stage_name: Amr Diab, Social_link: https://www.facebook.com/Amr_Diab>,

  <Artist: Stage_name: Asala, Social_link: https://www.facebook.com/Asala>,

  <Artist: Stage_name: Nancy Ajram, Social_link: https://www.facebook.com/Nancy_Ajram>,

  <Artist: Stage_name: Om Kalthoum, Social_link: https://www.facebook.com/Om_Kalthoum>,

  <Artist: Stage_name: Tamer Hosney, Social_link: https://www.facebook.com/Tamer_Hosney>

  ]>

# list down all artists whose name starts with `a`

## Artist.objects.filter.Stage_name\_\_startswith='a')

- <QuerySet [
  <Artist: Stage_name: Amr Diab, Social_link: https://www.facebook.com/Amr_Diab>,
  <Artist: Stage_name: Asala, Social_link: https://www.facebook.com/Asala>
  ]>

# in 2 different ways, create some albums and assign them to any artists

## First Way

- Artist.objects.all()[0].id
- artist = Artist.objects.get(pk=10)
- artist.albums_set.create(name = "album1", release_date = timezone.now(), cost="99.99")

## Second Way

- Albums(artist = Artist.objects.get(pk=1) , name = "album2", release_date = timezone.now() , cost = 99.99).save()

# get the latest released album

## Albums.objects.latest('release_date')

- <Albums: name: album2, creation_date: 2022-10-14 20:20:49.997334+00:00, release_date: 2022-10-14 20:20:49.997334+00:00, cost: 99.99>

# get all albums released before today

## Albums.objects.filter(release_date**day**lt = timezone.now().day)

- <QuerySet []>

# get all albums released today or before but not after today

## Albums.objects.filter(release_date**day**lte = timezone.now().day)

- <QuerySet [

  <Albums: name: album1, creation_date: 2022-10-14 19:54:03.959223+00:00, release_date: 2022-10-14 19:54:03.958227+00:00, cost: 99.99>,

  <Albums: name: album2, creation_date: 2022-10-14 20:20:49.997334+00:00, release_date: 2022-10-14 20:20:49.997334+00:00, cost: 99.99>
  ]>

# count the total number of albums

## Albums.objects.count()

- 2

# in 2 different ways, for each artist, list down all of his/her albums

## First Way

- for artist in Artist.objects.all():  
   print(Albums.objects.filter(artist=artist.id))

- <QuerySet [<Albums: name: album1, creation_date: 2022-10-14 19:54:03.959223+00:00, release_date: 2022-10-14 19:54:03.958227+00:00, cost: 99.99>]>

  <QuerySet []>

  <QuerySet [<Albums: name: album2, creation_date: 2022-10-14 20:20:49.997334+00:00, release_date: 2022-10-14 20:20:49.997334+00:00, cost: 99.99>]>

  <QuerySet []>

  <QuerySet []>

## Second Way

- for artist in Artist.objects.all():
  print(artist.albums_set.all())

- <QuerySet [<Albums: name: album1, creation_date: 2022-10-14 19:54:03.959223+00:00, release_date: 2022-10-14 19:54:03.958227+00:00, cost: 99.99>]>

  <QuerySet []>

  <QuerySet [<Albums: name: album2, creation_date: 2022-10-14 20:20:49.997334+00:00, release_date: 2022-10-14 20:20:49.997334+00:00, cost: 99.99>]>

  <QuerySet []>

  <QuerySet []>

# list down all albums ordered by cost then by name

## Albums.objects.order_by('-cost' , 'name')

- <QuerySet [

  <Albums: name: album1, creation_date: 2022-10-14 19:54:03.959223+00:00, release_date: 2022-10-14 19:54:03.958227+00:00, cost: 99.99>,

  <Albums: name: album2, creation_date: 2022-10-14 20:20:49.997334+00:00, release_date: 2022-10-14 20:20:49.997334+00:00, cost: 99.99>]>
