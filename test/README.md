# Ejecución de las pruebas
Pararse en esta carpeta y ejecutar el siguiente comando:
```
python3 all_test.py
```
# Generar nuevas pruebas
La idea es que cada entidad (como "device") tenga una clase nombre_entidad_test.py.
Todos estos archivos deberían tener un método "def allTest(self)" el cual ejecuta todas las pruebas de la clase. Luego se llama a este método desde "all_test.py"