"""Caso de prueba: Interacción con productos (carrito de compras)."""
import logging

from selenium.webdriver.common.by import By

from utils.helpers import (
    esperar_visible,
    esperar_clickeable,
    obtener_primer_producto,
)

logger = logging.getLogger(__name__)


def test_agregar_primer_producto_al_carrito(driver_logueado):
    # Agregar el primer producto
    primer_producto = obtener_primer_producto(driver_logueado)
    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_producto.find_element(By.TAG_NAME, "button").click()
    logger.info("Producto agregado: %s", nombre_producto)

    # Verificar que el contador del carrito se incrementa
    contador = esperar_visible(driver_logueado, (By.CLASS_NAME, "shopping_cart_badge"))
    assert contador.text == "1", f"Contador esperado '1', se obtuvo '{contador.text}'"

    # Navegar al carrito
    esperar_clickeable(driver_logueado, (By.CLASS_NAME, "shopping_cart_link")).click()

    # Comprobar que el producto aparece correctamente en el carrito
    nombre_en_carrito = esperar_visible(
        driver_logueado, (By.CLASS_NAME, "inventory_item_name")
    ).text
    assert nombre_en_carrito == nombre_producto, (
        f"Se esperaba '{nombre_producto}' en el carrito y se encontró '{nombre_en_carrito}'"
    )
