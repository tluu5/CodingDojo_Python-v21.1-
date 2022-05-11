USE CodingDojo;
DROP TABLE student;
CREATE TABLE student (
	student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    major VARCHAR(20)
);
SELECT *
FROM student
ORDER BY student_id ASC;
INSERT INTO student(name, major) VALUES('Jack', 'Biology');
INSERT INTO student(name, major) VALUES('Kate', 'Sociology');
INSERT INTO student(name, major) VALUES('Claire', 'Chemistry');
INSERT INTO student(name, major) VALUES('Jack', 'Biology');
INSERT INTO student(name, major) VALUES('Mike', 'Computer Science');
DELETE FROM student
WHERE student_id = 5;
show databases