-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 14, 2023 at 03:14 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `laporan_iae`
--

-- --------------------------------------------------------

--
-- Table structure for table `laporan`
--

CREATE TABLE `laporan` (
  `id_laporan` int(10) NOT NULL,
  `laporan_bulan` varchar(50) NOT NULL,
  `tgl_pembelian` date NOT NULL,
  `merk_kendaraan` varchar(50) NOT NULL,
  `harga_modal` bigint(20) NOT NULL,
  `harga_satuan` bigint(20) NOT NULL,
  `total_terjual` bigint(20) NOT NULL,
  `total_income` bigint(20) NOT NULL,
  `total_profit` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `laporan`
--

INSERT INTO `laporan` (`id_laporan`, `laporan_bulan`, `tgl_pembelian`, `merk_kendaraan`, `harga_modal`, `harga_satuan`, `total_terjual`, `total_income`, `total_profit`) VALUES
(1, 'juni', '2023-06-02', 'Toyota Fortuner', 560000000, 700000000, 5, 3500000000, 700000000),
(2, 'juni', '2023-06-03', 'Toyota Camry', 750000000, 870000000, 8, 6960000000, 960000000),
(5, 'juni', '2023-06-03', 'Toyota Camry', 750000000, 870000000, 8, 6960000000, 960000000),
(6, 'juni', '2023-06-03', 'Toyota Camry', 750000000, 870000000, 8, 6960000000, 960000000),
(7, 'juli', '2023-07-01', 'Toyota Avanza', 700000000, 800000000, 9, 7200000000, 900000000),
(8, 'Agustus', '2023-08-16', 'Toyota Inova', 800000000, 900000000, 4, 3600000000, 400000000);

-- --------------------------------------------------------

--
-- Table structure for table `pembayaran`
--

CREATE TABLE `pembayaran` (
  `id_pembelian` int(10) NOT NULL,
  `tgl_pembelian` date NOT NULL,
  `merk_kendaraan` varchar(50) NOT NULL,
  `harga_modal` bigint(20) NOT NULL,
  `harga_satuan` bigint(20) NOT NULL,
  `total_terjual` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pembayaran`
--

INSERT INTO `pembayaran` (`id_pembelian`, `tgl_pembelian`, `merk_kendaraan`, `harga_modal`, `harga_satuan`, `total_terjual`) VALUES
(1, '2023-06-02', 'Toyota Fortuner', 560000000, 700000000, 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `laporan`
--
ALTER TABLE `laporan`
  ADD PRIMARY KEY (`id_laporan`);

--
-- Indexes for table `pembayaran`
--
ALTER TABLE `pembayaran`
  ADD PRIMARY KEY (`id_pembelian`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `laporan`
--
ALTER TABLE `laporan`
  MODIFY `id_laporan` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `pembayaran`
--
ALTER TABLE `pembayaran`
  MODIFY `id_pembelian` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
