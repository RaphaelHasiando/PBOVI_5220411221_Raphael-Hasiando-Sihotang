-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2024 at 05:43 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5220411221`
--

-- --------------------------------------------------------

--
-- Table structure for table `sosial_kampus_users`
--

CREATE TABLE `sosial_kampus_users` (
  `id` int(11) DEFAULT NULL,
  `nama_kampus` varchar(255) DEFAULT NULL,
  `jurusan` varchar(255) DEFAULT NULL,
  `fakultas` varchar(255) DEFAULT NULL,
  `npm` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sosial_kampus_users`
--

INSERT INTO `sosial_kampus_users` (`id`, `nama_kampus`, `jurusan`, `fakultas`, `npm`) VALUES
(7, 'Universitas Teknologi Yogyakarta', 'Informatika', 'Sains dan Teknologi', '5220411222'),
(8, 'Universitas Teknologi Yogyakarta', 'Informatika', 'Sains dan Teknologi', '5220411223'),
(9, 'Universitas Teknologi Yogyakarta', 'Informatika', 'Sains dan Teknologi', '5220411224'),
(10, 'Universitas Teknologi Yogyakarta', 'Informatika', 'Sains dan Teknologi', '5220411225'),
(11, 'Universitas Teknologi Yogyakarta', 'Informatika', 'Sains dan Teknologi', '5220411226'),
(12, 'Universitas Teknologi Yogyakarta', 'Informatika', 'Sains dan Teknologi', '5220411227');

-- --------------------------------------------------------

--
-- Table structure for table `sosial_kelas_users`
--

CREATE TABLE `sosial_kelas_users` (
  `id` int(11) DEFAULT NULL,
  `kelas` varchar(255) DEFAULT NULL,
  `nama_matkul` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sosial_kelas_users`
--

INSERT INTO `sosial_kelas_users` (`id`, `kelas`, `nama_matkul`) VALUES
(11, 'D', 'Pengantar Analisis Data'),
(11, 'D', 'Basis Data'),
(11, 'D', 'Agama'),
(12, 'D', 'Pengantar Analisis Data'),
(12, 'D', 'Pemrograman Berorientasi Objek');

-- --------------------------------------------------------

--
-- Table structure for table `sosial_masyarakat_users`
--

CREATE TABLE `sosial_masyarakat_users` (
  `id` int(11) DEFAULT NULL,
  `NIK` varchar(255) NOT NULL,
  `kelurahan` varchar(255) DEFAULT NULL,
  `kecamatan` varchar(255) DEFAULT NULL,
  `sosialisasi_poin` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sosial_masyarakat_users`
--

INSERT INTO `sosial_masyarakat_users` (`id`, `NIK`, `kelurahan`, `kecamatan`, `sosialisasi_poin`) VALUES
(1, '217110', 'Lurah 1', 'Matan', 0),
(2, '217111', 'Lurah 1', 'Matan 2', 0),
(3, '217112', 'Lurah 13', 'Matan 40', 0),
(4, '217120', 'Lurah 102', 'Matan 23', 0),
(5, '217402', 'Lurah 201', 'Matan 192', 0),
(13, '217952', 'Lurah 201', 'Kecamatan 201', 4);

-- --------------------------------------------------------

--
-- Table structure for table `sosial_users`
--

CREATE TABLE `sosial_users` (
  `id` int(11) NOT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `tempat_lahir` varchar(255) DEFAULT NULL,
  `tanggal_lahir` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sosial_users`
--

INSERT INTO `sosial_users` (`id`, `alamat`, `nama`, `tempat_lahir`, `tanggal_lahir`) VALUES
(1, 'Jl. Kernagari', 'Raphael', 'Batam', '30 September 2003'),
(2, 'Jl. Kornogere', 'Hasiando', 'Jakarta', '29 Januari 2003'),
(3, 'Jl. Moshi', 'Sihotang', 'Semarang', '17 Maret 2002'),
(4, 'Jl. Mobom', 'John', 'Medan', '28 April 2001'),
(5, 'Jl. Shero', 'Jimmy', 'Bandung', '27 May 1999'),
(7, 'Jl. Mombos', 'Jene', 'Semarang', '18 Maret 2002'),
(8, 'Jl. Gaser', 'Jana', 'Batam', '19 Januari 2000'),
(9, 'Jl. Wekser', 'Jina', 'Batam', '10 Januari 2000'),
(10, 'Jl. Gaksing', 'Jason', 'Cilegon', '28 September 2002'),
(11, 'Jl. Bandungsss', 'Kasires', 'Bandung', '18 September 2000'),
(12, 'Jl. Merdeka', 'Konsih', 'Jakarta', '18 Maret 2003'),
(13, 'Jl. Api', 'Hasiodn', 'Batam', '29 April 2000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sosial_kampus_users`
--
ALTER TABLE `sosial_kampus_users`
  ADD PRIMARY KEY (`npm`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `sosial_kelas_users`
--
ALTER TABLE `sosial_kelas_users`
  ADD KEY `id` (`id`);

--
-- Indexes for table `sosial_masyarakat_users`
--
ALTER TABLE `sosial_masyarakat_users`
  ADD PRIMARY KEY (`NIK`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `sosial_users`
--
ALTER TABLE `sosial_users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sosial_users`
--
ALTER TABLE `sosial_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `sosial_kampus_users`
--
ALTER TABLE `sosial_kampus_users`
  ADD CONSTRAINT `sosial_kampus_users_ibfk_1` FOREIGN KEY (`id`) REFERENCES `sosial_users` (`id`);

--
-- Constraints for table `sosial_kelas_users`
--
ALTER TABLE `sosial_kelas_users`
  ADD CONSTRAINT `sosial_kelas_users_ibfk_1` FOREIGN KEY (`id`) REFERENCES `sosial_kampus_users` (`id`);

--
-- Constraints for table `sosial_masyarakat_users`
--
ALTER TABLE `sosial_masyarakat_users`
  ADD CONSTRAINT `sosial_masyarakat_users_ibfk_1` FOREIGN KEY (`id`) REFERENCES `sosial_users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
