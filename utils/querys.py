class Consultas_sql:
    SA_CATE = "SELECT * FROM categoria WHERE estado = 1"
    SA_PROD = "SELECT * FROM producto WHERE estado = 1"

    SO_CATE = "SELECT id_cat, nombre_cat FROM categoria WHERE id_cat = %s"
    SO_PROD = "SELECT * FROM producto WHERE id_prod = %s"

    I_CATE = "INSERT INTO categoria (nombre_cat) VALUE(%s)"
    I_PROD = "INSERT INTO producto VALUE(NULL, %s, %s, %s, %s, 1)"
    I_VENTA = "INSERT INTO venta(num_venta) VALUES(null)"
    I_DET_VENTA = "INSERT INTO detalle_venta VALUE(%s, %s, %s, %s)"

    U_CATE = "UPDATE categoria SET nombre_cat = %s WHERE id_cat = %s"
    U_STOCK = "UPDATE producto SET stock = stock - %s WHERE id_prod = %s"
    U_VENTA = 'UPDATE venta v SET total = (SELECT SUM(subtotal) FROM detalle_venta dv WHERE dv.num_venta = v.num_venta) WHERE num_venta = %s'

    D_CATE = "UPDATE categoria SET estado = 0 WHERE id_cat = %s"

    SP_LISTADO = "CALL sp_listado()"
    
    SCOUNT_VENTA = "SELECT COUNT(*) FROM venta"