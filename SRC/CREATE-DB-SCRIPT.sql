create table movies (imdb_id varchar(20), adult boolean, budget long, homepage varchar(500), original_language varchar(5),
                original_title varchar(100), overview varchar(1000), popularity float, release_date date, revenue long,
                runtime int, status varchar(20), tagline varchar(1000), title varchar(100), vote_average float, vote_count int,
                primary key (imdb_id));

create table genres (id int, genre VARCHAR(50), primary key (id));

create table directors (id int, director varchar(100), primary key (id));

create table spoken_languages (id varchar(5), english_name varchar(20), primary key (id));

create table production_countries (id varchar(5), name varchar(100), primary key (id));

create table production_companies (id int, name varchar(100), origin_country varchar(5),
                foreign key (origin_country) references production_countries(id),
                primary key (id));

create table movies_to_production_countries (id int auto_increment, imdb_id varchar(20), production_countries_id varchar(5),
                foreign key (production_countries_id) references production_countries(id),
                foreign key (imdb_id) references movies(imdb_id),
                primary key (id));

create table movies_to_spoken_languages (id int auto_increment, imdb_id varchar(20), spoken_languages_id varchar(5),
                foreign key (spoken_languages_id) references spoken_languages(id),
                foreign key (imdb_id) references movies(imdb_id),
                primary key (id));

create table movies_to_production_companies (id int auto_increment, imdb_id varchar(20), production_companies_id int,
                foreign key (imdb_id) references movies(imdb_id),
                foreign key (production_companies_id) references production_companies(id),
                primary key (id));

create table movies_to_genres (id int auto_increment, imdb_id varchar(20), genres_id int,
                foreign key (imdb_id) references movies(imdb_id),
                foreign key (genres_id) references genres(id),
                primary key (id));

create table movies_to_directors (id int auto_increment, imdb_id varchar(20), director_id int,
                foreign key (imdb_id) references movies(imdb_id),
                foreign key (director_id) references directors(id),
                primary key (id));

create fulltext index titleOverview on movies(title, overview);
