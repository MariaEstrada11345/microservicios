const express = require("express");
const app = express();
const PORT = 5000;

const usuarios = [
  { id: 1, nombre: "Ana López" },
  { id: 2, nombre: "Carlos Méndez" }
];

app.get("/usuarios", (req, res) => {
  res.json(usuarios);
});

app.get("/health", (req, res) => {
  res.json({ status: "ok", service: "usuarios" });
});

app.listen(PORT, () => {
  console.log(`Servicio de usuarios corriendo en puerto ${PORT}`);
});
