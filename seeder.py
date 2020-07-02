family_background_seeder = '''INSERT INTO 'family_background_types' VALUES
(1,'Ant. Familiar 1 (Paterno)', 'Ant'),
(2,'Ant. Familiar 2 (Paterno)', 'Ant'),
(3,'Ant. Familiar 1 (Materno)', 'Ant'),
(4,'Ant. Familiar 2 (Materno)', 'Ant')'''

personal_background_seeder = '''INSERT INTO 'personal_background_types' VALUES
(1,'Ant. Personal 1', 'Ant'),
(2,'Ant. Personal 2', 'Ant')'''

vaccine_seeder = '''INSERT INTO 'vaccine_types' VALUES
(1,'Vacuna 1', 'Ant'),
(2,'Vacuna 2', 'Ant'),
(3,'Vacuna 3', 'Ant'),
(4,'Vacuna 4', 'Ant'),
(5,'Vacuna 5', 'Ant'),
(6,'Vacuna 6', 'Ant')'''

allergy_seeder = '''INSERT INTO 'allergy_types' VALUES
(1,'Alergia 1', 'Ant'),
(2,'Alergia 2', 'Ant'),
(3,'Alergia 3', 'Ant'),
(4,'Alergia 4', 'Ant'),
(5,'Alergia 5', 'Ant'),
(6,'Alergia 6', 'Ant')'''

medicine_seeder = '''INSERT INTO 'medicine_types' VALUES
(1,'Medicamento 1', 'Ant'),
(2,'Medicamento 2', 'Ant'),
(3,'Medicamento 3', 'Ant'),
(4,'Medicamento 4', 'Ant'),
(5,'Medicamento 5', 'Ant'),
(6,'Medicamento 6', 'Ant')'''

country_seeder = "INSERT INTO `countries` VALUES (1, 'VE', 'Venezuela')"

state_seeder = '''INSERT INTO 'states' ('id', 'name', 'country_id') VALUES
(1, 'Amazonas', 1),
(2, 'Anzoátegui', 1),
(3, 'Apure', 1),
(4, 'Aragua', 1),
(5, 'Barinas', 1),
(6, 'Bolívar', 1),
(7, 'Carabobo', 1),
(8, 'Cojedes', 1),
(9, 'Delta Amacuro', 1),
(10, 'Falcón', 1),
(11, 'Guárico', 1),
(12, 'Lara', 1),
(13, 'Mérida', 1),
(14, 'Miranda', 1),
(15, 'Monagas', 1),
(16, 'Nueva Esparta', 1),
(17, 'Portuguesa', 1),
(18, 'Sucre', 1),
(19, 'Táchira', 1),
(20, 'Trujillo', 1),
(21, 'Vargas', 1),
(22, 'Yaracuy', 1),
(23, 'Zulia', 1),
(24, 'Distrito Capital', 1);'''

municipality_seeder = '''INSERT INTO 'municipalities' ('id', 'state_id', 'name') VALUES
(1, 1, 'Alto Orinoco'),
(2, 1, 'Atabapo'),
(3, 1, 'Atures'),
(4, 1, 'Autana'),
(5, 1, 'Manapiare'),
(6, 1, 'Maroa'),
(7, 1, 'Río Negro'),
(8, 2, 'Anaco'),
(9, 2, 'Aragua'),
(10, 2, 'Manuel Ezequiel Bruzual'),
(11, 2, 'Diego Bautista Urbaneja'),
(12, 2, 'Fernando Peñalver'),
(13, 2, 'Francisco Del Carmen Carvajal'),
(14, 2, 'General Sir Arthur McGregor'),
(15, 2, 'Guanta'),
(16, 2, 'Independencia'),
(17, 2, 'José Gregorio Monagas'),
(18, 2, 'Juan Antonio Sotillo'),
(19, 2, 'Juan Manuel Cajigal'),
(20, 2, 'Libertad'),
(21, 2, 'Francisco de Miranda'),
(22, 2, 'Pedro María Freites'),
(23, 2, 'Píritu'),
(24, 2, 'San José de Guanipa'),
(25, 2, 'San Juan de Capistrano'),
(26, 2, 'Santa Ana'),
(27, 2, 'Simón Bolívar'),
(28, 2, 'Simón Rodríguez'),
(29, 3, 'Achaguas'),
(30, 3, 'Biruaca'),
(31, 3, 'Muñóz'),
(32, 3, 'Páez'),
(33, 3, 'Pedro Camejo'),
(34, 3, 'Rómulo Gallegos'),
(35, 3, 'San Fernando'),
(36, 4, 'Atanasio Girardot'),
(37, 4, 'Bolívar'),
(38, 4, 'Camatagua'),
(39, 4, 'Francisco Linares Alcántara'),
(40, 4, 'José Ángel Lamas'),
(41, 4, 'José Félix Ribas'),
(42, 4, 'José Rafael Revenga'),
(43, 4, 'Libertador'),
(44, 4, 'Mario Briceño Iragorry'),
(45, 4, 'Ocumare de la Costa de Oro'),
(46, 4, 'San Casimiro'),
(47, 4, 'San Sebastián'),
(48, 4, 'Santiago Mariño'),
(49, 4, 'Santos Michelena'),
(50, 4, 'Sucre'),
(51, 4, 'Tovar'),
(52, 4, 'Urdaneta'),
(53, 4, 'Zamora'),
(54, 5, 'Alberto Arvelo Torrealba'),
(55, 5, 'Andrés Eloy Blanco'),
(56, 5, 'Antonio José de Sucre'),
(57, 5, 'Arismendi'),
(58, 5, 'Barinas'),
(59, 5, 'Bolívar'),
(60, 5, 'Cruz Paredes'),
(61, 5, 'Ezequiel Zamora'),
(62, 5, 'Obispos'),
(63, 5, 'Pedraza'),
(64, 5, 'Rojas'),
(65, 5, 'Sosa'),
(66, 6, 'Caroní'),
(67, 6, 'Cedeño'),
(68, 6, 'El Callao'),
(69, 6, 'Gran Sabana'),
(70, 6, 'Heres'),
(71, 6, 'Piar'),
(72, 6, 'Angostura (Raúl Leoni)'),
(73, 6, 'Roscio'),
(74, 6, 'Sifontes'),
(75, 6, 'Sucre'),
(76, 6, 'Padre Pedro Chien'),
(77, 7, 'Bejuma'),
(78, 7, 'Carlos Arvelo'),
(79, 7, 'Diego Ibarra'),
(80, 7, 'Guacara'),
(81, 7, 'Juan José Mora'),
(82, 7, 'Libertador'),
(83, 7, 'Los Guayos'),
(84, 7, 'Miranda'),
(85, 7, 'Montalbán'),
(86, 7, 'Naguanagua'),
(87, 7, 'Puerto Cabello'),
(88, 7, 'San Diego'),
(89, 7, 'San Joaquín'),
(90, 7, 'Valencia'),
(91, 8, 'Anzoátegui'),
(92, 8, 'Tinaquillo'),
(93, 8, 'Girardot'),
(94, 8, 'Lima Blanco'),
(95, 8, 'Pao de San Juan Bautista'),
(96, 8, 'Ricaurte'),
(97, 8, 'Rómulo Gallegos'),
(98, 8, 'San Carlos'),
(99, 8, 'Tinaco'),
(100, 9, 'Antonio Díaz'),
(101, 9, 'Casacoima'),
(102, 9, 'Pedernales'),
(103, 9, 'Tucupita'),
(104, 10, 'Acosta'),
(105, 10, 'Bolívar'),
(106, 10, 'Buchivacoa'),
(107, 10, 'Cacique Manaure'),
(108, 10, 'Carirubana'),
(109, 10, 'Colina'),
(110, 10, 'Dabajuro'),
(111, 10, 'Democracia'),
(112, 10, 'Falcón'),
(113, 10, 'Federación'),
(114, 10, 'Jacura'),
(115, 10, 'José Laurencio Silva'),
(116, 10, 'Los Taques'),
(117, 10, 'Mauroa'),
(118, 10, 'Miranda'),
(119, 10, 'Monseñor Iturriza'),
(120, 10, 'Palmasola'),
(121, 10, 'Petit'),
(122, 10, 'Píritu'),
(123, 10, 'San Francisco'),
(124, 10, 'Sucre'),
(125, 10, 'Tocópero'),
(126, 10, 'Unión'),
(127, 10, 'Urumaco'),
(128, 10, 'Zamora'),
(129, 11, 'Camaguán'),
(130, 11, 'Chaguaramas'),
(131, 11, 'El Socorro'),
(132, 11, 'José Félix Ribas'),
(133, 11, 'José Tadeo Monagas'),
(134, 11, 'Juan Germán Roscio'),
(135, 11, 'Julián Mellado'),
(136, 11, 'Las Mercedes'),
(137, 11, 'Leonardo Infante'),
(138, 11, 'Pedro Zaraza'),
(139, 11, 'Ortíz'),
(140, 11, 'San Gerónimo de Guayabal'),
(141, 11, 'San José de Guaribe'),
(142, 11, 'Santa María de Ipire'),
(143, 11, 'Sebastián Francisco de Miranda'),
(144, 12, 'Andrés Eloy Blanco'),
(145, 12, 'Crespo'),
(146, 12, 'Iribarren'),
(147, 12, 'Jiménez'),
(148, 12, 'Morán'),
(149, 12, 'Palavecino'),
(150, 12, 'Simón Planas'),
(151, 12, 'Torres'),
(152, 12, 'Urdaneta'),
(179, 13, 'Alberto Adriani'),
(180, 13, 'Andrés Bello'),
(181, 13, 'Antonio Pinto Salinas'),
(182, 13, 'Aricagua'),
(183, 13, 'Arzobispo Chacón'),
(184, 13, 'Campo Elías'),
(185, 13, 'Caracciolo Parra Olmedo'),
(186, 13, 'Cardenal Quintero'),
(187, 13, 'Guaraque'),
(188, 13, 'Julio César Salas'),
(189, 13, 'Justo Briceño'),
(190, 13, 'Libertador'),
(191, 13, 'Miranda'),
(192, 13, 'Obispo Ramos de Lora'),
(193, 13, 'Padre Noguera'),
(194, 13, 'Pueblo Llano'),
(195, 13, 'Rangel'),
(196, 13, 'Rivas Dávila'),
(197, 13, 'Santos Marquina'),
(198, 13, 'Sucre'),
(199, 13, 'Tovar'),
(200, 13, 'Tulio Febres Cordero'),
(201, 13, 'Zea'),
(223, 14, 'Acevedo'),
(224, 14, 'Andrés Bello'),
(225, 14, 'Baruta'),
(226, 14, 'Brión'),
(227, 14, 'Buroz'),
(228, 14, 'Carrizal'),
(229, 14, 'Chacao'),
(230, 14, 'Cristóbal Rojas'),
(231, 14, 'El Hatillo'),
(232, 14, 'Guaicaipuro'),
(233, 14, 'Independencia'),
(234, 14, 'Lander'),
(235, 14, 'Los Salias'),
(236, 14, 'Páez'),
(237, 14, 'Paz Castillo'),
(238, 14, 'Pedro Gual'),
(239, 14, 'Plaza'),
(240, 14, 'Simón Bolívar'),
(241, 14, 'Sucre'),
(242, 14, 'Urdaneta'),
(243, 14, 'Zamora'),
(258, 15, 'Acosta'),
(259, 15, 'Aguasay'),
(260, 15, 'Bolívar'),
(261, 15, 'Caripe'),
(262, 15, 'Cedeño'),
(263, 15, 'Ezequiel Zamora'),
(264, 15, 'Libertador'),
(265, 15, 'Maturín'),
(266, 15, 'Piar'),
(267, 15, 'Punceres'),
(268, 15, 'Santa Bárbara'),
(269, 15, 'Sotillo'),
(270, 15, 'Uracoa'),
(271, 16, 'Antolín del Campo'),
(272, 16, 'Arismendi'),
(273, 16, 'García'),
(274, 16, 'Gómez'),
(275, 16, 'Maneiro'),
(276, 16, 'Marcano'),
(277, 16, 'Mariño'),
(278, 16, 'Península de Macanao'),
(279, 16, 'Tubores'),
(280, 16, 'Villalba'),
(281, 16, 'Díaz'),
(282, 17, 'Agua Blanca'),
(283, 17, 'Araure'),
(284, 17, 'Esteller'),
(285, 17, 'Guanare'),
(286, 17, 'Guanarito'),
(287, 17, 'Monseñor José Vicente de Unda'),
(288, 17, 'Ospino'),
(289, 17, 'Páez'),
(290, 17, 'Papelón'),
(291, 17, 'San Genaro de Boconoíto'),
(292, 17, 'San Rafael de Onoto'),
(293, 17, 'Santa Rosalía'),
(294, 17, 'Sucre'),
(295, 17, 'Turén'),
(296, 18, 'Andrés Eloy Blanco'),
(297, 18, 'Andrés Mata'),
(298, 18, 'Arismendi'),
(299, 18, 'Benítez'),
(300, 18, 'Bermúdez'),
(301, 18, 'Bolívar'),
(302, 18, 'Cajigal'),
(303, 18, 'Cruz Salmerón Acosta'),
(304, 18, 'Libertador'),
(305, 18, 'Mariño'),
(306, 18, 'Mejía'),
(307, 18, 'Montes'),
(308, 18, 'Ribero'),
(309, 18, 'Sucre'),
(310, 18, 'Valdéz'),
(341, 19, 'Andrés Bello'),
(342, 19, 'Antonio Rómulo Costa'),
(343, 19, 'Ayacucho'),
(344, 19, 'Bolívar'),
(345, 19, 'Cárdenas'),
(346, 19, 'Córdoba'),
(347, 19, 'Fernández Feo'),
(348, 19, 'Francisco de Miranda'),
(349, 19, 'García de Hevia'),
(350, 19, 'Guásimos'),
(351, 19, 'Independencia'),
(352, 19, 'Jáuregui'),
(353, 19, 'José María Vargas'),
(354, 19, 'Junín'),
(355, 19, 'Libertad'),
(356, 19, 'Libertador'),
(357, 19, 'Lobatera'),
(358, 19, 'Michelena'),
(359, 19, 'Panamericano'),
(360, 19, 'Pedro María Ureña'),
(361, 19, 'Rafael Urdaneta'),
(362, 19, 'Samuel Darío Maldonado'),
(363, 19, 'San Cristóbal'),
(364, 19, 'Seboruco'),
(365, 19, 'Simón Rodríguez'),
(366, 19, 'Sucre'),
(367, 19, 'Torbes'),
(368, 19, 'Uribante'),
(369, 19, 'San Judas Tadeo'),
(370, 20, 'Andrés Bello'),
(371, 20, 'Boconó'),
(372, 20, 'Bolívar'),
(373, 20, 'Candelaria'),
(374, 20, 'Carache'),
(375, 20, 'Escuque'),
(376, 20, 'José Felipe Márquez Cañizalez'),
(377, 20, 'Juan Vicente Campos Elías'),
(378, 20, 'La Ceiba'),
(379, 20, 'Miranda'),
(380, 20, 'Monte Carmelo'),
(381, 20, 'Motatán'),
(382, 20, 'Pampán'),
(383, 20, 'Pampanito'),
(384, 20, 'Rafael Rangel'),
(385, 20, 'San Rafael de Carvajal'),
(386, 20, 'Sucre'),
(387, 20, 'Trujillo'),
(388, 20, 'Urdaneta'),
(389, 20, 'Valera'),
(390, 21, 'Vargas'),
(391, 22, 'Arístides Bastidas'),
(392, 22, 'Bolívar'),
(407, 22, 'Bruzual'),
(408, 22, 'Cocorote'),
(409, 22, 'Independencia'),
(410, 22, 'José Antonio Páez'),
(411, 22, 'La Trinidad'),
(412, 22, 'Manuel Monge'),
(413, 22, 'Nirgua'),
(414, 22, 'Peña'),
(415, 22, 'San Felipe'),
(416, 22, 'Sucre'),
(417, 22, 'Urachiche'),
(418, 22, 'José Joaquín Veroes'),
(441, 23, 'Almirante Padilla'),
(442, 23, 'Baralt'),
(443, 23, 'Cabimas'),
(444, 23, 'Catatumbo'),
(445, 23, 'Colón'),
(446, 23, 'Francisco Javier Pulgar'),
(447, 23, 'Páez'),
(448, 23, 'Jesús Enrique Losada'),
(449, 23, 'Jesús María Semprún'),
(450, 23, 'La Cañada de Urdaneta'),
(451, 23, 'Lagunillas'),
(452, 23, 'Machiques de Perijá'),
(453, 23, 'Mara'),
(454, 23, 'Maracaibo'),
(455, 23, 'Miranda'),
(456, 23, 'Rosario de Perijá'),
(457, 23, 'San Francisco'),
(458, 23, 'Santa Rita'),
(459, 23, 'Simón Bolívar'),
(460, 23, 'Sucre'),
(461, 23, 'Valmore Rodríguez'),
(462, 24, 'Libertador');'''

# INSERT INTO `mydb`.`usuarios` (`username`, `nombre`, `apellido`, `email`, `contrasena`, `rol`, `titulo`, `documento`, `telefono`, `numero_colegio`, `numero_medico`, `sexo`) VALUES ('pattihrr', 'Patricia', 'Herrera', 'pat@herrera.com', 'sha256$N1kioOcL$8946c6730f0409ec5935ba45a599c52a7dc75988f8bcfb2659787989cbf9b978', 'doctor', 'Neurocirujano', '9790110', '584129344128', '8564', '1871', 'f');
# INSERT INTO `mydb`.`usuarios` (`username`, `nombre`, `apellido`, `email`, `contrasena`, `rol`, `titulo`, `documento`, `telefono`, `numero_colegio`, `numero_medico`, `sexo`) VALUES ('cali5050', 'Tomas', 'Valenzuela', 'tomas@valen.com', 'sha256$N1kioOcL$8946c6730f0409ec5935ba45a599c52a7dc75988f8bcfb2659787989cbf9b978', 'doctor', 'Neurologo', '17665414', '584248754255', '1900', '2004', 'm');
# INSERT INTO `mydb`.`usuarios` (`username`, `nombre`, `apellido`, `email`, `contrasena`, `rol`, `titulo`, `documento`, `telefono`, `numero_colegio`, `numero_medico`, `sexo`) VALUES ('findemundo', 'Juan', 'Davila', 'juan@davila.com', 'sha256$N1kioOcL$8946c6730f0409ec5935ba45a599c52a7dc75988f8bcfb2659787989cbf9b978', 'researcher', 'Neurologo', '12990021', '584261109932', '2230', '1984', 'm');
# INSERT INTO `mydb`.`usuarios` (`username`, `nombre`, `apellido`, `email`, `contrasena`, `rol`, `titulo`, `documento`, `telefono`, `numero_colegio`, `numero_medico`, `sexo`) VALUES ('magm', 'Maria', 'Garcia', 'maria@garcia.com', 'sha256$N1kioOcL$8946c6730f0409ec5935ba45a599c52a7dc75988f8bcfb2659787989cbf9b978', 'doctor', 'Neurologo', '16777102', '584142441591', '1987', '2101', 'f');
# INSERT INTO `mydb`.`usuarios` (`username`, `nombre`, `apellido`, `email`, `contrasena`, `rol`, `titulo`, `documento`, `telefono`, `numero_colegio`, `numero_medico`, `sexo`) VALUES ('pedro.rivas', 'Pedro', 'Rivas', 'pedro@rivas.com', 'sha256$N1kioOcL$8946c6730f0409ec5935ba45a599c52a7dc75988f8bcfb2659787989cbf9b978', 'researcher', 'Neurologo', '9911202', '584240901122', '765', '1776', 'm');
# INSERT INTO `mydb`.`usuarios` (`username`, `nombre`, `apellido`, `email`, `contrasena`, `rol`, `titulo`, `documento`, `telefono`, `numero_colegio`, `numero_medico`, `sexo`) VALUES ('gonpezzi', 'Gonzalo', 'Pezzi', 'gonzalo@pezzi.com', 'sha256$N1kioOcL$8946c6730f0409ec5935ba45a599c52a7dc75988f8bcfb2659787989cbf9b978', 'doctor', 'Neurocirujano', '6456733', '584129025551', '4991', '1965', 'm');

# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Dolor de cabeza', 'Sensación dolorosa en cualquier parte de la cabeza, que va desde un dolor agudo a un dolor leve');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Encefalopatía', 'cualquier enfermedad cerebral que altera la función o la estructura del cerebro.');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Ataque cerebrovascular', 'Lesión en el cerebro ocasionada por la interrupción de la irrigación sanguínea.');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Convulsión', 'Un síntoma transitorio caracterizado por actividad neuronal en el cerebro que conlleva a hallazgos físicos peculiares como la contracción y distensión repetida y temblorosa de uno o varios músculos de forma brusca y generalmente violenta');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Debilidad general', 'Debilidad generalizada');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Neuropatía Craneal', 'ocurre cuando uno o más de los doce nervios que salen del cerebro o del tronco cerebral están dañados.');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Neuropatía Periférica', 'Debilidad, entumecimiento y dolor, generalmente en las manos y los pies, ocasionado por un daño neurológico.');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Miopatía', 'Deficiencia o anomalía en los grupos musculares');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Trastornos del movimiento', 'grupo de afecciones del sistema nervioso (afecciones neurológicas) que provocan un aumento de movimientos anormales, que pueden ser voluntarios o involuntarios');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Cambios en la personalidad o comportamiento', 'comportamiento');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Depresión', 'Grupo de afecciones asociadas a los cambios de humor de una persona, como la depresión o el trastorno bipolar');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Embarazo', 'Etapa de gestación');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Nausea/Vomito/Mareo', 'Nausea/Vomito/Mareo');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Vejez', 'Paciento con edad mayor a 65 años');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Medicación', 'Paciente consumiendo recientemente algún medicamento');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Pasado medico', 'Paciente con historial relevante de patologias');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Perdida de memoria', 'Incapacidad para recordar eventos durante un período de tiempo');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Cirugia', 'Paciente con historial quirurgico relevante');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Diarrea', 'Heces blandas y líquidas con mayor frecuencia de lo habitual');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Problema Visual', 'Cualquier impedimento a la correcta función de los ojos');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Abuso de sustancias', 'Cigarrillo, alcohol, entre otras drogas');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Paralisis de nervio', 'Paralisis de cualquier nervio');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Disfagia', 'Dificultad para tragar alimentos');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Peso', 'Perdida o aumento súbito de peso');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Fatiga', 'Sensación de mucho cansancio, con poca energía y un fuerte deseo de dormir');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Capacidad de respuesta', 'Deterioro de la capacidad de respuesta');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Herida', 'Herida relevante a la historica clínica');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Declive cognitivo', 'Declive de las funciones cognitivas');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Fiebre', 'Aumento temporal de la temperatura corporal promedio');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Antecedente familiar', 'Familiar con cualquier patología relevante');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Anomalia de signos vitales', 'Pulso, presión sanguinea, etc');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Linfadenopatía', 'agrandamiento de los ganglios');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Candidiasis', 'Infección Vaginal');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Rigidez de nuca', 'Sensación de dolor o molestia en el cuello al intentar mover o girar la cabeza de lado a lado');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Examen de sangre', 'Anomalia en los parametros de un examen de sangre');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Anomalia LCR', 'Anomalia en los parametros de un examen del liquido cefalorraquídeo');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Alucinaciones', 'Percepción de haber visto, escuchado, tocado, probado u olido algo que no estaba allí');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Dolor General', 'Dolor general');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Apetito', 'Perdida o aumento del apetito');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Piel', 'Anomalia en la piel');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Problemas urinarios', 'Problema en la funcion urinaria');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Hipoestesia', 'Disminución en el sentido del tacto o las sensaciones');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Coma', 'Período prolongado de inconsciencia provocada por enfermedad o lesión');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Problemas respiratorios', 'Problemas de los pulmones como asma, enfisema o neumonía');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Edema Cerebral', ' acumulación de líquido en los espacios intra o extracelulares del cerebro');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Historial Profesional', 'Profesión relevante a la historia clínica');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Debilidad en piernas', 'Debilidad EXCLUSIVA en las piernas');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Cardiopatía', 'padecimiento del corazón o del resto del sistema cardiovascular');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Estreñimiento', 'Dificultad para defecar');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Disfunción eréctil', 'Incapacidad de un hombre de conseguir o mantener una erección firme para la relación sexual');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Disminucion sentidos', 'Disminución en el olfato, gusto y audición');
# INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Examen Orina', 'Anomalia en los parametros de un examen de orina');


# INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Angiografía cerebral', 'procedimiento para localizar posibles singularidades vasculares en el cerebro');
# INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Electroencefalograma', 'Pequeños electrodos transporta la actividad eléctrica del cerebro hasta un aparato que lee dicha actividad y la convierte en un trazado del registro eléctrico');
# INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Punción lumbar', 'se realizan con el objetivo de obtener muestras de líquido cefalorraquídeo.');
# INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Tomografía computerizada', 'La TC neurológica puede ayudar a realizar diagnósticos diferenciales en trastornos neurológicos con varias propiedades parecidas');
# INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Resonancia magnética', 'se utilizan las radioondas que se generan en un aparato y un gran campo magnético que revelan los detalles de órganos, tejidos, nervios y huesos');
# INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Tomografía por emisión de positrones ', 'Esta imagen se logra a través de la medición de isótopos radioactivos inyectados en el torrente sanguíneo del paciente');
# INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Potenciales evocados', 'En la prueba de potenciales evocados se pueden evaluar posibles problemas nerviosos sensoriales');
# INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Hemograma', 'consiste en un conteo de los elementos celulares de la sangre como son las células rojas, blancas y plaquetas.');
# INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Urinálisis', 'clave para detectar un problema de salud relacionado con el sistema urinario');
# INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Heces por Parásito', 'Este sencillo examen puede determinar si la causa de la diarrea se debe a parásitos, amebas o entero patógenos');
# INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Perfil Renal', 'Urea es el producto final del metabolismo de la proteína. La cantidad de urea excretada varia directamente con la ingesta de proteínas');


# INSERT INTO `mydb`.`tipo_vacunas` (`nombre`, `descripcion`) VALUES ('DTaP', 'Difteria, Tetanos y Tos Ferina');
# INSERT INTO `mydb`.`tipo_vacunas` (`nombre`, `descripcion`) VALUES ('Hepatitis B', 'se aplica en 3 o 4 inyecciones durante un período de 6 meses.');
# INSERT INTO `mydb`.`tipo_vacunas` (`nombre`, `descripcion`) VALUES ('Poliomielitis', 'Vacuna contra la poliomielitis');
# INSERT INTO `mydb`.`tipo_vacunas` (`nombre`, `descripcion`) VALUES ('Haemophilus influenzae tipo b', 'Vacuna contra la influenza tipo b');


# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Agente de viaje', 'Persona que vende y organiza viajes, vacaciones y vuelos');
# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Barrendero/a', ' Persona que limpia los lugares públicos (calles, plazas, etc.)');
# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Bibliotecario/a', 'Persona que trabaja en una biblioteca manteniendo el orden de los libros, videos, discos, etc.');
# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Bombero/a', 'Persona que apaga el fuego en un incendio. (2) Persona que carga combustible en una estación de servicios');
# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Carnicero/a', 'Persona que trabaja con carne. Ellos cortan la carne y la venden');
# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Cientifico/a', 'Persona que trabaja en investigaciones científicas haciendo muchos experimentos');
# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Chef', 'Persona que prepara comida para otros, comúnmente en un restaurante');
# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Doctor', 'Persona a la que vas cuando tienes problemas de salud.');


# INSERT INTO `mydb`.`antecedentes` (`nombre`, `descripcion`) VALUES ('Cancer', 'Enfermedad en la que células anómalas se dividen sin control y destruyen los tejidos corporales');
# INSERT INTO `mydb`.`antecedentes` (`nombre`, `descripcion`) VALUES ('Absceso hepático', 'causado por la Entamoeba histolytica');
# INSERT INTO `mydb`.`antecedentes` (`nombre`, `descripcion`) VALUES ('Trombosis', 'formación de un coágulo en el interior de un vaso sanguíneo y uno de los causantes de un infarto agudo de miocardio');
# INSERT INTO `mydb`.`antecedentes` (`nombre`, `descripcion`) VALUES ('Mielitis', 'Inflamación de la médula espinal');
# INSERT INTO `mydb`.`antecedentes` (`nombre`, `descripcion`) VALUES ('Hipertensión', 'Afección en la que la presión de la sangre hacia las paredes de la arteria es demasiado alta');
# INSERT INTO `mydb`.`antecedentes` (`nombre`, `descripcion`) VALUES ('Derrame cerebral', 'Lesión en el cerebro ocasionada por la interrupción de la irrigación sanguínea');
# INSERT INTO `mydb`.`antecedentes` (`nombre`, `descripcion`) VALUES ('Otro', 'No registrado en el sistema');

# INSERT INTO `mydb`.`pacientes` (`nombre`, `apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`) VALUES ('Gilberto', 'Armada', '3200980', 'm', '1946-04-13', 'casado', 'A+');
# INSERT INTO `mydb`.`pacientes` (`nombre`, `segundo_nombre`, `apellido`, `segundo_apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`, `telefono`, `telefono2`) VALUES ('Juan', 'Alberto', 'Carrasco', 'Medina', '6126909', 'm', '1953-03-05', 'casado', 'A-', '584144740153', '584169477348');
# INSERT INTO `mydb`.`pacientes` (`nombre`, `segundo_nombre`, `apellido`, `segundo_apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`, `telefono`, `telefono2`) VALUES ('Ivan', 'Jesus', 'Rojas', 'Perez', '9644169', 'm', '1969-12-25', 'soltero', 'A-', '584144740153', '584169477348');
# INSERT INTO `mydb`.`pacientes` (`nombre`, `apellido`, `segundo_apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`, `telefono`, `telefono2`) VALUES ('Fernando', 'Rodriguez', 'Manrique', '9420111', 'm', '1968-06-15', 'divorciado', 'B+', '58424696109', '584141133191');
# INSERT INTO `mydb`.`pacientes` (`nombre`, `segundo_nombre`, `apellido`, `segundo_apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`, `telefono`, `telefono2`) VALUES ('Ana', 'Maria', 'Garcia', 'Garcia', '7298711', 'f', '1959-01-22', 'soltero', 'B-', '58424696109', '584141133191');
# INSERT INTO `mydb`.`pacientes` (`nombre`, `segundo_nombre`, `apellido`, `segundo_apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`, `telefono`) VALUES ('Gabriela', 'Carolina', 'Pezzi', 'Fuenmayor', '2987110', 'f', '1940-04-07', 'viudo', 'B+', '584144740153');
# INSERT INTO `mydb`.`pacientes` (`nombre`, `segundo_nombre`, `apellido`, `segundo_apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`, `telefono`, `img_url`) VALUES ('José', 'Manuel', 'Orellana', 'Mijares', '26681153', 'm', '1999-04-13', 'soltero', 'B-', '584144740153', 'N/A');
# INSERT INTO `mydb`.`pacientes` (`nombre`, `segundo_nombre`, `apellido`, `segundo_apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`, `telefono`, `telefono2`, `img_url`) VALUES ('Manuel', 'Alejandro', 'Carmona', 'Carrasco', '1599855', 'm', '1987-12-21', 'casado', 'B-', '584169477348', '584266337841', 'N/A');
# INSERT INTO `mydb`.`pacientes` (`nombre`, `segundo_nombre`, `apellido`, `segundo_apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`, `img_url`) VALUES ('Rosa', 'Liz', 'Bolivar', 'Perez', '16666123', 'f', '1987-12-30', 'casado', 'A-', 'N/A');
# INSERT INTO `mydb`.`pacientes` (`nombre`, `segundo_nombre`, `apellido`, `segundo_apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`, `img_url`) VALUES ('Luis', 'Alberto', 'Peña', 'Navarro', '8944001', 'm', '1972-05-05', 'viudo', 'A+', 'N/A');
# INSERT INTO `mydb`.`pacientes` (`nombre`, `segundo_nombre`, `apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`, `telefono`, `telefono2`, `img_url`) VALUES ('Ariana', 'Daniela', 'Correa', '18150224', 'f', '1994-04-06', 'soltero', 'A-', '584141350990', '584249911565', 'N/A');
# INSERT INTO `mydb`.`pacientes` (`nombre`, `apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`, `telefono`, `img_url`) VALUES ('Carlos', 'Briceño', '12116790', 'm', '1980-01-22', 'casado', 'B+', '58419498124', 'N/A');


# INSERT INTO `mydb`.`historias_clinicas` (`usuarios_id`, `pacientes_id`, `edad_paciente`, `motivo_consulta`, `rasgos_cognitivos`, `sistolica`, `diastolica`, `pulso`, `freq_respiratoria`, `temp`) VALUES ('1', '1', '74', 'Hombre de 88 años con dolor de cabeza de lado derecho y dificultades para camina', 'ESTADO MENTAL: Alerta y orientado × 3. Discurso fluido, con buen nombre y repetición. Capaz de contar desde 100 por siete (una prueba de atención y habilidades de cálculo). NERVIOS CRANEALES (VER TABLA 2.5): Alumnos iguales y redondos y reactivos a la luz (CN II, III). Movimientos extraoculares intactos (CN III, IV, VI). Campos visuales (CN II) completos, pero con extinción a la izquierda para doble estimulación simultánea. Facial sensación intacta (CN V). Cara simétrica (CN VII). Mordaza normal (CN IX, X). Fuerza esternomastoidea normal (CN XI). Línea media de la lengua (CN XII). MOTOR: Deriva del pronador del brazo izquierdo (ver KCC 6.4). Leve izquierda hemiparesia (4 + / 5 de fuerza en todo el brazo izquierdo y pierna). Fuerza normal en el lado derecho. SENSORIAL: Intacto, excepto por extinción izquierda con doble estimulación simultánea. REFLEJOS CAMINAR: da pasos cortos, pero con buena velocidad. Capaz de realizar la marcha en tándem. COORDINACIÓN: No probado.', '146', '80', '86', '18', '36');
# INSERT INTO `mydb`.`historias_clinicas` (`usuarios_id`, `pacientes_id`, `edad_paciente`, `motivo_consulta`, `rasgos_cognitivos`, `sistolica`, `diastolica`, `pulso`, `freq_respiratoria`, `temp`) VALUES ('2', '2', '67', 'Un hombre de 67 años fue encontrado al pie de un tramo de escaleras, letargico y oliendo a alcohol', 'ESTADO MENTAL: letárgico pero excitable, con confuso habla. Indicó su nombre completo pero no sabía su ubicación ni la fecha. No recuerdo lo que le pasó a él, diciendo "Estoy bien". Seguido simples comandos. MOTOR: Capaz de mover las cuatro extremidades. ACTUALIZACIÓN ESTADO MENTAL: no responde excepto por movimiento a estímulos dolorosos NERVIOS CRANEALES: Pupilas de 3 mm, que se contraen a 2 mm bilateralmente. Las maniobras oculocefálicas (ver Capítulo 3) no fueron hecho debido al collarín cervical. Reflejo corneal presente a la izquierda, pero ausente a la derecha. SENSORIAL Y MOTOR: movió el brazo y la pierna izquierda en respuesta a estimulación dolorosa El brazo y la pierna derechos no se movieron respuesta al dolor REFLEJOS PLANTARES: No hay respuesta a la derecha, sigue adelante la izquierda.', '184', '90', '95', '20', '37');
# INSERT INTO `mydb`.`historias_clinicas` (`usuarios_id`, `pacientes_id`, `edad_paciente`, `motivo_consulta`, `rasgos_cognitivos`, `sistolica`, `diastolica`, `pulso`, `freq_respiratoria`, `temp`) VALUES ('1', '4', '51', 'Se descubrió que un hombre de 51 años no respondía progresivamente la mañana siguiente a una lesión en la cabeza', 'ESTADO MENTAL: no responde a los comandos. No hablando. Ocasionalmente golpeado en camilla agitado, Moda semipropósito. NERVIOS CRANEALES: pupila izquierda de 5 mm, fija (sin respuesta a ligero). Pupila derecha de 2 mm, que se contrae a 1 mm en respuesta a la luz. Las maniobras oculocefálicas no se realizan debido al collarín cervical. Presente reflejo nauseoso. SENSORIAL Y MOTOR: el brazo izquierdo y la pierna izquierda se movieron espontáneamente. Retiró el brazo izquierdo y la pierna a propósito de estimulación dolorosa El brazo y la pierna derechos no se movieron, incluso en respuesta al dolor. REFLEJOS COORDINACIÓN Y MARCA: No probado. Poco después de llegar a la sala de emergencias, el paciente desarrolló dificultad respiratoria y, por lo tanto, fue intubado. Él posteriormente dejó de mover su lado izquierdo también y se convirtió completamente insensible,', '150', '100', '97', '288', '37');
# INSERT INTO `mydb`.`historias_clinicas` (`usuarios_id`, `pacientes_id`, `edad_paciente`, `motivo_consulta`, `rasgos_cognitivos`) VALUES ('2', '5', '52', 'Un ejecutivo maderero de 52 años desarrolló dificultades leves para correr, inicialmente se golpeó el dedo gordo del pie izquierdo, que progresó a constante debilidad en la pierna izquierda en el transcurso de 6 meses', 'También se quejó de dolores de cabeza. El examen fue normal excepto por la disminución del pliegue nasolabial izquierdo y 4 + / 5 debilidad en el tríceps izquierdo y la pierna izquierda.');
# INSERT INTO `mydb`.`historias_clinicas` (`usuarios_id`, `pacientes_id`, `edad_paciente`, `motivo_consulta`, `rasgos_cognitivos`) VALUES ('3', '6', '61', 'Una mujer de 61 años se presentó en la sala de emergencias con 2 horas de debilidad en la cara y el brazo izquierdo', 'En examen a las 8:00 a.m. estaba completamente alerta, con debilidad leve en la cara izquierda y el brazo completamente ahorrando la pierna izquierda. Tenía antecedentes de fibrilación auricular, lo que puede causar la formación de coágulos sanguíneos en el corazón. aurículas como resultado de estasis (ver KCC 10.4). Por esta razón, ella era tomando el anticoagulante oral warfarina (Coumadin). Sin embargo, análisis de sangre en la sala de emergencias mostraron que ella no estaba adecuadamente anticoagulada en su dosis actual. Se consideró que probablemente tuvo una embolia desde el corazón hacia la derecha lado del cerebro. Una tomografía computarizada de la cabeza dentro de las 3 horas posteriores al inicio no fue notable. Este hallazgo fue consistente con el diagnóstico, ya que Pueden pasar de 6 a 24 horas para que se produzca un accidente cerebrovascular agudo visible en CT (ver Capítulo 4). Por lo tanto, fue admitida en el hospital y comenzó con la heparina anticoagulante intravenosa para lograr rápidamente un rango terapéutico de anticoagulación (tenga en cuenta que hoy este paciente también habría sido un candidato para la administración aguda de tPA; ver KCC 10.4). los el paciente permaneció estable durante todo el día, pero a las 10:00 p.m. De repente se descubrió que no podía despertarse. El examen fue notable para pupilas fijas, medianas, sin movimientos extraoculares, y postura extensora bilateral (decerebrate) de ambos brazos y piernas. Fue intubada de manera emergente debido a respiraciones superficiales.');
# INSERT INTO `mydb`.`historias_clinicas` (`usuarios_id`, `pacientes_id`, `edad_paciente`, `motivo_consulta`, `rasgos_cognitivos`) VALUES ('4', '7', '80', 'Una mujer de 80 años fue encontrada tirada en las rocas debajo de un muro de 6 pies de alto cerca de la costa.', 'Estuvo consciente y hablando por un breve tiempo antes de caer en coma. En el examen inicial tenía una abrasión del cuero cabelludo derecho; Pupila derecha de 6 mm y Pupila izquierda de 5 mm, ambas no reactivas a la luz; sin reflejos corneales; postura flexora (decorticada) de las extremidades superiores al dolor (ver Figura 3.5A); y respuestas plantares salientes bilateralmente.');
