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
    def getNodes(rmin,rmax):
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

    @staticmethod
    def getEdges(rmin,rmax):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct q1.id as idA ,q2.id as idB, q2.worlwide_gross_income as peso 
from (
select distinct n.id, rm.movie_id  
from names n, role_mapping rm, ratings r, movie m
where n.id =rm.name_id and rm.movie_id =r.movie_id and n.date_of_birth is not null
and r.avg_rating between %s and %s and m.id =r.movie_id 
group by n.id 
) q1,
(select distinct n.id, rm.movie_id, m.worlwide_gross_income  
from names n, role_mapping rm, ratings r, movie m
where n.id =rm.name_id and rm.movie_id =r.movie_id and n.date_of_birth is not null
and r.avg_rating between %s and %s and m.id =r.movie_id 
group by n.id 
)q2, movie m
where q1.movie_id =q2.movie_id and q1.id >q2.id  and m.worlwide_gross_income is not null
and m.id =q1.movie_id 
group by q1.id, q2.id """

        cursor.execute(query, (rmin, rmax,rmin,rmax,))

        for row in cursor:
            results.append(row)

        cursor.close()
        conn.close()
        return results