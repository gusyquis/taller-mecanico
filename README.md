# Taller Mecánico - Base de Datos con SQLite

Aplicación en Python que modela la gestión de un taller mecánico usando `sqlite3`.

**Estudiante:** Gustavo Mamani Quisberth (GMQ) — Código: 11097581

## Tablas

- `clientes` — dueños de los vehículos.
- `vehiculos` — vehículos registrados, con `cliente_id` (FK a `clientes`).
- `servicios` — catálogo de servicios ofrecidos y su costo.
- `ordenes_trabajo` — relaciona un vehículo con un servicio realizado en una fecha (FK a `vehiculos` y `servicios`).

## Cómo ejecutar

```bash
python app.py
```

Esto crea `taller.db` (si no existe), inserta datos de ejemplo y muestra el contenido de cada tabla por consola.