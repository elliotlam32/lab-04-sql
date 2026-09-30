CREATE TABLE users (
	user_id INT PRIMARY KEY,
	username VARCHAR(50) NOT NULL,
	age INT,
	followers INT,
	following INT
);

CREATE TABLE posts (
	post_id INT PRIMARY KEY,
	user_id INT,
	likes INT,
	shares INT,
	comments INT,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (user_id, username, age, followers, following) VALUES (1, 'elliot', 19, 171, 160);
INSERT INTO users (user_id, username, age, followers, following) VALUES ( 2 , 'jimmy' , 19, 210, 190);
INSERT INTO users (user_id, username, age, followers, following) VALUES ( 3 , 'harish' , 19, 5000, 3040);
INSERT INTO users (user_id, username, age, followers, following) VALUES ( 4 , 'jun' , 19, 2000303, 323232);
INSERT INTO users (user_id, username, age, followers, following) VALUES ( 5 , 'diego' , 19, 32, 1);
INSERT INTO users (user_id, username, age, followers, following) VALUES ( 6 , 'prabhav' , 20, 391, 320);
INSERT INTO users (user_id, username, age, followers, following) VALUES ( 7 , 'anirudh' , 24, 2131, 1023);
INSERT INTO users (user_id, username, age, followers, following) VALUES ( 8 , 'ajitesh' , 32, 103, 89);
INSERT INTO users (user_id, username, age, followers, following) VALUES ( 9 , 'thomas' , 32, 3132, 3231);
INSERT INTO users (user_id, username, age, followers, following) VALUES ( 10 , 'liam' , 21, 321, 89);

INSERT INTO posts (post_id, user_id, likes, shares, comments) VALUES ( 1 , 1 , 1, 1, 1); 
INSERT INTO posts (post_id, user_id, likes, shares, comments) VALUES ( 2 , 1 , 3, 2, 1); 
INSERT INTO posts (post_id, user_id, likes, shares, comments) VALUES ( 3 , 2 , 43, 43, 54); 
INSERT INTO posts (post_id, user_id, likes, shares, comments) VALUES ( 4 , 2 , 432, 54, 11); 
INSERT INTO posts (post_id, user_id, likes, shares, comments) VALUES ( 5 , 3 , 43, 31, 12); 
INSERT INTO posts (post_id, user_id, likes, shares, comments) VALUES ( 6 , 4 , 5, 66, 76);
INSERT INTO posts (post_id, user_id, likes, shares, comments) VALUES ( 7 , 5 , 4134, 434, 65); 
INSERT INTO posts (post_id, user_id, likes, shares, comments) VALUES ( 8 , 6 , 64, 767, 765); 
INSERT INTO posts (post_id, user_id, likes, shares, comments) VALUES ( 9 , 7 , 56, 66563, 6553); 
INSERT INTO posts (post_id, user_id, likes, shares, comments) VALUES ( 10 , 8 , 656, 653, 6563);  
