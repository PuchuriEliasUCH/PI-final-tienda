class Consultas_sql:
    SA_CATE = "SELECT * FROM categoria"
    SA_PROD = "SELECT * FROM producto"

    SO_CATE = "SELECT id_cat, nombre_cat FROM categoria WHERE id_cat = %s"

    I_CATE = "INSERT INTO categoria (nombre_cat) VALUE(%s)"
    I_PROD = "INSERT INTO producto VALUE(NULL, %s, %s, %s)"

    U_CATE = "UPDATE categoria SET nombre_cat = %s WHERE id_cat = %s"

    D_CATE = "DELETE FROM categoria WHERE id_cat = %s"

    SP_LISTADO = "CALL sp_listado()"