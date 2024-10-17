from django.test import TestCase, Client
from fabrics.models import Fabric
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('fabrics:fabric-list')
        

    def test_fabric_list_GET(self):

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fabrics/fabric_list.html')
        

class FabricModelTestCase(TestCase):
    """
    Test case for the Fabric model.
    """


    def setUp(self):
        """
        Setup method to create test data before each test.
        """
        Fabric.objects.create(
            name="Test Fabric",
            description="This is a test fabric.",
            price=10.50
        )

    def test_fabric_creation(self):
        """
        Test case to verify that a Fabric instance is created correctly.
        """
        # Retrieve the Fabric instance created in the setUp method
        fabric = Fabric.objects.get(name="Test Fabric")
        
        # Check if the Fabric instance exists
        self.assertIsNotNone(fabric)

        # Check if the Fabric instance attributes are correct
        self.assertEqual(fabric.name, "Test Fabric")
        self.assertEqual(fabric.description, "This is a test fabric.")
        self.assertEqual(fabric.price, 10.50)

    def test_fabric_string_representation(self):
        """
        Test case to verify the string representation of a Fabric instance.
        """
        fabric = Fabric.objects.get(name="Test Fabric")
        
        # Check if the string representation of the Fabric instance is correct
        self.assertEqual(str(fabric), "Test Fabric")

