CREATE TABLE `(용어 북마크)` (
	`Key` int NOT NULL,
	`user_id` varchar NOT NULL,
	`Key2` int NOT NULL,
	`Field` varchar NULL,
	`Field2` date NULL
);

CREATE TABLE `(경제 용어 사전)` (
	`Key` int NOT NULL,
	`Field` varchar NULL,
	`Field2` varchar NULL,
	`Field3` varchar NULL,
	`Field4` date NULL
);

CREATE TABLE `(권한 역할)` (
	`role_id` int NOT NULL,
	`role_key` varchar NULL
);

CREATE TABLE `(회원 권한 매핑)` (
	`user_role_id` int NOT NULL,
	`role_id` int NOT NULL,
	`user_id` varchar NOT NULL
);

CREATE TABLE `(페이지 이동 로그)` (
	`Key` int NOT NULL,
	`user_id` varchar NOT NULL,
	`Field` varchar NULL,
	`Field2` varchar NULL,
	`Field3` date NULL
);

CREATE TABLE `(키워드 클릭 로그)` (
	`Key` int NOT NULL,
	`user_id` varchar NOT NULL,
	`Field3` date NULL,
	`Field` int NULL
);

CREATE TABLE `(처리 상태 코드)` (
	`Key` int NOT NULL,
	`Field` varchar NULL,
	`Field2` varchar NULL
);

CREATE TABLE `(인사이트 기사 열람 로그)` (
	`Key` int NOT NULL,
	`user_id` varchar NOT NULL,
	`Field` varchar NULL,
	`Field2` date NULL,
	`Field3` int NULL
);

CREATE TABLE `(배치 실행 요약)` (
	`Key` int NOT NULL,
	`Field` varchar NULL,
	`Field2` date NULL,
	`Field3` date NULL,
	`Key2` int NOT NULL,
	`Field4` varchar NULL,
	`Field5` date NULL
);

CREATE TABLE `(회원)` (
	`user_id` varchar NOT NULL,
	`password_hash` varchar NULL,
	`email` varchar NULL,
	`name` varchar NULL,
	`birthday` date NULL,
	`phone` varchar NULL,
	`eco_state` varchar NULL,
	`gender` varchar NULL,
	`created_at` date NULL,
	`last_login_at` date NULL
);

CREATE TABLE `(로그인 시도 로그)` (
	`Key` int NOT NULL,
	`user_id` varchar NOT NULL,
	`Field` boolean NULL,
	`Field2` date NULL
);

ALTER TABLE `(용어 북마크)` ADD CONSTRAINT `PK_(용어 북마크)` PRIMARY KEY (
	`Key`
);

ALTER TABLE `(경제 용어 사전)` ADD CONSTRAINT `PK_(경제 용어 사전)` PRIMARY KEY (
	`Key`
);

ALTER TABLE `(권한 역할)` ADD CONSTRAINT `PK_(권한 역할)` PRIMARY KEY (
	`role_id`
);

ALTER TABLE `(회원 권한 매핑)` ADD CONSTRAINT `PK_(회원 권한 매핑)` PRIMARY KEY (
	`user_role_id`
);

ALTER TABLE `(페이지 이동 로그)` ADD CONSTRAINT `PK_(페이지 이동 로그)` PRIMARY KEY (
	`Key`
);

ALTER TABLE `(키워드 클릭 로그)` ADD CONSTRAINT `PK_(키워드 클릭 로그)` PRIMARY KEY (
	`Key`
);

ALTER TABLE `(처리 상태 코드)` ADD CONSTRAINT `PK_(처리 상태 코드)` PRIMARY KEY (
	`Key`
);

ALTER TABLE `(인사이트 기사 열람 로그)` ADD CONSTRAINT `PK_(인사이트 기사 열람 로그)` PRIMARY KEY (
	`Key`
);

ALTER TABLE `(배치 실행 요약)` ADD CONSTRAINT `PK_(배치 실행 요약)` PRIMARY KEY (
	`Key`
);

ALTER TABLE `(회원)` ADD CONSTRAINT `PK_(회원)` PRIMARY KEY (
	`user_id`
);

ALTER TABLE `(로그인 시도 로그)` ADD CONSTRAINT `PK_(로그인 시도 로그)` PRIMARY KEY (
	`Key`
);
