from django.test import TestCase
from django.contrib.auth import get_user_model
from contracts.models import Contract
from fabrics.models import Fabric
from orders.models import Order
from measurements.models import Measurement

User = get_user_model()

class ContractModelTestCase(TestCase):
    """
    Test case for the Contract model.
    """

    def setUp(self):
        """
        Setup method to create test data before each test.
        """
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="testpassword")
        self.fabric1 = Fabric.objects.create(name="Fabric 1", description="Fabric 1 description", price=10.00)
        self.fabric2 = Fabric.objects.create(name="Fabric 2", description="Fabric 2 description", price=15.00)
        self.measurement = Measurement.objects.create(user=self.user, chest=30.5, waist=25.0, hip=35.5, length=50.0)
        self.order = Order.objects.create(user=self.user, total_price=25.00)
        self.contract = Contract.objects.create(
            user=self.user,
            specification="Test specification",
            order=self.order
        )
        self.contract.fabric.add(self.fabric1)
        self.contract.fabric.add(self.fabric2)

    def test_contract_creation(self):
        """
        Test case to verify that a Contract instance is created correctly.
        """
        # Retrieve the Contract instance created in the setUp method
        contract = Contract.objects.get(user=self.user)
        
        # Check if the Contract instance exists
        self.assertIsNotNone(contract)

        # Check if the Contract instance attributes are correct
        self.assertEqual(contract.user, self.user)
        self.assertEqual(contract.specification, "Test specification")
        self.assertEqual(contract.order, self.order)

        # Check if the fabrics are associated with the contract correctly
        self.assertIn(self.fabric1, contract.fabric.all())
        self.assertIn(self.fabric2, contract.fabric.all())

    def test_contract_string_representation(self):
        """
        Test case to verify the string representation of a Contract instance.
        """
        contract = Contract.objects.get(user=self.user)
        
        # Check if the string representation of the Contract instance is correct
        self.assertEqual(str(contract), f"{self.user} - {self.order}")
