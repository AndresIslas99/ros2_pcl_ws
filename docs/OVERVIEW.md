# Overview

## Objetivo
Pipeline reproducible para nubes 3D:
1) Publisher sintético → sin hardware.
2) Filtro PCL PassThrough → ROI/ejes.
3) RViz2 → visualización inmediata.

## Extensiones
- Cambiar fuente por LiDAR/cámara de profundidad.
- Añadir VoxelGrid / SOR / RANSAC.
- Publicar normales y colorear por curvatura.

## Buenas prácticas
- Ignora `build/ install/ log/`.
- Documenta topics, frames y parámetros.
- CI mínimo para compilar en Ubuntu limpio.
