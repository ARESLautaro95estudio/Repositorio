import sqlite3 as sql
import re
def createDB():

    with sql.connect("ranking.db") as conexion:
        conexion.commit()

def createTable():

    with sql.connect("ranking.db") as conexion:
        try:
            conexion.execute(
                """CREATE TABLE score(
                    id integer primary key autoincrement,
                    nivel text,
                    name text,
                    score integer
                )"""
            )
        except sql.OperationalError:
            print("La tabla score ya existe")

def insertRow(name,score,nivel):

    with sql.connect("ranking.db") as conexion:
        try:
            conexion.execute(
                "insert into score(name,score,nivel) values (?,?,?)", (name, score,nivel))
            conexion.commit()
        except:
            print("Error")

def readRows(lvl):

    with sql.connect("ranking.db") as conexion:
        try:
            cursor = conexion.cursor()
            instruccion = f"SELECT * FROM score WHERE nivel = ? ORDER BY score DESC LIMIT 3"
            cursor.execute(instruccion,(lvl,))
            datos = cursor.fetchall()
            conexion.commit()
            return datos
        except:
            print("Error")

# # #
# print(readRows("Nivel uno"))
# # print(readRows("Nivel dos"))
# # print(readRows("Nivel tres"))
# top_3 =readRows("Nivel uno")+readRows("Nivel dos")+readRows("Nivel tres")

# # print(top_3[0][3])
# # print(top_3[1][3])
# print(top_3[7][2])
# print(top_3[6][2])
# print(top_3[8][2])

# datos = readRows()
# for score in datos:
#     print(score[3])


# print(datos[0][3])
# print(datos[3][3])
#createTable()
#insertRow("Messi",10)
#print( type(readRows()))

# def top_tres():
#     archivo = readRows()
#     puntaje_1=0
#     puntaje_2=0
#     puntaje_3=0
#     top_3=[]
#     for name_score in archivo:
#         for name in name_score[1:2]:
#             print(name)
          
#         for score in name_score[3:]:
#             if score > puntaje_1:
#                 puntaje_1=score
#                 best_player1=name_score
#                 best_player2=name_score
#                 best_player3=name_score
#             if name_score!= best_player1:
#                 if score > puntaje_2:
#                     puntaje_2=score
#                     best_player2=name_score
#             if name_score!= best_player2:
#                 if score > puntaje_3:
#                     puntaje_3=score
#                     best_player3=name_score
#     top_3.append(best_player1)
#     top_3.append(best_player2)
#     top_3.append(best_player3)
#     return top_3


# def highscor_top3():

#         archivo = readRows()
#         puntaje_1=0
#         puntaje_2=0
#         puntaje_3=0
#         top_3=[]
#         for score in archivo:
#             if score[3] > puntaje_1:
#                 puntaje_1=score[3]
#                 best_player1=score
#                 best_player2=score
#                 best_player3=score

#             elif score[2] != best_player1:
#                 if score[3]  > puntaje_2:   
#                     puntaje_2=score[3]
#                     best_player2=score
                    
#             elif score[2] != best_player2:
#                 if score[3]  > puntaje_3:
#                     puntaje_3=score[3]
#                     best_player3=score

#         top_3.append(best_player1)
#         top_3.append(best_player2)
#         top_3.append(best_player3)
#         return top_3




# text =highscor_top3()
# print((text[0][1]))
# # print(type(text[0][3]))









# print(top_tres)

#createTable()
# insertRow("Lautaro",100,"Nivel tres")
# insertRow("Juan",50,"Nivel tres")
# insertRow("Carlos",60,"Nivel tres")

# #print(type(score))

#     string_sucio.append(re.split( ",",name_score))
#     print(name_score)
# #     lista_highscore=[]
# #     puntaje_max=0
# #     string_sucio.pop(0)
# print(string_sucio)
