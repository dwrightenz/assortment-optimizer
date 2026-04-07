# Assortment Optimizer

## Project Overview
Herramienta de optimización de surtido basada en scores. Pure client-side SPA (HTML + JS).
- **Owner:** David (VP Comercial Alimentos, CF)
- **Port:** 5002 (`python3 serve.py`)
- **Origin:** Exportado desde Claude.ai artifact (single HTML file)

## Critical Rules
- **Todo es client-side** — no hay backend ni base de datos
- **No agregar dependencias server-side** — mantener como SPA puro
- **SheetJS (xlsx.js)** para parsing de Excel — ya incluido en el HTML
- Los archivos HTML son autocontenidos — CSS, JS, y lógica en un solo archivo

## Input Files
- **Dataset Unificado:** Excel con 5 hojas (VENTA USD, VENTAS UND, RENTABILIDAD NC, MARGEN NC, ALCANCE) en formato long (1 fila = 1 SKU × 1 local). Detectado automáticamente.
- **Ventas:** Excel cross-table con 4 métricas por local (Venta, Rentabilidad, Unidades, Margen)
- **Alcances:** Excel con Clase R (1=active, campo binario)
- Se puede subir Dataset Unificado O Ventas+Alcances por separado (mutuamente excluyentes en la UI)

## Score Formula
`Score = 0.40×%Rent + 0.25×%Vta + 0.20×%Uds + 0.15×%Mrg`
- Threshold: Score < 25 = candidato a retiro

## Features
- Percentile ranking por score
- Simulación de retiro/activación de SKUs
- Modelo de canibalización
- Análisis por marca
- Exports: CSV, multi-sheet XLSX, native PPTX

## Structure
```
Assortment Optimizer.html      — Main SPA
Assortment Optimizer Cel.html  — Versión Cel (variante)
serve.py                       — Simple HTTP server
```

## Agent Usage
- **commercial-analyst** → Análisis de resultados de optimización, impacto en márgenes
- **market-researcher** → Benchmarking de prácticas de assortment optimization en retail LATAM
