import sqlite3


def task_1(path):
    conn = sqlite3.connect(path)
    curs = conn.cursor()
    curs.execute("CREATE TABLE Shops("
                 "id int PRIMARY KEY NOT NULL,"
                 "name varchar(32) NOT NULL,"
                 "address varchar(32),"
                 "staff_amount int NOT NULL)")
    curs.execute("CREATE TABLE Departments("
                 "id int PRIMARY KEY NOT NULL,"
                 "sphere varchar(32) NOT NULL,"
                 "staff_amount int NOT NULL,"
                 "shop int NOT NULL,"
                 "FOREIGN KEY (shop) REFERENCES Shops(id))")
    curs.execute("CREATE TABLE Items("
                 "id int PRIMARY KEY NOT NULL,"
                 "name varchar(32) NOT NULL,"
                 "description text,"
                 "price int NOT NULL,"
                 "department int NOT NULL,"
                 "FOREIGN KEY (department) REFERENCES Departments(id))")
    conn.commit()
    pass


def task_2(path):
    conn = sqlite3.connect(path)
    curs = conn.cursor()

    data = [(1, 'Auchan', None, 250),
            (2, 'IKEA', 'Street Žirnių g. 56, Vilnius, Lithuania.', 500)]
    curs.executemany("INSERT INTO Shops VALUES (?,?,?,?)", data)

    data = [(1, 'Furniture', 250, 1),
            (2, 'Furniture', 300, 2),
            (3, 'Dishes', 200, 2)]
    curs.executemany("INSERT INTO Departments VALUES (?,?,?,?)", data)

    data = [(1, 'Table', 'Cheap wooden table', 300, 1),
            (2, 'Table', None, 750, 2),
            (3, 'Bed', 'Amazing wooden bed', 1200,2),
            (4, 'Cup', None, 10, 3),
            (5, 'Plate', 'Glass plate', 20, 3)]
    curs.executemany("INSERT INTO Items VALUES (?,?,?,?,?)", data)

    conn.commit()
    pass


# def select_krome(cursor, table_name, krome_list):
#     cursor.execute(f"pragma table_info({table_name})")
#     sel0 = ''
#     sel1 = []
#     sel2 = []
#     for n in cursor.fetchall():
#         if n[1] not in krome_list:
#             sel0 = sel0 + table_name + '.' + n[1] + ', '
#             sel1.append(table_name)
#             sel2.append(n[1])
#     sel0 = sel0[:-2]
#     return [sel0, sel1, sel2]


def task_3(path):
    t = []
    conn = sqlite3.connect(path)
    curs = conn.cursor()

    # a
    curs.execute("SELECT * FROM Items WHERE description NOT NULL")
    t.append(curs.fetchall())

    # b
    curs.execute("SELECT DISTINCT sphere FROM Departments WHERE staff_amount > 200")
    t.append(curs.fetchall())

    # c
    curs.execute("SELECT address FROM Shops WHERE name LIKE 'i%'")
    t.append(curs.fetchall())

    # d
    curs.execute("SELECT Items.name FROM Items, Departments "
                 "WHERE Items.department = Departments.id AND Departments.sphere = 'Furniture'")
    t.append(curs.fetchall())

    # e
    curs.execute("SELECT DISTINCT Shops.name FROM Items, Departments, Shops "
                 "WHERE Items.department = Departments.id AND Departments.shop = Shops.id "
                 "AND Items.description NOT NULL")
    t.append(curs.fetchall())

    # f
    curs.execute(f"SELECT I.name, I.description, I.price, "
                 f"'department_{{sphere}} ' || D.sphere, "
                 f"'department_{{staff_amount}} ' || D.staff_amount, "
                 f"'shop_{{name}} ' || S.name, "
                 f"'shop_{{address}} ' || S.address, "
                 f"'shop_{{staff_amount}} ' || S.staff_amount FROM Items AS I "
                 f"JOIN Departments AS D ON I.department = D.id "
                 f"JOIN Shops AS S ON D.shop = S.id")
    t.append(curs.fetchall())

    return tuple(t)


def task_4(path):
    conn = sqlite3.connect(path)
    curs = conn.cursor()

    res = tuple(curs.execute("DELETE FROM Items WHERE description IS NULL OR price > 500"))

    curs.close()
    conn.commit()
    conn.close()
    return res


def task_5(path):
    conn = sqlite3.connect(path)
    curs = conn.cursor()

    curs.execute("DELETE FROM Items WHERE department "
                 "IN (SELECT Departments.id FROM Departments JOIN Shops ON Shops.id = Departments.Shop "
                 "WHERE Shops.address is NULL)")

    curs.close()
    conn.commit()
    conn.close()
    pass


p = 'base.db'
# task_1(p)
# task_2(p)
# print('--- task_3 --------start---', '\n', task_3(p), '\n' + '--- task_3 ----------end---')
# task_4(p)
task_5(p)









