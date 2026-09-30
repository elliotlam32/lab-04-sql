SELECT users.username, users.age, posts.likes
FROM users JOIN posts 
  WHERE users.user_id = posts.user_id;
