import mysql.connector
from mysql.connector import Error

def insert_scraped_data(url: str, scraped_text: str, ai_response_data: dict):
    try:
        connection = mysql.connector.connect(
            host='if.unismuh.ac.id',
            user='root',
            password='mariabelajar',
            database='scrappe_db',
            port=3388
        )

        cursor = connection.cursor()

        insert_query = """
        INSERT INTO scraped_data (
            url, scraped_text, judul_pekerjaan, deskripsi_pekerjaan, tag_keahlian,
            minimal_budget, maksimal_budget, jangka_waktu, persyaratan_pelamar
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        tag_keahlian = ','.join(ai_response_data.get('tag_keahlian', []))
        minimal_budget = ai_response_data['budget']['minimal_budget']
        maksimal_budget = ai_response_data['budget']['maksimal_budget']

        data_tuple = (
            url,
            scraped_text,
            ai_response_data['judul_pekerjaan'],
            ai_response_data['deskripsi_pekerjaan'],
            tag_keahlian,
            minimal_budget,
            maksimal_budget,
            ai_response_data['jangka_waktu'],
            ai_response_data['persyaratan_pelamar']
        )

        cursor.execute(insert_query, data_tuple)
        connection.commit()

    except Error as e:
        print(f"Error while inserting data into MySQL: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
