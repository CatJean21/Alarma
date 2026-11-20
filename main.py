"""Punto de entrada principal de la aplicación de Alarma."""

from src.config import ensure_directories
from src.ui.main_window import run_app


def main() -> None:
    """Inicializa directorios necesarios y arranca la interfaz gráfica."""
    ensure_directories()
    run_app()


if __name__ == "__main__":
    main()
