USE tarea2;

INSERT INTO region (nombre) VALUES ('Metropolitana');

INSERT INTO comuna (nombre, region_id) VALUES ('Santiago', 1), ('Maipú', 1);

-- 2 avisos de ejemplo:
INSERT INTO aviso_adopcion (fecha_ingreso, comuna_id, sector, nombre, email, celular, tipo, cantidad, edad, unidad_medida, fecha_entrega, descripcion)
VALUES
  ('2025-06-02 10:00:00', 1, 'Beauchef 859, terraza', 'Aviso1', 'a@a.com', '912345678', 'gato', 1, 2, 'm', '2025-06-15 00:00:00', 'Gatito en adopción'),
  ('2025-05-28 09:30:00', 2, 'Plaza Maipú', 'Aviso2', 'b@b.com', '912345679', 'perro', 3, 2, 'm', '2025-06-10 00:00:00', 'Perros en adopción');

-- notas las mostramos como "-" cuando no hay
