"""Funciones auxiliares reutilizables por todos los tests de saucedemo.com."""
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)

# ---- Datos de prueba ----
BASE_URL = "https://www.saucedemo.com/"
USUARIO_VALIDO = "standard_user"
PASSWORD_VALIDO = "secret_sauce"
TIMEOUT = 10  # segundos para las esperas explícitas


def esperar_visible(driver, locator, timeout=TIMEOUT):
    """Espera explícita hasta que el elemento sea visible y lo devuelve."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def esperar_clickeable(driver, locator, timeout=TIMEOUT):
    """Espera explícita hasta que el elemento sea clickeable y lo devuelve."""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def realizar_login(driver, usuario=USUARIO_VALIDO, password=PASSWORD_VALIDO):
    """Navega a la página de login e ingresa las credenciales."""
    logger.info("Navegando a %s", BASE_URL)
    driver.get(BASE_URL)

    logger.info("Ingresando credenciales del usuario '%s'", usuario)
    esperar_visible(driver, (By.ID, "user-name")).send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    esperar_clickeable(driver, (By.ID, "login-button")).click()


def obtener_primer_producto(driver):
    """Devuelve el primer producto del catálogo (esperando a que cargue)."""
    return esperar_visible(driver, (By.CLASS_NAME, "inventory_item"))
