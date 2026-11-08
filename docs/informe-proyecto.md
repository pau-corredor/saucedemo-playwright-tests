# Informe del proyecto: SauceDemo Playwright Tests

## 1. Información general
- **Nombre del proyecto:** SauceDemo Playwright Tests: automatización de pruebas de interfaz
- **Especialidad:** QA
- **Fuente del proyecto:** App de práctica (SauceDemo, una tienda en línea de demostración). Los casos de prueba salen de mi proyecto 1 de pruebas manuales.
- **Link a la fuente original:** https://www.saucedemo.com
- **Link al proyecto publicado:** https://github.com/pau-corredor/saucedemo-playwright-tests

## 2. Objetivo
Automatizar los 17 casos de prueba manuales de una tienda en línea (login, inventario, carrito y checkout), para revisar sus flujos principales de forma rápida y repetible, sin repetir las pruebas a mano en cada cambio. Está pensado para un equipo de desarrollo y QA que necesita saber si un cambio rompió algo importante. El riesgo que busca prevenir es que fallen sin que nadie lo note acciones críticas, como iniciar sesión, agregar productos al carrito o completar una compra. Las pruebas corren solas en GitHub Actions cada vez que se sube código.

## 3. Plan de trabajo
1. **Exploración inicial (análisis de requisitos):** exploré SauceDemo con sus 6 usuarios de prueba y anoté cómo debe funcionar cada módulo (login, inventario, carrito y checkout), usando `standard_user` como referencia.
2. **Preparación (diseño de casos de prueba):** diseñé 17 casos de prueba manuales en un proyecto anterior y preparé el entorno de automatización (Python 3.13, Playwright, pytest y un repositorio en GitHub).
3. **Construcción (ejecución de pruebas automatizadas):** automaticé los 17 casos con Playwright y los organicé por módulo. En cada uno comprobé que la prueba realmente vigila algo, cambiando a propósito el resultado esperado para ver que fallara.
4. **Evaluación (cobertura y bugs encontrados):** los 17 casos pasan con `standard_user`. Configuré GitHub Actions para correrlos solos y, al ejecutarlos allí, una prueba falló por un problema de tiempos en la página; la corregí agregando una espera. Los 10 bugs de los otros usuarios están documentados en el proyecto anterior.
5. **Conclusiones y próximos pasos:** documenté el proyecto en el README y en este informe. Quedan como mejora ampliar el Page Object Model al carrito y al checkout.

## 4. Preguntas clave
1. **¿Qué pasaría si el login o el botón Finish fallaran en producción?**
2. **¿Mis pruebas detectan fallos de verdad o solo pasan?**
3. **¿Las pruebas son estables o fallan a veces por tiempos?**
   
## 5. Qué se hizo y cómo
**Tipos de pruebas aplicadas**
- Pruebas funcionales de interfaz (de punta a punta) sobre los flujos principales: login, inventario, carrito y checkout.
- Pruebas positivas (el flujo normal funciona) y negativas (usuario bloqueado, credenciales incorrectas, campos vacíos, apellido vacío en el checkout).

**Herramientas**
- Python 3.13, Playwright y pytest para escribir y correr las pruebas.
- PyCharm como editor, y Git y GitHub para el control de versiones.
- GitHub Actions para correr las pruebas automáticamente en cada cambio.

**Decisiones técnicas**
- Automaticé los 17 casos que diseñé antes de forma manual ([saucedemo-qa-testing](https://github.com/pau-corredor/saucedemo-qa-testing)), organizados en un archivo por módulo.
- Usé localizadores estables (`data-test` o `id`) en vez de clases de estilo, que cambian con más frecuencia.
- Cada verificación comprueba algo concreto: textos de error, direcciones, que un elemento sea visible, el atributo `src` de las imágenes y que el contador del carrito suba o desaparezca.
- Apliqué el Page Object Model en el login, el inventario y el carrito: `LoginPage`, `InventoryPage` (cerrar sesión, agregar productos, ordenar y abrir el carrito) y `CartPage`. Además, un archivo `config.py` con el usuario y la contraseña, para cambiarlos en un solo lugar. El checkout y algunas pruebas del inventario todavía usan localizadores directos y quedan como próximo paso.
- Al correr las pruebas en GitHub Actions, una falló por un tema de tiempos entre pantallas. La corregí agregando una espera al elemento correcto.

**Criterios de aceptación**
- Cada caso pasa con `standard_user` y cumple el resultado esperado de mi documento de casos de prueba.
- Las 17 pruebas corren en verde en GitHub Actions.
- Fuera de alcance por ahora: automatizar los otros usuarios de prueba (los que tienen defectos), pruebas de rendimiento y de seguridad.

## 6. Resultados
**Cobertura lograda**
- 17 de 17 casos de prueba automatizados.
- Por módulo: Login (5), Menú (1), Inventario (5), Carrito (2) y Checkout (4).
- Resultado: las 17 pruebas pasan con `standard_user`, tanto en mi computador como en GitHub Actions.

**Bugs encontrados**
Los defectos de la aplicación los encontré al probarla con los otros usuarios de prueba, en la fase manual de este trabajo ([reportes de bugs](https://github.com/pau-corredor/saucedemo-qa-testing/blob/main/bug-reports/bug-reports.md)). En total son 10: 4 de severidad alta, 5 media y 1 baja.

| Severidad | Ejemplos |
|---|---|
| Alta | El botón Finish no permite completar la compra (`error_user`); los precios de la lista no coinciden con los del detalle (`visual_user`) |
| Media | El ordenamiento de productos no funciona; no permite agregar todos los productos; la página carga con demoras (`performance_glitch_user`) |
| Baja | Elementos desalineados o fuera de lugar (`visual_user`) |

**Hallazgo de la automatización**
Al correr las pruebas en GitHub Actions, una falló por un tema de tiempos entre pantallas (no por un defecto de la aplicación). La corregí esperando a que la página mostrara el elemento correcto.

**Alcance**
Las pruebas automatizadas cubren el comportamiento esperado con `standard_user`. Los defectos de los otros usuarios están documentados, pero no automatizados.

## 7. Conclusiones
**Qué aprendí**
- A pasar de pruebas manuales a pruebas automatizadas con Playwright y Python, y a organizarlas por módulo.
- A elegir localizadores estables (`data-test` o `id`) y a manejar casos en que un mismo localizador encuentra varios elementos.
- Que un `passed` no basta: hay que comprobar que la prueba falla cuando cambio a propósito el resultado esperado.
- A leer los errores de pytest y de Playwright para encontrar la causa.
- Que una prueba puede pasar en mi computador y fallar en otro entorno por una cuestión de tiempos, y a corregirlo esperando al elemento correcto.
- A usar el Page Object Model y un archivo de configuración para no repetir código y cambiar los datos en un solo lugar.

**Qué mejoraría con más tiempo**
- Completar el Page Object Model con la página del checkout y las pruebas del inventario que faltan.
- Hacer que el inicio de sesión se ejecute solo antes de cada prueba, con una fixture de pytest.
- Automatizar los otros usuarios de prueba y marcar como fallas esperadas los defectos ya documentados.
- Generar un reporte HTML con capturas de los fallos y correr las pruebas en más navegadores.

**Qué mencionaría en una entrevista**
- El proceso completo: diseñé los casos y encontré 10 bugs de forma manual, y después automaticé los casos con Playwright y los conecté a GitHub Actions.
- El fallo por tiempos que apareció al correr las pruebas en GitHub Actions: cómo lo detecté en el log y cómo lo resolví.
- El hábito de verificar que mis pruebas realmente vigilan algo.
- 
## 8. Checklist antes de publicar
- [ ] README explica el proyecto sin necesidad de revisar todo el detalle
- [ ] Archivos organizados, sin pruebas sueltas o versiones viejas
- [ ] Sin credenciales ni datos sensibles en el repositorio
- [ ] Link a la fuente original incluido y funcionando
- [ ] Proyecto publicado y accesible (repo, sitio en vivo, o prototipo interactivo según corresponda)
- [ ] Link compartido con tu coach