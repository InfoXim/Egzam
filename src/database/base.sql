create table Users(
	id integer PRIMARY KEY autoincrement,
    login varchar(16) not null unique,
    password varchar(16) not null,
    power_level integer
);

create table Applications(
	id integer PRIMARY KEY autoincrement,
    Application_number varchar(50),
    Date_added integer,
    Fault_type varchar(50),
    Description_problem varchar(50),
    id_cars integer,
    id_client integer,
    id_application_status integer
);

create table Cars(
	id integer PRIMARY KEY autoincrement,
    brand varchar(50),
    Model integer,
);

create table client(
    id     integer PRIMARY KEY autoincrement,
    name varchar(50),
    fio varchar(50),
    phone integer,
    Email integer
);

create table Application_statuses(
    id     integer PRIMARY KEY autoincrement,
    titles_applications varchar(50),
);

