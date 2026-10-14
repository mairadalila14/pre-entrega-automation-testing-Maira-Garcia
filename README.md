# Pre-Entrega Automation Testing – saucedemo.com

## Propósito del proyecto
Automatizar con **Selenium WebDriver y Python** flujos básicos de navegación sobre
[saucedemo.com](https://www.saucedemo.com), aplicando estrategias de localización de
elementos, esperas explícitas y validación de estados.

Casos automatizados:

| Archivo | Caso de prueba |
|---|---|
| `tests/test_login.py` | Login exitoso: redirección a `/inventory.html`, logo "Swag Labs" y título "Products" |
| `tests/test_inventory.py` | Título de página, productos visibles, nombre/precio del primer producto, menú y filtro |
| `tests/test_cart.py` | Agregar el primer producto, contador del carrito y verificación del ítem en el carrito |

## Tecnologías utilizadas
- Python 3.10+
- Pytest (estructura de testing)
- Selenium WebDriver (automatización)
- pytest-html (reporte HTML)
- Git y GitHub (control de versiones)

## Estructura del proyecto
```
pre-entrega-automation-testing-nombre-apellido/
├── tests/              # Casos de prueba
├── utils/              # Funciones auxiliares (login, esperas explícitas)
├── datos/              # Datos externos (CSV/JSON), si aplica
├── reports/            # Reporte HTML, capturas y logs
│   ├── screenshots/
│   └── logs/
├── conftest.py         # Fixtures y captura automática en fallos
├── pytest.ini
├── requirements.txt
└── README.md
```

## Instalación de dependencias
Requiere tener Google Chrome instalado (Selenium 4 gestiona el driver automáticamente).

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## Cómo ejecutar las pruebas
```bash
pytest tests -v --html=reports/reporte.html --self-contained-html
```

Modo sin ventana (opcional):
```bash
# Windows (PowerShell)
$env:HEADLESS="1"; pytest tests -v --html=reports/reporte.html --self-contained-html
# macOS / Linux
HEADLESS=1 pytest tests -v --html=reports/reporte.html --self-contained-html
```

## Evidencias
- **Reporte HTML:** `reports/reporte.html`
- **Capturas de pantalla automáticas en caso de fallo:** `reports/screenshots/`
- **Logs de ejecución:** `reports/logs/ejecucion.log`

## Criterios aplicados
- Cada test abre y cierra su propio navegador (los tests son independientes entre sí).
- Se usan esperas explícitas (`WebDriverWait`) en lugar de `sleep`.
- Nomenclatura descriptiva y comentarios en todos los archivos.
