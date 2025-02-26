-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: economy
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `government_finance`
--

DROP TABLE IF EXISTS `government_finance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `government_finance` (
  `Country_Id` varchar(10) NOT NULL,
  `Financial_Year` int NOT NULL,
  `General_Government_Revenue` decimal(15,4) DEFAULT NULL,
  `General_Government_Total_Expenditure` decimal(15,4) DEFAULT NULL,
  `General_Government_Gross_Debt` decimal(15,4) DEFAULT NULL,
  PRIMARY KEY (`Country_Id`,`Financial_Year`),
  CONSTRAINT `government_finance_ibfk_1` FOREIGN KEY (`Country_Id`) REFERENCES `country` (`Country_Id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `government_finance`
--

LOCK TABLES `government_finance` WRITE;
/*!40000 ALTER TABLE `government_finance` DISABLE KEYS */;
INSERT INTO `government_finance` VALUES ('AR',2018,4940.7000,5742.9900,12569.4100),('AR',2019,7261.8100,8220.0300,19368.0400),('AR',2020,9198.3200,11558.5200,28248.0900),('AR',2021,15506.6900,17509.3400,37457.2200),('AR',2022,27580.4000,30784.3600,69811.0500),('BD',2018,2344.1500,3417.9200,7799.7500),('BD',2019,2403.6300,3999.8300,9430.2200),('BD',2020,2684.6800,4219.3300,10941.1000),('BD',2021,3304.9200,4577.6800,12572.5600),('BD',2022,3470.4800,4998.8900,15524.6200),('BG',2018,37.8650,37.7300,22.0660),('BG',2019,42.0130,43.1650,22.0410),('BG',2020,42.0280,45.5590,27.9530),('BG',2021,49.7450,53.6550,31.6340),('BG',2022,61.8990,63.2460,36.1260),('BR',2018,2478.2800,2965.7500,5998.5000),('BR',2019,2704.9000,3134.0100,6492.8400),('BR',2020,2563.1900,3576.6000,7369.1600),('BR',2021,3281.1900,3663.9100,8073.0800),('BR',2022,3841.8600,4295.4700,8517.8400),('BS',2018,2.0420,2.4570,7.7730),('BS',2019,2.4260,2.6460,7.8720),('BS',2020,2.0820,2.9210,8.4840),('BS',2021,1.9090,3.2440,10.1670),('BS',2022,2.6090,3.3270,10.9910),('BT',2018,52.1130,54.7370,185.3120),('BT',2019,42.0330,44.7770,184.1750),('BT',2020,54.6040,57.9890,215.3700),('BT',2021,59.6960,70.8360,238.3990),('BT',2022,54.3550,69.3870,248.5710),('BY',2018,48.4990,46.2910,58.1200),('BY',2019,51.5530,50.3270,55.2390),('BY',2020,52.6640,56.9620,71.1070),('BY',2021,61.2340,64.1750,71.3080),('BY',2022,61.8440,71.2510,76.9220),('CD',2018,8478.5500,8510.3800,11517.8400),('CD',2019,8999.5100,10638.1100,12450.5000),('CD',2020,8071.9800,9355.6400,15036.6200),('CD',2021,15485.3300,16444.6300,18326.9600),('CD',2022,21714.1900,23698.0700,18421.2900),('CL',2018,45717.1500,48525.0000,48870.4600),('CL',2019,46471.5400,51810.5500,55393.4400),('CL',2020,44263.2500,58541.2900,65167.4600),('CL',2021,62468.7700,80468.6200,87262.7800),('CL',2022,73240.9800,69737.7600,99724.6400),('CN',2018,26551.4600,30474.1700,51887.1000),('CN',2019,27790.0900,33835.2800,59842.3600),('CN',2020,26342.8700,36310.0500,71934.9800),('CN',2021,30511.6500,37434.9300,82272.5200),('CN',2022,31140.3700,40339.0700,94013.3800),('CO',2018,296240.9100,342347.5600,529298.8700),('CO',2019,311629.0800,348538.2900,555485.7500),('CO',2020,265397.5900,335057.8300,655736.4100),('CO',2021,324591.2000,410747.6500,763753.3300),('CO',2022,403479.1000,501196.2100,931406.7900),('CR',2018,4766.5100,6830.1800,18669.8300),('CR',2019,5675.6600,8222.6100,21346.9700),('CR',2020,5077.3700,8146.6100,24419.5200),('CR',2021,6326.2100,8378.7000,27271.9900),('CR',2022,7341.1800,8563.8500,28223.5200),('GH',2018,43.5230,64.4800,191.2510),('GH',2019,53.3800,80.1890,208.0220),('GH',2020,55.1380,123.5040,283.5200),('GH',2021,70.0970,125.6360,365.4730),('GH',2022,96.1630,157.2390,546.1460),('HU',2018,19107.0500,20023.5000,29970.6800),('HU',2019,20983.2400,21951.4400,31139.2500),('HU',2020,21081.6600,24730.0700,38388.6900),('HU',2021,22752.9200,26690.9000,42351.5300),('HU',2022,27336.1100,31125.6500,47550.8300),('ID',2018,2209495.3700,2477417.7400,4514353.6900),('ID',2019,2244258.7600,2586436.2300,4839007.0100),('ID',2020,1924434.5500,2865856.1700,6138288.9900),('ID',2021,2315466.3900,3086211.6700,6984287.7100),('ID',2022,2977287.5200,3435854.9200,7822402.2400),('IN',2018,37708.3400,49758.4200,133039.2100),('IN',2019,38501.9200,53969.7700,150858.1400),('IN',2020,36044.7800,61585.9200,175563.0700),('IN',2021,46190.5100,68829.8400,198762.1300),('IN',2022,52276.9500,78400.1600,226324.5900),('KE',2018,1638.6100,2283.9000,5272.5000),('KE',2019,1740.4300,2498.0000,6048.9300),('KE',2020,1785.9400,2657.1200,7269.1900),('KE',2021,2022.9600,2886.7400,8101.8800),('KE',2022,2384.8300,3211.2500,9287.6500),('LK',2018,1932.4600,2693.2300,12831.9100),('LK',2019,1898.8100,3095.1900,13141.5200),('LK',2020,1373.3100,3283.7000,15158.2600),('LK',2021,1463.8100,3521.7400,18082.3800),('LK',2022,2012.1800,4472.5500,27871.8800),('LR',2018,0.9130,1.0660,1.2110),('LR',2019,0.8440,0.9950,1.4950),('LR',2020,0.9500,1.0660,1.7810),('LR',2021,0.9570,1.0420,1.8690),('LR',2022,0.9120,1.1870,2.2000),('MD',2018,57.9960,59.6090,60.1210),('MD',2019,62.9490,65.9720,59.3850),('MD',2020,62.6550,73.2750,73.1690),('MD',2021,77.3780,83.7140,80.0460),('MD',2022,91.4810,100.3740,91.4900),('MG',2018,5971.2900,6585.1700,19681.9100),('MG',2019,7114.6900,7839.7900,20901.6600),('MG',2020,6129.1500,8085.2300,25299.7000),('MG',2021,6248.5800,7803.0500,29167.4100),('MG',2022,8466.7700,12687.1900,35558.1900),('MU',2018,110.6650,121.6040,325.2070),('MU',2019,103.8730,142.4530,387.1780),('MU',2020,98.7110,146.4010,432.1770),('MU',2021,126.2430,147.5200,464.4490),('MU',2022,144.8570,164.4000,491.1950),('MX',2018,5519.8100,6036.8500,12620.6200),('MX',2019,5777.2700,6346.5300,13038.7200),('MX',2020,5658.6400,6691.9800,14084.2500),('MX',2021,6121.9400,7121.9300,15139.4300),('MX',2022,7341.9900,8602.9100,15946.9100),('MY',2018,291.8000,330.0880,805.6200),('MY',2019,326.2500,356.6530,863.5090),('MY',2020,285.8680,355.3360,960.2200),('MY',2021,287.5950,376.7900,1071.1100),('MY',2022,339.2240,434.0010,1184.9400),('NA',2018,56.5570,65.7810,91.2600),('NA',2019,57.8490,67.8000,107.5770),('NA',2020,58.2090,72.2710,116.0390),('NA',2021,56.0500,72.0910,130.9550),('NA',2022,60.7100,75.3690,143.9800),('NG',2018,10978.4800,16548.5600,35743.2200),('NG',2019,11406.7700,18237.8100,42483.6300),('NG',2020,10027.6200,18635.1100,53195.3700),('NG',2021,12871.8000,23487.3600,64284.3600),('NG',2022,17786.6900,28878.2800,76933.7700),('NP',2018,766.0360,967.6340,1074.3800),('NP',2019,862.5610,1055.0100,1313.2000),('NP',2020,865.0310,1073.6200,1684.1000),('NP',2021,1012.7900,1186.0000,1884.0000),('NP',2022,1139.0000,1299.1900,2126.4900),('PE',2018,143.7850,158.6010,193.9670),('PE',2019,153.4580,163.9730,208.7590),('PE',2020,128.3650,193.2620,251.6980),('PE',2021,184.1290,206.4450,318.7110),('PE',2022,206.8810,219.4660,317.1760),('PL',2018,876.0060,881.1990,1035.7200),('PL',2019,941.0180,957.9070,1045.8700),('PL',2020,966.0170,1127.6900,1336.5600),('PL',2021,1109.9900,1158.1700,1410.4900),('PL',2022,1257.7400,1353.0900,1520.8900),('PY',2018,43938.3900,47490.5400,51489.1400),('PY',2019,45471.4800,54346.2600,60987.8600),('PY',2020,44849.3400,62022.2500,88526.3400),('PY',2021,50714.0200,67115.7500,101488.9900),('PY',2022,58174.5100,71113.7200,117818.5100),('RO',2018,278.0310,304.3030,347.0760),('RO',2019,305.8830,354.3550,389.6620),('RO',2020,305.2960,407.3260,526.8960),('RO',2021,361.7200,441.6550,606.8310),('RO',2022,437.6520,519.0870,688.2660),('RS',2018,2105.2400,2064.0900,2704.1100),('RS',2019,2278.5300,2278.7800,2803.6800),('RS',2020,2254.9600,2653.4400,3131.3700),('RS',2021,2711.9300,2919.4500,3527.3700),('RS',2022,3075.7800,3086.3100,3796.3400),('SV',2018,6.3900,7.0940,18.3070),('SV',2019,6.4880,7.3140,19.1740),('SV',2020,6.1100,8.1280,21.9600),('SV',2021,7.5940,9.2010,23.6900),('SV',2022,8.3720,9.1640,24.4110),('TH',2018,3462.5700,3452.2100,6780.9500),('TH',2019,3530.9300,3668.0000,6901.8000),('TH',2020,3276.1000,4023.7700,7848.1600),('TH',2021,3235.0100,4359.1700,9337.5400),('TH',2022,3437.0200,4383.7800,10373.9400),('TY',2018,1158.5700,1300.8900,1130.0900),('TY',2019,1334.9400,1539.9800,1406.4200),('TY',2020,1456.6300,1715.2000,2001.6400),('TY',2021,1975.2900,2262.0400,3030.2400),('TY',2022,3962.7000,4208.1100,4678.7700),('UA',2018,1416.9200,1492.5300,2148.7200),('UA',2019,1567.8400,1650.6500,2006.6300),('UA',2020,1675.3900,1925.2500,2554.6900),('UA',2021,1982.6800,2198.3300,2666.5300),('UA',2022,2608.6800,3426.0700,4002.9600),('VN',2018,1363869.0100,1435435.0000,3049894.0400),('VN',2019,1496315.4000,1526893.0000,3144533.0100),('VN',2020,1479360.8100,1709524.0000,3319350.3400),('VN',2021,1563805.0000,1854940.0000,3333329.6000),('VN',2022,1737779.7100,1973349.8000,3528617.4400),('XK',2018,1.7750,1.9660,1.1430),('XK',2019,1.9050,2.1110,1.2470),('XK',2020,1.7360,2.2700,1.5230),('XK',2021,2.2090,2.3110,1.7170),('XK',2022,2.4830,2.5330,1.7230),('ZM',2018,53.4500,76.3130,207.0120),('ZM',2019,61.3310,89.5950,283.7020),('ZM',2020,67.4370,113.2270,465.8120),('ZM',2021,98.9450,134.9290,NULL),('ZM',2022,100.6840,138.6870,NULL),('ZW',2018,5.4910,7.4970,18.8420),('ZW',2019,22.9710,24.8400,174.6990),('ZW',2020,183.0390,172.6850,1164.3600),('ZW',2021,489.5920,558.3440,1905.2100),('ZW',2022,2056.7500,2329.1500,11964.9600);
/*!40000 ALTER TABLE `government_finance` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-21 15:13:27
