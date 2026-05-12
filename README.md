<p align="center">
  <h1 align="center">🔒 latex-privacy</h1>
  <p align="center"><i>Strip stylistic fingerprints from LaTeX source before sharing.</i></p>
  <p align="center"><i>在分享 .tex 源码之前，抹掉你的写作风格痕迹。</i></p>
</p>

<p align="center">
  <a href="https://pypi.org/project/texfuscate/"><img src="https://img.shields.io/pypi/v/texfuscate" alt="PyPI"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License"></a>
  <a href="https://github.com/Sylvan/latex-privacy"><img src="https://img.shields.io/github/stars/Sylvan/latex-privacy?style=social" alt="Stars"></a>
</p>

---

## 📌 Overview · 概述

**latex-privacy** (packaged as `texfuscate`) applies **semantics-preserving transformations** to LaTeX source code, removing stylistic fingerprints before you share `.tex` files with collaborators, submit to journals, or upload to public repositories.

**latex-privacy**（pip 包名 `texfuscate`）是一个 LaTeX 源码隐私保护工具。它对你的 `.tex` 文件进行**语义无损的变换**，抹掉个人写作风格痕迹，再分享给合作者、投稿或上传到公开仓库。

The compiled PDF is **content-identical** — only the source representation changes. Not a single character, formula, or layout element is altered.

编译后的 PDF **内容完全不变**——只是源码的"长相"变了。论文里的文字、公式、图表、排版，一个像素都不动。

### Key Features · 核心特性

| English | 中文 |
|---------|------|
| ✅ **Content-preserving** – PDF output unaffected | ✅ **内容不变** – PDF 输出完全一致 |
| ✅ **Strips writing-style signatures** – comments, spacing, command variants | ✅ **抹去写作风格指纹** – 注释、空格、命令偏好全部随机化 |
| ✅ **One command** – CLI tool + Python API | ✅ **一键使用** – 命令行 + Python API |
| ✅ **Collaborator-ready** – share `.tex` without exposing personal patterns | ✅ **放心协作** – 分享源码时不泄露个人写法习惯 |

---

## 🚀 Why Do I Need This? · 什么时候用？

### English

When you share `.tex` files, you unintentionally expose:

- **Personal writing habits** – your preferred LaTeX commands, spacing patterns, comment style.
- **Tool provenance** – AI-assisted writing leaves characteristic patterns in source code that can be identified.
- **Revision history** – collaborators can see exactly how the source evolved.

latex-privacy **decouples** what the source *looks like* from what the PDF *renders as*. The transformations are semantically null — LaTeX compilers ignore them entirely — but they effectively anonymize the source representation.

### 中文

分享 `.tex` 源码时，你无意中暴露了这些信息：

- **个人写作习惯** – 你爱用的命令风格、空格方式、注释频率。
- **工具来源** – 用 AI 辅助写出来的 LaTeX 源码有可识别的特征。
- **修改痕迹** – 合作者能从源码看出哪些地方改过。

latex-privacy 的作用是让源码的"长相"和 PDF 的"内容"**脱钩**。所有变换都是语义无损的——LaTeX 编译器完全忽略它们——但源码层面的个人特征被抹掉了。

---

## 📦 Installation · 安装

### Via pip (recommended)

```bash
pip install texfuscate
```

### From source

```bash
git clone https://github.com/Sylvan/latex-privacy.git
cd latex-privacy
pip install -e .
```

---

## ⚡ Quick Start · 快速开始

```bash
# Medium strength (default) · 中强度混淆
texfuscate paper.tex -o paper_obf.tex

# High strength · 高强度混淆
texfuscate paper.tex -s high -o paper_obf.tex

# Reproducible · 固定随机种子以复现结果
texfuscate paper.tex --seed 42 -o paper_obf.tex
```

Compile the output and verify → **the PDF is identical** to the original.

```bash
pdflatex paper_obf.tex
```

编译输出的 PDF → **跟原版一模一样**。

---

## 🧠 Obfuscation Strategies · 混淆策略

| Strategy · 策略 | Effect · 作用 |
|----------------|---------------|
| Random comment injection (`% a1b2c`) | Breaks line-level profiling patterns · 打乱行级统计特征 |
| Zero-width spaces (`\hspace{0pt}`) | Disrupts character-position fingerprinting · 干扰字符位置分析 |
| Escaped spaces (`\ `) | Varies whitespace before punctuation · 改变标点前的空格表示 |
| Command synonym substitution (`\textbf` ↔ `{\bf }`) | Normalizes away command preferences · 抹平命令使用偏好 |
| Package option shuffling | Eliminates ordering signatures · 消除选项顺序特征 |
| Quote style variation (`"` ↔ `\`\` ''`) | Adds stylistic ambiguity · 增加引号风格不确定性 |
| Dummy macro injection | Pads statistical features with inert code · 注入无害宏代码 |

All transformations produce **zero change** in the rendered PDF.

所有变换对编译后的 PDF **零影响**。

---

## 📖 CLI Reference · 命令行参考

```
texfuscate [-h] [-o OUTPUT] [-s {low,medium,high}] [--seed SEED]
           [--no-comments] [--no-spaces] [--no-commands]
           [--no-options] [--no-quotes] [--no-macros]
           input
```

| Argument | Description | 说明 |
|----------|-------------|------|
| `input` | Input `.tex` file | 输入的 .tex 文件（必需） |
| `-o, --output` | Output file path | 输出文件路径 |
| `-s, --strength` | `low`, `medium` (default), `high` | 混淆强度 |
| `--seed` | Random seed for reproducibility | 随机种子，用于复现 |
| `--no-comments` | Disable comment injection | 禁用注释插入 |
| `--no-spaces` | Disable harmless space insertion | 禁用空格混淆 |
| `--no-commands` | Disable command replacement | 禁用命令替换 |
| `--no-options` | Disable package option shuffling | 禁用它选项打乱 |
| `--no-quotes` | Disable quote variation | 禁用引号变异 |
| `--no-macros` | Disable macro injection | 禁用宏注入 |

---

## 📝 Example · 示例

### Before · 混淆前

```latex
\documentclass{article}
\begin{document}
This is a \textbf{test}. See \cite{key}.
\end{document}
```

### After (medium) · 混淆后（中等强度）

```latex
\documentclass{article} % k9m2n
\begin{document}
This is a \textbf{test} \hspace{0pt}. See \citep{key}. % r5t8v
\end{document}
% \def\zzx{}
\zzx
```

---

## ⚠️ Limitations · 局限性

| English | 中文 |
|---------|------|
| latex-privacy operates **only on LaTeX source**. It cannot alter PDF-rendered text. | **仅作用于源码层面**，无法改变 PDF 渲染后的文字。 |
| The obfuscation is **not cryptographically secure** — a motivated analyst can reverse comments and whitespace changes. | 混淆**不是加密**，有动机的分析者可以还原注释和空格。 |
| Output files are **larger** (especially at high strength). Compilation time is unaffected. | 输出文件**体积变大**（高强度下更明显），但编译时间不变。 |
| If a reviewer analyzes the **compiled PDF's text content** (not the source), this tool has no effect. | 如果审稿人分析的是**编译后的 PDF 文本**，此工具无效。 |

---

## 🤝 Contributing · 贡献

PRs welcome! Especially new obfuscation strategies that preserve semantics while adding source-level noise.

欢迎提交 PR！特别是新的混淆策略——只要不改变语义，不限于已有的几种。

---

## 📄 License · 许可证

MIT

---

## ⚖️ Disclaimer · 免责声明

latex-privacy is a **privacy tool** for protecting source-level writing style. It is not designed or intended to facilitate academic dishonesty, plagiarism, or the circumvention of integrity policies. Users are solely responsible for complying with their institution's code of conduct.

latex-privacy 是一个**源码隐私保护工具**，用于保护个人写作风格不被 profiling。它不是也不打算用于学术不端、抄袭或规避诚信政策。使用者自行负责遵守所在机构的学术规范。
