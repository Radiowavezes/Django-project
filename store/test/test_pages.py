from django.test import TestCase
from django.urls import reverse


class TestStorePage(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/store/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("store:store"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("store:store"))
        self.assertTemplateUsed(response, "store.html")

    def test_template_content(self):
        response = self.client.get(reverse("store:store"))
        self.assertContains(response, """        <h2>
          Готові пропозиції
        </h2>""")
        self.assertNotContains(response, "Not on the page")
