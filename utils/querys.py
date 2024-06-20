class Consultas_sql:
    SA_CATE = "SELECT * FROM categoria WHERE estado = 1"
    SA_PROD = "SELECT * FROM producto WHERE estado = 1"

    SO_CATE = "SELECT id_cat, nombre_cat FROM categoria WHERE id_cat = %s"
    SO_PROD = "SELECT * FROM producto WHERE id_prod = %s"

    I_CATE = "INSERT INTO categoria (nombre_cat) VALUE(%s)"
    I_PROD = "INSERT INTO producto VALUE(NULL, %s, %s, %s, %s, 1)"

    U_CATE = "UPDATE categoria SET nombre_cat = %s WHERE id_cat = %s"

    D_CATE = "UPDATE categoria SET estado = 0 WHERE id_cat = %s"

    SP_LISTADO = "CALL sp_listado()"