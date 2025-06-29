# 📚 Sistema de Gestión de Biblioteca - Django

Proyecto académico desarrollado en Django como tarea universitaria. Permite administrar libros, usuarios, préstamos, devoluciones y realizar respaldos en formato JSON desde consola y desde la interfaz web.

---

## 🚀 Funcionalidades principales

- **Gestión de Libros**: Crear, listar, editar y eliminar libros.
- **Gestión de Préstamos**: Registrar préstamos y devoluciones de libros.
- **Historial**: Cada usuario puede ver su historial de préstamos.
- **Autenticación**: Login y logout de usuarios, con permisos diferenciados.
- **Backup y Restauración**: Exportar e importar los datos del sistema en formato JSON (por consola y desde botón web para administradores).
- **Panel de Administración**: Gestión avanzada desde el panel `/admin/`.
- **Interfaz Moderna**: Uso de Bootstrap para un diseño responsive y profesional.

---

## ⚙️ Instalación y ejecución

1. **Clonar el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/django-biblioteca.git
    cd django-biblioteca
    ```

2. **Crear y activar un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Realizar migraciones y crear superusuario:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

5. **Ejecutar el servidor:**
    ```bash
    python manage.py runserver
    ```

---

## 🛡️ Control de Accesos

- Solo los usuarios con permiso de *staff* (administradores) pueden realizar backup desde la interfaz.
- Los usuarios normales solo pueden prestar, devolver y ver su historial.
- El panel de administración es solo para superusuarios o staff.

---

## 💾 Backup y restauración de datos

- **Exportar desde consola:**
    ```bash
    python manage.py dumpdata biblioteca > backup_biblioteca.json
    ```
- **Restaurar desde consola:**
    ```bash
    python manage.py loaddata backup_biblioteca.json
    ```
- **Exportar desde interfaz:**  
  (Solo administradores)  
  Botón “Exportar Backup” en la página principal.

---

## 👤 Créditos

- Desarrollado por: [Sebas]
- Universidad: [Nombre de tu universidad]
- Semestre: Tercero
- Año: 2025

---

## 📝 Notas

- El proyecto incluye archivos de ejemplo para exportar y restaurar datos.
- Los archivos `.sqlite3`, `.env` y otros datos sensibles están excluidos por `.gitignore`.
- Si tienes dudas o sugerencias, ¡puedes abrir un Issue o hacer un Pull Request!

---

