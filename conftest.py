"""Fixtures compartidas y evidencias automáticas (capturas) para pytest."""
import base64
import logging
import os
from datetime import datetime

import pytest
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.helpers import realizar_login, esperar_visible
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)
CARPETA_CAPTURAS = os.path.join("reports", "screenshots")


@pytest.fixture
def driver():
    """Crea un navegador nuevo por test (garantiza independencia entre tests)."""
    opciones = Options()
    opciones.add_argument("--start-maximized")
    # Desactiva popups del gestor de contraseñas de Chrome
    opciones.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    if os.getenv("HEADLESS") == "1":
        opciones.add_argument("--headless=new")
        opciones.add_argument("--window-size=1920,1080")

    navegador = webdriver.Chrome(options=opciones)
    logger.info("Navegador iniciado")
    yield navegador
    navegador.quit()
    logger.info("Navegador cerrado")


@pytest.fixture
def driver_logueado(driver):
    """Navegador ya autenticado y ubicado en el inventario."""
    realizar_login(driver)
    esperar_visible(driver, (By.CLASS_NAME, "inventory_item"))
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Si un test falla, guarda captura de pantalla y la adjunta al reporte HTML."""
    outcome = yield
    reporte = outcome.get_result()

    if reporte.when == "call" and reporte.failed:
        navegador = item.funcargs.get("driver")
        if navegador is None:
            return

        os.makedirs(CARPETA_CAPTURAS, exist_ok=True)
        marca = datetime.now().strftime("%Y%m%d_%H%M%S")
        ruta = os.path.join(CARPETA_CAPTURAS, f"{item.name}_{marca}.png")
        navegador.save_screenshot(ruta)
        logger.error("Test '%s' falló. Captura guardada en %s", item.name, ruta)

        with open(ruta, "rb") as archivo:
            imagen_b64 = base64.b64encode(archivo.read()).decode()
        reporte.extras = getattr(reporte, "extras", []) + [extras.png(imagen_b64)]
