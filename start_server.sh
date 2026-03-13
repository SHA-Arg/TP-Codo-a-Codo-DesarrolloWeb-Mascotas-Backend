#!/bin/bash
cd "$(dirname "$0")"
echo "Matando procesos Python anteriores..."
taskkill //F //IM python.exe 2>/dev/null || true
sleep 1
echo "Iniciando servidor Flask en http://127.0.0.1:5000"
echo "Presiona Ctrl+C para detener"
echo "-------------------------------------------"
./venv/Scripts/python app.py
