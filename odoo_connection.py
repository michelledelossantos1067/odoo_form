import xmlrpc.client

# Datos de conexión
url = 'http://localhost:8069'  # URL de tu instancia de Odoo
db = 'nombre_de_tu_base_de_datos'  # Nombre de tu base de datos
username = 'tu_usuario'  # Usuario de Odoo
password = 'tu_contraseña'  # Contraseña de Odoo

# Conexión al servidor XML-RPC de Odoo
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

# Si la autenticación es exitosa, uid tendrá el ID del usuario autenticado
if uid:
    print("Autenticación exitosa. UID:", uid)
    # Ahora puedes usar el ID de usuario (uid) para realizar operaciones en Odoo
else:
    print("La autenticación ha fallado.")
