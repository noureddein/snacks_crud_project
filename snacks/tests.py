from urllib import request
from django.test import TestCase
from django.urls import reverse
from snacks.models import Snack
from django.contrib.auth.models import User


class SnackTest(TestCase):
    def setUp(self):
        kebab_snack = Snack.objects.create(
            title='Salad',
            description='Mixed vegetables',
            purchaser=User.objects.create_user(
                'admin', 'admin@admin.com', 'admin')
        )

    # Test home page
    def test_home_page_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "index.html")
        self.assertTemplateUsed(response, "_base.html")

    # Test create snack
    def test_create_snack_page_template(self):
        url = reverse("create-snack")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "create_snack.html")

    def test_create_snack_page_status_code(self):
        url = reverse("create-snack")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # Test snack detail
    def test_snack_detail_page_template(self):
        url = reverse("snack-detail", args=['1'])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_detail_page_status_code(self):
        url = reverse("snack-detail", args=['1'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # Test delete snack
    def test_delete_snack_page_template(self):
        url = reverse("delete-snack", args=['1'])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "delete_snack.html")

    def test_delete_snack_page_status_code(self):
        url = reverse("delete-snack", args=['1'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # Test update snack
    def test_update_snack_page_template(self):
        url = reverse("update-snack", args=['1'])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "update_snack.html")

    def test_update_snack_page_status_code(self):
        url = reverse("update-snack", args=['1'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
