PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE user_info (
  User_Id INTEGER PRIMARY KEY AUTOINCREMENT,
  Email TEXT NOT NULL,
  FirstName TEXT NOT NULL,
  LastName TEXT NOT NULL,
  DOB TEXT NOT NULL,
  Username TEXT NOT NULL,
  Password TEXT NOT NULL,
  Profile_Id INTEGER
);

CREATE TABLE user_profile (
  Profile_Id INTEGER PRIMARY KEY AUTOINCREMENT,
  Profile_Picture TEXT,
  Bio TEXT,
  User_Id INTEGER,
  FOREIGN KEY (User_Id) REFERENCES user_info(User_Id)
);

CREATE TABLE followers (
  User_Id INTEGER,
  Followers INTEGER,
  Following INTEGER,
  FOREIGN KEY (User_Id) REFERENCES user_info(User_Id)
);

CREATE TABLE user_posts (
  user_post INTEGER PRIMARY KEY AUTOINCREMENT,
  user_profile_id INTEGER NOT NULL,
  Media TEXT NOT NULL,
  body TEXT,
  date_time TEXT,
  likes INTEGER,
  dislikes INTEGER,
  FOREIGN KEY (user_profile_id) REFERENCES user_profile(Profile_Id)
);

CREATE TABLE reply (
  reply_comment INTEGER PRIMARY KEY AUTOINCREMENT,
  reply TEXT,
  date_time TEXT,
  users_id INTEGER,
  users_post INTEGER,
  FOREIGN KEY (users_id) REFERENCES user_profile(Profile_Id),
  FOREIGN KEY (users_post) REFERENCES user_posts(user_post)
);

INSERT INTO user_profile (Profile_Id, Profile_Picture, Bio, User_Id) VALUES
(1, 'mypic.jpg', 'You Know I Had To Dobule It.', 1),
(2, 'Jpeg', 'Love to sing and dance', 2),
(3, 'Jpeg', 'Hi everyone im Chris', 3);

INSERT INTO user_info (User_Id, Email, FirstName, LastName, DOB, Username, Password, Profile_Id) VALUES
(1, 'Carlabrown8@gmail.com', 'Carla', 'Brown', '2000-10-10', 'cabrown', 'ptkry20@', 1),
(2, 'thomasfisher@gmail.com', 'Thomas', 'Fisher', '0000-00-00', 'tfish', 'getwbs1!', 2),
(3, 'christopherwalker23@gmail.com', 'Christopher', 'Walker', '0000-00-00', 'chrisW', 'tobeqsh$8', 3);

INSERT INTO followers (User_Id, Followers, Following) VALUES
(1, 100, 200),
(1, 100, 200),
(2, 400, 10),
(3, 343, 600);

INSERT INTO user_posts (user_post, user_profile_id, Media, body, date_time, likes, dislikes) VALUES
(1, 1, 'mypicture.jpg', 'Today is a sunny day', '2022-09-12 22:43:00', 50, 10),
(2, 2, 'Two rare birds flying', 'Moving.gif', '2021-10-15 11:00:00', 100, 20),
(3, 3, 'video.mp4', 'Another Good day, watch my video!!!', '2022-12-12 05:00:00', 200, 30);

INSERT INTO reply (reply_comment, reply, date_time, users_id, users_post) VALUES
(1, 'No Way!!!', '2022-01-05 08:00:00', 1, 2),
(2, 'They were so lovely', '2022-01-13 09:45:00', 2, 2),
(3, 'Those birds are the rarest in the world no way you saw that', '2022-02-22 11:15:00', 3, 2),
(4, 'Happy Birthday!!!', '2022-03-15 13:00:00', 3, 1),
(5, 'Nice Pic Christopher!!! Happy Late Birthday, Call me soon', '2022-03-29 15:26:00', 2, 1),
(6, 'My day was draining unforutnally ', '2022-04-10 04:30:00', 1, 3);

COMMIT;
