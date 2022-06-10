from django.test import TestCase
from .models import Profile, Image
from django.contrib.auth.models import User

# Create your tests here.
class TestImage(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='kleitich', user=User(username='kleitich'))
        self.profile_test.save()

        self.image_test = Image(image='pic.png', caption='default test', user=self.profile_test)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)

    def test_total_likes(self):
        self.image_test.save_image()
        self.image_test.likes.add(self.profile_test)
        self.assertTrue(self.image_test.total_likes() == 1)

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='kleitch')
        self.user.save()
        self.profile_test = Profile(id=1, profile_picture='pic.jpg', bio='bio',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_profile(self):
        self.profile_test.save_profile()
        self.profile_test.delete_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) == 0)

    def test_search_profile(self):
        self.profile_test.save_profile()
        after = Profile.search_profile('kleitich')
        self.assertTrue(len(after) > 0)