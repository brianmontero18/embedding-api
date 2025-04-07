# Embedding API

Servicio de embeddings gratuito usando GTE-Base y Flask, diseñado para desplegarse fácilmente en Render con plan gratuito.

### Endpoints

- `GET /` → Verifica que el servicio está corriendo
- `POST /embed` → Recibe `{ "text": "..." }` y devuelve `{ "embedding": [...] }`

### Despliegue

1. Crear un repo con estos archivos
2. Ir a [https://dashboard.render.com](https://dashboard.render.com)
3. Click en "New Web Service" > seleccionar repo
4. Plan: Free
5. Start command: `gunicorn app:app`
6. Listo 🚀
