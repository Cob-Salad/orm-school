from sqlalchemy import create_engine, text


engine = create_engine("sqlite+pysqlite:///education.db", echo=True)


create_students_table = """
CREATE TABLE students(
    student_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email  TEXT,
    enrollment_year INT NOT NULL
)
"""

insert_student = """
INSERT INTO students 
    (first_name, last_name, email, enrollment_year)
    VALUES ('cob', 'jens', 'cobsalad@gmail.com', 2024)
"""

with engine.connect() as conn:
    conn.execute(text(create_students_table))
    conn.execute(text(insert_student))
    conn.commit()
    result = conn.execute(text("select * from students"))
    conn.commit()
    print(result.all())

