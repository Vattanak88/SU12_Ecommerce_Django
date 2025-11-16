-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

USE `ecommerceforfinal`;

-- Dumping data for table ecommerceforfinal.auth_permission
INSERT IGNORE INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
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
    (25, 'Can add address', 7, 'add_address'),
    (26, 'Can change address', 7, 'change_address'),
    (27, 'Can delete address', 7, 'delete_address'),
    (28, 'Can view address', 7, 'view_address'),
    (29, 'Can add cart', 8, 'add_cart'),
    (30, 'Can change cart', 8, 'change_cart'),
    (31, 'Can delete cart', 8, 'delete_cart'),
    (32, 'Can view cart', 8, 'view_cart'),
    (33, 'Can add category', 9, 'add_category'),
    (34, 'Can change category', 9, 'change_category'),
    (35, 'Can delete category', 9, 'delete_category'),
    (36, 'Can view category', 9, 'view_category'),
    (37, 'Can add feature', 10, 'add_feature'),
    (38, 'Can change feature', 10, 'change_feature'),
    (39, 'Can delete feature', 10, 'delete_feature'),
    (40, 'Can view feature', 10, 'view_feature'),
    (41, 'Can add order detail', 11, 'add_orderdetail'),
    (42, 'Can change order detail', 11, 'change_orderdetail'),
    (43, 'Can delete order detail', 11, 'delete_orderdetail'),
    (44, 'Can view order detail', 11, 'view_orderdetail'),
    (45, 'Can add slider', 12, 'add_slider'),
    (46, 'Can change slider', 12, 'change_slider'),
    (47, 'Can delete slider', 12, 'delete_slider'),
    (48, 'Can view slider', 12, 'view_slider'),
    (49, 'Can add checkout', 13, 'add_checkout'),
    (50, 'Can change checkout', 13, 'change_checkout'),
    (51, 'Can delete checkout', 13, 'delete_checkout'),
    (52, 'Can view checkout', 13, 'view_checkout'),
    (53, 'Can add order', 14, 'add_order'),
    (54, 'Can change order', 14, 'change_order'),
    (55, 'Can delete order', 14, 'delete_order'),
    (56, 'Can view order', 14, 'view_order'),
    (57, 'Can add payment', 15, 'add_payment'),
    (58, 'Can change payment', 15, 'change_payment'),
    (59, 'Can delete payment', 15, 'delete_payment'),
    (60, 'Can view payment', 15, 'view_payment'),
    (61, 'Can add product', 16, 'add_product'),
    (62, 'Can change product', 16, 'change_product'),
    (63, 'Can delete product', 16, 'delete_product'),
    (64, 'Can view product', 16, 'view_product'),
    (65, 'Can add cart checkout', 17, 'add_cartcheckout'),
    (66, 'Can change cart checkout', 17, 'change_cartcheckout'),
    (67, 'Can delete cart checkout', 17, 'delete_cartcheckout'),
    (68, 'Can view cart checkout', 17, 'view_cartcheckout');

-- Dumping data for table ecommerceforfinal.django_content_type
INSERT IGNORE INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
    (1, 'admin', 'logentry'),
    (3, 'auth', 'group'),
    (2, 'auth', 'permission'),
    (4, 'auth', 'user'),
    (5, 'contenttypes', 'contenttype'),
    (7, 'Home', 'address'),
    (8, 'Home', 'cart'),
    (17, 'Home', 'cartcheckout'),
    (9, 'Home', 'category'),
    (13, 'Home', 'checkout'),
    (10, 'Home', 'feature'),
    (14, 'Home', 'order'),
    (11, 'Home', 'orderdetail'),
    (15, 'Home', 'payment'),
    (16, 'Home', 'product'),
    (12, 'Home', 'slider'),
    (6, 'sessions', 'session');

-- Dumping data for table ecommerceforfinal.django_migrations
INSERT IGNORE INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
    (1, 'Home', '0001_initial', '2025-10-27 07:49:37.390361'),
    (2, 'contenttypes', '0001_initial', '2025-10-27 07:49:37.420046'),
    (3, 'auth', '0001_initial', '2025-10-27 07:49:37.788478'),
    (4, 'admin', '0001_initial', '2025-10-27 07:49:37.877673'),
    (5, 'admin', '0002_logentry_remove_auto_add', '2025-10-27 07:49:37.886750'),
    (6, 'admin', '0003_logentry_add_action_flag_choices', '2025-10-27 07:49:37.893087'),
    (7, 'contenttypes', '0002_remove_content_type_name', '2025-10-27 07:49:37.950970'),
    (8, 'auth', '0002_alter_permission_name_max_length', '2025-10-27 07:49:37.995671'),
    (9, 'auth', '0003_alter_user_email_max_length', '2025-10-27 07:49:38.018400'),
    (10, 'auth', '0004_alter_user_username_opts', '2025-10-27 07:49:38.025462'),
    (11, 'auth', '0005_alter_user_last_login_null', '2025-10-27 07:49:38.068067'),
    (12, 'auth', '0006_require_contenttypes_0002', '2025-10-27 07:49:38.071284'),
    (13, 'auth', '0007_alter_validators_add_error_messages', '2025-10-27 07:49:38.077731'),
    (14, 'auth', '0008_alter_user_username_max_length', '2025-10-27 07:49:38.123162'),
    (15, 'auth', '0009_alter_user_last_name_max_length', '2025-10-27 07:49:38.170285'),
    (16, 'auth', '0010_alter_group_name_max_length', '2025-10-27 07:49:38.187068'),
    (17, 'auth', '0011_update_proxy_permissions', '2025-10-27 07:49:38.198568'),
    (18, 'auth', '0012_alter_user_first_name_max_length', '2025-10-27 07:49:38.244571'),
    (19, 'sessions', '0001_initial', '2025-10-27 07:49:38.277996'),
    (20, 'Home', '0002_alter_checkout_currency', '2025-10-28 15:50:33.925927'),
    (21, 'Home', '0003_remove_cart_checkout', '2025-10-28 16:32:42.807385'),
    (22, 'Home', '0004_remove_checkout_cart_cart_checkout', '2025-10-28 16:33:37.612882'),
    (23, 'Home', '0005_remove_cart_checkout', '2025-10-28 16:34:09.933710'),
    (24, 'Home', '0006_checkout_cart', '2025-10-28 16:34:50.725324'),
    (25, 'Home', '0007_remove_checkout_cart_cartcheckout', '2025-10-28 16:45:25.367705'),
    (26, 'Home', '0008_remove_cartcheckout_cart_and_more', '2025-10-28 16:48:13.910258'),
    (27, 'Home', '0009_remove_order_order_details_order_orderdetail', '2025-10-28 16:53:14.327512'),
    (28, 'Home', '0010_cart_disable', '2025-10-29 02:07:15.053520'),
    (29, 'Home', '0011_remove_cart_disable', '2025-10-29 02:13:22.869316'),
    (30, 'Home', '0012_remove_payment_address_order_address', '2025-11-01 04:44:43.728057'),
    (31, 'Home', '0013_address_instructions', '2025-11-01 04:49:41.531517'),
    (32, 'Home', '0014_remove_order_address_delete_address', '2025-11-02 07:56:14.629769'),
    (33, 'Home', '0015_cart_disabled', '2025-11-02 09:08:21.290489');

-- Dumping data for table ecommerceforfinal.django_session
INSERT IGNORE INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
    ('19fumtw8fqm7wadfk6v3ay48c99ojs0z', '.eJyFjs0OgjAQhF_F7JkYyp_C3WiiYqInT83absVIWyz1QAjvbkm4e9udmd1vRrBOkuMSPUI1gkFNUAFE0DXWzCMr2TYJO0rpqO-D4vFNFqYIPo4LK2m-0zIPjiwTkWyRiVSmZaE2GeYZI6EQKVGPcn7jrceWdzhoMh6qIo4jEF_nyIiB-6GbkcfDNSQ1OdGg8XzpdN7V-9XtUp_uwVSvlhb9H3TdmSdM0w9Sn0ih:1vI0a5:Icl1qozFr7zEcQtAFa1GNSWAo29iJ5wQQjOW82xoGTs', '2025-11-23 08:15:25.831536'),
    ('98k995n1c6xkm6gficwig0hax1qftj1g', '.eJyFjbEKwjAURX9F3lwkpkZj9qKgVtDJKcSXFxWaNIY4hNJ_t4K767mHewZ4JY29JVADeCtAwUoupFgyJtAQ2dpJJmrnbsTRSbFZc6gg99l0OpriKWRQnLEK8J0SBSw6lzi9wX53nkxPCR8mZB2M_9Jj025nl1N7uE6je3b04_-i8xjuMI4fcPE1iA:1vIKkP:DY01_pBeJSuVuxnClm5H50RyYv8LQ0IHmPmr3vj7SXQ', '2025-11-24 05:47:25.423298'),
    ('9gcotfkcwlfj8i2t61pywim8fcj8mzke', '.eJyFzbEOwiAYBOBXMf9sGtoIQmeNi9ahcXAiFH6qSaFIcCBN311M3F2_y90t8IpSzwahXcAZCi3wveWoB4KCcVGzoVG2Joxqi6JhhlDYQpqTmmRQ2aFPpUIqsius3zGi11mmHMog3PpDUYdRP5RP0iv31cuxO236a3e-l9A-J_z5v98q-BHW9QP04zYN:1vFRNh:Rr2fizHdk5Zl8cKi1axXhbDv4d4OiUF8AL9RzDygjSM', '2025-11-16 06:16:01.427939'),
    ('ybxc4hevt0otb0ph64nt8s8mwvsku0f9', '.eJyFjb0KwjAYRV9FvrlIDG2N2QKCglShxcEp5FeFJo0hDqH03Y3g7nru4Z4ZXpGrSRugMzjdAAVEpDA7hATRxMq62cp60yKsMbEYt1pDBWlKYuRBZGd8AooRqkC9YzReZZ5yKG9wOvbFdCaqh_CJe-G-dLhezofVwLqO9Wx_K4Z9juY3_iuvg7_DsnwAfxo20w:1vIfJq:GptuFpuavWuvkSkjjIrPUKXDh68ECdOFp3n11DVJ4Sc', '2025-11-25 03:45:22.251289');

-- Dumping data for table ecommerceforfinal.Home_cart
INSERT IGNORE INTO `Home_cart` (`id`, `name`, `image`, `qty`, `price`, `status`, `product_id`, `disabled`) VALUES
    (49, 'Regular Stripped Shirt', 'ZD__4559.jpg', 1, 0.03, 0, 34, 0),
    (50, 'Mini Polo Dresses', 'ZD__3880.jpg', 1, 0.03, 0, 40, 0),
    (51, 'Cropped Fitted T-Shirts', 'ZANDO30.06.20250663.jpg', 1, 0.03, 1, 31, 0);

-- Dumping data for table ecommerceforfinal.Home_cartcheckout
INSERT IGNORE INTO `Home_cartcheckout` (`id`, `cart_id`, `checkout_id`) VALUES
    (686, 51, 679),
    (687, 51, 680);

-- Dumping data for table ecommerceforfinal.Home_category
INSERT IGNORE INTO `Home_category` (`id`, `name`) VALUES
    (7, 'Hoodies'),
    (4, 'Jackets'),
    (2, 'Jeans'),
    (6, 'Pants'),
    (5, 'Shirts'),
    (8, 'Shorts'),
    (3, 'Sweaters'),
    (1, 'T-Shirts');

-- Dumping data for table ecommerceforfinal.Home_feature
INSERT IGNORE INTO `Home_feature` (`id`, `title`, `image`) VALUES
    (1, 'Regular Wrap Shirts', '7_lc5kla.jpg'),
    (2, 'Bubble Hem Mini Skirts', '8_mapllr.jpg'),
    (3, 'Mini Skirts', '9_b8oq2u.jpg'),
    (4, 'Tube Top', '11_wlhpor.jpg');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
