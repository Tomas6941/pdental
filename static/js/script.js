document.getElementById("formTurno").addEventListener("submit", function(e) {
  e.preventDefault();
  document.getElementById("respuesta").innerText =
    "Turno enviado correctamente (modo demo).";
});
