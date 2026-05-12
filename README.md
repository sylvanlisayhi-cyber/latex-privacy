<p align="center">
  <h1 align="center">🔒 latex-privacy</h1>
  <p align="center"><i>Strip stylistic fingerprints from LaTeX source before sharing.</i></p>
  <p align="center"><i>在分享 .tex 源码之前，抹掉你的写作风格痕迹。</i></p>
</p>

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License"></a>
  <a href="https://github.com/sylvanlisayhi-cyber/latex-privacy"><img src="https://img.shields.io/github/stars/sylvanlisayhi-cyber/latex-privacy?style=social" alt="Stars"></a>
</p>

---

## 📌 What is this? · 这是什么？

**latex-privacy** is a LaTeX source privacy tool. Before you share your `.tex` file, run this tool — it inserts harmless noise (random comments, invisible spaces, equivalent command swaps) into the source code. Other people will see different source code, but the compiled PDF stays **exactly the same**.

**latex-privacy** 是一个 LaTeX 源码隐私保护工具。在分享 `.tex` 文件之前跑一下它——它会往源码里插入无害的噪音。别人拿到你的源码看不出你的写作习惯，但 PDF 跟原来一模一样。

> **English:** Source changes, PDF doesn't.  
> **中文：** 源码变样了，PDF 一点没变。

---

## 🚀 When to use · 什么时候用？

| English | 中文 |
|---------|------|
| Share `.tex` with collaborators | 把 `.tex` 发给合作者前 |
| Upload to GitHub / Overleaf | 上传到 GitHub 或 Overleaf 前 |
| Submit to journals (source review) | 投稿前清理源码 |

---

## 📥 Download & Install · 下载与安装

> ⏱ Takes **2 minutes**, one-time setup.  
> ⏱ 整个过程只需 **2 分钟**，仅需做一次。

### Step 1 · 第 1 步：Download

Open this page, click the green **Code** button, then **Download ZIP**:

👉 **https://github.com/sylvanlisayhi-cyber/latex-privacy**

Extract the ZIP to your computer (e.g., Desktop).

把下载的 ZIP 解压到你电脑上（比如桌面）。

> If you know git: `git clone https://github.com/sylvanlisayhi-cyber/latex-privacy.git`  
> 如果你会用 git，也可以直接 clone。

### Step 2 · 第 2 步：Install

Open the `latex-privacy` folder. Click the address bar in File Explorer, type `cmd`, and press Enter.

打开解压后的 `latex-privacy` 文件夹，在地址栏输入 `cmd` 然后按回车。

In the black window, paste this command and press Enter:

在黑色窗口里粘贴这行命令，按回车：

```bash
pip install -e .
```

> **If `pip` is not found:** Install Python 3.7+ from [python.org](https://python.org), **check "Add Python to PATH"**, then retry.  
> **如果提示 `pip` 不是命令：** 去 python.org 下载 Python，安装时**务必勾选 "Add Python to PATH"**。

Done. Now you can use `texp` from the command line.

安装成功后，你就可以在命令行使用 `texp` 命令了。

---

## ⚡ Quick Start · 快速上手

```bash
# Medium strength (default) · 中强度（默认）
texp paper.tex -o paper_obf.tex

# High strength · 高强度
texp paper.tex -s high -o paper_obf.tex

# Low strength · 低强度
texp paper.tex -s low -o paper_obf.tex
```

Compile the output · 编译输出文件：

```bash
pdflatex paper_obf.tex
```

**Compare:** The PDF looks identical. The `.tex` files look different.  
**对比一下：** PDF 完全一样，但两个 `.tex` 文件不一样了。

---

## 📖 All Commands · 命令大全

### View help · 查看帮助

```bash
texp --help
```

### Basic usage · 基础用法

```bash
texp paper.tex -o paper_obf.tex    # Medium (default) · 中强度
texp paper.tex                      # Auto output name · 自动命名
```

### Strength levels · 强度选择

| Command · 命令 | Effect · 效果 |
|----------------|---------------|
| `texp paper.tex -s low -o out.tex` | Minimal changes · 改动较少 |
| `texp paper.tex -s medium -o out.tex` | Balanced (default) · 适中（默认） |
| `texp paper.tex -s high -o out.tex` | Maximum noise · 改动最多 |

### Reproducible output · 固定随机种子

```bash
texp paper.tex --seed 42 -o out1.tex
texp paper.tex --seed 42 -o out2.tex    # Same result · 结果一样
```

Same seed = same output. Useful for team collaboration.

填同样的数字，每次结果一样。适合团队协作。

### Enable/disable specific transforms · 开关特定功能

| Command · 命令 | Disables · 关闭 |
|----------------|-----------------|
| `texp paper.tex --no-comments -o out.tex` | Random comments · 随机注释 |
| `texp paper.tex --no-spaces -o out.tex` | Invisible spaces · 零宽空格 |
| `texp paper.tex --no-commands -o out.tex` | Command swapping · 命令替换 |
| `texp paper.tex --no-options -o out.tex` | Package option shuffle · 包选项打乱 |
| `texp paper.tex --no-quotes -o out.tex` | Quote variation · 引号变异 |
| `texp paper.tex --no-macros -o out.tex` | Dummy macros · 假宏注入 |

Combine them · 也可以组合：

```bash
# Only comments, nothing else · 只要注释
texp paper.tex --no-spaces --no-commands --no-options --no-quotes --no-macros -o out.tex

# Spaces + commands only, no comments · 只要空格和命令替换
texp paper.tex --no-comments --no-quotes -o out.tex
```

### Full parameter reference · 所有参数一览

| Argument · 参数 | Description · 作用 |
|-----------------|-------------------|
| `input` | Input `.tex` file (required) · 要处理的 .tex 文件（必填） |
| `-o, --output` | Output path (default: `input_obf.tex`) · 输出文件名 |
| `-s, --strength` | `low` / `medium` (default) / `high` · 混淆强度 |
| `--seed` | Random seed for reproducible output · 随机种子 |
| `--no-comments` | Disable comment injection · 禁用注释插入 |
| `--no-spaces` | Disable space insertion · 禁用空格混淆 |
| `--no-commands` | Disable command replacement · 禁用命令替换 |
| `--no-options` | Disable package option shuffling · 禁用选项打乱 |
| `--no-quotes` | Disable quote variation · 禁用引号变异 |
| `--no-macros` | Disable macro injection · 禁用宏注入 |

---

## 🧠 How it works · 原理

| Technique · 手法 | Example · 例子 | Effect · 作用 |
|------------------|---------------|--------------|
| Random comments · 随机注释 | `\section{Intro} % x9k2m` | Break line-level patterns · 打乱行级特征 |
| Zero-width spaces · 零宽空格 | `\hspace{0pt}` | Disrupt position fingerprinting · 干扰位置分析 |
| Escaped spaces · 转义空格 | `word.` → `word\ .` | Vary whitespace style · 改变空格表示 |
| Command substitution · 命令替换 | `\textbf{xxx}` ↔ `{\bf xxx}` | Normalize command preferences · 抹平命令偏好 |
| Package option shuffle · 选项打乱 | Randomize `\usepackage[...]` order | Remove ordering signatures · 消除顺序特征 |
| Quote variation · 引号变异 | `"text"` ↔ `` ``text'' `` | Add stylistic ambiguity · 增加风格不确定性 |
| Dummy macros · 假宏注入 | `\def\zzx{}` + `\zzx` | Pad statistical features · 增加源码噪声 |

**All changes are ignored by the LaTeX compiler. The PDF stays identical.**  
**所有改法都被 LaTeX 编译器忽略，PDF 完全不变。**

---

## 📝 Full Example · 完整示例

**Before · 混淆前:**

```latex
\documentclass{article}
\begin{document}
This is a \textbf{test}. See \cite{key}.
\end{document}
```

**After `texp paper.tex -o paper_obf.tex` · 混淆后:**

```latex
\documentclass{article} % k9m2n
\begin{document}
This is a \textbf{test} \hspace{0pt}. See \citep{key}. % r5t8v
\end{document}
% \def\zzx{}
\zzx
```

**Compile · 编译:**

```bash
pdflatex paper_obf.tex
```

Identical PDF. Different source.  
PDF 一样，源码不一样了。

---

## ⚠️ Limitations · 注意事项

| English | 中文 |
|---------|------|
| Only works on **LaTeX source**, not compiled PDF text. | **只改源码**，不改 PDF 里的文字。 |
| **Not encryption** — a motivated person could reverse it. | 混淆**不是加密**，想查的人可以还原。 |
| Output files are **larger**, but compile time is unchanged. | 输出文件**变大**，编译时间不变。 |
| If someone checks the **PDF content** (not the .tex), this tool does nothing. | 如果检查的是 **PDF 内容**，此工具无效。 |

---

## 🤝 Contributing · 贡献

PRs welcome — especially new obfuscation strategies that preserve semantics.

欢迎提交 PR！特别是新的混淆策略，只要不改变语义。

---

## 📄 License · 许可证

MIT

---

## ⚖️ Disclaimer · 免责声明

This is a **privacy tool** for protecting source-level writing style. It is not intended for academic dishonesty or plagiarism. Users are responsible for complying with their institution's code of conduct.

这是一个**隐私保护工具**，用于保护源码层面的写作风格不被分析。它不是也不用于学术不端或抄袭。使用者自行负责。
