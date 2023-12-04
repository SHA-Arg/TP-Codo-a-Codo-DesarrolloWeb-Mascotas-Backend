


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `login_python`
--

CREATE TABLE `login_python` (
  `id` int(11) NOT NULL,
  `tipo_user` int(11) DEFAULT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` text DEFAULT NULL,  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `login_python`
--

INSERT INTO `login_python` (`id`, `tipo_user`, `nombre`, `apellido`, `email`, `password`) VALUES
(2, 1, 'Urian Viera', 'Viera Parra', 'desarrollo@gmail.com', 'sha256$rNCs0EiH36AogNa3$c8b59ab82bdd53643143ad04d80767e7c21157fcf035ee4022e8eba70a7c5003'),
(3, 2, 'Brenda', 'Viera', 'brenda@gmail.com', 'sha256$7jaYfYrtIWJngvFv$9dda11aea048705442096b09eabf54808fb2db537aaff3da48f2fe2b38834e29');

--
-- Índices para tablas volcadas
--



--
-- Indices de la tabla `login_python`
--
ALTER TABLE `login_python`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--



--
-- AUTO_INCREMENT de la tabla `login_python`
--
ALTER TABLE `login_python`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;



