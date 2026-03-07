-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 12, 2025 at 01:27 PM
-- Server version: 10.6.19-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `django_hrm`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_attendance`
--

CREATE TABLE `app_attendance` (
  `id` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `check_in` time(6) DEFAULT NULL,
  `check_out` time(6) DEFAULT NULL,
  `status` varchar(10) NOT NULL,
  `work_hours` double NOT NULL,
  `overtime_hours` double NOT NULL,
  `late_entry_approved` tinyint(1) NOT NULL,
  `early_leave_approved` tinyint(1) NOT NULL,
  `employee_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `app_attendance`
--

INSERT INTO `app_attendance` (`id`, `date`, `check_in`, `check_out`, `status`, `work_hours`, `overtime_hours`, `late_entry_approved`, `early_leave_approved`, `employee_id`) VALUES
(1, '2025-05-06', '08:25:37.000000', '08:25:41.000000', 'Present', 8, 0, 0, 0, 2);

-- --------------------------------------------------------

--
-- Table structure for table `app_document`
--

CREATE TABLE `app_document` (
  `id` bigint(20) NOT NULL,
  `filename` varchar(255) NOT NULL,
  `filedescription` longtext NOT NULL,
  `file` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `app_document`
--

INSERT INTO `app_document` (`id`, `filename`, `filedescription`, `file`) VALUES
(2, 'Harriet Acosta', 'Magna incidunt dign', 'officialDocs/chapter-05_-_zooming_Uvw98wT.pdf'),
(3, 'Felix Lane', 'Dolor libero exercit', 'officialDocs/chapter-05_-_zooming_WRjy1j8.pdf'),
(4, 'Nadine Mack', 'Duis qui qui commodo', 'officialDocs/Screenshot_2.png');

-- --------------------------------------------------------

--
-- Table structure for table `app_employee`
--

CREATE TABLE `app_employee` (
  `id` bigint(20) NOT NULL,
  `employee_id` varchar(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(25) NOT NULL,
  `designation` varchar(255) NOT NULL,
  `present_address` varchar(255) NOT NULL,
  `permanent_address` varchar(255) NOT NULL,
  `department` varchar(255) NOT NULL,
  `salary` decimal(10,2) NOT NULL,
  `joining_date` date NOT NULL,
  `employment_status` varchar(20) NOT NULL,
  `employee_photo` varchar(100) DEFAULT NULL,
  `employee_doc` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `app_expense`
--

CREATE TABLE `app_expense` (
  `id` bigint(20) NOT NULL,
  `category` varchar(100) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `receipt` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `uploaded_on` datetime(6) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `travel_request_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `app_leavebalance`
--

CREATE TABLE `app_leavebalance` (
  `id` bigint(20) NOT NULL,
  `leave_type` varchar(20) NOT NULL,
  `total_leaves` int(11) NOT NULL,
  `used_leaves` int(11) NOT NULL,
  `remaining_leaves` int(11) NOT NULL,
  `employee_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `app_leaves`
--

CREATE TABLE `app_leaves` (
  `id` bigint(20) NOT NULL,
  `leave_type` varchar(20) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `status` varchar(10) NOT NULL,
  `remarks` longtext DEFAULT NULL,
  `employee_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `app_payroll`
--

CREATE TABLE `app_payroll` (
  `id` bigint(20) NOT NULL,
  `pay_period_start` date NOT NULL,
  `pay_period_end` date NOT NULL,
  `basic_salary` decimal(10,2) NOT NULL,
  `allowances` decimal(10,2) NOT NULL,
  `deductions` decimal(10,2) NOT NULL,
  `net_salary` decimal(10,2) NOT NULL,
  `status` varchar(20) NOT NULL,
  `payment_date` date DEFAULT NULL,
  `employee_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `app_reimbursement`
--

CREATE TABLE `app_reimbursement` (
  `id` bigint(20) NOT NULL,
  `reimbursed` tinyint(1) NOT NULL,
  `reimbursed_on` date DEFAULT NULL,
  `expense_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `app_travelrequest`
--

CREATE TABLE `app_travelrequest` (
  `id` bigint(20) NOT NULL,
  `destination` varchar(255) NOT NULL,
  `purpose` longtext NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `requested_on` datetime(6) NOT NULL,
  `employee_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `attendance_attendancerecord`
--

CREATE TABLE `attendance_attendancerecord` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `time` datetime(6) NOT NULL,
  `accuracy` double NOT NULL,
  `image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendance_attendancerecord`
--

INSERT INTO `attendance_attendancerecord` (`id`, `name`, `time`, `accuracy`, `image`) VALUES
(501, 'Mamun', '2025-07-10 10:35:57.346893', 89.19, 'attendance_images/Mamun_20250710103557.jpg'),
(502, 'Mamun', '2025-07-10 10:35:58.417135', 87.63, 'attendance_images/Mamun_20250710103558.jpg'),
(503, 'Mamun', '2025-07-10 10:35:59.564206', 87.28, 'attendance_images/Mamun_20250710103559.jpg'),
(504, 'Mamun', '2025-07-10 10:36:00.708398', 87.09, 'attendance_images/Mamun_20250710103600.jpg'),
(505, 'Mamun', '2025-07-10 10:36:01.898144', 88.5, 'attendance_images/Mamun_20250710103601.jpg'),
(506, 'Mamun', '2025-07-10 10:36:02.956671', 87.45, 'attendance_images/Mamun_20250710103602.jpg'),
(507, 'Mamun', '2025-07-10 10:36:04.148896', 87.96, 'attendance_images/Mamun_20250710103604.jpg'),
(508, 'Mamun', '2025-07-10 10:36:05.218723', 87.78, 'attendance_images/Mamun_20250710103605.jpg'),
(509, 'Mamun', '2025-07-10 10:36:06.354712', 88.49, 'attendance_images/Mamun_20250710103606.jpg'),
(510, 'Mamun', '2025-07-10 10:36:07.543646', 87.57, 'attendance_images/Mamun_20250710103607.jpg'),
(511, 'Mamun', '2025-07-10 10:36:08.845204', 87.32, 'attendance_images/Mamun_20250710103608.jpg'),
(512, 'Mamun', '2025-07-10 10:36:09.931947', 87.92, 'attendance_images/Mamun_20250710103609.jpg'),
(513, 'Mamun', '2025-07-10 10:36:11.146593', 87.28, 'attendance_images/Mamun_20250710103611.jpg'),
(514, 'Mamun', '2025-07-10 10:36:12.342386', 86.79, 'attendance_images/Mamun_20250710103612.jpg'),
(515, 'Mamun', '2025-07-10 10:36:13.587938', 87.61, 'attendance_images/Mamun_20250710103613.jpg'),
(516, 'Mamun', '2025-07-10 10:36:14.713579', 86.98, 'attendance_images/Mamun_20250710103614.jpg'),
(517, 'Mamun', '2025-07-10 10:36:15.903370', 88.03, 'attendance_images/Mamun_20250710103615.jpg'),
(518, 'Mamun', '2025-07-10 10:36:16.971131', 86.64, 'attendance_images/Mamun_20250710103616.jpg'),
(519, 'Mamun', '2025-07-10 10:36:18.162615', 87.26, 'attendance_images/Mamun_20250710103618.jpg'),
(520, 'Mamun', '2025-07-10 10:36:19.299463', 88.57, 'attendance_images/Mamun_20250710103619.jpg'),
(521, 'Mamun', '2025-07-10 10:36:20.493961', 87.32, 'attendance_images/Mamun_20250710103620.jpg'),
(522, 'Mamun', '2025-07-10 10:36:21.790291', 87.6, 'attendance_images/Mamun_20250710103621.jpg'),
(523, 'Mamun', '2025-07-10 10:36:22.915162', 88.56, 'attendance_images/Mamun_20250710103622.jpg'),
(524, 'Mamun', '2025-07-10 10:36:24.138132', 87.66, 'attendance_images/Mamun_20250710103624.jpg'),
(525, 'Mamun', '2025-07-10 10:36:25.358001', 87.18, 'attendance_images/Mamun_20250710103625.jpg'),
(526, 'Mamun', '2025-07-10 10:36:26.609460', 86.84, 'attendance_images/Mamun_20250710103626.jpg'),
(527, 'Mamun', '2025-07-10 10:36:27.813933', 86.12, 'attendance_images/Mamun_20250710103627.jpg'),
(528, 'Mamun', '2025-07-10 10:36:28.930850', 86.23, 'attendance_images/Mamun_20250710103628.jpg'),
(529, 'Mamun', '2025-07-10 10:36:30.095635', 86.55, 'attendance_images/Mamun_20250710103630.jpg'),
(530, 'Mamun', '2025-07-10 10:36:31.242014', 87.12, 'attendance_images/Mamun_20250710103631.jpg'),
(531, 'Mamun', '2025-07-10 10:36:32.507238', 87.09, 'attendance_images/Mamun_20250710103632.jpg'),
(532, 'Mamun', '2025-07-10 10:36:33.685290', 86.31, 'attendance_images/Mamun_20250710103633.jpg'),
(533, 'Mamun', '2025-07-10 10:36:34.889926', 86.95, 'attendance_images/Mamun_20250710103634.jpg'),
(534, 'Mamun', '2025-07-10 10:36:36.088005', 86.15, 'attendance_images/Mamun_20250710103636.jpg'),
(535, 'Mamun', '2025-07-10 10:36:37.216003', 86.52, 'attendance_images/Mamun_20250710103637.jpg'),
(536, 'Mamun', '2025-07-10 10:36:38.657063', 87.38, 'attendance_images/Mamun_20250710103638.jpg'),
(537, 'Mamun', '2025-07-10 10:36:39.775175', 88.3, 'attendance_images/Mamun_20250710103639.jpg'),
(538, 'Mamun', '2025-07-10 10:36:41.063302', 88.08, 'attendance_images/Mamun_20250710103641.jpg'),
(539, 'Mamun', '2025-07-10 10:36:42.183077', 88.39, 'attendance_images/Mamun_20250710103642.jpg'),
(540, 'Mamun', '2025-07-10 10:36:43.323145', 88.5, 'attendance_images/Mamun_20250710103643.jpg'),
(541, 'Mamun', '2025-07-10 10:36:44.432220', 87.99, 'attendance_images/Mamun_20250710103644.jpg'),
(542, 'Mamun', '2025-07-10 10:36:45.507297', 88.27, 'attendance_images/Mamun_20250710103645.jpg'),
(543, 'Mamun', '2025-07-10 10:36:46.719624', 88.82, 'attendance_images/Mamun_20250710103646.jpg'),
(544, 'Mamun', '2025-07-10 10:36:47.856406', 88.15, 'attendance_images/Mamun_20250710103647.jpg'),
(545, 'Mamun', '2025-07-10 10:36:48.963296', 87.77, 'attendance_images/Mamun_20250710103648.jpg'),
(546, 'Mamun', '2025-07-10 10:36:50.150756', 88.67, 'attendance_images/Mamun_20250710103650.jpg'),
(547, 'Mamun', '2025-07-10 10:36:51.212972', 88.63, 'attendance_images/Mamun_20250710103651.jpg'),
(548, 'Mamun', '2025-07-10 10:36:52.341691', 88.16, 'attendance_images/Mamun_20250710103652.jpg'),
(549, 'Mamun', '2025-07-10 10:36:53.479956', 89.51, 'attendance_images/Mamun_20250710103653.jpg'),
(550, 'Mamun', '2025-07-10 10:36:54.603880', 87.18, 'attendance_images/Mamun_20250710103654.jpg'),
(551, 'Mamun', '2025-07-10 10:36:55.873753', 88.28, 'attendance_images/Mamun_20250710103655.jpg'),
(552, 'Mamun', '2025-07-10 10:36:56.986299', 85.8, 'attendance_images/Mamun_20250710103656.jpg'),
(553, 'Mamun', '2025-07-10 10:36:58.180406', 88.68, 'attendance_images/Mamun_20250710103658.jpg'),
(554, 'Mamun', '2025-07-10 10:36:59.260861', 87.35, 'attendance_images/Mamun_20250710103659.jpg'),
(555, 'Mamun', '2025-07-10 10:37:00.455772', 87.61, 'attendance_images/Mamun_20250710103700.jpg'),
(556, 'Mamun', '2025-07-10 10:37:01.704170', 87.1, 'attendance_images/Mamun_20250710103701.jpg'),
(557, 'Mamun', '2025-07-10 10:37:02.787451', 86.91, 'attendance_images/Mamun_20250710103702.jpg'),
(558, 'Mamun', '2025-07-10 10:37:03.921543', 88.39, 'attendance_images/Mamun_20250710103703.jpg'),
(559, 'Mamun', '2025-07-10 10:37:05.089599', 88.2, 'attendance_images/Mamun_20250710103705.jpg'),
(560, 'Mamun', '2025-07-10 10:37:06.230606', 88.44, 'attendance_images/Mamun_20250710103706.jpg'),
(561, 'Mamun', '2025-07-10 10:37:07.488082', 87.83, 'attendance_images/Mamun_20250710103707.jpg'),
(562, 'Mamun', '2025-07-10 10:37:08.812912', 87.46, 'attendance_images/Mamun_20250710103708.jpg'),
(563, 'Mamun', '2025-07-10 10:37:10.104535', 87.35, 'attendance_images/Mamun_20250710103710.jpg'),
(564, 'Mamun', '2025-07-10 10:37:11.268355', 87.73, 'attendance_images/Mamun_20250710103711.jpg'),
(565, 'Mamun', '2025-07-10 10:37:12.433407', 87.07, 'attendance_images/Mamun_20250710103712.jpg'),
(566, 'Mamun', '2025-07-10 10:37:13.591671', 88.43, 'attendance_images/Mamun_20250710103713.jpg'),
(567, 'Mamun', '2025-07-10 10:37:14.720466', 87.63, 'attendance_images/Mamun_20250710103714.jpg'),
(568, 'Mamun', '2025-07-10 10:37:15.986273', 88.07, 'attendance_images/Mamun_20250710103715.jpg'),
(569, 'Mamun', '2025-07-10 10:37:17.185899', 88.64, 'attendance_images/Mamun_20250710103717.jpg'),
(570, 'Mamun', '2025-07-10 10:37:18.356125', 88.73, 'attendance_images/Mamun_20250710103718.jpg'),
(571, 'Mamun', '2025-07-10 10:37:19.547859', 90.03, 'attendance_images/Mamun_20250710103719.jpg'),
(572, 'Mamun', '2025-07-10 10:37:20.695235', 90.49, 'attendance_images/Mamun_20250710103720.jpg'),
(573, 'Mamun', '2025-07-10 10:37:21.889550', 90.97, 'attendance_images/Mamun_20250710103721.jpg'),
(574, 'Mamun', '2025-07-10 10:37:22.953013', 90.65, 'attendance_images/Mamun_20250710103722.jpg'),
(575, 'Mamun', '2025-07-10 10:37:24.138578', 92.22, 'attendance_images/Mamun_20250710103724.jpg'),
(576, 'Mamun', '2025-07-10 10:37:25.146238', 92.44, 'attendance_images/Mamun_20250710103725.jpg'),
(577, 'Mamun', '2025-07-10 10:37:26.417688', 91.59, 'attendance_images/Mamun_20250710103726.jpg'),
(578, 'Mamun', '2025-07-10 10:37:27.641484', 86.36, 'attendance_images/Mamun_20250710103727.jpg'),
(579, 'Mamun', '2025-07-10 10:37:28.844216', 76.98, 'attendance_images/Mamun_20250710103728.jpg'),
(580, 'Mamun', '2025-07-10 10:37:29.936530', 75.52, 'attendance_images/Mamun_20250710103729.jpg'),
(581, 'Mamun', '2025-07-10 10:37:31.188039', 90.06, 'attendance_images/Mamun_20250710103731.jpg'),
(582, 'Mamun', '2025-07-10 10:37:32.193690', 92.09, 'attendance_images/Mamun_20250710103732.jpg'),
(583, 'Mamun', '2025-07-10 10:37:33.232779', 91.46, 'attendance_images/Mamun_20250710103733.jpg'),
(584, 'Mamun', '2025-07-10 10:37:34.375202', 91.61, 'attendance_images/Mamun_20250710103734.jpg'),
(585, 'Mamun', '2025-07-10 10:37:35.492369', 90.76, 'attendance_images/Mamun_20250710103735.jpg'),
(586, 'Mamun', '2025-07-10 10:37:36.717846', 90.43, 'attendance_images/Mamun_20250710103736.jpg'),
(587, 'Mamun', '2025-07-10 10:37:37.944440', 89.87, 'attendance_images/Mamun_20250710103737.jpg'),
(588, 'Mamun', '2025-07-10 10:37:39.077771', 90.47, 'attendance_images/Mamun_20250710103739.jpg'),
(589, 'Mamun', '2025-07-10 10:37:40.206468', 90.45, 'attendance_images/Mamun_20250710103740.jpg'),
(590, 'Mamun', '2025-07-10 10:37:41.228508', 80.81, 'attendance_images/Mamun_20250710103741.jpg'),
(591, 'Mamun', '2025-07-10 10:37:42.374111', 89.41, 'attendance_images/Mamun_20250710103742.jpg'),
(592, 'Mamun', '2025-07-10 10:37:43.392075', 89.81, 'attendance_images/Mamun_20250710103743.jpg'),
(593, 'Mamun', '2025-07-10 10:37:44.513431', 90.14, 'attendance_images/Mamun_20250710103744.jpg'),
(594, 'Mamun', '2025-07-10 10:37:45.611218', 82.52, 'attendance_images/Mamun_20250710103745.jpg'),
(595, 'Mamun', '2025-07-10 10:37:46.836936', 89.24, 'attendance_images/Mamun_20250710103746.jpg'),
(596, 'Mamun', '2025-07-10 10:37:47.884513', 83.25, 'attendance_images/Mamun_20250710103747.jpg'),
(597, 'Mamun', '2025-07-10 10:37:49.168254', 79.49, 'attendance_images/Mamun_20250710103749.jpg'),
(598, 'Mamun', '2025-07-10 10:37:50.219233', 85.31, 'attendance_images/Mamun_20250710103750.jpg'),
(599, 'Mamun', '2025-07-10 10:37:51.325884', 88.71, 'attendance_images/Mamun_20250710103751.jpg'),
(600, 'Mamun', '2025-07-10 10:37:52.448535', 88.71, 'attendance_images/Mamun_20250710103752.jpg'),
(601, 'Mamun', '2025-07-10 10:37:53.675296', 88.77, 'attendance_images/Mamun_20250710103753.jpg'),
(602, 'Mamun', '2025-07-10 10:37:54.981952', 88.9, 'attendance_images/Mamun_20250710103754.jpg'),
(603, 'Mamun', '2025-07-10 10:37:56.312523', 88.77, 'attendance_images/Mamun_20250710103756.jpg'),
(604, 'Mamun', '2025-07-10 10:37:57.375848', 89.05, 'attendance_images/Mamun_20250710103757.jpg'),
(605, 'Mamun', '2025-07-10 10:37:58.687205', 89.4, 'attendance_images/Mamun_20250710103758.jpg'),
(606, 'Mamun', '2025-07-10 10:37:59.691433', 89.45, 'attendance_images/Mamun_20250710103759.jpg'),
(607, 'Mamun', '2025-07-10 10:38:00.904322', 89.75, 'attendance_images/Mamun_20250710103800.jpg'),
(608, 'Mamun', '2025-07-10 10:38:02.115298', 89.04, 'attendance_images/Mamun_20250710103802.jpg'),
(609, 'Mamun', '2025-07-10 10:38:03.308146', 85.47, 'attendance_images/Mamun_20250710103803.jpg'),
(610, 'Mamun', '2025-07-10 10:38:04.590486', 90.61, 'attendance_images/Mamun_20250710103804.jpg'),
(611, 'Mamun', '2025-07-10 10:38:05.867649', 87.97, 'attendance_images/Mamun_20250710103805.jpg'),
(612, 'Mamun', '2025-07-10 10:38:07.100382', 86.36, 'attendance_images/Mamun_20250710103807.jpg'),
(613, 'Mamun', '2025-07-10 10:38:08.219671', 86.87, 'attendance_images/Mamun_20250710103808.jpg'),
(614, 'Mamun', '2025-07-10 10:38:09.418090', 88.37, 'attendance_images/Mamun_20250710103809.jpg'),
(615, 'Mamun', '2025-07-10 10:38:10.571233', 80.75, 'attendance_images/Mamun_20250710103810.jpg'),
(616, 'Mamun', '2025-07-10 10:38:11.888320', 76.83, 'attendance_images/Mamun_20250710103811.jpg'),
(617, 'Mamun', '2025-07-10 10:38:13.207877', 88.81, 'attendance_images/Mamun_20250710103813.jpg'),
(618, 'Mamun', '2025-07-10 10:38:14.450540', 86.84, 'attendance_images/Mamun_20250710103814.jpg'),
(619, 'Mamun', '2025-07-10 10:38:15.652775', 88.88, 'attendance_images/Mamun_20250710103815.jpg'),
(620, 'Mamun', '2025-07-10 10:38:16.896129', 88.04, 'attendance_images/Mamun_20250710103816.jpg'),
(621, 'Mamun', '2025-07-10 10:38:18.071805', 88.97, 'attendance_images/Mamun_20250710103818.jpg'),
(622, 'Mamun', '2025-07-10 10:38:19.217390', 87.13, 'attendance_images/Mamun_20250710103819.jpg'),
(623, 'Mamun', '2025-07-10 10:38:20.448188', 84.48, 'attendance_images/Mamun_20250710103820.jpg'),
(624, 'Mamun', '2025-07-10 10:38:21.622386', 86.96, 'attendance_images/Mamun_20250710103821.jpg'),
(625, 'Mamun', '2025-07-10 10:38:23.203726', 87.64, 'attendance_images/Mamun_20250710103823.jpg'),
(626, 'Mamun', '2025-07-10 10:38:24.497846', 89.03, 'attendance_images/Mamun_20250710103824.jpg'),
(627, 'Mamun', '2025-07-10 10:38:25.805913', 85.8, 'attendance_images/Mamun_20250710103825.jpg'),
(628, 'Mamun', '2025-07-10 10:38:26.939682', 87.41, 'attendance_images/Mamun_20250710103826.jpg'),
(629, 'Mamun', '2025-07-10 10:38:28.003993', 89.99, 'attendance_images/Mamun_20250710103827.jpg'),
(630, 'Mamun', '2025-07-10 10:38:29.137701', 85.65, 'attendance_images/Mamun_20250710103829.jpg'),
(631, 'Mamun', '2025-07-10 10:38:30.197858', 87.43, 'attendance_images/Mamun_20250710103830.jpg'),
(632, 'Mamun', '2025-07-10 10:38:31.409387', 88.77, 'attendance_images/Mamun_20250710103831.jpg'),
(633, 'Mamun', '2025-07-10 10:38:32.593262', 83.55, 'attendance_images/Mamun_20250710103832.jpg'),
(634, 'Mamun', '2025-07-10 10:38:33.921029', 87.47, 'attendance_images/Mamun_20250710103833.jpg'),
(635, 'Mamun', '2025-07-10 10:38:35.131903', 82.76, 'attendance_images/Mamun_20250710103835.jpg'),
(636, 'Mamun', '2025-07-10 10:38:36.222439', 87.36, 'attendance_images/Mamun_20250710103836.jpg'),
(637, 'Mamun', '2025-07-10 10:38:37.373527', 88.71, 'attendance_images/Mamun_20250710103837.jpg'),
(638, 'Mamun', '2025-07-10 10:38:38.548613', 87, 'attendance_images/Mamun_20250710103838.jpg'),
(639, 'Mamun', '2025-07-10 10:38:39.690612', 89.59, 'attendance_images/Mamun_20250710103839.jpg'),
(640, 'Mamun', '2025-07-10 10:38:40.849396', 93.08, 'attendance_images/Mamun_20250710103840.jpg'),
(641, 'Mamun', '2025-07-10 10:38:42.078040', 93.7, 'attendance_images/Mamun_20250710103842.jpg'),
(642, 'Mamun', '2025-07-10 10:38:43.321547', 88.92, 'attendance_images/Mamun_20250710103843.jpg'),
(643, 'Mamun', '2025-07-10 10:38:44.629494', 89.49, 'attendance_images/Mamun_20250710103844.jpg'),
(644, 'Mamun', '2025-07-10 10:38:45.692967', 88.33, 'attendance_images/Mamun_20250710103845.jpg'),
(645, 'Mamun', '2025-07-10 10:38:46.922960', 87.9, 'attendance_images/Mamun_20250710103846.jpg'),
(646, 'Mamun', '2025-07-10 10:38:48.060083', 87.54, 'attendance_images/Mamun_20250710103848.jpg'),
(647, 'Mamun', '2025-07-10 10:38:49.440150', 87.8, 'attendance_images/Mamun_20250710103849.jpg'),
(648, 'Mamun', '2025-07-10 10:38:50.445568', 88.8, 'attendance_images/Mamun_20250710103850.jpg'),
(649, 'Mamun', '2025-07-10 10:38:51.514744', 88.92, 'attendance_images/Mamun_20250710103851.jpg'),
(650, 'Mamun', '2025-07-10 10:38:52.875527', 87.58, 'attendance_images/Mamun_20250710103852.jpg'),
(651, 'Mamun', '2025-07-10 10:38:54.088988', 87.58, 'attendance_images/Mamun_20250710103854.jpg'),
(652, 'Mamun', '2025-07-10 10:38:55.101786', 88.69, 'attendance_images/Mamun_20250710103855.jpg'),
(653, 'Mamun', '2025-07-10 10:38:56.348810', 86.88, 'attendance_images/Mamun_20250710103856.jpg'),
(654, 'Mamun', '2025-07-10 10:38:57.617186', 85.82, 'attendance_images/Mamun_20250710103857.jpg'),
(655, 'Mamun', '2025-07-10 10:38:58.809228', 89.11, 'attendance_images/Mamun_20250710103858.jpg'),
(656, 'Mamun', '2025-07-10 10:39:00.028878', 88.57, 'attendance_images/Mamun_20250710103900.jpg'),
(657, 'Mamun', '2025-07-10 10:39:01.192399', 85.83, 'attendance_images/Mamun_20250710103901.jpg'),
(658, 'Mamun', '2025-07-10 10:39:02.297035', 84.72, 'attendance_images/Mamun_20250710103902.jpg'),
(659, 'Mamun', '2025-07-10 10:39:03.493857', 86.1, 'attendance_images/Mamun_20250710103903.jpg'),
(660, 'Mamun', '2025-07-10 10:39:04.558876', 86.25, 'attendance_images/Mamun_20250710103904.jpg'),
(661, 'Mamun', '2025-07-10 10:39:05.625347', 87.24, 'attendance_images/Mamun_20250710103905.jpg'),
(662, 'Mamun', '2025-07-10 10:39:06.662661', 86, 'attendance_images/Mamun_20250710103906.jpg'),
(663, 'Mamun', '2025-07-10 10:39:07.983517', 85.3, 'attendance_images/Mamun_20250710103907.jpg'),
(664, 'Mamun', '2025-07-10 10:39:09.056586', 85.94, 'attendance_images/Mamun_20250710103909.jpg'),
(665, 'Mamun', '2025-07-10 10:39:10.141173', 87.13, 'attendance_images/Mamun_20250710103910.jpg'),
(666, 'Mamun', '2025-07-10 10:39:11.521379', 88.17, 'attendance_images/Mamun_20250710103911.jpg'),
(667, 'Mamun', '2025-07-10 10:39:12.567154', 88.44, 'attendance_images/Mamun_20250710103912.jpg'),
(668, 'Mamun', '2025-07-10 10:39:13.593090', 88.29, 'attendance_images/Mamun_20250710103913.jpg'),
(669, 'Mamun', '2025-07-10 10:39:14.866738', 84.81, 'attendance_images/Mamun_20250710103914.jpg'),
(670, 'Mamun', '2025-07-10 10:39:16.057510', 87.62, 'attendance_images/Mamun_20250710103916.jpg'),
(671, 'Mamun', '2025-07-10 10:39:17.246555', 86.5, 'attendance_images/Mamun_20250710103917.jpg'),
(672, 'Mamun', '2025-07-10 10:39:18.457812', 88, 'attendance_images/Mamun_20250710103918.jpg'),
(673, 'Mamun', '2025-07-10 10:39:19.642441', 86.37, 'attendance_images/Mamun_20250710103919.jpg'),
(674, 'Mamun', '2025-07-10 10:39:20.693996', 86.31, 'attendance_images/Mamun_20250710103920.jpg'),
(675, 'Mamun', '2025-07-10 10:39:21.769583', 86.89, 'attendance_images/Mamun_20250710103921.jpg'),
(676, 'Mamun', '2025-07-10 10:39:22.906061', 85.99, 'attendance_images/Mamun_20250710103922.jpg'),
(677, 'Mamun', '2025-07-10 10:39:24.022994', 87.54, 'attendance_images/Mamun_20250710103924.jpg'),
(678, 'Mamun', '2025-07-10 10:39:25.328988', 86.43, 'attendance_images/Mamun_20250710103925.jpg'),
(679, 'Mamun', '2025-07-10 10:39:26.434815', 86.78, 'attendance_images/Mamun_20250710103926.jpg'),
(680, 'Mamun', '2025-07-10 10:39:27.457633', 87.27, 'attendance_images/Mamun_20250710103927.jpg'),
(681, 'Mamun', '2025-07-10 10:39:28.725055', 86.09, 'attendance_images/Mamun_20250710103928.jpg'),
(682, 'Mamun', '2025-07-10 10:39:29.962352', 85.23, 'attendance_images/Mamun_20250710103929.jpg'),
(683, 'Mamun', '2025-07-10 10:39:31.343986', 81.74, 'attendance_images/Mamun_20250710103931.jpg'),
(684, 'Mamun', '2025-07-10 10:39:32.545402', 85.46, 'attendance_images/Mamun_20250710103932.jpg'),
(685, 'Mamun', '2025-07-10 10:39:33.786705', 82.56, 'attendance_images/Mamun_20250710103933.jpg'),
(686, 'Mamun', '2025-07-10 10:39:34.967778', 86.52, 'attendance_images/Mamun_20250710103934.jpg'),
(687, 'Mamun', '2025-07-10 10:39:36.175883', 85.71, 'attendance_images/Mamun_20250710103936.jpg'),
(688, 'Mamun', '2025-07-10 10:39:37.870581', 86.86, 'attendance_images/Mamun_20250710103937.jpg'),
(689, 'Mamun', '2025-07-10 10:39:39.096254', 85.46, 'attendance_images/Mamun_20250710103939.jpg'),
(690, 'Mamun', '2025-07-10 10:39:40.244923', 83.97, 'attendance_images/Mamun_20250710103940.jpg'),
(691, 'Mamun', '2025-07-10 10:39:41.507734', 85.08, 'attendance_images/Mamun_20250710103941.jpg'),
(692, 'Mamun', '2025-07-10 10:39:42.744487', 86.29, 'attendance_images/Mamun_20250710103942.jpg'),
(693, 'Mamun', '2025-07-10 10:39:43.874607', 86.46, 'attendance_images/Mamun_20250710103943.jpg'),
(694, 'Mamun', '2025-07-10 10:39:45.075612', 86.76, 'attendance_images/Mamun_20250710103945.jpg'),
(695, 'Mamun', '2025-07-10 10:39:46.270504', 86.37, 'attendance_images/Mamun_20250710103946.jpg'),
(696, 'Mamun', '2025-07-10 10:39:47.474610', 85.32, 'attendance_images/Mamun_20250710103947.jpg'),
(697, 'Mamun', '2025-07-10 10:39:48.659761', 85.6, 'attendance_images/Mamun_20250710103948.jpg'),
(698, 'Mamun', '2025-07-10 10:39:49.947100', 84.71, 'attendance_images/Mamun_20250710103949.jpg'),
(699, 'Mamun', '2025-07-10 10:39:51.192647', 85.62, 'attendance_images/Mamun_20250710103951.jpg'),
(700, 'Mamun', '2025-07-10 10:39:52.201430', 85.45, 'attendance_images/Mamun_20250710103952.jpg'),
(701, 'Mamun', '2025-07-10 10:39:53.462762', 83.71, 'attendance_images/Mamun_20250710103953.jpg'),
(702, 'Mamun', '2025-07-10 10:39:54.703967', 85.48, 'attendance_images/Mamun_20250710103954.jpg'),
(703, 'Mamun', '2025-07-10 10:39:55.964008', 85.75, 'attendance_images/Mamun_20250710103955.jpg'),
(704, 'Mamun', '2025-07-10 10:39:57.251102', 86.4, 'attendance_images/Mamun_20250710103957.jpg'),
(705, 'Mamun', '2025-07-10 10:39:58.567012', 85.76, 'attendance_images/Mamun_20250710103958.jpg'),
(706, 'Mamun', '2025-07-10 10:39:59.843848', 86.96, 'attendance_images/Mamun_20250710103959.jpg'),
(707, 'Mamun', '2025-07-10 10:40:00.960704', 84.84, 'attendance_images/Mamun_20250710104000.jpg'),
(708, 'Mamun', '2025-07-10 10:40:02.132821', 83.98, 'attendance_images/Mamun_20250710104002.jpg'),
(709, 'Mamun', '2025-07-10 10:40:03.454879', 84.69, 'attendance_images/Mamun_20250710104003.jpg'),
(710, 'Mamun', '2025-07-10 10:40:04.582111', 85.84, 'attendance_images/Mamun_20250710104004.jpg'),
(711, 'Mamun', '2025-07-10 10:40:05.709277', 86.46, 'attendance_images/Mamun_20250710104005.jpg'),
(712, 'Mamun', '2025-07-10 10:40:06.775868', 86.24, 'attendance_images/Mamun_20250710104006.jpg'),
(713, 'Mamun', '2025-07-10 10:40:07.838985', 83.61, 'attendance_images/Mamun_20250710104007.jpg'),
(714, 'Mamun', '2025-07-10 10:40:08.895291', 88.02, 'attendance_images/Mamun_20250710104008.jpg'),
(715, 'Mamun', '2025-07-10 10:40:09.951021', 86.49, 'attendance_images/Mamun_20250710104009.jpg'),
(716, 'Mamun', '2025-07-10 10:40:11.028092', 86.97, 'attendance_images/Mamun_20250710104011.jpg'),
(717, 'Mamun', '2025-07-10 10:40:12.143129', 87.7, 'attendance_images/Mamun_20250710104012.jpg'),
(718, 'Mamun', '2025-07-10 10:40:13.244806', 87.6, 'attendance_images/Mamun_20250710104013.jpg'),
(719, 'Mamun', '2025-07-10 10:40:14.394697', 87.28, 'attendance_images/Mamun_20250710104014.jpg'),
(720, 'Mamun', '2025-07-10 10:40:15.482425', 86.5, 'attendance_images/Mamun_20250710104015.jpg'),
(721, 'Mamun', '2025-07-10 10:40:16.670652', 86.02, 'attendance_images/Mamun_20250710104016.jpg'),
(722, 'Mamun', '2025-07-10 10:40:17.787288', 89.5, 'attendance_images/Mamun_20250710104017.jpg'),
(723, 'Mamun', '2025-07-10 10:40:18.847015', 87.19, 'attendance_images/Mamun_20250710104018.jpg'),
(724, 'Mamun', '2025-07-10 10:40:19.931020', 88.39, 'attendance_images/Mamun_20250710104019.jpg'),
(725, 'Mamun', '2025-07-10 10:40:21.109289', 89.18, 'attendance_images/Mamun_20250710104021.jpg'),
(726, 'Mamun', '2025-07-10 10:40:22.304350', 89.27, 'attendance_images/Mamun_20250710104022.jpg'),
(727, 'Mamun', '2025-07-10 10:40:23.448111', 88.8, 'attendance_images/Mamun_20250710104023.jpg'),
(728, 'Mamun', '2025-07-10 10:40:24.623059', 86.99, 'attendance_images/Mamun_20250710104024.jpg'),
(729, 'Mamun', '2025-07-10 10:40:25.907854', 88.62, 'attendance_images/Mamun_20250710104025.jpg'),
(730, 'Mamun', '2025-07-10 10:40:27.158545', 85.01, 'attendance_images/Mamun_20250710104027.jpg'),
(731, 'Mamun', '2025-07-10 10:40:28.411060', 85.93, 'attendance_images/Mamun_20250710104028.jpg'),
(732, 'Mamun', '2025-07-10 10:40:29.537413', 85.54, 'attendance_images/Mamun_20250710104029.jpg'),
(733, 'Mamun', '2025-07-10 10:40:30.668453', 86.21, 'attendance_images/Mamun_20250710104030.jpg'),
(734, 'Mamun', '2025-07-10 10:40:31.726639', 83.95, 'attendance_images/Mamun_20250710104031.jpg'),
(735, 'Mamun', '2025-07-10 10:40:32.862672', 84.96, 'attendance_images/Mamun_20250710104032.jpg'),
(736, 'Mamun', '2025-07-10 10:40:34.046008', 83.83, 'attendance_images/Mamun_20250710104034.jpg'),
(737, 'Mamun', '2025-07-10 10:40:35.121712', 88.16, 'attendance_images/Mamun_20250710104035.jpg'),
(738, 'Mamun', '2025-07-10 10:40:36.269335', 89.78, 'attendance_images/Mamun_20250710104036.jpg'),
(739, 'Mamun', '2025-07-10 10:40:37.465221', 87.75, 'attendance_images/Mamun_20250710104037.jpg'),
(740, 'Mamun', '2025-07-10 10:40:38.714595', 85.02, 'attendance_images/Mamun_20250710104038.jpg'),
(741, 'Mamun', '2025-07-10 10:40:39.899497', 85.33, 'attendance_images/Mamun_20250710104039.jpg'),
(742, 'Mamun', '2025-07-10 10:40:41.036722', 88.17, 'attendance_images/Mamun_20250710104041.jpg'),
(743, 'Mamun', '2025-07-10 10:40:42.400084', 86.38, 'attendance_images/Mamun_20250710104042.jpg'),
(744, 'Mamun', '2025-07-10 10:40:43.482842', 86.96, 'attendance_images/Mamun_20250710104043.jpg'),
(745, 'Mamun', '2025-07-10 10:40:44.613011', 84.18, 'attendance_images/Mamun_20250710104044.jpg'),
(746, 'Mamun', '2025-07-10 10:40:45.755347', 86.16, 'attendance_images/Mamun_20250710104045.jpg'),
(747, 'Mamun', '2025-07-10 10:40:47.067760', 85.55, 'attendance_images/Mamun_20250710104047.jpg'),
(748, 'Mamun', '2025-07-10 10:40:48.307576', 87.37, 'attendance_images/Mamun_20250710104048.jpg'),
(749, 'Mamun', '2025-07-10 10:40:49.463253', 86.54, 'attendance_images/Mamun_20250710104049.jpg'),
(750, 'Mamun', '2025-07-10 10:40:50.517092', 85.18, 'attendance_images/Mamun_20250710104050.jpg'),
(751, 'Mamun', '2025-07-10 10:50:29.776068', 72.99, 'attendance_images/Mamun_20250710105029.jpg'),
(752, 'Mamun', '2025-07-10 10:50:30.904532', 89.6, 'attendance_images/Mamun_20250710105030.jpg'),
(753, 'Mamun', '2025-07-10 10:50:32.041506', 86.97, 'attendance_images/Mamun_20250710105032.jpg'),
(754, 'Mamun', '2025-07-10 10:50:33.218624', 86.12, 'attendance_images/Mamun_20250710105033.jpg'),
(755, 'Mamun', '2025-07-10 10:50:34.335726', 89.25, 'attendance_images/Mamun_20250710105034.jpg'),
(756, 'Mamun', '2025-07-10 10:50:35.507407', 88.66, 'attendance_images/Mamun_20250710105035.jpg'),
(757, 'Mamun', '2025-07-10 10:50:36.674900', 87.35, 'attendance_images/Mamun_20250710105036.jpg'),
(758, 'Mamun', '2025-07-10 10:50:37.833921', 87.42, 'attendance_images/Mamun_20250710105037.jpg'),
(759, 'Mamun', '2025-07-10 10:50:38.864629', 87.96, 'attendance_images/Mamun_20250710105038.jpg'),
(760, 'Mamun', '2025-07-10 10:50:39.901347', 87.28, 'attendance_images/Mamun_20250710105039.jpg'),
(761, 'Mamun', '2025-07-10 10:50:40.945933', 85.88, 'attendance_images/Mamun_20250710105040.jpg'),
(762, 'Mamun', '2025-07-10 10:50:42.015785', 79.78, 'attendance_images/Mamun_20250710105042.jpg'),
(763, 'Mamun', '2025-07-10 10:50:43.053398', 82.59, 'attendance_images/Mamun_20250710105043.jpg'),
(764, 'Mamun', '2025-07-10 10:50:44.107567', 79.55, 'attendance_images/Mamun_20250710105044.jpg'),
(765, 'Mamun', '2025-07-10 10:50:45.151811', 80.29, 'attendance_images/Mamun_20250710105045.jpg'),
(766, 'Mamun', '2025-07-10 10:50:46.236631', 79.9, 'attendance_images/Mamun_20250710105046.jpg'),
(767, 'Mamun', '2025-07-10 10:50:47.302078', 87.99, 'attendance_images/Mamun_20250710105047.jpg'),
(768, 'Mamun', '2025-07-10 10:50:48.384018', 87.34, 'attendance_images/Mamun_20250710105048.jpg'),
(769, 'Mamun', '2025-07-10 10:50:49.418292', 90.96, 'attendance_images/Mamun_20250710105049.jpg'),
(770, 'Mamun', '2025-07-10 10:50:50.453051', 88.68, 'attendance_images/Mamun_20250710105050.jpg'),
(771, 'Mamun', '2025-07-10 10:50:51.563657', 91, 'attendance_images/Mamun_20250710105051.jpg'),
(772, 'Mamun', '2025-07-10 10:50:52.606123', 90.91, 'attendance_images/Mamun_20250710105052.jpg'),
(773, 'Mamun', '2025-07-10 10:50:53.647240', 91.7, 'attendance_images/Mamun_20250710105053.jpg'),
(774, 'Mamun', '2025-07-10 10:50:54.690068', 91.49, 'attendance_images/Mamun_20250710105054.jpg'),
(775, 'Mamun', '2025-07-10 10:50:55.745305', 85.15, 'attendance_images/Mamun_20250710105055.jpg'),
(776, 'Mamun', '2025-07-10 10:50:56.824129', 85.65, 'attendance_images/Mamun_20250710105056.jpg'),
(777, 'Mamun', '2025-07-10 10:50:57.883632', 83.13, 'attendance_images/Mamun_20250710105057.jpg'),
(778, 'Mamun', '2025-07-10 10:50:58.938021', 88.25, 'attendance_images/Mamun_20250710105058.jpg'),
(779, 'Mamun', '2025-07-10 10:51:00.008168', 87.61, 'attendance_images/Mamun_20250710105100.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'admin'),
(4, 'Finance Manager'),
(3, 'HR Manager'),
(2, 'Managing Director');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add attendance', 7, 'add_attendance'),
(26, 'Can change attendance', 7, 'change_attendance'),
(27, 'Can delete attendance', 7, 'delete_attendance'),
(28, 'Can view attendance', 7, 'view_attendance'),
(29, 'Can add leave balance', 8, 'add_leavebalance'),
(30, 'Can change leave balance', 8, 'change_leavebalance'),
(31, 'Can delete leave balance', 8, 'delete_leavebalance'),
(32, 'Can view leave balance', 8, 'view_leavebalance'),
(33, 'Can add leaves', 9, 'add_leaves'),
(34, 'Can change leaves', 9, 'change_leaves'),
(35, 'Can delete leaves', 9, 'delete_leaves'),
(36, 'Can view leaves', 9, 'view_leaves'),
(37, 'Can add document', 10, 'add_document'),
(38, 'Can change document', 10, 'change_document'),
(39, 'Can delete document', 10, 'delete_document'),
(40, 'Can view document', 10, 'view_document'),
(41, 'Can add employee', 11, 'add_employee'),
(42, 'Can change employee', 11, 'change_employee'),
(43, 'Can delete employee', 11, 'delete_employee'),
(44, 'Can view employee', 11, 'view_employee'),
(45, 'Can add travel request', 12, 'add_travelrequest'),
(46, 'Can change travel request', 12, 'change_travelrequest'),
(47, 'Can delete travel request', 12, 'delete_travelrequest'),
(48, 'Can view travel request', 12, 'view_travelrequest'),
(49, 'Can add expense', 13, 'add_expense'),
(50, 'Can change expense', 13, 'change_expense'),
(51, 'Can delete expense', 13, 'delete_expense'),
(52, 'Can view expense', 13, 'view_expense'),
(53, 'Can add reimbursement', 14, 'add_reimbursement'),
(54, 'Can change reimbursement', 14, 'change_reimbursement'),
(55, 'Can delete reimbursement', 14, 'delete_reimbursement'),
(56, 'Can view reimbursement', 14, 'view_reimbursement'),
(57, 'Can add Attendance Record', 15, 'add_attendancerecord'),
(58, 'Can change Attendance Record', 15, 'change_attendancerecord'),
(59, 'Can delete Attendance Record', 15, 'delete_attendancerecord'),
(60, 'Can view Attendance Record', 15, 'view_attendancerecord'),
(61, 'Can add payroll', 16, 'add_payroll'),
(62, 'Can change payroll', 16, 'change_payroll'),
(63, 'Can delete payroll', 16, 'delete_payroll'),
(64, 'Can view payroll', 16, 'view_payroll'),
(65, 'Can add employee input', 17, 'add_employeeinput'),
(66, 'Can change employee input', 17, 'change_employeeinput'),
(67, 'Can delete employee input', 17, 'delete_employeeinput'),
(68, 'Can view employee input', 17, 'view_employeeinput');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$870000$cNHd75WuVVYEc4shrwbVrj$A2S7ihpI28gKaWjw6tma7vEJ2JLKrHRhBL2Sbx1A7iw=', '2025-07-10 10:34:15.806763', 1, 'superadmin', '', '', 'almamun.dev21@gmail.com', 1, 1, '2025-05-06 07:10:39.864876'),
(2, 'pbkdf2_sha256$870000$2pKQsU59d2rbUtEdg2ZftH$MhdUULrPPq2hK9MUrDyAx1wb8uAYufkTaoAbg0waoKo=', NULL, 0, 'raju06', '', '', '', 0, 1, '2025-05-06 08:24:16.496267'),
(3, 'pbkdf2_sha256$870000$9PxhpBVvctfBqc0kiur1MA$BcVMAa7nZy162zpRyedtLXSKjgeVnNkbiM9a3HeHTzU=', '2025-05-06 09:17:41.225367', 0, 'shuvo', 'Md Abdul Monem', 'Shuvo', 'monem@gmail.com', 1, 1, '2025-05-06 09:13:38.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user_user_permissions`
--

INSERT INTO `auth_user_user_permissions` (`id`, `user_id`, `permission_id`) VALUES
(1, 3, 40);

-- --------------------------------------------------------

--
-- Table structure for table `churn_prediction_employeeinput`
--

CREATE TABLE `churn_prediction_employeeinput` (
  `id` bigint(20) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `satisfaction` double NOT NULL,
  `work_hours` int(11) NOT NULL,
  `relationship_satisfaction` double NOT NULL,
  `environment_satisfaction` double NOT NULL,
  `overtime` varchar(5) NOT NULL,
  `education_background` varchar(50) NOT NULL,
  `emp_department` varchar(50) NOT NULL,
  `emp_job_role` varchar(50) NOT NULL,
  `distance_from_home` double NOT NULL,
  `emp_education_level` varchar(10) NOT NULL,
  `emp_job_involvement` double NOT NULL,
  `emp_last_salary_hike_percent` double NOT NULL,
  `total_work_experience_in_years` double NOT NULL,
  `predicted_churn` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `churn_prediction_employeeinput`
--

INSERT INTO `churn_prediction_employeeinput` (`id`, `age`, `gender`, `satisfaction`, `work_hours`, `relationship_satisfaction`, `environment_satisfaction`, `overtime`, `education_background`, `emp_department`, `emp_job_role`, `distance_from_home`, `emp_education_level`, `emp_job_involvement`, `emp_last_salary_hike_percent`, `total_work_experience_in_years`, `predicted_churn`) VALUES
(1, 42, 'Male', 2, 22, 1, 2, 'Yes', 'Medical', 'Research & Development', 'Sales Executive', 100, 'Corrupti', 1, 84, 2014, 1.7);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2025-05-06 08:24:16.793959', '2', 'raju06', 1, '[{\"added\": {}}]', 4, 1),
(2, '2025-05-06 08:25:55.170772', '1', 'raju06 - 2025-05-06 - Present', 1, '[{\"added\": {}}]', 7, 1),
(3, '2025-05-06 08:38:25.070416', '1', 'admin', 1, '[{\"added\": {}}]', 3, 1),
(4, '2025-05-06 08:56:05.963735', '2', 'Managing Director', 1, '[{\"added\": {}}]', 3, 1),
(5, '2025-05-06 08:56:16.218523', '3', 'HR Manager', 1, '[{\"added\": {}}]', 3, 1),
(6, '2025-05-06 08:56:31.085498', '4', 'Finance Manager', 1, '[{\"added\": {}}]', 3, 1),
(7, '2025-05-06 09:08:04.858176', '1', 'Yvonne Schroeder', 1, '[{\"added\": {}}]', 10, 1),
(8, '2025-05-06 09:08:25.937376', '2', 'Harriet Acosta', 1, '[{\"added\": {}}]', 10, 1),
(9, '2025-05-06 09:08:34.443761', '3', 'Felix Lane', 1, '[{\"added\": {}}]', 10, 1),
(10, '2025-05-06 09:13:38.961120', '3', 'shovo', 1, '[{\"added\": {}}]', 4, 1),
(11, '2025-05-06 09:16:05.212919', '3', 'shuvo', 2, '[{\"changed\": {\"fields\": [\"Username\", \"First name\", \"Last name\", \"Email address\", \"User permissions\"]}}]', 4, 1),
(12, '2025-05-06 09:17:25.410364', '3', 'shuvo', 2, '[{\"changed\": {\"fields\": [\"Staff status\"]}}]', 4, 1),
(13, '2025-07-10 10:39:07.723307', '4', 'Nadine Mack', 1, '[{\"added\": {}}]', 10, 1),
(14, '2025-07-10 10:39:59.517110', '1', 'Yvonne Schroeder', 3, '', 10, 1),
(15, '2025-07-12 10:51:49.862143', '1', 'Male - Sales Executive', 1, '[{\"added\": {}}]', 17, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'app', 'attendance'),
(10, 'app', 'document'),
(11, 'app', 'employee'),
(13, 'app', 'expense'),
(8, 'app', 'leavebalance'),
(9, 'app', 'leaves'),
(16, 'app', 'payroll'),
(14, 'app', 'reimbursement'),
(12, 'app', 'travelrequest'),
(15, 'attendance', 'attendancerecord'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(17, 'churn_prediction', 'employeeinput'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-05-06 07:09:16.995446'),
(2, 'auth', '0001_initial', '2025-05-06 07:09:17.258187'),
(3, 'admin', '0001_initial', '2025-05-06 07:09:17.313434'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-05-06 07:09:17.314444'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-05-06 07:09:17.323135'),
(6, 'app', '0001_initial', '2025-05-06 07:09:17.343555'),
(7, 'app', '0002_rename_officialdocument_documents_and_more', '2025-05-06 07:09:17.490405'),
(8, 'app', '0003_rename_documents_document_rename_employees_employee', '2025-05-06 07:09:17.520277'),
(9, 'app', '0004_travelrequest_expense', '2025-05-06 07:09:17.580741'),
(10, 'app', '0005_reimbursement', '2025-05-06 07:09:17.621461'),
(11, 'contenttypes', '0002_remove_content_type_name', '2025-05-06 07:09:17.664335'),
(12, 'auth', '0002_alter_permission_name_max_length', '2025-05-06 07:09:17.692145'),
(13, 'auth', '0003_alter_user_email_max_length', '2025-05-06 07:09:17.719067'),
(14, 'auth', '0004_alter_user_username_opts', '2025-05-06 07:09:17.726660'),
(15, 'auth', '0005_alter_user_last_login_null', '2025-05-06 07:09:17.751536'),
(16, 'auth', '0006_require_contenttypes_0002', '2025-05-06 07:09:17.752537'),
(17, 'auth', '0007_alter_validators_add_error_messages', '2025-05-06 07:09:17.757868'),
(18, 'auth', '0008_alter_user_username_max_length', '2025-05-06 07:09:17.767301'),
(19, 'auth', '0009_alter_user_last_name_max_length', '2025-05-06 07:09:17.796835'),
(20, 'auth', '0010_alter_group_name_max_length', '2025-05-06 07:09:17.817843'),
(21, 'auth', '0011_update_proxy_permissions', '2025-05-06 07:09:17.827841'),
(22, 'auth', '0012_alter_user_first_name_max_length', '2025-05-06 07:09:17.846843'),
(23, 'sessions', '0001_initial', '2025-05-06 07:09:17.872841'),
(24, 'attendance', '0001_initial', '2025-07-03 07:02:21.902229'),
(25, 'app', '0006_payroll', '2025-07-10 10:48:16.282211'),
(26, 'churn_prediction', '0001_initial', '2025-07-12 10:47:46.145586');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('m4rfqaykdcjp6jr461s73jw68ajqvhsc', '.eJxVjDsOwjAQBe_iGlnrX1hT0ucM1tpe4wBypDipEHeHSCmgfTPzXiLQttawdV7ClMVFKHH63SKlB7cd5Du12yzT3NZlinJX5EG7HOfMz-vh_h1U6vVbG1-M0waBFCimxEMukdkpawEMRgaOPlEZ8AzaFsfZa7AICAUQsYj3B-BwN50:1uCF0o:m9qxj148D6DX9IG0StePsNoVjx9siGoUSw41HLRTjL8', '2025-05-20 09:54:54.548609'),
('ojzb5yzpf6eaxxcyz0el8dc9parcbxtv', '.eJxVjDsOwjAQBe_iGlnrX1hT0ucM1tpe4wBypDipEHeHSCmgfTPzXiLQttawdV7ClMVFKHH63SKlB7cd5Du12yzT3NZlinJX5EG7HOfMz-vh_h1U6vVbG1-M0waBFCimxEMukdkpawEMRgaOPlEZ8AzaFsfZa7AICAUQsYj3B-BwN50:1uZobX:g5MzToymOqZIAd18RkO7adca6Y29xxe02H8VbxUHANc', '2025-07-24 10:34:15.808769');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app_attendance`
--
ALTER TABLE `app_attendance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_attendance_employee_id_8e24606c_fk_auth_user_id` (`employee_id`);

--
-- Indexes for table `app_document`
--
ALTER TABLE `app_document`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app_employee`
--
ALTER TABLE `app_employee`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `employee_id` (`employee_id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `phone` (`phone`);

--
-- Indexes for table `app_expense`
--
ALTER TABLE `app_expense`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_expense_travel_request_id_21047f7a_fk_app_travelrequest_id` (`travel_request_id`);

--
-- Indexes for table `app_leavebalance`
--
ALTER TABLE `app_leavebalance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_leavebalance_employee_id_3265f792_fk_auth_user_id` (`employee_id`);

--
-- Indexes for table `app_leaves`
--
ALTER TABLE `app_leaves`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_leaves_employee_id_8a604c77_fk_auth_user_id` (`employee_id`);

--
-- Indexes for table `app_payroll`
--
ALTER TABLE `app_payroll`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_payroll_employee_id_5e2adb4b_fk_app_employee_id` (`employee_id`);

--
-- Indexes for table `app_reimbursement`
--
ALTER TABLE `app_reimbursement`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `expense_id` (`expense_id`);

--
-- Indexes for table `app_travelrequest`
--
ALTER TABLE `app_travelrequest`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_travelrequest_employee_id_e5370e65_fk_auth_user_id` (`employee_id`);

--
-- Indexes for table `attendance_attendancerecord`
--
ALTER TABLE `attendance_attendancerecord`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `churn_prediction_employeeinput`
--
ALTER TABLE `churn_prediction_employeeinput`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app_attendance`
--
ALTER TABLE `app_attendance`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app_document`
--
ALTER TABLE `app_document`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `app_employee`
--
ALTER TABLE `app_employee`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_expense`
--
ALTER TABLE `app_expense`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_leavebalance`
--
ALTER TABLE `app_leavebalance`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_leaves`
--
ALTER TABLE `app_leaves`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_payroll`
--
ALTER TABLE `app_payroll`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_reimbursement`
--
ALTER TABLE `app_reimbursement`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_travelrequest`
--
ALTER TABLE `app_travelrequest`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `attendance_attendancerecord`
--
ALTER TABLE `attendance_attendancerecord`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=780;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `churn_prediction_employeeinput`
--
ALTER TABLE `churn_prediction_employeeinput`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `app_attendance`
--
ALTER TABLE `app_attendance`
  ADD CONSTRAINT `app_attendance_employee_id_8e24606c_fk_auth_user_id` FOREIGN KEY (`employee_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `app_expense`
--
ALTER TABLE `app_expense`
  ADD CONSTRAINT `app_expense_travel_request_id_21047f7a_fk_app_travelrequest_id` FOREIGN KEY (`travel_request_id`) REFERENCES `app_travelrequest` (`id`);

--
-- Constraints for table `app_leavebalance`
--
ALTER TABLE `app_leavebalance`
  ADD CONSTRAINT `app_leavebalance_employee_id_3265f792_fk_auth_user_id` FOREIGN KEY (`employee_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `app_leaves`
--
ALTER TABLE `app_leaves`
  ADD CONSTRAINT `app_leaves_employee_id_8a604c77_fk_auth_user_id` FOREIGN KEY (`employee_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `app_payroll`
--
ALTER TABLE `app_payroll`
  ADD CONSTRAINT `app_payroll_employee_id_5e2adb4b_fk_app_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `app_employee` (`id`);

--
-- Constraints for table `app_reimbursement`
--
ALTER TABLE `app_reimbursement`
  ADD CONSTRAINT `app_reimbursement_expense_id_74a1a88c_fk_app_expense_id` FOREIGN KEY (`expense_id`) REFERENCES `app_expense` (`id`);

--
-- Constraints for table `app_travelrequest`
--
ALTER TABLE `app_travelrequest`
  ADD CONSTRAINT `app_travelrequest_employee_id_e5370e65_fk_auth_user_id` FOREIGN KEY (`employee_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
