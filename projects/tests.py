from django.test import TestCase
from .models import Project,User, Profile

class TestUser(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='john_doe', email='johndoe@example.com', password='password')

    def tearDown(self):
        User.objects.all().delete()

    def test_user_instance(self):
        self.assertIsInstance(self.new_user, User)

    def test_create_user(self):
        self.assertEqual(self.new_user.username, 'john_doe')
        self.assertEqual(self.new_user.email, 'johndoe@example.com')
        self.assertTrue(self.new_user.check_password('password'))
        
        with self.assertRaises(ValueError):
            User.objects.create_user(
                 username='', email='',  password=''
            )
        
    
class ProjectTest(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='john_doe', email='johndoe@example.com', password='password')

        self.new_project = Project.objects.create(title = "project", description = 'description.', link = "https://nbihnijb.com",  owner = self.new_user)

    def tearDown(self):
        User.objects.all().delete()
        Project.objects.all().delete()

    def test_instance(self):
        self.assertIsInstance(self.new_project, Project)
    
    def test_project(self):
        self.new_project.save()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    