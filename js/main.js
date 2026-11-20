/**
 * U4 - Manipulando el DOM
 * Demostraciones usadas en el perfil profesional de Maycolt Erick Laime Ugarte.
 * Cada bloque está etiquetado para capturas del informe.
 */

document.addEventListener("DOMContentLoaded", () => {
  setActiveNavLink();
  initContentChange();
  initStyleChange();
  initClassToggle();
  initAttributeDemo();
  initEventListeners();
  initElementCRUD();
});

/* =========================================================
   Utilidad: marcar enlace activo del menú
   ========================================================= */
function setActiveNavLink() {
  const current = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll("[data-nav]").forEach((link) => {
    const href = link.getAttribute("href");
    if (href === current) {
      link.classList.add("active");
      link.setAttribute("aria-current", "page");
    }
  });
}

/* =========================================================
   1) CAMBIAR CONTENIDO  (textContent / innerHTML)
   Captura sugerida: función changeGreetingContent
   ========================================================= */
function initContentChange() {
  const button = document.getElementById("btn-cambiar-contenido");
  const target = document.getElementById("texto-dinamico");
  if (!button || !target) return;

  button.addEventListener("click", changeGreetingContent);
}

function changeGreetingContent() {
  const target = document.getElementById("texto-dinamico");
  const variants = [
    "¡Hola! Soy Maycolt, estudiante de Ingeniería en Sistemas apasionado por la IA.",
    "Actualmente curso el 2do semestre en Univalle y construyo soluciones con impacto.",
    "Ganador en hackathones de IA: EcoVision AI y Shieldmail.",
  ];
  const current = target.textContent.trim();
  const next = variants[(variants.indexOf(current) + 1) % variants.length];

  // Cambio de contenido textual del nodo
  target.textContent = next;
}

/* =========================================================
   2) MODIFICAR ESTILOS CSS  (element.style)
   Captura sugerida: función applyDynamicStyles
   ========================================================= */
function initStyleChange() {
  const button = document.getElementById("btn-cambiar-estilo");
  const target = document.getElementById("caja-estilo");
  if (!button || !target) return;

  button.addEventListener("click", applyDynamicStyles);
}

function applyDynamicStyles() {
  const target = document.getElementById("caja-estilo");
  const isAlt = target.dataset.alt === "true";

  if (!isAlt) {
    target.style.backgroundColor = "#0b6e4f";
    target.style.color = "#ffffff";
    target.style.border = "2px solid #d97706";
    target.style.transform = "scale(1.02)";
    target.style.boxShadow = "0 10px 24px rgba(11, 110, 79, 0.35)";
    target.dataset.alt = "true";
    target.textContent = "Estilos aplicados con JavaScript (element.style).";
  } else {
    target.style.backgroundColor = "";
    target.style.color = "";
    target.style.border = "";
    target.style.transform = "";
    target.style.boxShadow = "";
    target.dataset.alt = "false";
    target.textContent = "Esta caja cambiará de estilo al pulsar el botón.";
  }
}

/* =========================================================
   3) AÑADIR / QUITAR CLASES  (classList)
   Captura sugerida: función toggleThemeClass
   ========================================================= */
function initClassToggle() {
  const button = document.getElementById("btn-toggle-clase");
  const panel = document.getElementById("panel-clases");
  const chips = document.querySelectorAll(".skill-chip");
  if (!button || !panel) return;

  button.addEventListener("click", toggleThemeClass);

  chips.forEach((chip) => {
    chip.addEventListener("click", () => {
      chip.classList.toggle("active-chip");
    });
  });
}

function toggleThemeClass() {
  const panel = document.getElementById("panel-clases");
  const photo = document.getElementById("foto-perfil");

  panel.classList.toggle("theme-warm");
  if (photo) {
    photo.classList.toggle("is-highlighted");
  }
}

/* =========================================================
   4) CONSULTAR Y MODIFICAR ATRIBUTOS
   Captura sugerida: función updateLinkAttributes
   ========================================================= */
function initAttributeDemo() {
  const button = document.getElementById("btn-atributos");
  const link = document.getElementById("link-atributos");
  const output = document.getElementById("atributos-info");
  if (!button || !link || !output) return;

  button.addEventListener("click", updateLinkAttributes);
  showCurrentAttributes(link, output);
}

function showCurrentAttributes(link, output) {
  const href = link.getAttribute("href");
  const target = link.getAttribute("target");
  const title = link.getAttribute("title");
  output.textContent = `href="${href}" | target="${target}" | title="${title}"`;
}

function updateLinkAttributes() {
  const link = document.getElementById("link-atributos");
  const output = document.getElementById("atributos-info");
  const mode = link.dataset.mode || "linkedin";

  if (mode === "linkedin") {
    link.setAttribute("href", "https://github.com/erickm29");
    link.setAttribute("title", "Perfil de GitHub de Maycolt");
    link.setAttribute("target", "_blank");
    link.textContent = "Abrir GitHub";
    link.dataset.mode = "github";
  } else {
    link.setAttribute("href", "https://www.linkedin.com/in/maycolt-erick-laime-ugarte-8a6763301");
    link.setAttribute("title", "Perfil de LinkedIn de Maycolt");
    link.setAttribute("target", "_blank");
    link.textContent = "Abrir LinkedIn";
    link.dataset.mode = "linkedin";
  }

  showCurrentAttributes(link, output);
}

/* =========================================================
   5) ESCUCHAR EVENTOS (mínimo 3 tipos)
   Captura sugerida: función initEventListeners
   Eventos: click, mouseover/mouseout, submit, input
   ========================================================= */
function initEventListeners() {
  const hoverBox = document.getElementById("caja-hover");
  const form = document.getElementById("form-contacto-demo");
  const input = document.getElementById("input-nombre-demo");
  const live = document.getElementById("evento-live");
  const clickBtn = document.getElementById("btn-evento-click");

  if (clickBtn && live) {
    // Evento 1: click
    clickBtn.addEventListener("click", () => {
      live.textContent = "Evento click detectado: mensaje actualizado.";
    });
  }

  if (hoverBox && live) {
    // Evento 2: mouseover / mouseout
    hoverBox.addEventListener("mouseover", () => {
      hoverBox.style.backgroundColor = "#fef3c7";
      live.textContent = "Evento mouseover: el cursor está sobre la caja.";
    });
    hoverBox.addEventListener("mouseout", () => {
      hoverBox.style.backgroundColor = "";
      live.textContent = "Evento mouseout: el cursor salió de la caja.";
    });
  }

  if (input && live) {
    // Evento 3: input
    input.addEventListener("input", (event) => {
      const value = event.target.value.trim();
      live.textContent = value
        ? `Evento input: estás escribiendo "${value}".`
        : "Evento input: el campo está vacío.";
    });
  }

  if (form && live) {
    // Evento 4 (extra): submit
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const name = input ? input.value.trim() : "";
      live.textContent = name
        ? `Evento submit: gracias, ${name}. Formulario capturado sin recargar.`
        : "Evento submit: escribe un nombre antes de enviar.";
    });
  }
}

/* =========================================================
   6) CREAR, INSERTAR Y ELIMINAR ELEMENTOS
   Captura sugerida: funciones addDynamicItem / removeDynamicItem
   ========================================================= */
function initElementCRUD() {
  const addBtn = document.getElementById("btn-agregar-item");
  const clearBtn = document.getElementById("btn-limpiar-lista");
  const list = document.getElementById("lista-dinamica");
  const input = document.getElementById("nuevo-item");
  if (!addBtn || !list) return;

  addBtn.addEventListener("click", () => addDynamicItem(list, input));
  if (clearBtn) {
    clearBtn.addEventListener("click", () => {
      list.innerHTML = "";
    });
  }
}

function addDynamicItem(list, input) {
  const text = (input && input.value.trim()) || `Logro ${list.children.length + 1}`;

  // Crear elemento
  const li = document.createElement("li");
  const span = document.createElement("span");
  span.textContent = text;

  const removeBtn = document.createElement("button");
  removeBtn.type = "button";
  removeBtn.className = "btn btn-sm btn-outline-danger";
  removeBtn.textContent = "Eliminar";
  removeBtn.addEventListener("click", () => removeDynamicItem(li));

  li.appendChild(span);
  li.appendChild(removeBtn);

  // Insertar en el DOM
  list.appendChild(li);

  if (input) input.value = "";
}

function removeDynamicItem(node) {
  // Eliminar elemento del DOM
  node.remove();
}
