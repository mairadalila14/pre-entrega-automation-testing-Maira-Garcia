"""Caso de prueba: Automatización de Login."""
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.helpers import realizar_login, esperar_visible, TIMEOUT

logger = logging.getLogger(__name__)


def test_login_exitoso(driver):
    realizar_login(driver)

    # Espera explícita: validar redirección a /inventory.html
    WebDriverWait(driver, TIMEOUT).until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"

    # Validación de textos de la página de inventario
    logo = esperar_visible(driver, (By.CLASS_NAME, "app_logo"))
    assert logo.text == "Swag Labs", f"Logo inesperado: {logo.text}"

    titulo = esperar_visible(driver, (By.CSS_SELECTOR, "[data-test='title']"))
    assert titulo.text == "Products", f"Título inesperado: {titulo.text}"
    logger.info("Login exitoso validado")
