# -*- coding: utf-8 -*-
import sass
from pathlib import Path
from main.logger_config import log
import tomllib

work_dir = Path(__file__).resolve().parent


def get_project_info(pyproject_path: Path) -> str | None:
    with pyproject_path.open("rb") as f:
        data = tomllib.load(f)
    return data.get("project", {})


def compile_scss_to_qss(input_file: Path, output_file: Path):
    try:
        pyproject_path = work_dir.parent / ".." / "pyproject.toml"
        version = get_project_info(pyproject_path).get("version", "0.0.1")
        description = get_project_info(pyproject_path).get(
            "description", "No description provided."
        )
        compiled = sass.compile(filename=input_file, output_style="expanded")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(
                f"""/**
* QSS-DESIGN-SYSTEM
* version: {version}
* author: biscuit_zhou@outlook.com
* description: {description}
* github: https://github.com/Byte-Biscuit/qss-desigin-system
*/
"""
            )
            f.write(compiled)
        log.info(f"Build successfully: {input_file} → {output_file}")
    except sass.CompileError as e:
        log.error(f"[!] Compile error: {e}", exc_info=True)
    except Exception as ex:
        log.error(f"[!] Unknown error: {ex}", exc_info=True)


if __name__ == "__main__":
    scss_input = Path(work_dir, "style", "main.scss")
    qss_output = Path(work_dir, "ui", "qss_desigin_system.qss")
    compile_scss_to_qss(str(scss_input), str(qss_output))
