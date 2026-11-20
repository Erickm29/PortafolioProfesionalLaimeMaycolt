# -*- coding: utf-8 -*-
"""Genera el informe de investigación U4 en formato Word."""

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Cm, Pt


def set_run_font(run, name="Calibri", size=11, bold=False):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.bold = bold


def add_heading_custom(doc, text, level=1):
    heading = doc.add_heading(text, level=level)
    for run in heading.runs:
        set_run_font(run, size=16 if level == 1 else 13, bold=True)
    return heading


def add_para(doc, text, bold=False, center=False, size=11, space_after=8):
    p = doc.add_paragraph()
    if center:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    set_run_font(run, size=size, bold=bold)
    p.paragraph_format.space_after = Pt(space_after)
    return p


def add_placeholder(doc, label):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(f"[PEGAR CAPTURA AQUÍ: {label}]")
    set_run_font(run, size=11, bold=True)
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(10)
    return p


def main():
    out_dir = Path(__file__).resolve().parent
    doc = Document()

    for section in doc.sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)

    # -------- CARÁTULA --------
    for _ in range(3):
        doc.add_paragraph()

    add_para(doc, "UNIVERSIDAD DEL VALLE", center=True, bold=True, size=16)
    add_para(doc, "Programación Web 1", center=True, bold=True, size=14)
    add_para(doc, "U4 – Manipulando el DOM", center=True, bold=True, size=14)
    doc.add_paragraph()
    add_para(doc, "Informe de investigación", center=True, bold=True, size=18)
    doc.add_paragraph()
    add_para(doc, "Estudiante: Maycolt Erick Laime Ugarte", center=True, size=12)
    add_para(doc, "Docente: Ing. Edwin Aguilar Verduguez", center=True, size=12)
    add_para(doc, "Fecha de entrega: 5 de noviembre de 2026", center=True, size=12)
    add_para(doc, "Santa Cruz de la Sierra – Bolivia", center=True, size=12)
    doc.add_page_break()

    # -------- ÍNDICE --------
    add_heading_custom(doc, "Índice", level=1)
    indice = [
        "1. Introducción",
        "2. Cambiar contenido mediante el DOM",
        "3. Modificar estilos CSS",
        "4. Añadir o quitar clases",
        "5. Consultar y modificar atributos",
        "6. Escuchar eventos (mínimo 3 tipos)",
        "7. Crear, insertar y eliminar elementos",
        "8. Descripción del sitio web desarrollado",
        "9. Conclusiones",
        "10. Bibliografía / referencias",
    ]
    for item in indice:
        add_para(doc, item, size=12)
    doc.add_page_break()

    # -------- INTRO --------
    add_heading_custom(doc, "1. Introducción", level=1)
    add_para(
        doc,
        "El Document Object Model (DOM) es la representación en forma de árbol de un "
        "documento HTML. JavaScript puede recorrer ese árbol para leer o modificar "
        "nodos, atributos, estilos y escuchar eventos del usuario. En esta investigación "
        "se explica cada operación solicitada y se evidencia su uso en el sitio de perfil "
        "profesional desarrollado, indicando exactamente qué fragmento de código capturar.",
    )
    add_para(
        doc,
        "El proyecto práctico consiste en un sitio multipágina (6 archivos HTML) con CSS "
        "y JavaScript externos, elementos Bootstrap, y demostraciones interactivas del DOM "
        "distribuidas en distintas secciones.",
    )

    # -------- 2 CONTENIDO --------
    add_heading_custom(doc, "2. Cambiar contenido mediante el DOM", level=1)
    add_para(
        doc,
        "Para cambiar el texto visible de un elemento se utilizan propiedades como "
        "textContent (seguro para texto plano) o innerHTML (cuando se necesita markup). "
        "También existe innerText, que respeta estilos de visibilidad.",
    )
    add_para(
        doc,
        "En el proyecto, el botón «Cambiar contenido» de index.html actualiza el párrafo "
        "con id texto-dinamico. La lógica está en js/main.js, función changeGreetingContent().",
    )
    add_para(doc, "Código clave:", bold=True)
    add_para(
        doc,
        "target.textContent = next;",
        size=10,
    )
    add_placeholder(doc, "js/main.js → changeGreetingContent() y botón en index.html")

    # -------- 3 ESTILOS --------
    add_heading_custom(doc, "3. Modificar estilos CSS", level=1)
    add_para(
        doc,
        "JavaScript puede alterar el aspecto visual escribiendo en element.style.propiedad. "
        "Esto genera estilos en línea con alta especificidad. Es útil para demos y estados "
        "temporales; para temas persistentes suele preferirse classList.",
    )
    add_para(
        doc,
        "En perfil.html, el botón «Modificar estilos CSS» llama a applyDynamicStyles() y "
        "cambia backgroundColor, color, border, transform y boxShadow de #caja-estilo.",
    )
    add_para(doc, "Código clave:", bold=True)
    add_para(doc, "target.style.backgroundColor = \"#0b6e4f\";", size=10)
    add_para(doc, "target.style.color = \"#ffffff\";", size=10)
    add_placeholder(doc, "js/main.js → applyDynamicStyles() y demo en perfil.html")

    # -------- 4 CLASES --------
    add_heading_custom(doc, "4. Añadir o quitar clases", level=1)
    add_para(
        doc,
        "La API classList permite add, remove, toggle y contains sobre el atributo class. "
        "Es la forma recomendada de activar temas, estados activos o animaciones definidas en CSS.",
    )
    add_para(
        doc,
        "En index.html, el botón «Resaltar foto / tema» ejecuta toggleThemeClass(), que hace "
        "toggle de theme-warm en el panel y de is-highlighted en la foto. Además, los chips "
        "de habilidades en perfil.html usan classList.toggle(\"active-chip\").",
    )
    add_para(doc, "Código clave:", bold=True)
    add_para(doc, "panel.classList.toggle(\"theme-warm\");", size=10)
    add_para(doc, "photo.classList.toggle(\"is-highlighted\");", size=10)
    add_placeholder(doc, "js/main.js → toggleThemeClass() y uso en index.html / perfil.html")

    # -------- 5 ATRIBUTOS --------
    add_heading_custom(doc, "5. Consultar y modificar atributos", level=1)
    add_para(
        doc,
        "Los atributos HTML se leen con getAttribute(nombre) y se escriben con "
        "setAttribute(nombre, valor). También existen propiedades directas (href, src, id), "
        "pero get/setAttribute es explícito y sirve para atributos personalizados data-*.",
    )
    add_para(
        doc,
        "En index.html, el enlace #link-atributos alterna entre LinkedIn y GitHub. "
        "La función updateLinkAttributes() consulta y modifica href, title y target; "
        "showCurrentAttributes() muestra el estado actual en pantalla.",
    )
    add_para(doc, "Código clave:", bold=True)
    add_para(doc, "link.setAttribute(\"href\", \"https://github.com/erickm29\");", size=10)
    add_para(doc, "const href = link.getAttribute(\"href\");", size=10)
    add_placeholder(doc, "js/main.js → updateLinkAttributes() / showCurrentAttributes()")

    # -------- 6 EVENTOS --------
    add_heading_custom(doc, "6. Escuchar eventos (mínimo 3 tipos)", level=1)
    add_para(
        doc,
        "addEventListener(tipo, callback) registra reacciones a interacciones del usuario "
        "o del navegador. En el proyecto se demuestran al menos estos eventos:",
    )
    add_para(doc, "1) click – botón «Probar click» actualiza el mensaje en vivo.")
    add_para(doc, "2) mouseover / mouseout – la caja #caja-hover cambia de color al pasar el cursor.")
    add_para(doc, "3) input – al escribir en el campo de nombre se refleja el texto.")
    add_para(doc, "4) submit – el formulario se captura con preventDefault() sin recargar la página.")
    add_para(
        doc,
        "La demostración está en experiencia.html y la lógica en initEventListeners() de main.js.",
    )
    add_placeholder(doc, "js/main.js → initEventListeners() y sección de eventos en experiencia.html")

    # -------- 7 CRUD ELEMENTOS --------
    add_heading_custom(doc, "7. Crear, insertar y eliminar elementos", level=1)
    add_para(
        doc,
        "document.createElement(etiqueta) crea nodos nuevos. Luego se insertan con "
        "appendChild, prepend, insertBefore o métodos modernos como append. Para eliminar "
        "se usa node.remove() o parent.removeChild(node).",
    )
    add_para(
        doc,
        "En proyectos.html, addDynamicItem() crea un <li>, un <span> y un botón Eliminar; "
        "los inserta en #lista-dinamica. removeDynamicItem() elimina el ítem. El botón "
        "«Vaciar lista» limpia todo con innerHTML = \"\".",
    )
    add_para(doc, "Código clave:", bold=True)
    add_para(doc, "const li = document.createElement(\"li\");", size=10)
    add_para(doc, "list.appendChild(li);", size=10)
    add_para(doc, "node.remove();", size=10)
    add_placeholder(doc, "js/main.js → addDynamicItem() / removeDynamicItem() y UI en proyectos.html")

    # -------- 8 SITIO --------
    add_heading_custom(doc, "8. Descripción del sitio web desarrollado", level=1)
    add_para(
        doc,
        "Se desarrolló un sitio de perfil profesional con seis páginas HTML enlazadas por "
        "un menú de navegación Bootstrap:",
    )
    add_para(doc, "• index.html – datos personales, foto y contacto")
    add_para(doc, "• perfil.html – perfil profesional")
    add_para(doc, "• experiencia.html – experiencia laboral (tabla + cards)")
    add_para(doc, "• formacion.html – formación académica (timeline + progress bars)")
    add_para(doc, "• proyectos.html – proyectos y hackathones (grid)")
    add_para(doc, "• referencias.html – referencias laborales (tablero + accordion)")
    add_para(
        doc,
        "CSS y JavaScript están en archivos externos (css/styles.css y js/main.js). "
        "Se usan texto, imagen, tablas, listas y componentes Bootstrap (navbar, cards, "
        "alerts, progress, accordion, badges, formularios). Los layouts no son idénticos "
        "entre páginas. El sitio está preparado para despliegue en InfinityFree.",
    )

    # -------- 9 CONCLUSIONES --------
    add_heading_custom(doc, "9. Conclusiones", level=1)
    add_para(
        doc,
        "Manipular el DOM permite construir interfaces dinámicas sin recargar la página. "
        "Separar HTML, CSS y JS facilita el mantenimiento. Combinar classList, estilos, "
        "atributos, eventos y creación/eliminación de nodos cubre la mayoría de "
        "interacciones básicas de un sitio web moderno.",
    )

    # -------- 10 BIBLIO --------
    add_heading_custom(doc, "10. Bibliografía / referencias", level=1)
    add_para(doc, "MDN Web Docs – Document Object Model (DOM). https://developer.mozilla.org/es/docs/Web/API/Document_Object_Model")
    add_para(doc, "MDN Web Docs – Element.classList. https://developer.mozilla.org/es/docs/Web/API/Element/classList")
    add_para(doc, "MDN Web Docs – EventTarget.addEventListener. https://developer.mozilla.org/es/docs/Web/API/EventTarget/addEventListener")
    add_para(doc, "Bootstrap 5 Documentation. https://getbootstrap.com/docs/5.3/getting-started/introduction/")

    out_path = out_dir / "Informe_U4_Manipulando_el_DOM_Maycolt_Laime.docx"
    doc.save(out_path)
    print(f"OK: {out_path}")


if __name__ == "__main__":
    main()
