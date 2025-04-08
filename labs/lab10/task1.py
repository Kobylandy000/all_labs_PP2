import psycopg2
import csv

# Дерекқорға қосылу мәліметтері
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "Kobylan2007"

def create_table(conn):
    """contacts кестесін жасайды."""
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                contact_id SERIAL PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50),
                phone VARCHAR(20) UNIQUE NOT NULL
            )
        """)
        conn.commit()
        print("contacts кестесі сәтті жасалды (егер бұрын болмаса).")
    except (Exception, psycopg2.Error) as error:
        print(f"Кестені жасау кезінде қате: {error}")
        conn.rollback()

def upload_from_csv(conn, csv_filepath):
    """CSV файлынан деректерді contacts кестесіне жүктейді."""
    cursor = conn.cursor()
    try:
        with open(csv_filepath, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader, None)  # Тақырып жолын өткізіп жіберу (қажет болса)
            for row in csv_reader:
                first_name, last_name, phone = row
                sql = "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s);"
                cursor.execute(sql, (first_name, last_name, phone))
        conn.commit()
        print(f"Деректер '{csv_filepath}' файлынан сәтті жүктелді.")
    except (Exception, psycopg2.Error) as error:
        print(f"Деректерді жүктеу кезінде қате: {error}")
        conn.rollback()

def insert_from_console(conn):
    """Пайдаланушы аты мен телефонды консольдан енгізіп, contacts кестесіне қосады."""
    first_name = input("Атын енгізіңіз: ")
    last_name = input("Тегін енгізіңіз (міндетті емес): ")
    phone = input("Телефон нөмірін енгізіңіз: ")

    cursor = conn.cursor()
    sql = "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s);"
    try:
        cursor.execute(sql, (first_name, last_name, phone))
        conn.commit()
        print(f"'{first_name} {last_name}' ({phone}) сәтті қосылды.")
    except psycopg2.Error as error:
        print(f"Деректерді енгізу кезінде қате: {error}")
        conn.rollback()

def update_contact(conn, identifier, new_value, update_field):
    """Берілген идентификатор бойынша contacts кестесіндегі деректерді жаңартады."""
    cursor = conn.cursor()
    sql = ""
    if update_field == 'first_name':
        sql = "UPDATE contacts SET first_name = %s WHERE first_name = %s OR phone = %s;"
    elif update_field == 'phone':
        sql = "UPDATE contacts SET phone = %s WHERE first_name = %s OR phone = %s;"
    else:
        print("Жаңартуға болатын дұрыс өрісті енгізіңіз ('first_name' немесе 'phone').")
        return

    try:
        cursor.execute(sql, (new_value, identifier, identifier))
        rows_affected = cursor.rowcount
        conn.commit()
        if rows_affected > 0:
            print(f"'{identifier}' үшін '{update_field}' '{new_value}'-ге сәтті жаңартылды.")
        else:
            print(f"'{identifier}' табылмады.")
    except psycopg2.Error as error:
        print(f"Деректерді жаңарту кезінде қате: {error}")
        conn.rollback()

def query_contacts(conn, filter_field=None, filter_value=None):
    """contacts кестесінен деректерді сұрайды. Сүзгі өрісі мен мәнін беруге болады."""
    cursor = conn.cursor()
    sql = "SELECT * FROM contacts"
    params = ()

    if filter_field:
        if filter_field == 'first_name':
            sql += " WHERE first_name LIKE %s"
            params = (f"%{filter_value}%",)
        elif filter_field == 'last_name':
            sql += " WHERE last_name LIKE %s"
            params = (f"%{filter_value}%",)
        elif filter_field == 'phone':
            sql += " WHERE phone LIKE %s"
            params = (f"%{filter_value}%",)
        else:
            print("Сұрау үшін дұрыс сүзгі өрісін енгізіңіз ('first_name', 'last_name' немесе 'phone').")
            return

    try:
        cursor.execute(sql, params)
        results = cursor.fetchall()
        if results:
            print("Нәтижелер:")
            for row in results:
                print(f"ID: {row[0]}, Аты: {row[1]}, Тегі: {row[2]}, Телефон: {row[3]}")
        else:
            print("Нәтиже табылмады.")
    except psycopg2.Error as error:
        print(f"Деректерді сұрау кезінде қате: {error}")

def delete_contact(conn, identifier):
    """Пайдаланушы аты немесе телефон нөмірі бойынша contacts кестесінен деректерді жояды."""
    cursor = conn.cursor()
    sql = "DELETE FROM contacts WHERE first_name = %s OR phone = %s;"
    try:
        cursor.execute(sql, (identifier, identifier))
        rows_affected = cursor.rowcount
        conn.commit()
        if rows_affected > 0:
            print(f"'{identifier}' сәтті жойылды.")
        else:
            print(f"'{identifier}' табылмады.")
    except psycopg2.Error as error:
        print(f"Деректерді жою кезінде қате: {error}")
        conn.rollback()

if __name__ == "__main__":
    conn = None
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        create_table(conn)

        while True:
            print("\nТелефон кітапшасының мәзірі:")
            print("1. CSV файлынан деректерді жүктеу")
            print("2. Консольдан жаңа контакт қосу")
            print("3. Контактіні жаңарту")
            print("4. Контактілерді сұрау")
            print("5. Контактіні жою")
            print("6. Шығу")

            choice = input("Әрекетті таңдаңыз (1-6): ")

            if choice == '1':
                csv_file = input("CSV файлының жолын енгізіңіз: ")
                upload_from_csv(conn, csv_file)
            elif choice == '2':
                insert_from_console(conn)
            elif choice == '3':
                identifier = input("Жаңартылатын пайдаланушы атын немесе телефон нөмірін енгізіңіз: ")
                field = input("Нені өзгерткіңіз келеді ('first_name' немесе 'phone'): ")
                new_value = input(f"Жаңа '{field}' мәнін енгізіңіз: ")
                update_contact(conn, identifier, new_value, field)
            elif choice == '4':
                filter_field = input("Сүзгі өрісін енгізіңіз ('first_name', 'last_name', 'phone' немесе барлық контактілер үшін Enter): ")
                filter_value = None
                if filter_field:
                    filter_value = input(f"'{filter_field}' бойынша іздеу мәнін енгізіңіз: ")
                query_contacts(conn, filter_field, filter_value)
            elif choice == '5':
                identifier_to_delete = input("Жойғыңыз келетін пайдаланушы атын немесе телефон нөмірін енгізіңіз: ")
                delete_contact(conn, identifier_to_delete)
            elif choice == '6':
                print("Бағдарламадан шығу.")
                break
            else:
                print("Дұрыс емес таңдау. Қайтадан енгізіңіз.")

    except psycopg2.Error as e:
        print(f"Дерекқорға қосылу қатесі: {e}")
    finally:
        if conn:
            conn.close()