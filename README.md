Link de acceso a la pagina https://compralia.streamlit.app/

# Motor de Búsqueda de Comercio Electrónico con Streamlit

Esta aplicación de Streamlit proporciona una interfaz de búsqueda básica para consultar múltiples plataformas de comercio electrónico 
(Amazon, eBay, MercadoLibre, AliExpress y Walmart). También incluye un formulario de comentarios para recopilar la opinión de los usuarios 
sobre su experiencia.

**Nota:** Esta aplicación actualmente utiliza marcadores de posición (placeholders) para la funcionalidad de búsqueda real. 
Para que sea completamente funcional, necesita implementar el web scraping o las llamadas a la API para cada plataforma de comercio electrónico. 
Tenga en cuenta sus términos de servicio y los posibles límites de velocidad al hacer scraping.

## Características

*   **Búsqueda en Múltiples Plataformas:** Permite a los usuarios ingresar una consulta de búsqueda y (eventualmente)
*   recuperar resultados de Amazon, eBay, MercadoLibre, AliExpress y Walmart.
*   **Interfaz de Usuario Simple:** Construida con Streamlit para facilitar la implementación y la interacción.
*   **Recopilación de Comentarios:** Recopila comentarios de los usuarios, incluyendo nombre, país, consulta de búsqueda,
*   nivel de satisfacción y comentarios adicionales.
*   **Datos Persistentes:** Guarda los comentarios en un archivo CSV.

## Cómo Ejecutar

1.  **Prerrequisitos:**
    *   Python 3.7+
    *   Streamlit: `pip install streamlit`
    *   Pandas: `pip install pandas`
    *   Requests: `pip install requests`
    *   BeautifulSoup4: `pip install beautifulsoup4`

2.  **Clonar el Repositorio (Opcional):** Si tiene el código en un repositorio Git:

    ```bash
    git clone <url_del_repositorio>
    cd <directorio_del_repositorio>
    ```

3.  **Ejecutar la Aplicación:**

    ```bash
    streamlit run nombre_del_script.py  # Reemplace nombre_del_script.py con el nombre real del archivo
    ```

    Streamlit abrirá automáticamente una nueva pestaña en su navegador web con la aplicación en ejecución.

## Uso

1.  **Página de Inicio (Index):** Proporciona un mensaje de bienvenida y muestra (o mostraría) elementos populares.
2.  *Nota: Esta sección requiere una implementación adicional para mostrar imágenes reales.*

3.  **Página de Resultados de Búsqueda:**
    *   Ingrese su consulta de búsqueda en el campo de entrada de texto.
    *   Haga clic en el botón "Buscar". *Actualmente, esto muestra resultados de marcador de posición. Para utilizar los enlaces generados, DEBE hacer clic en el botón "Ver Resultados de Búsqueda"*
    *   Los resultados de búsqueda de cada plataforma (eventualmente) se mostrarán.
    *   *Nota: Se necesita la implementación de web scraping para la funcionalidad de búsqueda de cada plataforma.*

4.  **Página de Comentarios:**
    *   Ingrese su nombre, país y la consulta de búsqueda que utilizó.
    *   Seleccione su nivel de satisfacción en el menú desplegable.
    *   Proporcione cualquier comentario adicional en el área de texto.
    *   Haga clic en el botón "Enviar Comentarios". Sus comentarios se guardarán en `feedback.csv`.

## Detalles de Implementación

*   **Función `main()`:** La función principal controla el diseño y la lógica de la aplicación Streamlit.
*   **Funciones `search_amazon(query)` , `search_ebay(query)`, `search_mercadolibre(query)`, `search_aliexpress(query)`,
*    `search_walmart(query)`:** Estas funciones son marcadores de posición para el web scraping real o las llamadas API a las
*    respectivas plataformas de comercio electrónico. Deben implementarse utilizando bibliotecas como `requests` y `BeautifulSoup4` o
*    utilizando las API de las plataformas (si están disponibles).
*   **Función `save_feedback(name, country, query, satisfaction, comment)`:** Guarda los comentarios del usuario en un archivo CSV
*   llamado `feedback.csv`.
*   **Estado de Sesión:** El estado de sesión de Streamlit se utiliza para preservar la consulta de búsqueda al navegar entre páginas.
*   **Web Scraping:** El web scraping mínimo para el ejemplo requiere manejo de errores y límites de velocidad para evitar ser bloqueado
*   por los sitios web. Considere usar proxies y técnicas de scraping robustas.

Descargo de Responsabilidad sobre Web Scraping (Fines Educativos)

Este proyecto fue desarrollado con fines puramente educativos y demostrativos. El web scraping implementado, si lo hubiera, 
se realizó únicamente para la obtención de datos de prueba y análisis en el contexto de un proyecto final académico.
Se ha procurado seguir las siguientes pautas en la medida de lo posible:
Respeto a :robots.txt Se ha intentado verificar y respetar el archivo de los sitios web scrapeados para evitar el acceso a 
secciones no permitidas y el cumplimiento de las directivas de rastreo.robots.txt
Evitar la sobrecarga: Se han implementado medidas (como retrasos en las solicitudes) para evitar la sobrecarga de los servidores de destino.
Fines no comerciales: Los datos obtenidos no se utilizaron con fines comerciales, de lucro, o para la creación de productos o servicios.
Conocimiento de la fragilidad: Se reconoce que el web scraping puede ser una técnica frágil y que los sitios web pueden cambiar su estructura
o términos de servicio en cualquier momento.
Se enfatiza que este proyecto no fue diseñado para ser utilizado en un entorno de producción o con fines ilegales o no éticos. Si en algún
momento se utilizara la funcionalidad de web scraping fuera del ámbito educativo, sería responsabilidad del usuario asegurarse de que 
cumple con todas las leyes, regulaciones y términos de servicio aplicables.
Los autores de este proyecto no se hacen responsables del uso indebido o ilegal de la información o el código aquí proporcionado.
## Descargo de Responsabilidad sobre Web Scraping

