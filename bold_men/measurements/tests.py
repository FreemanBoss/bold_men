from django.test import TestCase
from django.contrib.auth import get_user_model
from measurements.models import Measurement

User = get_user_model()

class MeasurementModelTestCase(TestCase):
    """
    Test case for the Measurement model.
    """

    def setUp(self):
        """
        Setup method to create test data before each test.
        """
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="testpassword")
        self.measurement = Measurement.objects.create(
            user=self.user,
            chest=30.5,
            waist=25.0,
            hip=35.5,
            length=50.0,
            created_at="2024-04-30 12:00:00",
            updated_at="2024-04-30 12:00:00"
        )

    def test_measurement_creation(self):
        """
        Test case to verify that a Measurement instance is created correctly.
        """
        # Retrieve the Measurement instance created in the setUp method
        measurement = Measurement.objects.get(user=self.user)
        
        # Check if the Measurement instance exists
        self.assertIsNotNone(measurement)

        # Check if the Measurement instance attributes are correct
        self.assertEqual(measurement.user, self.user)
        self.assertEqual(measurement.chest, 30.5)
        self.assertEqual(measurement.waist, 25.0)
        self.assertEqual(measurement.hip, 35.5)
        self.assertEqual(measurement.length, 50.0)
        self.assertEqual(str(measurement.created_at), "2024-04-30 12:00:00")
        self.assertEqual(str(measurement.updated_at), "2024-04-30 12:00:00")

    def test_measurement_string_representation(self):
        """
        Test case to verify the string representation of a Measurement instance.
        """
        measurement = Measurement.objects.get(user=self.user)
        
        # Check if the string representation of the Measurement instance is correct
        self.assertEqual(str(measurement), f"{self.user} - 2024-04-30 12:00:00")

    def test_user_measurement_info_property(self):
        """
        Test case to verify the user_measurement_info property of a Measurement instance.
        """
        measurement = Measurement.objects.get(user=self.user)
        
        # Check if the user_measurement_info property returns the correct value
        self.assertEqual(measurement.user_measurement_info, "30.5-25.0-35.5-50.0")

