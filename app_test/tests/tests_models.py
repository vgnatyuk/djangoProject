from django.test import TestCase
from app_test.models import TestModel, AnotherModel


class ModelsTest(TestCase):
    def test_testmodel_create(self):
        counter = TestModel.objects.all().count()
        TestModel.objects.create(name='test_name', apartment_id=10)
        self.assertEqual(TestModel.objects.all().count(), counter + 1)

    def test_anothermodel_create(self):
        counter = AnotherModel.objects.all().count()
        AnotherModel.objects.create(another_name='another_test_name', another_id='id')
        self.assertEqual(AnotherModel.objects.all().count(), counter + 1)
