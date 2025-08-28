# Publicar en GitHub

## Primer push
```bash
git init
git add .
git commit -m "feat: initial ROS2 + PCL demo with docs"
git branch -M main
git remote add origin git@github.com:andresislas99/ros2_pcl_ws.git
git push -u origin main
```

## Tags/Releases
```bash
git tag v0.1.0
git push origin v0.1.0
```

## Sugerencias
- Issues con etiquetas y plantillas.
- Badge de CI visible en el README.
- GIF/imagen de RViz en `docs/img/` enlazado desde el README.
