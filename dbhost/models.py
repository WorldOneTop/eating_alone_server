from django.db import models

class User(models.Model):
    id = models.CharField(max_length=11, primary_key=True)
    password = models.CharField(max_length=64)
    nickName = models.CharField(max_length=20)
    image = models.CharField(max_length=20, null=True)

class Review(models.Model):
    user_id_fk = models.ForeignKey("User", on_delete=models.CASCADE)
    house_id_fk = models.ForeignKey("House_main", on_delete=models.CASCADE)
    body = models.TextField()
    hashtag = models.CharField(max_length=200, null=True)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)

class Image(models.Model):
    url = models.CharField(max_length=20, primary_key=True)
    review_id_fk = models.ForeignKey("Review", on_delete=models.CASCADE)

class House_main(models.Model):
    category = models.CharField(max_length=10)
    rating = models.DecimalField(max_digits=2,decimal_places=1, default=0.0)
    review_count = models.PositiveSmallIntegerField(default=0)
    location = models.CharField(max_length=70)
    price_image = models.ForeignKey("Image", on_delete=models.CASCADE, null=True, related_name="price_fk")
    profile_image = models.ForeignKey("Image", on_delete=models.CASCADE, null=True, related_name="profile_fk")

class House_detail(models.Model):
    house_id_fk = models.ForeignKey("House_main", on_delete=models.CASCADE, primary_key=True)
    info = models.CharField(max_length=200)
    time = models.CharField(max_length=120, null=True)
    lat = models.DecimalField(max_digits=9,decimal_places=7)
    lng = models.DecimalField(max_digits=10,decimal_places=7)

class House_menu(models.Model):
    house_id_fk = models.ForeignKey("House_main", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price =  models.PositiveIntegerField()
    image = models.ForeignKey("Image", related_name="menu_image", on_delete=models.CASCADE, db_column="url", null=True)

class Question(models.Model):
    head = models.CharField(max_length=60)
    body = models.TextField()
    image = models.CharField(max_length=60)
    category = models.CharField(max_length=20)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)

class Notice(models.Model):
    head = models.CharField(max_length=60)
    body = models.TextField()
    time = models.DateTimeField(auto_now=False, auto_now_add=True)

"""
CREATE TABLE users(
    id CHAR(11) PRIMARY KEY,
    password CHAR(64) NOT NULL,
    nickName VARCHAR(20),
    image VARCHAR(20)
);

CREATE TABLE review(
    review_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id CHAR(11) NOT NULL,
    body TEXT NOT NULL,
    hashtag VARCHAR(200),
    time DATE,
    CONSTRAINT review_user_id FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE image(
    url VARCHAR(20) PRIMARY KEY,
    review_id INT NOT NULL,

    CONSTRAINT image_review_id FOREIGN KEY(review_id) REFERENCES review(review_id)
);

CREATE TABLE house_main(
    house_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(10) NOT NULL,
    rating DECIMAL(2,1) DEFAULT 0.0,
    review_count INT DEFAULT 0,
    location VARCHAR(70) NOT NULL,
    price_image VARCHAR(20) UNIQUE,
    profile_image VARCHAR(20) UNIQUE,
    CONSTRAINT profile_image_fk FOREIGN KEY(profile_image) REFERENCES image(url),
    CONSTRAINT price_image_fk FOREIGN KEY(price_image) REFERENCES image(url)
);
CREATE TABLE house_detail(
    house_id INT UNIQUE NOT NULL,
    info VARCHAR(200),
    time VARCHAR(120),
    lat DECIMAL(9,7) NOT NULL,
    lng DECIMAL(10,7) NOT NULL,
    CONSTRAINT dtail_pk FOREIGN KEY(house_id) REFERENCES house_main(house_id)
);
CREATE TABLE house_menu (
    house_id INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    price MEDIUMINT NOT NULL,
    image VARCHAR(20) UNIQUE,
    CONSTRAINT menu_image_fk FOREIGN KEY(image) REFERENCES image(url),
    CONSTRAINT menu_pk FOREIGN KEY(house_id) REFERENCES house_main(house_id)
);

CREATE TABLE question(
    question_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    head VARCHAR(60) NOT NULL,
    body TEXT NOT NULL,
    image VARCHAR(60),
    category VARCHAR(20) NOT NULL,
    user_id  CHAR(11) NOT NULL,
    CONSTRAINT user_id_fk FOREIGN KEY(user_id) REFERENCES users(id)
);"""