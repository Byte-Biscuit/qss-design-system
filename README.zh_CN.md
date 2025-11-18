# qss-design-system

[English](README.md)

一个用于 PySide6 (Qt for Python) 桌面应用的 QSS 设计系统示例与打包工具。

此项目的目标是：提供一套基于 QSS 的组件样式，使得在其他 PySide6 项目中只需引入生成的 `.qss` 文件与图标资源，便可获得一致、可复用的 UI 风格（视觉参考：Ant Design）。

## 目录结构

-   `src/main/ui/` - 包含 `qss_desigin_system.qss`、`icons/` 等 UI 资源
-   `src/main/style/` - SCSS 源文件（可通过 `build.py` 编译为 QSS）
-   `src/main/build.py` - 把 SCSS 编译为 QSS 的脚本（使用 libsass）
-   `scripts/package_qss.ps1` - Windows PowerShell 脚本：读取 `pyproject.toml` 的版本，打包 `.qss` 和 `icons/` 为 `qss-desigin-system.<version>.zip`
-   `pyproject.toml` - 项目元数据（版本、依赖、Python 要求等）

## 快速开始

本项目使用 `uv` 管理依赖与运行环境。下面示例在 Windows / PowerShell 中演示常用操作。

1. 验证 `uv` 可用：

    ```powershell
    uv --version
    ```

2. 同步/安装项目依赖（根据 `pyproject.toml`）：

    ```powershell
    uv sync
    ```

3. 编译 SCSS 为 QSS（在 uv 管理的环境中运行）：

    ```powershell
    uv run python src/main/build.py

    # 备用（如果不使用 uv）
    & .\.venv\Scripts\python.exe src\main\build.py
    ```

4. 在 uv 环境中运行示例应用（用于预览样式）：

    ```powershell
    uv run python src/main/qss_desigin_system.py

    # 备用（如果不使用 uv）
    & .\.venv\Scripts\python.exe src\main\qss_desigin_system.py
    ```

5. 打包 QSS 与图标为版本化 ZIP：

    ```powershell
    # 在 uv 管理的环境中运行 PowerShell 打包脚本：
    uv run pwsh -File .\scripts\package_qss.ps1

    # 或者直接在宿主 shell 中运行：
    .\scripts\package_qss.ps1
    # 输出文件将位于 ./dist/qss-desigin-system.<version>.zip
    ```

## 使用说明

-   打包后得到的 zip 内包含 `qss_desigin_system.qss` 与 `icons/` 文件夹。
-   引入到目标项目时：
    -   将 `qss_desigin_system.qss` 放到项目资源目录并在程序启动时加载为应用样式（例如 `QApplication.setStyleSheet(...)`）。
    -   保持 `icons/` 的相对路径或按需修改 `url(...)` 路径。

示例（PySide6）:

```python
from PySide6.QtWidgets import QApplication
app = QApplication([])
# 假设 qss 路径和 icons 路径已正确设置
with open('path/to/qss_desigin_system.qss', 'r', encoding='utf-8') as f:
    app.setStyleSheet(f.read())
```

## 兼容性与注意事项

-   本项目在 `pyproject.toml` 中声明的 Python 范围建议为 `>=3.9, <3.14`（PySide6 >=6.9 支持 Python 3.9–3.13）。
-   QSS 样式在不同平台（Windows/Linux/macOS）上的渲染会有细微差别，必要时在目标平台上进行微调。

![GUI](images/screenshot-1.png)

## 贡献

欢迎提交 issue 或 pull request：

-   修复样式问题或补充组件样式
-   添加更多 UI 示例
-   改进打包脚本（跨平台）、增加自动化测试

提交 PR 前请确保：

-   在本地运行 `src/main/build.py` 并检查生成的 QSS
-   提交清晰的变更说明与截图（如果是视觉调整）

## 许可证

本项目采用 MIT 许可证，详见 `LICENSE.txt`。
