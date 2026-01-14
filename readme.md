# 🛡️ PhishingPredictor

> **Tu guardespaldas digital contra el fraude.**
> Sistema de detección de phishing inteligente basado en **IA Híbrida** (LLM + Machine Learning) capaz de analizar URLs, textos (SMS/Emails) e imágenes.

![Estado](https://img.shields.io/badge/Estado-MVP%20Completado-success)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Stack](https://img.shields.io/badge/Flask-MongoDB-green)
![AI](https://img.shields.io/badge/AI-Cohere%20%2B%20ONNX-orange)

## 📖 Descripción

**PhishingPredictor** es una aplicación web diseñada para democratizar la ciberseguridad. A diferencia de los antivirus tradicionales que dependen de listas negras estáticas, este sistema utiliza Inteligencia Artificial para **entender el contexto** del fraude y detectar amenazas nuevas en tiempo real.

El núcleo del proyecto es su **Arquitectura Híbrida**: combinamos la capacidad de razonamiento y comprensión del lenguaje de los LLMs (**Cohere**) con la precisión matemática y velocidad de los modelos de Machine Learning clásico (**ONNX**).

## ✨ Características Principales

* **🌐 Análisis de URLs Híbrido (Robustez Total):**
    * Utiliza un LLM para extraer 30 características técnicas de la URL (SSL, longitud, redirecciones, ofuscación IP...).
    * Un modelo ONNX predice el riesgo matemático basándose en esos datos.
    * *Feature:* Incluye sistema "Plan B" a prueba de fallos para manejar URLs complejas sin romper la experiencia de usuario.
* **💬 Análisis de Texto (Smishing):**
    * Detecta intentos de ingeniería social en SMS, WhatsApps y correos electrónicos.
    * Explica en lenguaje natural *por qué* el mensaje es sospechoso (urgencia, miedo, autoridad).
* **📸 Análisis de Imágenes:**
    * Utiliza Visión Artificial para leer y analizar capturas de pantalla de mensajes fraudulentos.
* **📊 Dashboard Interactivo:** Interfaz limpia, moderna y fácil de usar para cualquier usuario.

## 🧠 ¿Cómo funciona la IA Híbrida?

Para el análisis técnico, utilizamos un enfoque de "Dos Cerebros":

1.  **🕵️ El Detective (Cohere / LLM):** Recibe la URL o texto crudo y actúa como un analista humano experto. Extrae un JSON estructurado con variables clave del dataset UCI Phishing.
2.  **📝 El Traductor (Python):** Limpia y procesa la respuesta de la IA (incluyendo manejo de errores de formato) y convierte los datos en vectores numéricos.
3.  **🧮 El Matemático (ONNX):** Recibe el vector y ejecuta un modelo de Machine Learning entrenado para devolver una probabilidad de riesgo precisa en milisegundos.

## 🛠️ Stack Tecnológico

* **Backend:** Python, Flask.
* **Base de Datos:** MongoDB Atlas (Nube).
* **IA Generativa:** Cohere API (Modelos `command-r` y `command-r-vision`).
* **Machine Learning:** ONNX Runtime & Scikit-learn.
* **Frontend:** HTML5, CSS3, JavaScript.
* **Presentación:** Reveal.js (integrado en el proyecto).

## 🚀 Instalación y Despliegue

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/TU_USUARIO/phishing-predictor.git](https://github.com/TU_USUARIO/phishing-predictor.git)
cd phishing-predictor
S
