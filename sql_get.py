def get_students_query():
    get_students_query = 'SELECT rowid, name, age, information FROM STUDENTS'
    return get_students_query
def get_student_query(id):
    get_student_query = f'SELECT name, age, information, rowid FROM STUDENTS WHERE rowid = {id}'
    return get_student_query
def create_table_query():
    create_table_query = f'''CREATE TABLE STUDENTS (
name string,
age integer,
information string
)'''
    return create_table_query
def edit_student_variant1_query(id, parameter, value):
    return f'UPDATE STUDENTS SET parameter = value WHERE rowid = {id}'
def edit_student_variant2_query(id, parameter, value):
    return f'UPDATE STUDENTS SET {parameter} = "{value}" WHERE rowid = {id}'
def add_student_query(name, age, information):
    add_student_query = f"INSERT INTO STUDENTS (name, age, information) VALUES ('{name}', {age}, '{information}')"
    return add_student_query