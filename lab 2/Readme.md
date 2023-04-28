# lab2

## run instructions

- install mysql connector using pip command
  `pip install mysql-connector-python`

- add table structure to database

  `
--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `salary` float NOT NULL,
  `age` int NOT NULL,
  `department` varchar(255) NOT NULL,
  `managed_department` varchar(255) DEFAULT NULL,
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
  `


- add database config to config.py file

- run app.py
  `python3 app.py`