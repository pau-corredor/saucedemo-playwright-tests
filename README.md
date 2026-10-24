# SauceDemo Playwright Tests

[![Playwright tests](https://github.com/pau-corredor/saucedemo-playwright-tests/actions/workflows/tests.yml/badge.svg)](https://github.com/pau-corredor/saucedemo-playwright-tests/actions/workflows/tests.yml)
Pruebas automatizadas de interfaz sobre [SauceDemo](https://www.saucedemo.com), una tienda en línea de demostración, hechas con Playwright, Python y pytest.

Este proyecto automatiza los 17 casos de prueba manuales que diseñé en [saucedemo-qa-testing](https://github.com/pau-corredor/saucedemo-qa-testing).

## Qué cubre
- **Login:** usuario válido, bloqueado, credenciales incorrectas y campos vacíos
- **Menú:** cerrar sesión
- **Inventario:** ordenar productos, agregar y quitar productos, imágenes y precios
- **Carrito:** ver y quitar productos
- **Checkout:** datos válidos, apellido vacío, finalizar la compra y verificar el total del pedido

## Herramientas
Python 3.13, Playwright, pytest, PyCharm y Git/GitHub.

## Cómo correrlo
En PowerShell, dentro de la carpeta del proyecto:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
pytest
```

Para ver el navegador mientras corre:

```powershell
pytest --headed --slowmo 500
```

## Estructura
- `tests/`: pruebas, organizadas por módulo (login, menú, inventario, carrito y checkout)
- `requirements.txt`: dependencias del proyecto

## Estado
- ✅ 17 casos automatizados
- ✅ Pruebas corriendo automáticamente con GitHub Actions
- ⏳ En progreso: reorganizar el código con Page Object Model (POM)

## Autora
Paula, Bogotá, Colombia.