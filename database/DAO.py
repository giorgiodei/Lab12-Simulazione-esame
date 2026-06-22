from database.DB_connect import DBConnect
from model.actor import Actor


class DAO():

    @staticmethod
    def getAllRatings():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct r.avg_rating as rating
from ratings r 
order by r.avg_rating asc"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row['rating'])

        cursor.close()
        cnx.close()
        return res


    @staticmethod
    def getAllNodes(rmin,rmax):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct n.*
from names n, role_mapping rm, ratings r
where n.id =rm.name_id and rm.movie_id =r.movie_id and n.date_of_birth is not null
and r.avg_rating between %s and %s
"""
            cursor.execute(query,(rmin,rmax,))

            for row in cursor:
                result.append(Actor(**row))

            cursor.close()
            cnx.close()
        return result
