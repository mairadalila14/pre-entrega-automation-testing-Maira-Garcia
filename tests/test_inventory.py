"""Caso de prueba: Navegación y verificación del catálogo."""
import logging

from selenium.webdriver.common.by import By

from utils.helpers import esperar_visible

logger = logging.getLogger(__name__)


def test_titulo_pagina_inventario(driver_logueado):
    assert driver_logueado.title == "Swag Labs", "Título de la página incorrecto"


def test_existen_productos_visibles(driver_logueado):
    productos = driver_logueado.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se encontraron productos en el catálogo"
    assert productos[0].is_displayed(), "El primer producto no está visible"


def test_nombre_y_precio_del_primer_producto(driver_logueado):
    primer_producto = driver_logueado.find_elements(By.CLASS_NAME, "inventory_item")[0]

    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    logger.info("Primer producto: %s - %s", nombre, precio)

    assert nombre == "Sauce Labs Backpack", f"Nombre inesperado: {nombre}"
    assert precio == "$29.99", f"Precio inesperado: {precio}"


def test_menu_y_filtro_presentes(driver_logueado):
    menu = esperar_visible(driver_logueado, (By.ID, "react-burger-menu-btn"))
    assert menu.is_displayed(), "El menú no está visible"

    filtro = esperar_visible(driver_logueado, (By.CLASS_NAME, "product_sort_container"))
    assert filtro.is_displayed(), "El filtro de ordenamiento no está visible"
