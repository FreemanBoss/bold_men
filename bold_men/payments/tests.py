from django.test import TestCase
from payments.models import Payment

class PaymentModelTestCase(TestCase):
    """
    Test case for the Payment model.
    """

    def setUp(self):
        """
        Setup method to create test data before each test.
        """
        Payment.objects.create(
            amount=100.00,
            method="Credit Card",
            created_at="2024-04-30 12:00:00"
        )

    def test_payment_creation(self):
        """
        Test case to verify that a Payment instance is created correctly.
        """
        # Retrieve the Payment instance created in the setUp method
        payment = Payment.objects.get(amount=100.00)
        
        # Check if the Payment instance exists
        self.assertIsNotNone(payment)

        # Check if the Payment instance attributes are correct
        self.assertEqual(payment.amount, 100.00)
        self.assertEqual(payment.method, "Credit Card")
        self.assertEqual(str(payment.created_at), "2024-04-30 12:00:00")

    def test_payment_string_representation(self):
        """
        Test case to verify the string representation of a Payment instance.
        """
        payment = Payment.objects.get(amount=100.00)
        
        # Check if the string representation of the Payment instance is correct
        self.assertEqual(str(payment), "Payment object (100.00)")

