# CropAdvisor

CropAdvisor es una API diseñada para proporcionar recomendaciones inteligentes para el seguimiento de cultivos. Se basa en un modelo de inteligencia artificial **Gemma:3** ejecutado localmente con **Ollama** y gestionado con **LangChain**. Se integra con el sistema Crops (Crop Resource Optimization Platform).

> [!IMPORTANT]
> Antes de ejecutar la API de CropAdvisor, asegúrate de tener instalados los siguientes componentes:
>
> 1. **Docker**: Para ejecutar Redis localmente.
> 2. **Python 3.10 o superior**: Para el backend de la API.
> 3. **Ollama**: Para ejecutar el modelo de inteligencia artificial localmente.

---

## Clona este repositorio

```bash
git clone https://github.com/jdtorrenegrap/cropadvisor.git
```

## Configuración de Redis con Docker

Redis es un servicio de base de datos en memoria que se utiliza para almacenar el historial de chat y otros datos temporales. Sigue estos pasos para configurarlo:

1. **Descargar la imagen oficial de Redis**:
   ```bash
   docker pull redis
   ```
2. **Crea y ejecuta un contenedor de Redis**:
   ```bash
   docker run -d --name redisCropAdvisor -p 6379:6379 redis
   ```
3. **Verifica que Redis esté en ejecución**:
   ```bash
   docker ps
   ```
   Deberías ver un contenedor llamado redisCropAdvisor en la lista de contenedores en ejecución.

## Intalación de Ollama

Ollama es necesario para ejecutar el modelo de inteligencia artificial localmente. Sigue las instrucciones según tu sistema operativo:

1. **Para Linux**:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```
2. **Para Windows:**
   Descarga e instala Ollama desde el sitio oficial.

3. **Ejecuta el modelo de IA:**
   Una vez instalado Ollama, descarga y ejecuta el modelo Gemma:3:
   ```bash
   ollama run gemma3:4b
   ```

## Configuración del entorno Python

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
```

```bash
 pip install -r requirements.txt
```

```bash
 uvicorn main:app --host 0.0.0.0 --port 8000
```
