create table login (
	codLogin integer primary key autoincrement,
	user varchar(50) not null,
	password varchar(200) not null,
	dateReg timestamp default current_timestamp
);
