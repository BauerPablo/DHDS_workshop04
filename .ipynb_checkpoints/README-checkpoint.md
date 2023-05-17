<div float: center>
    <img src="../common/../common/logo_DH.png" width="30%" height="30%" style="text-align: left;">
    <img src="../common/wipro_logo.png"  width="20%" height="20%" style="text-align: right; margin-left:400px;">
<div/>
    
---

# WORKSHOP 4 - Trabajo integrador de DataScience

## GRUPO 8

Integrantes:
- Agustín García 
- Florencia Mosconi
- Ezequiel López Mondo 
- Pablo Bauer 

<a id="tabla_contenidos"></a> 
## Tabla de Contenidos

### <a href='#section_repaso'>1. Introducción</a>
- #### <a href='#explicacion_dataset'>1.1 Presentación del caso</a>
- #### <a href='#metodologia'>1.2 La metodología de trabajo</a>
    
---
<a id="section_repaso"></a> 
## 1. Introducción
---
<a href='#tabla_contenidos'>Volver a la Tabla de Contenidos</a>

<a id="explicacion_dataset"></a> 
### 1.1 Presentación del caso

<img src="../common/solar_farms.png"  width="100%" height="100%">

:es:

**Objetivo del Poryecto**

El objetivo de este proyecto es optimizar la producción de energía solar de una empresa de líder en el campo. Para ello, se requiere desarrollar un modelo de predicción capaz de predecir los valores de 'Clearsky DHI', 'Clearsky DNI' y 'Clearsky GHI', que son índices de incidencia solar clave.

Utilizando un conjunto de datos recopilados durante 10 años con un intervalo de 30 minutos, se entrenará el modelo de predicción. Este modelo permitirá predecir la capacidad de producción de una granja solar en función de ciertos parámetros meteorológicos relevantes.

El objetivo final es proporcionar a la empresa de generación de energía solar una herramienta precisa y confiable para optimizar la producción. Esto permitirá una planificación más eficiente de las operaciones, una mejor gestión de los recursos disponibles y proporcionar valores de entrega de energía, basados en predicciones meteorológicas a través de los servicios de Meteorología Nacionales.

Con este proyecto, se busca aprovechar al máximo el potencial de la energía solar y contribuir a un enfoque más sostenible y respetuoso con el medio ambiente en la generación de energía.

---

:us:

**Goal of the Project**

*The objective of this project is to optimize the solar energy production of a leading company in the field. For this, it is necessary to develop a prediction model capable of predicting the values of 'Clearsky DHI', 'Clearsky DNI' and 'Clearsky GHI', which are key solar incidence indices.

*Using a data set collected over 10 years with an interval of 30 minutes, the prediction model will be trained. This model will make it possible to predict the production capacity of a solar farm based on certain relevant meteorological parameters.

*The ultimate goal is to provide the solar power generation company with an accurate and reliable tool to optimize production. This will allow for more efficient planning, better management of available resources and will provide energy delivery values, based on weather predictions through the National Meteorology services.

*This project seeks to make the most of the potential of solar energy and contribute to a more sustainable and environmentally friendly approach to power generation.


:es:

#### Contexto

Wipro Limited (NYSE: WIT, BSE: 507685, NSE: WIPRO) es una empresa líder mundial en servicios de tecnología de la información, consultoría y procesos comerciales. Aprovechamos el poder de la computación cognitiva, la hiperautomatización, la robótica, nubes, el análisis y las tecnologías emergentes para ayudar a nuestros clientes a adaptarse al mundo digital y hacerlos exitosos. Una empresa reconocida a nivel mundial por su cartera integral de servicios, fuerte compromiso con la sostenibilidad y capital humano comprometido, tenemos más de 220 000 empleados dedicados, que atienden a clientes en seis continentes. Juntos, descubrimos ideas y conectamos los puntos para construir un futuro mejor y más audaz.

Además de ser un líder mundial en servicios de inteligencia artificial según los últimos informes de analistas como Forrester, IDC y Everest Group, Wipro ha sido calificada como la segunda mejor organización para que los científicos de datos trabajen en India en 2021 por Analytics India Magazine. La compañía también se ha comprometido a alcanzar unas emisiones netas de gases de efecto invernadero cero para 2040.

Aunque un poco tarde, el mundo se está dando cuenta del efecto nocivo de los combustibles fósiles en nuestro medio ambiente. A medida que avanza el reloj del fin del mundo, los seres humanos recurren a las energías renovables para evitar un posible apocalipsis. Afortunadamente, el sol es un manantial de energía limpia. Siguiendo el ejemplo, Wipro, en asociación con MachineHack, ha diseñado un desafío de pronóstico para optimizar la generación de energía solar utilizando modelos ML.

---
:us:

#### Context

*Wipro Limited (NYSE: WIT, BSE: 507685, NSE: WIPRO) is a leading global information technology, consulting and business process services company. We harness the power of cognitive computing, hyper-automation, robotics, cloud, analytics and emerging technologies to help our clients adapt to the digital world and make them successful. A company recognized globally for its comprehensive portfolio of services, strong commitment to sustainability and good corporate citizenship, we have over 220,000 dedicated employees serving clients across six continents. Together, we discover ideas and connect the dots to build a better and a bold new future.*

*Along with being a global leader in artificial intelligence services from the latest reports of analysts like Forrester, IDC and Everest Group, Wipro has been rated as the second-best organization for data scientists to work in India in 2021 by Analytics India Magazine. The company has also been committed to reaching a Net-Zero Greenhouse Gas Emissions by 2040.*

*Though a little late in the day, the world is waking up to the deleterious effect of fossil fuels on our environment. As the doomsday clock ticks away, human beings are turning to renewable energy to avert a possible apocalypse. Fortunately, the sun is a well-spring of clean energy. Taking the cue, Wipro, in association with MachineHack, has designed a forecasting challenge to optimise solar power generation using ML models.*

---

['Year', 'Month', 'Day', 'Hour', 'Minute', 'Temperature', 'Clearsky DHI', 'Clearsky DNI', 'Clearsky GHI', 'Cloud Type', 'Dew Point', 'Fill Flag', 'Relative Humidity', 'Solar Zenith Angle', 'Pressure', 'Precipitable Water', 'Wind Direction', 'Wind Speed']

#### Columnas
- **Year** - Año de toma de datos
- **Month** - Mes de toma de datos
- **Day** - Día de toma de datos
- **Hour** - Hora de toma de datos
- **Minute** - Minuto de toma de datos
- **Temperature** - Temperatura local
- **Clearsky_DHI** - Diffuese Horizontal Irradiance
- **Clearsky_DNI** - Direct Normal Irradiance
- **Clearsky_GHI** - Global Horizontal Irradiance
- **Cloud_Type** - Tipo de Nubosidad en el ambiente
    - Cloud Type 0 Clear
    - Cloud Type 1 Probably Clear
    - Cloud Type 2 Fog
    - Cloud Type 3 Water
    - Cloud Type 4 Super-Cooled Water
    - Cloud Type 5 Mixed
    - Cloud Type 6 Opaque Ice
    - Cloud Type 7 Cirrus
    - Cloud Type 8 Overlapping
    - Cloud Type 9 Overshooting
    - Cloud Type 10 Unknown
    - Cloud Type 11 Dust
    - Cloud Type 12 Smoke
    - Cloud Type -15 N/A
- **Dew_Point** - Punto de rocío
- **Fill_Flag** - 
- **Relative_Humidity** - Humedad relativa
- **Solar_Zenith_Angle** - Ángulo de zenit solar
- **Pressure** - Presión atomsférica
- **Precipitable_Water** - Precipitación de lluvia en mm
- **Wind_Direction** - Dirección del viento
- **Wind_Speed** - Velocidad del viento

<a id="metodologia"></a> 
### 1.2 La metodología de trabajo

Hemos estructurado nuestra metodología de trabajo en varias tareas con el fin de cumplir con nuestros objetivos principales. El objetivo primario es desarrollar un sistema predictivo en la notebook y crear una presentación en PowerPoint, tal como se requiere en el curso.

Además de esto, hemos definido una serie de tareas complementarias para cumplir con nuestro objetivo secundario. Este objetivo implica poner en producción una pequeña página web en un servidor local, la cual contará con las funcionalidades mínimas necesarias para el funcionamiento del sistema y permitirá realizar consultas.

A través de esta metodología, aseguramos un enfoque ordenado y organizado para alcanzar tanto el objetivo primario como el secundario. Cada tarea predictiva se realizará de manera paralela, permitiendo una progresión lógica en el desarrollo del proyecto y permitiendo un proceso comparativo de distintos modelos de aprendizaje. De esta manera, podremos cumplir con los requisitos del curso y también lograr la puesta en funcionamiento del sistema en una página web, brindando una solución más completa y accesible para los usuarios.

Esta metodología nos permite maximizar la eficiencia y garantizar la entrega exitosa de los resultados esperados en los plazos establecidos.

---