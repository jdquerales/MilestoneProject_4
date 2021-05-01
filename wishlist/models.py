from django.db import models

class WishManager(models.Manager):
    def validateWish(self, post_data):
        is_valid = True
        errors = []
        if len(post_data.get('item')) < 3:
            is_valid = False
            errors.append('Message must be more than 3 characters')
            return (is_valid, errors)

class Wish(models.Model):
 #   user = models.ForeignKey(User, related_name="wishes")
    item = models.CharField(max_length=255)
#    wishers = models.ManyToManyField(User, related_name="items")
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    objects = WishManager()
