from errno import errorcode

import mysql.connector

def main():
    print("il mio primo programma MySQL")

    try:
        #stabilisco la connessione con il database
        cnx = mysql.connector.connect(user="root",
                                  passwd="",
                                  host="localhost",
                                  port="3306",
                                  database="products-suppliers")

        print("Connesso al database")

        #mi faccio dare dalla connessione un cursore
        cursore = cnx.cursor()
        #scrivo la query
        query = "SELECT * FROM S"
        #la eseguo attraverso il cursore
        cursore.execute(query)

        #il cursore è un container di Python ... quindi posso iterare su di esso con for
        for riga in cursore:
            print(riga)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        else:
            print("Something is wrong with your user name or password")

    else:
        cnx.close()


main()