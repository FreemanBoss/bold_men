from django.test import TestCase
from orders.models import Order
from payments.models import Payment
from django.contrib.auth import get_user_model
User = get_user_model()
from datetime import datetime

# Create your tests here.

class OrderModelTest(TestCase):
    def setUp(self):
        # User instance
        self.user = User.objects.create(username="testuser", email="test@example.com")

        # Payment instance
        self.payment = Payment.objects.create(amount=100.0)

        # Order instance
        self.order = Order.objects.create(user=self.user, status="Pending", payment=self.payment)

    def test_order_creation(self):
        # Check that the order was created successfully
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.status, "Pending")
        self.assertEqual(self.order.payment, self.payment)

    def test_order_string_representation(self):
        # Check that the string representation of the order is as expected
        expected_str = f"{self.user.username}'s Order"
        self.assertEqual(str(self.order), expected_str)

    def test_order_timestamps(self):
        # Check that created_at and updated_at timestamps are set correctly
        now = datetime.now()
        self.assertTrue(self.order.created_at <= now)
        self.assertTrue(self.order.updated_at <= now)
        self.assertTrue(self.order.created_at < self.order.updated_at)
