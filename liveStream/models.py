from django.db import models

# Create your models here.
class ArtistModel(models.Model):
    title = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    artist_name = models.CharField(max_length = 200)

    def __str__(self) -> str:
        return self.artist_name

class FileModel(models.Model):
    song = models.ForeignKey(ArtistModel,on_delete= models.CASCADE,null=True)
    upload_file = models.FileField()
    audio_id = models.IntegerField(null=True)

    def post_upload(self):
        return self.upload_file
    
    def get_uplaod(self):
        return self.song,self.upload_file


