from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio de Prueba",
            ciudad="Ciudad de Prueba",
            pais="País de Prueba"
        )

    def test_laboratorio_data(self):
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, "Laboratorio de Prueba")
        self.assertEqual(laboratorio.ciudad, "Ciudad de Prueba")
        self.assertEqual(laboratorio.pais, "País de Prueba")

class LaboratorioViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio de Vista",
            ciudad="Ciudad de Vista",
            pais="País de Vista"
        )

    def test_laboratorio_detail_view(self):
        response = self.client.get(reverse('laboratorio_detail', args=[self.laboratorio.id]))
        self.assertEqual(response.status_code, 200)

    def test_laboratorio_detail_view_template_and_content(self):
        url = reverse('laboratorio_detail', args=[self.laboratorio.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_detail.html')
        self.assertContains(response, "Laboratorio de Vista")
        self.assertContains(response, "Ciudad de Vista")
        self.assertContains(response, "País de Vista")
