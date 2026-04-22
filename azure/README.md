# Deploy con Azure

API simple para el taller con 2 endpoints GET y 1 POST.

## Endpoints

- `GET /` devuelve nombre y apellido.
- `GET /{number}` devuelve `(number + 5) * 2`.
- `POST /` recibe `nombre`, `edad` y `numeroN` y responde con `frase` y `calculo`.

## Desarrollo local

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Variables de entorno

Para desarrollo local puedes crear un archivo `.env` copiando `.env.example`.
Ese archivo no se sube al repositorio; en Azure se configuran los valores desde App Settings.

## Ejemplos

### GET /

```bash
curl http://127.0.0.1:8000/
```

### GET /7

```bash
curl http://127.0.0.1:8000/7
```

### POST /

```bash
curl -X POST http://127.0.0.1:8000/ \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Ana","edad":24,"numeroN":3}'
```

## Azure

En Azure App Service usa este comando de inicio:

```bash
uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
```

Si quieres personalizar el `GET /`, define `FIRST_NAME` y `LAST_NAME` como variables de entorno.

## Despliegue en Azure App Service

1. Crea una App Service para Python.
2. Sube el código con Git, GitHub Actions o Zip Deploy.
3. En Configuration > Application settings agrega `FIRST_NAME` y `LAST_NAME` si quieres cambiar el nombre devuelto por `GET /`.
4. En General settings o Startup Command usa:

```bash
uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
```

5. Reinicia la app y prueba la URL pública.
