import json
import mysql
import mysql.connector

def load_json(path):
    with open (path, "+r") as f:
        api_result=json.loads(f.read())
    return api_result["data"]

def insert_data(conn, data, table_name):
    cursor = conn.cursor()

    # Insert data into the MySQL table
    columns = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    data_tuple = tuple(data.values())
    cursor.execute(insert_query, data_tuple)

    # Commit changes and close the connection
    conn.commit()
    cursor.close()

def get_unique_column(data, col_name):
    unique_kat=[]

    # print(list(data[0].keys())[1:])
    for dt in data:
        if(dt[col_name] not in unique_kat):
            unique_kat.append(dt[col_name])
    return unique_kat


def main():
    data = load_json("ETL_API/api_result.json")

    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "",
        "database": "tes_fastprint"
    }

    try:
        # Establishing connection
        connection = mysql.connector.connect(**db_config)
        
        # # insert kategori
        kategori_col=get_unique_column(data, col_name="kategori")
        # for c in kategori_col:
        #     insert_data(connection, {'nama_kategori':c}, table_name="kategori")

        # # insert status
        status_col=get_unique_column(data, col_name="status")
        # for c in status_col:
        #     insert_data(connection, {'nama_status':c}, table_name="status")

        # insert produk
        for dt in data:
            # rename
            dt['kategori_id']=dt.pop('kategori')
            dt['status_id']=dt.pop('status')

            # convert name to id (foreign key)
            dt['kategori_id'] = kategori_col.index(dt['kategori_id'])+1
            dt['status_id'] = status_col.index(dt['status_id'])+1

            del(dt['no'])
            insert_data(connection, dt, table_name="produk")

        # close connection
        connection.close()
    except mysql.connector.Error as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()