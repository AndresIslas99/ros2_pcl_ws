# Contribuir a ros2_pcl_ws

## Flujo
1. Haz **fork** y crea rama: `git switch -c feature/nombre`.
2. Ejecuta linters/tests localmente (si aplica).
3. Abre un **Pull Request** a `main` describiendo cambios y pruebas.

## Estilo
- C++: `ament_uncrustify` / `ament_cpplint`.
- Python: `ament_flake8` / `ament_pep257`.

## Commits / PR
- Mensajes claros (`feat:`, `fix:`, `docs:`…).
- Incluye resultados de `colcon test` y capturas si aplica.
