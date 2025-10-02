package main

import (
	"encoding/json"
	"net/http"
	"time"
)

type Producto struct {
	ID     int    `json:"id"`
	Nombre string `json:"nombre"`
	Stock  int    `json:"stock"`
}

func main() {
	http.HandleFunc("/inventario", func(w http.ResponseWriter, r *http.Request) {
		inventario := []Producto{
			{ID: 1, Nombre: "Laptop", Stock: 12},
			{ID: 2, Nombre: "Mouse", Stock: 34},
			{ID: 3, Nombre: "Teclado", Stock: 20},
		}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(inventario)
	})

	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		status := map[string]string{
			"status":  "ok",
			"service": "inventario",
			"uptime":  time.Now().Format(time.RFC3339),
		}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(status)
	})

	http.ListenAndServe(":5002", nil)
}
