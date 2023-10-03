-- USAMOS LA BD 

USE DB_TIF_Grupo_14;

-- Carga 10 registros de ejemplo en la tabla "usuarios"
INSERT INTO usuarios (nombre_usuario, clave, email, nombre, apellido, imagen_perfil)
VALUES
  ('DptoProfesorados', 'clave1', 'usuario1@example.com', 'Encargado', 'Catedra: Matemática', 'imagen1.jpg'),
  ('DptoQuimica', 'clave2', 'usuario2@example.com', 'Nombre2', 'Apellido2', 'imagen2.jpg'),
  ('DptoInformatica', 'clave3', 'usuario3@example.com', 'Nombre3', 'Apellido3', 'imagen3.jpg'),
  ('DeptoFisica', 'clave4', 'usuario4@example.com', 'Nombre4', 'Apellido4', 'imagen4.jpg'),
  ('DeptoMatematica', 'clave5', 'usuario5@example.com', 'Nombre5', 'Apellido5', 'imagen5.jpg'),
  ('usuario6', 'clave6', 'usuario6@example.com', 'Nombre6', 'Apellido6', 'imagen6.jpg'),
  ('usuario7', 'clave7', 'usuario7@example.com', 'Nombre7', 'Apellido7', 'imagen7.jpg'),
  ('usuario8', 'clave8', 'usuario8@example.com', 'Nombre8', 'Apellido8', 'imagen8.jpg'),
  ('usuario9', 'clave9', 'usuario9@example.com', 'Nombre9', 'Apellido9', 'imagen9.jpg'),
  ('usuario10', 'clave10', 'usuario10@example.com', 'Nombre10', 'Apellido10', 'imagen10.jpg');

-- Carga 10 registros de ejemplo en la tabla "servidores"
INSERT INTO servidores (nombreServidor, descripcion)
VALUES
  ('Profesorado en Matematica', 'Tipo de Carrera: Grado
Modalidad: Presencial
Título que emitirá: Profesor en Matematica
Cantidad de Años: 4
Cantidad de Materias: 25
Resolución: Res. Ministerial N°89/00 - C.S N° 190/96 - RESCD-DEXA N°475/96'),
  ('Licenciatura en Matemáticas', 'Tipo de Carrera: Grado
Modalidad: Presencial
Título que emitirá: Licenciado en Matemáticas
Cantidad de Años: 4
Cantidad de Materias: 22
Resolución: Res. Ministerial N°265/ 04 - C.S Nº 020/2001, 132/03 - RESCD-DEXA N°353/00'),
  ('Licenciatura en Análisis de Sistemas', 'Tipo de Carrera: Grado
Modalidad: PRESENCIAL
Título que emitirá: Licenciado en Análisis de Sistemas
Cantidad de Años: 5
Cantidad de Materias: 29
Resolución: RES. MINISTERIAL N°1891/22 - C.S 135/10, 262/12, 042/14, 426/17 - RESCD-DEXA 403/12, 001/10, 440/17'),
  ('Tecnicatura Universitaria en Programación', 'Tipo de Carrera: Pre Grado
Modalidad: Presencial
Título que emitirá: Técnico Universitario en Programación
Cantidad de Años: 3
Cantidad de Materias: 17
Resolución: Res. Ministerial N° 2251/19 - C. S. Nº 596/2011, 391/17 - RESCD-DEXA N°889/11'),
  ('Profesorado en Química', 'Tipo de Carrera: Grado
Modalidad: presencial
Título que emitirá: Profesor en Química
Cantidad de Años: 4
Cantidad de Materias: 26
Resolución: RES MINIS N°1255/05 - CS N° 0190/02, 305/03 , 086/18- RESCD- EXA N°157/02, 180/97, 190/03, 629/17'),
  ('Licenciatura en Química', 'Tipo de Carrera: Grado
Modalidad: Presencial
Título que emitirá: Licenciado en Química
Cantidad de Años: 5
Cantidad de Materias: 32
Resolución: Res. Ministerial N° 1139/14 - C.S N° 584/17, 394/16, 579/16 - RESCD- EXA N°731/16, 430/16, 219/11'),
  ('Profesorado en Física', 'Tipo de Carrera: Pre Grado
Modalidad: Presencial
Título que emitirá: Profesor en Física
Cantidad de Años: 4
Cantidad de Materias: 27
Resolución: Res. Ministerial N° 334/99 - C.S. Nº 191/96 - RESCD-EXA N° 474/96'),
  ('Licenciatura en Física', 'Tipo de Carrera: Grado
Modalidad: Presencial
Título que emitirá: Licenciado en Física
Cantidad de Años: 5
Cantidad de Materias: 26
Resolución: Res. Ministerial N° 478/04 - C.S. Nº585/17, 661/04 - RESCD-EXA N°646/17, 328/04'),
  ('Tecnicatura Universitaria en Estadística', 'Tipo de Carrera: Pre Grado
Modalidad: Presencial
Título que emitirá: Tecnico Universitario en Estadística
Cantidad de Años: 3
Cantidad de Materias: 17
Resolución: Res. Ministerial N° 2033/13 - C.S N° 172/11, 356/15 - RESCD-EXA Nº 096/2011'),
  ('Tecnicatura Universitaria en Energía Solar', 'Tipo de Carrera: Grado
Modalidad: Presencial
Título que emitirá: Técnico Universitaria en Energía Solar
Cantidad de Años: 3
Cantidad de Materias: 14
Resolución: Res. Ministerial N°2585/13 - CS N°144/2012 - RESCD-EXA N°945/11 - RES CS 299/19'),
  ('Tecnicatura Electrónica Universitaria', 'Tipo de Carrera: Pre Grado
Modalidad: Presencial
Título que emitirá: Técnico Electrónico Universitario
Cantidad de Años: 3
Cantidad de Materias: 15
Resolución: Res. Ministerial N° 380/06 - C.S. Nº 589/17 , 356/05 - RESCD-EXA N°647/17, 537/07, 250/05'),
  ('Licenciatura en Energías Renovables', 'Tipo de Carrera: Grado
Modalidad: Presencial
Título que emitirá: Licenciado en Energías Renovables
Cantidad de Años: 4
Cantidad de Materias: 24
Resolución: Res. Min. N°332/07 - C.S. Nº379/18, 353/15, 28/05 - RESCD- EXA N° 187/18, 543/07, 542/07, 013/05'),
  ('Analista Químico', 'Tipo de Carrera: Pre Grado
Modalidad: Presencial
Título que emitirá: Analista Químico
Cantidad de Años: 3
Cantidad de Materias: 14
Resolución: Res. Ministerial N°595/20, CS N° 586/17, 204/17, 594/11 - CD N°091/17, 739/11'),
  ('Licenciatura en Bromatología', 'Tipo de Carrera: Grado
Modalidad: Presencial
Título que emitirá: Licenciado en Bromatología
Cantidad de Años: 5
Cantidad de Materias: 25
Resolución: Res Minis N° 2703/17 - C.S. N°395/16, 587/17, 444/08, 652/15 - RESCD-EXA N° 345/08, 631/17, 243/16');

-- Carga 10 registros de ejemplo en la tabla "canales"
INSERT INTO canales (nombreCanal, descripcion, id_user_creo_canal, id_server)
VALUES
  ('Introduccion a la Matemática - Año1', 'Objetivos generales:
  Al terminar el cursado de la asignatura se espera que el alumno: 
  • Utilice y aplique correctamente los símbolos y la terminología que brinda la asignatura en la interpretación y traducción de diferentes enunciados. 
  • Formule, interprete y resuelva problemas traduciéndolos en distintos lenguajes (verbal, simbólico y gráfico). 
  • Adquiera interés en obtener auto información a través de la consulta bibliográfica sugeriday empiece a estudiar con autonomía.', 
  1, 1),
  ('Geometría Plana y Espacial - Año1', 'DOBJETIVOS GENERALES 
  Que el alumno ejercite sus habilidades y/o adquiera nuevas habilidades en el manejo del pensamiento lógico­deductivo 
  como tambien en la exposición y/o defensa de sus propias ideas tanto en forma escrita como oral. 
  Aproveche la interacción con el docente y con sus propios compañeros para tomar conciencia de la 
  utilidad del trabajo grupal, pero con un fuerte compromiso y desempeño individual, independiente y
  crítico, respetando el disenso y potenciando el consenso. ', 1, 2),
  ('Elementos de Programacion - Año1', 'Objetivos de la asignatura: Que el alumno 
  resuelva problemas computacionales aplicando algoritmos fundamentales; 
  diseñe circuitos lógicos sencillos usando principios del Álgebra de Boole; 
  convierta números entre distintos sistemas de numeración e identifique 
  elementos básicos de alfabetización informática.', 3, 3),
  ('Algoritmos y Estructuras de Datos - Año2', 'Objetivos de la asignatura: 
  Consolidar el pensameinto logico para la resolucion de problemas computacionales.
  Fomentar la aplicación de técnicas de diseño para el desarrollo de programas/software.
  Promover una formacion solida en el manejo de diferentes estructuras de datos estaticas y dinamicas.
  Revisar conceptos de la matemática discreta.
  Promover el uso de nuevas herramientas tecnologicas.', 3, 3),
  ('Base de Datos I - Año3', 'Objetivos de la asignatura:
  Formar al alumno en todos los aspectos del Modelo Relacional: 
  modelado conceptual, modelado lógico, modelado fisico y gestión de datos.', 3, 3),
  ('Redes de Computadoras I - Año4', 'Objetivos de la asignatura: 
  Introducir al alumno en los conceptos de transmisión de datos, protocolos de comunicación y aplicaciones sobre redes de computadoras. 
  Adicionalmente, se introduce como funciona la Internet sobre la base de sus protocolos y aplicaciones. 
  Al finalizar el curso, el alumno será capaz de: 
  Comprender y manejar los conceptos fundamentales de las redes de datos.
  Fundamentar la necesidad del modelo de capas. 
  Definir para cada capa objetivos, funciones e interrelación entre capas. 
  Describir los principales protocolos de las capas de aplicación, capa de transporte y capa de red, sus características y ámbito de aplicación. 
  Describir y analizar ejemplos de redes usados en la realidad.', 3, 3),
  ('Derecho Informatico - Año5', 'OBJETIVOS DE LA MATERIA: 
  Impartir conocimientos básicos relativos al derecho. 
  Analizar el contexto de restricciones éticas y legales en el ejercicio de la profesión.
  Abordar problemáticas legales.
  Establecer formulaciones de solución en políticas y problemas legales.', 3, 3),
  ('Optativa: Ciberseguridad - Año5', 'Objetivos de la asignatura:
  -Efectuar una revisión de los aspectos fundamentales de la seguridad informática.
  -Presentar los conceptos básicos relacionados con ciberseguridad y uso seguro de las tecnologías de la información.
  -Explicar detalladamente las ciberamenazas existentes, evaluando los riesgos y consecuencias de un ciberataque, demanera que el estudiante comprenda la importancia de la ciberseguridad en una organización.
  -Estudiar normas, mecanismos y protocolos para proteger infraestructuras críticas que procesan, almacenan o transmiten la información digital de una organización.
  -Analizar herramientas y metodologías específicas para la prevención, detección, respuesta y recupero; ante ataques informáticos maliciosos en el mundo digital.', 
  3, 3),
  ('Introducción a los Circuitos Eléctricos - Año1', 'Objetivos de la asignatura: 
  Teniendo en cuenta que este curso está dirigido a futuros técnicos electrónicos y licenciados en física, 
  los objetivos específicos son que el estudiante: 
  • Distinga los componentes pasivos y activos estudiados. 
  • Maneje los conceptos de fuentes de tensión y corrientes reales e ideales, circuito abierto y cortocircuito. 
  • Seleccione el método de análisis que sea más conveniente para la resolución de un circuito. 
  • Aprenda métodos de simplificación de circuitos complicados. 
  • Conozca el comportamiento y propiedades de los circuitos de uso más frecuente en la práctica 
  • Maneje el concepto de amplificación del transistor. 
  • Identifique los amplificadores operacionales inversores y no inversores Calcule ganancia, voltajes y corrientes. ',
  4, 10),
  ('Fundamentos de Energía Solar - Año2', 'Objetivos de la asignatura: 
Capacitar al alumno sobre los fundamentos físicos asociados a las aplicaciones de la energía solar, 
especialmente las de baja temperatura y generación de electricidad. 
Contenidos Mínimos: Mecánica. Trabajo y energía. Hidrodinámica. Flujos activos y pasivos. 
Propiedades termodinámicas. Psicrometría del aire húmedo. Mecanismos de transferencia de energía y materia. 
Balances y rendimiento energético. Intercambiadores y acumulación de calor. La radiación solar. El recurso. 
Geometría solar. Orientación de planos. Conversión de la Energía Solar. ', 
4, 10);

-- Carga 10 registros de ejemplo en la tabla "chats"
INSERT INTO chats (contenido, fecha_creacion, id_user, id_canal)
VALUES
  ('Bienvenido a el canal de la materia Introducción a la Matemática - Año1: Este es un espacio para Consultar 
  e interactuar con tus compañeros de cursado. Disfrutenlo respetando las normas de uso.', NOW(), 1, 1),
  ('Bienvenido a el canal de la materia Geometría Plana y Espacial - Año1: Este es un espacio para Consultar 
  e interactuar con tus compañeros de cursado. Disfrutenlo respetando las normas de uso.', NOW(), 1, 2),
  ('Bienvenido a el canal de la materia Elementos de Programacion - Año1: Este es un espacio para Consultar 
  e interactuar con tus compañeros de cursado. Disfrutenlo respetando las normas de uso.', NOW(), 3, 3),
  ('Bienvenido a el canal de la materia Algoritmos y Estructuras de Datos - Año2: Este es un espacio para Consultar 
  e interactuar con tus compañeros de cursado. Disfrutenlo respetando las normas de uso.', NOW(), 3, 4),
  ('Bienvenido a el canal de la materia Base de Datos I - Año3: Este es un espacio para Consultar 
  e interactuar con tus compañeros de cursado. Disfrutenlo respetando las normas de uso.', NOW(), 3, 5),
  ('Bienvenido a el canal de la materia Redes de Computadoras I - Año4: Este es un espacio para Consultar 
  e interactuar con tus compañeros de cursado. Disfrutenlo respetando las normas de uso.', NOW(), 3, 6),
  ('Bienvenido a el canal de la materia Derecho Informatico - Año5: Este es un espacio para Consultar 
  e interactuar con tus compañeros de cursado. Disfrutenlo respetando las normas de uso.', NOW(), 3, 7),
  ('Bienvenido a el canal de la materia Optativa: Ciberseguridad - Año5: Este es un espacio para Consultar 
  e interactuar con tus compañeros de cursado. Disfrutenlo respetando las normas de uso.', NOW(), 3, 8),
  ('Bienvenido a el canal de la materia Introducción a los Circuitos Eléctricos - Año1: Este es un espacio para Consultar 
  e interactuar con tus compañeros de cursado. Disfrutenlo respetando las normas de uso.', NOW(), 4, 9),
  ('Bienvenido a el canal de la materia Geometría Fundamentos de Energía Solar - Año2: Este es un espacio para Consultar 
  e interactuar con tus compañeros de cursado. Disfrutenlo respetando las normas de uso.', NOW(), 4, 10);


-- Carga 17 registros de ejemplo en la tabla "usuario_Servidor"
  -- Relaciona usuario1 al Servidor 1
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (1, 1);

-- Relaciona usuario1 al Servidor 5
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (1, 5);

-- Relaciona usuario1 al Servidor 7
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (1, 7);

-- Relaciona usuario2 al Servidor 5
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (2, 5);


-- Relaciona usuario2 al Servidor 6
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (2, 6);

-- Relaciona usuario2 al Servidor 13
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (2, 13);

-- Relaciona usuario2 al Servidor 14
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (2, 14);

-- Relaciona usuario3 al Servidor 3
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (3, 3);

-- Relaciona usuario3 al Servidor 4
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (3, 4);

-- Relaciona usuario4 al Servidor 8
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (4, 8);

-- Relaciona usuario4 al Servidor 9
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (4, 9);

-- Relaciona usuario4 al Servidor 10
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (4, 10);

-- Relaciona usuario4 al Servidor 11
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (4, 11);


-- Relaciona usuario4 al Servidor 12
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (4, 12);

-- Relaciona usuario5 al Servidor 1
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (5, 1);

-- Relaciona usuario5 al Servidor 2
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (5, 2);

-- Relaciona usuario5 al Servidor 3
INSERT INTO DB_TIF_Grupo_14.usuario_Servidor (id_user, id_server)
VALUES (5, 3);


