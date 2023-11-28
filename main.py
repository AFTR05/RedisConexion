import redis

class RedisExample:
    def __init__(self, host='localhost', port=6379, db=1):
        # Crear una conexión al servidor de Redis
        self.redis_conn = redis.Redis(host=host, port=port, db=db)

    def set_data(self, key, value):
        self.redis_conn.set(key, value)

    def keys(self,pattern):
        value= self.redis_conn.keys(pattern)
        return value


    def get_data(self, key):
        value = self.redis_conn.get(key)
        return value.decode('utf-8') if value else None

    def update_data(self, key, new_value):
        if self.redis_conn.exists(key):
            self.redis_conn.set(key, new_value)
            return True
        return False

    def delete_data(self, key):
        if self.redis_conn.exists(key):
            self.redis_conn.delete(key)
            return True
        return False

# Ejemplo de uso
if __name__ == "__main__":
    redis_example = RedisExample()

    # Almacenar datos
    redis_example.set_data('frutas', 'pera')

    # Recuperar y mostrar datos
    retrieved_value = redis_example.get_data('frutas')
    print(f"Valor recuperado: {retrieved_value}")

    # Actualizar datos
    if redis_example.update_data('frutas', 'mango'):
        print("Valor actualizado correctamente")
    else:
        print("La clave no existe, no se puede actualizar")

    # Recuperar y mostrar datos actualizados
    updated_value = redis_example.get_data('frutas')
    print(f"Valor actualizado recuperado: {updated_value}")

    # Eliminar datos
    if redis_example.delete_data('frutas'):
        print("Datos eliminados correctamente")
    else:
        print("La clave no existe, no se puede eliminar")

    # Intentar recuperar datos después de la eliminación
    deleted_value = redis_example.get_data('frutas:1')
    print(f"Intento de recuperar valor eliminado: {deleted_value}")

    print(f"keys:{redis_example.keys('frutas:*')}")
