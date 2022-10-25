from django.test import TestCase
from app_media.forms import RegisterForm, RegisterFormUpdate, EntryForm, UploadFileForm
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class FileFormTest(TestCase):
    def test_file_forms(self):
        cwd = os.getcwd()
        file_csv = open(os.path.join(cwd, 'app_media', 'tests', 'tests_file', 'file.csv'), "rb")
        file = SimpleUploadedFile(file_csv.name, file_csv.read())
        post_dict = {'name': 'Test name'}
        file_dict = {'file': file}
        form = UploadFileForm(data=post_dict, files=file_dict)
        self.assertTrue(form.is_valid())

class RegUpdateFormTest(TestCase):
    def test_regup_forms(self):
        form = RegisterFormUpdate({'number': 7777777, 'city': 'test'})
        self.assertTrue(form.is_valid())

class RegisterFormTest(TestCase):
    def test_regup_forms(self):
        form = RegisterFormUpdate({'first_name': 'test_name', 'last_name': 'test_lname',
                                   'email': 'test@test.ru', 'number': 7777777, 'city': 'test'})
        self.assertTrue(form.is_valid())

class EntryFormTest(TestCase):
    def test_entry_forms(self):
        cwd = os.getcwd()
        image_jpg = open(os.path.join(cwd, 'app_media', 'tests', 'tests_file', 'image.jpg'), "rb")
        image = SimpleUploadedFile(image_jpg.name, image_jpg.read())
        post_dict = {'name': 'test_name', 'description': 'test_desc'}
        file_dict = {'file': image}
        form = EntryForm(data=post_dict, files=file_dict)
        self.assertTrue(form.is_valid())