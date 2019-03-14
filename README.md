# Proyecto 1 Semillero

## Proyecto 1: Market Basket Analysis ( Datos estructurados )
### I.Introducción
Sea que hagamos las compras a partir de caprichos, necesidades inmediatas o a través de listas planeadas, las formas las que compramos comida son únicas y están altamente influenciado por nuestros hábitos. Una aplicación de pedido y entrega de comestibles, tiene como objetivo facilitar este proceso y hacerlo en el momento que usted los necesite. Después de seleccionar productos en la aplicación, los compradores personales revisan su pedido y hacen las compras y la entrega en la tienda por usted.	
El cliente actualmente posee 3 retos de negocio los cuales espera que usted como profesional en analítica pueda abordar:
1.	Segmentar los diferentes tipos de clientes que tiene basado en sus comportamientos de consumo, con el fin de establecer estrategias de mercadeo específicas para cada segmento.
2.	Identificar los factores que influyen en la recompra de productos con el fin de entender mejor a los usuarios y  hacer cambios en los sistemas de recomendación.


### II.Bases de datos
El conjunto de datos es un conjunto relacional de archivos que describen las órdenes de los clientes a lo largo del tiempo. Es anónimo y contiene una muestra de más de 200,000 usuarios en 3 millones de pedidos. Para cada usuario, se proporcionan entre 4 y 100 de sus pedidos, con la secuencia en orden cronológico de productos comprados en cada pedido y variables de temporalidad (semana y la hora del día en que se realizó el pedido  y una medida relativa del tiempo entre los pedidos).

Descripciones de las bases de datos

Cada entidad (cliente, producto, pedido, pasillo, etc.) tiene un ID único asociada. 
1.	aisles.csv: contiene los nombres de las islas de productos(pasillos) y sus IDs asociados.
2.	departments.csv: contiene los nombres de los departamentos de productos y sus IDs asociados.
3.	order_products__*.csv: Especifica qué productos se compraron en cada pedido, además muestra los contenidos de pedidos anteriores para todos los clientes. Puede incluir la palabra 'reordered' lo cual indica que el cliente tiene un pedido anterior que contiene el mismo producto. Tenga en cuenta que algunas órdenes no tendrán artículos reordenados y que además puede predecir un valor 'None' en clientes en los cuales considere que no existirá una recompra de productos, (“*” puede ser prior o train, en ambos casos podemos omitir dicha clasificacion ya que nuestra finalidad es identificar patrones de consumo).
4.	orders.csv:  Contiene las ordines con sus respectivos IDs y respectivas variables de tiempo  asociadas.

5.	Products.csv: contiene los nombres de los productos y sus IDs, departamento e islas asociados.


### III. Proyecto
Estructure un modelo que ayude a suplir las necesidades de negocio del cliente, los
Entregables esperados por el cliente son los siguientes:

1. Documento detallado que contenga la siguiente estructura:

•	Planteamiento de necesidad del negocio
•	Fuentes de información
•	Descripción de fuentes de datos
•	Preparación de datos
•	Construcción del set de datos
•	Diagnóstico inicial de la información
•	Calidad de datos
•	Análisis Descriptivo detallado y Resumen Ejecutivo
•	Modelación	
•	Validación
•	Despliegue de Resultados

2. Presentación Ejecutiva: Esta presentación debe construirla y presentarla, en esta debe mostrar los hallazgos relevantes de la información.

•	Planteamiento de necesidad del negocio
•	Fuentes de información
•	Descripción de fuentes de datos
•	Diagnóstico inicial de la información
•	Análisis Descriptivo detallado y Resumen Ejecutivo
•	Modelación
•	Validación
•	Despliegue de Resultados
