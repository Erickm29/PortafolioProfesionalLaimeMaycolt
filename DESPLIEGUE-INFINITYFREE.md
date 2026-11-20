# Despliegue en InfinityFree

## 1. Crear cuenta y sitio
1. Entra a https://www.infinityfree.com/ y crea una cuenta.
2. En el panel: **Create Account** (hosting) → elige un subdominio (ej. `maycolt-perfil.infinityfreeapp.com`).
3. Anota el usuario FTP, contraseña FTP y host FTP del panel.

## 2. Subir archivos
Sube **todo el contenido del proyecto** a la carpeta `htdocs` (no subas la carpeta `informe` si no quieres publicarla).

Estructura esperada dentro de `htdocs`:
```
htdocs/
  index.html
  perfil.html
  experiencia.html
  formacion.html
  proyectos.html
  referencias.html
  css/styles.css
  js/main.js
  assets/foto-perfil.png
```

### Opción A – File Manager del panel
1. Abre **File Manager**.
2. Entra a `htdocs`.
3. Sube los archivos y carpetas (`css`, `js`, `assets` y los `.html`).

### Opción B – FTP (FileZilla)
1. Host: el que indique InfinityFree (suele ser `ftpupload.net`).
2. Usuario / contraseña: los del panel.
3. Arrastra la carpeta del sitio a `/htdocs`.

## 3. Verificar
Abre `https://TU-SUBDOMINIO.infinityfreeapp.com/` y prueba el menú y los botones del laboratorio DOM.

## 4. Entrega digital
- Enlace del sitio publicado
- ZIP del proyecto (incluye HTML, CSS, JS, assets e informe Word)
