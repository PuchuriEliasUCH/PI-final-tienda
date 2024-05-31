class Consultas_sql:
    SA_CATE = "SELECT * FROM categoria
    SO_CATE = "SELECT id_cat, nombre FROM categoria WHERE id_cat = %s"
    "
    SA_PROD = "SELECT * FROM producto"

    I_CATE = "INSERT INTO categoria (nombre_cat) VALUE(%s)"
    I_PROD = "INSERT INTO producto VALUE(NULL, %s, %s, %s)"

    U_CATE = "UPDATE categoria SET nombre = %s WHERE id_cat = %s"

    D_CATE = "DELETE FROM categoria WHERE id_cat = %s"