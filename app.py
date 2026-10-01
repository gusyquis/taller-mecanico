import sqlite3

conn = sqlite3.connect("taller.db")

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        telefono TEXT NOT NULL
    )
    """
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS vehiculos(
        id INTEGER PRIMARY KEY,
        placa TEXT NOT NULL,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        cliente_id INTEGER NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
    """
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS servicios(
        id INTEGER PRIMARY KEY,
        descripcion TEXT NOT NULL,
        costo REAL NOT NULL
    )
    """
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS ordenes_trabajo(
        id INTEGER PRIMARY KEY,
        fecha TEXT NOT NULL,
        vehiculo_id INTEGER NOT NULL,
        servicio_id INTEGER NOT NULL,
        FOREIGN KEY (vehiculo_id) REFERENCES vehiculos(id),
        FOREIGN KEY (servicio_id) REFERENCES servicios(id)
    )
    """
)

# --- Datos base (clientes, vehículos, catálogo de servicios) ---
conn.execute(
    """
    INSERT INTO clientes (nombre, apellidos, telefono)
    VALUES ('Gustavo', 'Mamani Quisberth', '70000001')
    """
)

conn.execute(
    """
    INSERT INTO vehiculos (placa, marca, modelo, cliente_id)
    VALUES ('1234-ABC', 'Toyota', 'Hilux', 1)
    """
)

conn.execute(
    """
    INSERT INTO servicios (descripcion, costo)
    VALUES ('Cambio de aceite', 150.0)
    """
)

conn.execute(
    """
    INSERT INTO servicios (descripcion, costo)
    VALUES ('Alineado y balanceado', 200.0)
    """
)

conn.commit()

# --- Órdenes de trabajo (relación vehículo-servicio) ---
conn.execute(
    """
    INSERT INTO ordenes_trabajo (fecha, vehiculo_id, servicio_id)
    VALUES ('2026-09-23', '1', '1')
    """
)

conn.execute(
    """
    INSERT INTO ordenes_trabajo (fecha, vehiculo_id, servicio_id)
    VALUES ('2026-09-23', '1', '2')
    """
)

conn.commit()


print("\nORDENES DE TRABAJO")
cursor = conn.execute("SELECT * FROM ordenes_trabajo")
for row in cursor:
    print(row)

print("\nCLIENTES")
cursor = conn.execute("SELECT * FROM clientes")
for row in cursor:
    print(row)

print("\nVEHICULOS")
cursor = conn.execute("SELECT * FROM vehiculos")
for row in cursor:
    print(row)

print("\nSERVICIOS")
cursor = conn.execute("SELECT * FROM servicios")
for row in cursor:
    print(row)

conn.close()