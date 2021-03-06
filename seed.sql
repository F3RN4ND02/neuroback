INSERT INTO paises VALUES (1, 'Venezuela','VE');

INSERT INTO estados (id, nombre, paises_id) VALUES
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
(24, 'Distrito Capital', 1);

INSERT INTO municipios (id, estado_id, nombre) VALUES
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
(462, 24, 'Libertador');

INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Dolor de cabeza', 'Sensación dolorosa en cualquier parte de la cabeza, que va desde un dolor agudo a un dolor leve');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Encefalopatía', 'cualquier enfermedad cerebral que altera la función o la estructura del cerebro.');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Ataque cerebrovascular', 'Lesión en el cerebro ocasionada por la interrupción de la irrigación sanguínea.');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Convulsión', 'Un síntoma transitorio caracterizado por actividad neuronal en el cerebro que conlleva a hallazgos físicos peculiares como la contracción y distensión repetida y temblorosa de uno o varios músculos de forma brusca y generalmente violenta');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Debilidad general', 'Debilidad generalizada');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Neuropatía Craneal', 'ocurre cuando uno o más de los doce nervios que salen del cerebro o del tronco cerebral están dañados.');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Neuropatía Periférica', 'Debilidad, entumecimiento y dolor, generalmente en las manos y los pies, ocasionado por un daño neurológico.');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Miopatía', 'Deficiencia o anomalía en los grupos musculares');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Trastornos del movimiento', 'grupo de afecciones del sistema nervioso (afecciones neurológicas) que provocan un aumento de movimientos anormales, que pueden ser voluntarios o involuntarios');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Cambios en la personalidad o comportamiento', 'comportamiento');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Depresión', 'Grupo de afecciones asociadas a los cambios de humor de una persona, como la depresión o el trastorno bipolar');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Embarazo', 'Etapa de gestación');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Nausea/Vomito/Mareo', 'Nausea/Vomito/Mareo');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Vejez', 'Paciento con edad mayor a 65 años');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Medicación', 'Paciente consumiendo recientemente algún medicamento');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Pasado medico', 'Paciente con historial relevante de patologias');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Perdida de memoria', 'Incapacidad para recordar eventos durante un período de tiempo');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Cirugia', 'Paciente con historial quirurgico relevante');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Diarrea', 'Heces blandas y líquidas con mayor frecuencia de lo habitual');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Problema Visual', 'Cualquier impedimento a la correcta función de los ojos');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Abuso de sustancias', 'Cigarrillo, alcohol, entre otras drogas');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Paralisis de nervio', 'Paralisis de cualquier nervio');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Disfagia', 'Dificultad para tragar alimentos');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Peso', 'Perdida o aumento súbito de peso');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Fatiga', 'Sensación de mucho cansancio, con poca energía y un fuerte deseo de dormir');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Capacidad de respuesta', 'Deterioro de la capacidad de respuesta');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Herida', 'Herida relevante a la historica clínica');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Declive cognitivo', 'Declive de las funciones cognitivas');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Fiebre', 'Aumento temporal de la temperatura corporal promedio');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Antecedente familiar', 'Familiar con cualquier patología relevante');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Anomalia de signos vitales', 'Pulso, presión sanguinea, etc');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Linfadenopatía', 'agrandamiento de los ganglios');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Candidiasis', 'Infección Vaginal');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Rigidez de nuca', 'Sensación de dolor o molestia en el cuello al intentar mover o girar la cabeza de lado a lado');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Examen de sangre', 'Anomalia en los parametros de un examen de sangre');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Anomalia LCR', 'Anomalia en los parametros de un examen del liquido cefalorraquídeo');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Alucinaciones', 'Percepción de haber visto, escuchado, tocado, probado u olido algo que no estaba allí');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Dolor General', 'Dolor general');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Apetito', 'Perdida o aumento del apetito');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Piel', 'Anomalia en la piel');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Problemas urinarios', 'Problema en la funcion urinaria');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Hipoestesia', 'Disminución en el sentido del tacto o las sensaciones');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Coma', 'Período prolongado de inconsciencia provocada por enfermedad o lesión');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Problemas respiratorios', 'Problemas de los pulmones como asma, enfisema o neumonía');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Edema Cerebral', ' acumulación de líquido en los espacios intra o extracelulares del cerebro');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Historial Profesional', 'Profesión relevante a la historia clínica');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Debilidad en piernas', 'Debilidad EXCLUSIVA en las piernas');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Cardiopatía', 'padecimiento del corazón o del resto del sistema cardiovascular');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Estreñimiento', 'Dificultad para defecar');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Disfunción eréctil', 'Incapacidad de un hombre de conseguir o mantener una erección firme para la relación sexual');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Disminucion sentidos', 'Disminución en el olfato, gusto y audición');
INSERT INTO `mydb`.`tipo_metadatos` (`nombre`, `descripcion`) VALUES ('Examen Orina', 'Anomalia en los parametros de un examen de orina');


INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Angiografía cerebral', 'procedimiento para localizar posibles singularidades vasculares en el cerebro');
INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Electroencefalograma', 'Pequeños electrodos transporta la actividad eléctrica del cerebro hasta un aparato que lee dicha actividad y la convierte en un trazado del registro eléctrico');
INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Punción lumbar', 'se realizan con el objetivo de obtener muestras de líquido cefalorraquídeo.');
INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Tomografía computerizada', 'La TC neurológica puede ayudar a realizar diagnósticos diferenciales en trastornos neurológicos con varias propiedades parecidas');
INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Resonancia magnética', 'se utilizan las radioondas que se generan en un aparato y un gran campo magnético que revelan los detalles de órganos, tejidos, nervios y huesos');
INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Tomografía por emisión de positrones ', 'Esta imagen se logra a través de la medición de isótopos radioactivos inyectados en el torrente sanguíneo del paciente');
INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Potenciales evocados', 'En la prueba de potenciales evocados se pueden evaluar posibles problemas nerviosos sensoriales');
INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Hemograma', 'consiste en un conteo de los elementos celulares de la sangre como son las células rojas, blancas y plaquetas.');
INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Urinálisis', 'clave para detectar un problema de salud relacionado con el sistema urinario');
INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Heces por Parásito', 'Este sencillo examen puede determinar si la causa de la diarrea se debe a parásitos, amebas o entero patógenos');
INSERT INTO `mydb`.`tipo_examenes` (`nombre`, `descripcion`) VALUES ('Perfil Renal', 'Urea es el producto final del metabolismo de la proteína. La cantidad de urea excretada varia directamente con la ingesta de proteínas');


INSERT INTO `mydb`.`tipo_vacunas` (`nombre`, `descripcion`) VALUES ('DTaP', 'Difteria, Tetanos y Tos Ferina');
INSERT INTO `mydb`.`tipo_vacunas` (`nombre`, `descripcion`) VALUES ('Hepatitis B', 'se aplica en 3 o 4 inyecciones durante un período de 6 meses.');
INSERT INTO `mydb`.`tipo_vacunas` (`nombre`, `descripcion`) VALUES ('Poliomielitis', 'Vacuna contra la poliomielitis');
INSERT INTO `mydb`.`tipo_vacunas` (`nombre`, `descripcion`) VALUES ('Haemophilus influenzae tipo b', 'Vacuna contra la influenza tipo b');


# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Agente de viaje', 'Persona que vende y organiza viajes, vacaciones y vuelos');
# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Barrendero/a', ' Persona que limpia los lugares públicos (calles, plazas, etc.)');
# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Bibliotecario/a', 'Persona que trabaja en una biblioteca manteniendo el orden de los libros, videos, discos, etc.');
# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Bombero/a', 'Persona que apaga el fuego en un incendio. (2) Persona que carga combustible en una estación de servicios');
# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Carnicero/a', 'Persona que trabaja con carne. Ellos cortan la carne y la venden');
# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Cientifico/a', 'Persona que trabaja en investigaciones científicas haciendo muchos experimentos');
# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Chef', 'Persona que prepara comida para otros, comúnmente en un restaurante');
# INSERT INTO `mydb`.`tipo_profesiones` (`nombre`, `descripcion`) VALUES ('Doctor', 'Persona a la que vas cuando tienes problemas de salud.');


INSERT INTO `mydb`.`antecedentes` (`nombre`, `descripcion`) VALUES ('Cancer', 'Enfermedad en la que células anómalas se dividen sin control y destruyen los tejidos corporales');
INSERT INTO `mydb`.`antecedentes` (`nombre`, `descripcion`) VALUES ('Absceso hepático', 'causado por la Entamoeba histolytica');
INSERT INTO `mydb`.`antecedentes` (`nombre`, `descripcion`) VALUES ('Trombosis', 'formación de un coágulo en el interior de un vaso sanguíneo y uno de los causantes de un infarto agudo de miocardio');
INSERT INTO `mydb`.`antecedentes` (`nombre`, `descripcion`) VALUES ('Mielitis', 'Inflamación de la médula espinal');
INSERT INTO `mydb`.`antecedentes` (`nombre`, `descripcion`) VALUES ('Hipertensión', 'Afección en la que la presión de la sangre hacia las paredes de la arteria es demasiado alta');
INSERT INTO `mydb`.`antecedentes` (`nombre`, `descripcion`) VALUES ('Derrame cerebral', 'Lesión en el cerebro ocasionada por la interrupción de la irrigación sanguínea');
INSERT INTO `mydb`.`antecedentes` (`nombre`, `descripcion`) VALUES ('Otro', 'No registrado en el sistema');

INSERT INTO `mydb`.`usuarios` (`username`, `nombre`, `apellido`, `email`, `contrasena`, `rol`, `documento`, `sexo`, `activo`) VALUES ('admin', 'Admin', 'Admin', 'admin@admin.com', 'sha256$XJI26Co3$bfe1cef229975aab5b419d62853c3f59700d427c150c833d34d287c462c3b4cf', 'Medico', '14544011', 'm', '');
INSERT INTO `mydb`.`usuarios` (`username`, `nombre`, `apellido`, `email`, `contrasena`, `rol`, `documento`, `sexo`, `activo`) VALUES ('jesusort', 'Jesus', 'Ortega', 'jesus@ortega.com', 'sha256$XJI26Co3$bfe1cef229975aab5b419d62853c3f59700d427c150c833d34d287c462c3b4cf', 'Medico', '12475544', 'm', '');
INSERT INTO `mydb`.`usuarios` (`username`, `nombre`, `apellido`, `email`, `contrasena`, `rol`, `documento`, `sexo`) VALUES ('carrana', 'Ana', 'Carrasco', 'ana@carrasco.com', 'sha256$XJI26Co3$bfe1cef229975aab5b419d62853c3f59700d427c150c833d34d287c462c3b4cf', 'Medico', '7414265', 'f');
INSERT INTO `mydb`.`usuarios` (`username`, `nombre`, `apellido`, `email`, `contrasena`, `rol`, `documento`, `sexo`) VALUES ('mjmo122', 'Mario', 'Molina', 'mario@molina.com', 'sha256$XJI26Co3$bfe1cef229975aab5b419d62853c3f59700d427c150c833d34d287c462c3b4cf', 'Estudiante', '19455001', 'm');
INSERT INTO `mydb`.`usuarios` (`username`, `nombre`, `apellido`, `email`, `contrasena`, `rol`, `documento`, `sexo`) VALUES ('Susand', 'Susana', 'Diaz', 'susana@diaz.com', 'sha256$XJI26Co3$bfe1cef229975aab5b419d62853c3f59700d427c150c833d34d287c462c3b4cf', 'Medico Especialista', '4124216', 'f');
INSERT INTO `mydb`.`usuarios` (`username`, `nombre`, `apellido`, `email`, `contrasena`, `rol`, `documento`, `sexo`) VALUES ('carlherrera', 'Carlos', 'Herrera', 'carl@herrera.com', 'sha256$XJI26Co3$bfe1cef229975aab5b419d62853c3f59700d427c150c833d34d287c462c3b4cf', 'Investigador', '5623144', 'm');
INSERT INTO `mydb`.`usuarios` (`username`, `nombre`, `apellido`, `email`, `contrasena`, `rol`, `documento`, `sexo`) VALUES ('gustavo', 'Gustavo', 'Fuentes', 'gustavo@fuentes.com', 'sha256$XJI26Co3$bfe1cef229975aab5b419d62853c3f59700d427c150c833d34d287c462c3b4cf', 'Doctor', '11345106', 'm');


INSERT INTO `mydb`.`direcciones` (`detalle`, `municipios_id`) VALUES ('Avenida junin con carvajal casa #04', '44');
INSERT INTO `mydb`.`direcciones` (`detalle`, `municipios_id`) VALUES ('Sector Oeste Fila 11 Casa 3', '79');
INSERT INTO `mydb`.`direcciones` (`detalle`, `municipios_id`) VALUES ('Los Naranjos Sector 5 Avenida Libertador Casa 14', '11');
INSERT INTO `mydb`.`direcciones` (`detalle`, `municipios_id`) VALUES ('Parque Americas Edificio 22 Piso 5', '22');
INSERT INTO `mydb`.`direcciones` (`detalle`, `municipios_id`) VALUES ('Avenida Bolivar Casa 133', '200');
INSERT INTO `mydb`.`direcciones` (`detalle`, `municipios_id`) VALUES ('Calle Panamericana con Michelena Edificio 12 Centro', '12');

INSERT INTO `mydb`.`pacientes` (`direccion_actual`, `nombre`, `segundo_nombre`, `apellido`, `segundo_apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`, `telefono`) VALUES ('1', 'Miguel', 'Antonio', 'Ramirez', 'Parra', '6955012', 'm', '1959-01-22', 'divorciado', 'A-', '42472564113');
INSERT INTO `mydb`.`pacientes` (`direccion_actual`, `nombre`, `segundo_nombre`, `apellido`, `segundo_apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`, `telefono`, `telefono2`) VALUES ('2', 'Ana', 'Carolina', 'Soto', 'Diaz', '14525901', 'f', '1967-04-15', 'casado', 'O+', '4241404962', '4125576712');
INSERT INTO `mydb`.`pacientes` (`direccion_actual`, `nombre`, `segundo_nombre`, `apellido`, `segundo_apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`, `telefono`) VALUES ('3', 'Fernando', 'Isaias', 'Rojas', 'Perez', '22551711', 'm', '1997-06-06', 'soltero', 'desconocido', '4162760216');
INSERT INTO `mydb`.`pacientes` (`direccion_actual`, `nombre`, `segundo_nombre`, `apellido`, `segundo_apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`) VALUES ('4', 'Luis', 'Alberto', 'Peña', 'Navarro', '24107112', 'm', '1998-12-21', 'soltero', 'A-');
INSERT INTO `mydb`.`pacientes` (`direccion_actual`, `nombre`, `segundo_nombre`, `apellido`, `segundo_apellido`, `documento`, `sexo`, `fecha_nacimiento`, `estado_civil`, `tipo_sangre`, `telefono`, `telefono2`) VALUES ('5', 'Maria', 'José', 'Ibarra', 'Guzman', '14987566', 'f', '1972-11-11', 'casado', 'B+', '4145051982', '2432760216');
INSERT INTO `mydb`.`pacientes` (`direccion_actual`, `nombre`, `segundo_nombre`, `apellido`, `segundo_apellido`, `documento`, `sexo`, `estado_civil`, `tipo_sangre`, `telefono`, `telefono2`) VALUES ('6', 'Ariana', 'Daniela', 'Ceballos', 'Ramos', '18800918', 'f', 'casado', 'B-', '4243331512', '2435650901');


INSERT INTO `mydb`.`antecedentes_personales` (`antecedentes_id`, `pacientes_id`) VALUES ('1', '1');
INSERT INTO `mydb`.`antecedentes_personales` (`antecedentes_id`, `pacientes_id`) VALUES ('3', '1');

INSERT INTO `mydb`.`antecedentes_familiares` (`pacientes_id`, `antecedentes_id`, `familiar`) VALUES ('1', '1', 'Madre');
INSERT INTO `mydb`.`antecedentes_familiares` (`pacientes_id`, `antecedentes_id`, `familiar`) VALUES ('1', '4', 'Abuelo Paterno');

INSERT INTO `mydb`.`historias_clinicas` (`usuarios_id`, `pacientes_id`, `edad_paciente`, `motivo_consulta`, `sistolica`, `diastolica`, `pulso`, `freq_respiratoria`, `temp`, `estatura`, `peso`, `observaciones`, `examen_fisico`) VALUES ('3', '2', '45', 'Movimiento involuntario de las extremidaddes', '110', '70', '77', '16', '37', '177', '71', 'Se podria tratar de un caso de...', 'Nervios craneales... Caminar... Reflejos...');

INSERT INTO `mydb`.`sintomas` (`historias_clinicas_id`, `tipo_sintomas_id`) VALUES ('2', '2');
INSERT INTO `mydb`.`sintomas` (`historias_clinicas_id`, `tipo_sintomas_id`) VALUES ('2', '4');
INSERT INTO `mydb`.`sintomas` (`historias_clinicas_id`, `tipo_sintomas_id`) VALUES ('2', '6');
INSERT INTO `mydb`.`sintomas` (`historias_clinicas_id`, `tipo_sintomas_id`) VALUES ('2', '3');


INSERT INTO `mydb`.`noticias` (`titulo`, `resumen`, `enlace`) VALUES ('Hallazgo cientifico en el lab...', 'Un nuevo hallazgo en el laboratorio LabEngine de la ciudad de Los Angeles', 'https://www.google.com');
INSERT INTO `mydb`.`noticias` (`titulo`, `resumen`, `enlace`) VALUES ('Entregado los premios a los nuevos...', 'El pasado domingo se realizaron la 25ma entrega de los...', 'https://www.google.com');
INSERT INTO `mydb`.`noticias` (`titulo`, `resumen`, `enlace`) VALUES ('Descubren nuevo...', 'Cientificos de la universidad de Kentucky...', 'https://www.google.com');
INSERT INTO `mydb`.`noticias` (`titulo`, `resumen`, `enlace`) VALUES ('Aplazada la convencion de neurologia', 'Tristes noticias para los medicos de todo el mundo, el evento...', 'https://www.google.com');
INSERT INTO `mydb`.`noticias` (`titulo`, `resumen`, `enlace`) VALUES ('Empresa desvela su nuevo producto..', 'Se trata de las nuevas herramientas para la neurologia..', 'https://www.google.com');
