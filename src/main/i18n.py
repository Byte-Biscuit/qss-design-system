# -*- coding: utf-8 -*-
import locale
from main.logger_config import log


i18n = {
    "zh": {
        "base_style_button": (
            "🌈 可选基础按钮类型有：primary, default, dashed, text, link。\n"
            "👉 使用方式：button.setProperty('class', 'default')\n"
            "🧪 示例：将按钮设置为“虚线样式”：button.setProperty('class', 'dashed')\n"
            "🎯 样式类名可叠加，如 primary large danger 表示主按钮、大尺寸、危险状态"
        ),
        "size_style_button": (
            "🔍 可选按钮尺寸有：large, small。\n"
            "👉 使用方式：button.setProperty('class', 'primary large')\n"
            "🧪 示例：将按钮设置为“大尺寸”：button.setProperty('class', 'large')\n"
            "🎯 样式类名可叠加，如 primary large danger 表示主按钮、大尺寸、危险状态"
        ),
        "danger_style_button": (
            "⚠️ 可选危险按钮类型有：primary, default, dashed, text, link。\n"
            "👉 使用方式：button.setProperty('class', 'default danger')\n"
            "🧪 示例：将按钮设置为“虚线样式”：button.setProperty('class', 'dashed danger')\n"
            "🎯 样式类名可叠加，如 primary large danger 表示主按钮、大尺寸、危险状态"
        ),
        "base_style_line_edit": (
            "🌈 可选基础输入框类型有：success, warning, error。\n"
            "👉 使用方式：line_edit.setProperty('class', 'success')\n"
            "🧪 示例：将输入框设置为“成功样式”：line_edit.setProperty('class', 'success')\n"
            "🎯 样式类名可叠加，如 success large danger 表示成功状态、大尺寸、危险状态"
        ),
        "disabled_style_line_edit": (
            "🔒 输入框的禁用状态是默认伪类，无需通过 class 设置。\n"
            "👉 直接将组件设置为禁用状态：line_edit.setDisabled(True)\n"
            "🧪 示例：将输入框设置为禁用：line_edit.setDisabled(True)\n"
            "🎯 样式类名可叠加，如 success large danger 表示成功状态、大尺寸、危险状态"
        ),
        "size_style_line_edit": (
            "🔍 可选输入框尺寸有：large, small。\n"
            "👉 使用方式：line_edit.setProperty('class', 'large')\n"
            "🧪 示例：将输入框设置为“大尺寸”：line_edit.setProperty('class', 'large')\n"
            "🎯 样式类名可叠加，如 success large danger 表示成功状态、大尺寸、危险状态"
        ),
        "default_style_tree_view": (
            "🌳 树形视图样式已预设，导入QSS后自动生效。\n"
            "👉 使用方式：需要正确设置QDir并处理资源路径\n"
            "🧪 示例代码：\n"
            "       # qss_file为pathlib的Path对象\n"
            "       with open(file=qss_file, mode='r', encoding='utf-8') as fp:\n"
            "           QDir.setCurrent(qss_file.parent.as_posix())\n"
            "           style_sheet = fp.read()\n"
            "           style_sheet = style_sheet.replace('url(icons/', f'url({qss_file.parent.as_posix()}/icons/')\n"
            "           self.window.setStyleSheet(style_sheet)\n"
            "🎯 此代码可解决树形视图中图标资源路径问题"
        ),
        "full_style_label": (
            "🎨 QLabel 支持多种状态样式：info、success、warning、error。\n"
            "📏 可选尺寸类：small、normal（默认）、large。\n"
            "👉 使用方式：label.setProperty('class', 'info') 或 'success large' 等。\n"
            "🧪 示例：设置标签为成功状态并使用大尺寸：label.setProperty('class', 'success large')。\n"
            "🎯 样式类名可叠加，例如 'warning small' 表示警告状态+小尺寸。\n"
            "📐 宽度与文字布局未强制设定，建议使用 Qt Designer 中的布局功能进行控制。"
        ),
        "plain_text_edit_style": (
            "📝 QPlainTextEdit 样式已预设，导入QSS后自动生效。\n"
            "👉 使用方式：无需进行额外样式设定\n"
            "🧪 仅需导入QSS文件，样式将自动应用\n"
            "🎯 包含默认文本颜色、背景色、边框等基础样式"
        ),
        "text_browser_style": (
            "📖 QTextBrowser 样式已预设，导入QSS后自动生效。\n"
            "👉 用于显示只读的富文本HTML内容\n"
            "🧪 支持超链接、格式化文本等富文本特性\n"
            "🎯 默认样式包含边框hover效果和焦点状态"
        ),
        "splitter_style": (
            "🔧 分割线样式已预设，导入QSS后自动生效。\n"
            "👉 使用方式：无需进行额外样式设定\n"
            "🧪 仅需导入QSS文件，样式将自动应用\n"
            "🎯 包含默认分割线颜色、宽度等基础样式"
        ),
        "check_box_style": (
            "🔲 复选框样式已预设，导入QSS后自动生效。\n"
            "👉 可选尺寸有：small、large。\n"
            "🧪 示例：check_box.setProperty('class', 'small') 或 check_box.setProperty('class', 'large')\n"
            "🎯 当前仅支持不同尺寸（small/large），没有不同的颜色设定"
        ),
        "combo_box_style": (
            "🔳 下拉框样式已预设,导入QSS后自动生效。\n"
            "👉 可选尺寸有:small、large。\n"
            "🧪 示例:combo_box.setProperty('class', 'small') 或 combo_box.setProperty('class', 'large')\n"
            "🎯 当前仅支持不同尺寸(small/large),没有不同的颜色设定"
        ),
        "spin_box_style": (
            "🔢 数字输入框样式已预设,导入QSS后自动生效。\n"
            "👉 可选状态有:success、warning、error。\n"
            "📏 可选尺寸有:small、large。\n"
            "🧪 示例:spin_box.setProperty('class', 'success') 或 spin_box.setProperty('class', 'large')\n"
            "🎯 样式类名可叠加,如 success large 表示成功状态、大尺寸\n"
            "✨ 同时支持 QSpinBox 和 QDoubleSpinBox"
        ),
        "status_bar_style": (
            "🛠️ QStatusBar 状态栏样式说明：\n"
            "1️⃣ 已内置多种状态（info, warning, error），导入QSS后自动生效。\n"
            "2️⃣ 通过 status_bar.setProperty('class', 'info') 等切换不同状态，支持 info（信息）、warning（警告）、error（错误）。\n"
            "3️⃣ 切换状态时，先清除原有 class，再设置新状态，并调用 unpolish/polish 以刷新样式：\n"
            "       status_bar.setProperty('class', 'info')\n"
            "       status_bar.showMessage('信息提示')\n"
            "       status_bar.style().unpolish(status_bar)\n"
            "       status_bar.style().polish(status_bar)\n"
            "4️⃣ 每种状态会自动显示对应的背景色、图标和文字颜色。\n"
            "5️⃣ 注意：状态栏的 class 只支持单一状态（不可叠加多个状态类）。\n"
            "7️⃣ 默认状态（无 class 或 class 设为 ''）为普通样式。\n"
        ),
    },
    "en": {
        "base_style_button": (
            "🌈 Available base button types: primary, default, dashed, text, link.\n"
            "👉 Usage: button.setProperty('class', 'default')\n"
            "🧪 Example: set button to dashed: button.setProperty('class', 'dashed')\n"
            "🎯 You can combine class names like 'primary large danger' for style mix"
        ),
        "size_style_button": (
            "🔍 Available sizes: large, small.\n"
            "👉 Usage: button.setProperty('class', 'primary large')\n"
            "🧪 Example: set button to large: button.setProperty('class', 'large')\n"
            "🎯 Class names can be combined, e.g., 'primary large danger'"
        ),
        "danger_style_button": (
            "⚠️ Available danger button types: primary, default, dashed, text, link.\n"
            "👉 Usage: button.setProperty('class', 'default danger')\n"
            "🧪 Example: set button to dashed: button.setProperty('class', 'dashed danger')\n"
            "🎯 Combine class names like 'primary large danger' for styling"
        ),
        "base_style_line_edit": (
            "🌈 Available base input types: success, warning, error.\n"
            "👉 Usage: line_edit.setProperty('class', 'success')\n"
            "🧪 Example: set input to success: line_edit.setProperty('class', 'success')\n"
            "🎯 Class names can be combined, e.g., 'success large danger' for style mix"
        ),
        "disabled_style_line_edit": (
            "🔒 The disabled state of the input box is a default pseudo-class and does not require class settings.\n"
            "👉 Directly set the component to disabled: line_edit.setDisabled(True)\n"
            "🧪 Example: set the input box to disabled: line_edit.setDisabled(True)\n"
            "🎯 Class names can be combined, e.g., 'success large danger' for style mix"
        ),
        "size_style_line_edit": (
            "🔍 Available input sizes: large, small.\n"
            "👉 Usage: line_edit.setProperty('class', 'large')\n"
            "🧪 Example: set input to large: line_edit.setProperty('class', 'large')\n"
            "🎯 Class names can be combined, e.g., 'success large danger' for style mix"
        ),
        "default_style_tree_view": (
            "🌳 The tree view style is preset and will take effect automatically after importing QSS.\n"
            "👉 Usage: Ensure correct QDir and resource path handling\n"
            "🧪 Example code:\n"
            "       # qss_file is a pathlib Path object\n"
            "       with open(file=qss_file, mode='r', encoding='utf-8') as fp:\n"
            "           QDir.setCurrent(qss_file.parent.as_posix())\n"
            "           style_sheet = fp.read()\n"
            "           style_sheet = style_sheet.replace('url(icons/', f'url({qss_file.parent.as_posix()}/icons/')\n"
            "           self.window.setStyleSheet(style_sheet)\n"
            "🎯 This code resolves the icon resource path issue in the tree view."
        ),
        "full_style_label": (
            "🎨 QLabel supports multiple state styles: info, success, warning, and error.\n"
            "📏 Available size classes: small, normal (default), and large.\n"
            "👉 Usage: label.setProperty('class', 'info') or use 'success large', etc.\n"
            "🧪 Example: Set the label to success state with large size: label.setProperty('class', 'success large')\n"
            "🎯 Class names can be combined, such as 'warning small' for warning state + small size.\n"
            "📐 Width and text alignment are not fixed — use Qt Designer's layout system for control."
        ),
        "plain_text_edit_style": (
            "📝 QPlainTextEdit style is preset and will take effect automatically after importing QSS.\n"
            "👉 Usage: No additional style settings required\n"
            "🧪 Just import the QSS file, and the style will be applied automatically\n"
            "🎯 Includes default text color, background color, border, and other basic styles"
        ),
        "text_browser_style": (
            "📖 QTextBrowser style is preset and will take effect automatically after importing QSS.\n"
            "👉 Used for displaying read-only rich text HTML content\n"
            "🧪 Supports hyperlinks, formatted text, and other rich text features\n"
            "🎯 Default style includes border hover effect and focus state"
        ),
        "splitter_style": (
            "🔧 Splitter style is preset and will take effect automatically after importing QSS.\n"
            "👉 Usage: No additional style settings required\n"
            "🧪 Just import the QSS file, and the style will be applied automatically\n"
            "🎯 Includes default splitter color, width, and other basic styles"
        ),
        "check_box_style": (
            "🔲 Check box style is preset and will take effect automatically after importing QSS.\n"
            "👉 Available sizes: small, large.\n"
            "🧪 Example: check_box.setProperty('class', 'small') or check_box.setProperty('class', 'large')\n"
            "🎯 Only different sizes (small/large) are supported currently, no color variations"
        ),
        "combo_box_style": (
            "🔳 Combo box style is preset and will take effect automatically after importing QSS.\n"
            "👉 Available sizes: small, large.\n"
            "🧪 Example: combo_box.setProperty('class', 'small') or combo_box.setProperty('class', 'large')\n"
            "🎯 Only different sizes (small/large) are supported currently, no color variations"
        ),
        "spin_box_style": (
            "🔢 Spin box style is preset and will take effect automatically after importing QSS.\n"
            "👉 Available states: success, warning, error.\n"
            "📏 Available sizes: small, large.\n"
            "🧪 Example: spin_box.setProperty('class', 'success') or spin_box.setProperty('class', 'large')\n"
            "🎯 Class names can be combined, e.g., 'success large' for success state + large size\n"
            "✨ Supports both QSpinBox and QDoubleSpinBox"
        ),
        "status_bar_style": (
            "🛠️ QStatusBar style explanation:\n"
            "1️⃣ Multiple states (info, warning, error) are built-in and will take effect automatically after importing QSS.\n"
            "2️⃣ Switch states using status_bar.setProperty('class', 'info') etc., supporting info (information), warning (warning), error (error).\n"
            "3️⃣ When switching states, first clear the existing class, then set the new state, and call unpolish/polish to refresh the style:\n"
            "       status_bar.setProperty('class', 'info')\n"
            "       status_bar.showMessage('Information message')\n"
            "       status_bar.style().unpolish(status_bar)\n"
            "       status_bar.style().polish(status_bar)\n"
            "4️⃣ Each state will automatically show corresponding background color, icon, and text color.\n"
            "5️⃣ Note: The class of the status bar only supports a single state (cannot combine multiple state classes).\n"
            "6️⃣ Default state (no class or class set to '') is normal style.\n"
        ),
    },
}

lang = None


def get_sys_lang():
    lang_code, _ = locale.getdefaultlocale()
    log.info(f"System language code: {lang_code}")
    if lang_code and lang_code.startswith("zh"):
        return "zh"
    else:
        return "en"


def get_text(key):
    global lang
    if lang is None:
        lang = get_sys_lang()
    if lang in i18n and key in i18n[lang]:
        return i18n[lang][key]
    else:
        return ""
