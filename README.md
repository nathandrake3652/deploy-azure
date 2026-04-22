# Deploy API (Railway)

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
Ese archivo no se sube al repositorio; en Railway se configuran los valores desde Variables.

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

## Comando de inicio

Usa este comando de inicio en cualquier plataforma (Railway, Render, etc):

```bash
uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
```

Si quieres personalizar el `GET /`, define `FIRST_NAME` y `LAST_NAME` como variables de entorno.

## Despliegue en Railway (desde GitHub)

1. Entra a Railway y crea un proyecto nuevo.
2. Elige Deploy from GitHub repo y selecciona este repositorio.
3. Railway detecta Python por `requirements.txt` y hace el build automático.
4. En la sección Variables agrega, si quieres personalizar salida:
  - FIRST_NAME
  - LAST_NAME
5. En Settings > Start Command define:
  `uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}`
6. En Networking, genera dominio público (Generate Domain).
7. Prueba tu URL con:
  - `/`
  - `/{number}` por ejemplo `/7`
  - `POST /` con JSON

## Postman (rápido)

Body JSON para `POST /`:

```json
{
  "nombre": "Ana",
  "edad": 24,
  "numeroN": 3
}
```
