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

## 📌 这是什么？

一个 **LaTeX 源码隐私保护工具**。你在分享 `.tex` 文件之前跑一下它——它会往源码里加一堆"无害的噪音"（随机注释、不占空间的命令、等效命令替换等）。

**效果：** 别人拿到你的 `.tex` 文件，看不出你的个人写作习惯和工具痕迹。但编译出来的 PDF **跟原来一模一样**，一个字、一个公式、一张图都不变。

---

## 🚀 什么时候用？

| 场景 | 说明 |
|------|------|
| 把 `.tex` 发给合作者 | 对方能看论文内容，看不出源码是谁写的 |
| 上传到 GitHub 公开仓库 | 源码里的个人风格特征被抹掉了 |
| 投稿前清理源码 | 去除编辑器和辅助工具留下的痕迹 |

---

## 📦 安装（小白教程）

### 第一步：下载代码

打开终端（CMD 或 PowerShell），输入：

```bash
git clone https://github.com/sylvanlisayhi-cyber/latex-privacy.git
```

这会把代码下载到你电脑上。

### 第二步：进入文件夹

```bash
cd latex-privacy
```

### 第三步：安装

```bash
pip install -e .
```

> 如果提示 `pip` 不是命令，说明你没装 Python。先去 [python.org](https://python.org) 下载安装 Python 3.7 以上版本，安装时勾选"Add Python to PATH"。

安装完成后，你就可以在命令行使用 `texp` 命令了。

---

## ⚡ 快速使用

```bash
# 基本用法（中强度）
texp paper.tex -o paper_obf.tex

# 高强度
texp paper.tex -s high -o paper_obf.tex

# 固定随机种子（每次运行结果一样，方便对比）
texp paper.tex --seed 42 -o paper_obf.tex
```

然后正常编译 PDF：

```bash
pdflatex paper_obf.tex
```

**对比一下：** 打开原版 PDF 和混淆后编译的 PDF——它们完全一样。再对比两个 `.tex` 源码——不一样了。

---

## 🧠 它到底改了源码的什么？

| 手法 | 举例 | 作用 |
|------|------|------|
| 插入随机注释 | `\section{Intro} % x9k2m` | 打乱行级统计特征 |
| 加零宽空格 | `\hspace{0pt}`（编译后看不见） | 干扰字符位置分析 |
| 加转义空格 | 单词 `word.` → `word\ .` | 改变空格表示方式 |
| 替换等效命令 | `\textbf{xxx}` ↔ `{\bf xxx}` | 抹平命令使用偏好 |
| 打乱包选项顺序 | 随机排列 `\usepackage[opt1,opt2]` 里的选项 | 消除顺序特征 |
| 变异引号风格 | `"text"` ↔ `` ``text'' `` | 增加风格不确定性 |
| 注入假宏 | 定义 `\def\zzx{}` 并在文中随机调用 | 增加源码噪声 |

所有改法都是 **LaTeX 编译器直接忽略的东西**，所以 PDF 一点不变。

---

## 📖 命令大全

```bash
texp [-h] [-o OUTPUT] [-s {low,medium,high}] [--seed SEED]
     [--no-comments] [--no-spaces] [--no-commands]
     [--no-options] [--no-quotes] [--no-macros]
     input
```

| 参数 | 作用 |
|------|------|
| `input` | 要处理的 `.tex` 文件（必填） |
| `-o, --output` | 输出文件名（默认在原名后加 `_obf`） |
| `-s, --strength` | 混淆强度：`low`（低）、`medium`（中，默认）、`high`（高） |
| `--seed` | 随机种子，填同样的数字每次结果一样 |
| `--no-comments` | 禁用注释插入 |
| `--no-spaces` | 禁用空格混淆 |
| `--no-commands` | 禁用命令替换 |
| `--no-options` | 禁用它选项打乱 |
| `--no-quotes` | 禁用引号变异 |
| `--no-macros` | 禁用宏注入 |

---

## 📝 完整示例

**混淆前：**

```latex
\documentclass{article}
\begin{document}
This is a \textbf{test}. See \cite{key}.
\end{document}
```

**运行 `texp paper.tex -o paper_obf.tex` 后：**

```latex
\documentclass{article} % k9m2n
\begin{document}
This is a \textbf{test} \hspace{0pt}. See \citep{key}. % r5t8v
\end{document}
% \def\zzx{}
\zzx
```

**编译 PDF：** `pdflatex paper_obf.tex` → 和原版一模一样。

---

## ⚠️ 注意

| 英文 | 中文 |
|------|------|
| Only works on **LaTeX source**, not compiled PDF text. | **只改源码**，不改 PDF 里的文字。 |
| **Not encryption** — a motivated person could reverse it. | 混淆**不是加密**，想查的人可以还原。 |
| Output files are **larger**, but compile time is unchanged. | 输出文件**变大**，但编译时间不变。 |
| If someone checks the **PDF content** (not the .tex), this tool does nothing. | 如果别人检查的是 **PDF 内容**（不是 .tex 源码），这工具没效果。 |

---

## 🤝 贡献

欢迎提交 PR！你有新的混淆思路（不改变语义的前提下）可以直接提。

---

## 📄 许可证

MIT

---

## ⚖️ 免责声明

这是一个**隐私保护工具**，用于保护源码层面的写作风格不被分析。它不是也不用于学术不端、抄袭或规避诚信政策。使用者自行负责。
