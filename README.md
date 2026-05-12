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

## 📌 这是什么？ / What is this?

**latex-privacy** 是一个 LaTeX 源码隐私保护工具。

你写好了论文的 `.tex` 文件，在分享之前跑一下这个工具——它会往源码里插入一堆"无害的噪音"。别人拿到你的 `.tex` 文件，看不出你的个人写作习惯和工具痕迹。但编译出来的 PDF **跟原来一模一样**。

> **一句话：源码变样了，PDF 一点没变。**

---

## 🚀 什么时候用？ / When to use it?

| 场景 | 说明 |
|------|------|
| 把 `.tex` 发给合作者 | 对方能看论文内容，看不出是谁写的 |
| 上传到 GitHub / Overleaf | 源码里的个人风格特征被抹掉了 |
| 投稿前清理源码 | 去除编辑器和辅助工具留下的痕迹 |

---

## 📥 下载与安装 / Download & Install

> ⏱ 整个过程只需 **2 分钟**，仅需做一次。

### 第 1 步：下载 / Step 1: Download

打开下面这个网页，点绿色的 **Code** 按钮，再点 **Download ZIP**：

👉 **https://github.com/sylvanlisayhi-cyber/latex-privacy**

把下载的 ZIP 解压到你电脑上（比如解压到桌面）。

> 如果你会用 git，也可以直接 `git clone https://github.com/sylvanlisayhi-cyber/latex-privacy.git`

### 第 2 步：安装 / Step 2: Install

打开解压后的 `latex-privacy` 文件夹，在地址栏输入 `cmd` 然后按回车。

在弹出的黑色窗口里粘贴这行命令，按回车：

```bash
pip install -e .
```

> **如果提示 `pip` 不是命令：** 说明你没装 Python。去 [python.org](https://python.org) 下载 Python（3.7 以上），安装时**务必勾选 "Add Python to PATH"**，然后重试这行命令。

安装成功后，你就可以在命令行使用 `texp` 命令了。

---

## ⚡ 快速上手 / Quick Start

```bash
# 基本用法（中强度）
texp 我的论文.tex -o 我的论文_安全版.tex

# 高强度
texp 我的论文.tex -s high -o 我的论文_安全版.tex

# 低强度
texp 我的论文.tex -s low -o 我的论文_安全版.tex
```

运行之后，文件夹里会出现一个 `我的论文_安全版.tex`。用这个文件编译 PDF：

```bash
pdflatex 我的论文_安全版.tex
```

**对比一下：** 原版 PDF 和这个 PDF 完全一样。但两个 `.tex` 文件的内容不一样了。

---

## 📖 命令大全 / All Commands

### 查看帮助

```bash
texp --help
```

### 基础用法

| 命令 | 说明 |
|------|------|
| `texp paper.tex -o paper_obf.tex` | 中强度混淆（默认），输出到新文件 |
| `texp paper.tex -o paper_obf.tex` | 不写 `-s` 就是中强度 |
| `texp paper.tex` | 省略 `-o`，自动生成 `paper_obf.tex` |

### 混淆强度

```bash
texp paper.tex -s low    -o out.tex    # 低强度 — 改动少
texp paper.tex -s medium -o out.tex    # 中强度 — 适中（默认）
texp paper.tex -s high   -o out.tex    # 高强度 — 改动最多
```

强度越高，源码改动越大，隐私保护效果越好。编译时间不受影响，PDF 始终不变。

### 固定随机种子

```bash
texp paper.tex --seed 42 -o out1.tex
texp paper.tex --seed 42 -o out2.tex
```

两次运行结果完全一样。适合团队协作时大家用同一个 seed，或者想复现某个结果。

### 只开部分功能

如果你只想用某几种混淆手法，可以用 `--no-*` 参数关掉不需要的：

| 命令 | 效果 |
|------|------|
| `texp paper.tex --no-comments -o out.tex` | 不加注释 |
| `texp paper.tex --no-spaces -o out.tex` | 不加空格 |
| `texp paper.tex --no-commands -o out.tex` | 不替换命令 |
| `texp paper.tex --no-options -o out.tex` | 不打乱包选项 |
| `texp paper.tex --no-quotes -o out.tex` | 不变异引号 |
| `texp paper.tex --no-macros -o out.tex` | 不注入假宏 |

也可以组合使用：

```bash
# 只加注释，其他全部关掉
texp paper.tex --no-spaces --no-commands --no-options --no-quotes --no-macros -o out.tex

# 只要空格和命令替换，不要注释和引号
texp paper.tex --no-comments --no-quotes -o out.tex
```

### 所有参数一览

| 参数 | 作用 |
|------|------|
| `input` | 要处理的 `.tex` 文件（必填） |
| `-o, --output` | 输出文件名（默认在原名后加 `_obf`） |
| `-s, --strength` | 混淆强度：`low`（低）、`medium`（中，默认）、`high`（高） |
| `--seed` | 随机种子，填同样数字每次结果一样 |
| `--no-comments` | 禁用注释插入 |
| `--no-spaces` | 禁用空格混淆 |
| `--no-commands` | 禁用命令替换 |
| `--no-options` | 禁用它选项打乱 |
| `--no-quotes` | 禁用引号变异 |
| `--no-macros` | 禁用宏注入 |

---

## 🧠 它到底改了源码的什么？ / How it works

| 手法 | 例子（编译后看不见） | 作用 |
|------|---------------------|------|
| 插入随机注释 | `\section{Intro} % x9k2m` | 打乱行级统计特征 |
| 加零宽空格 | `\hspace{0pt}` | 干扰字符位置分析 |
| 加转义空格 | `word.` → `word\ .` | 改变空格表示方式 |
| 替换等效命令 | `\textbf{xxx}` ↔ `{\bf xxx}` | 抹平命令使用偏好 |
| 打乱包选项 | 随机排列 `\usepackage[...]` 里的顺序 | 消除顺序特征 |
| 变异引号 | `"text"` ↔ `` ``text'' `` | 增加风格不确定性 |
| 注入假宏 | 定义 `\def\zzx{}` 并在文中调用 | 增加源码噪声 |

**所有改法都是 LaTeX 编译器直接忽略的东西，所以 PDF 一点不变。**

---

## 📝 完整示例 / Full Example

**混淆前 / Before:**

```latex
\documentclass{article}
\begin{document}
This is a \textbf{test}. See \cite{key}.
\end{document}
```

**运行 `texp paper.tex -o paper_obf.tex` 后 / After:**

```latex
\documentclass{article} % k9m2n
\begin{document}
This is a \textbf{test} \hspace{0pt}. See \citep{key}. % r5t8v
\end{document}
% \def\zzx{}
\zzx
```

**编译 / Compile:**

```bash
pdflatex paper_obf.tex
```

跟原版 PDF 一模一样。

---

## ⚠️ 注意事项 / Limitations

| 英文 | 中文 |
|------|------|
| Only works on **LaTeX source**, not compiled PDF text. | **只改源码**，不改 PDF 里的文字。 |
| **Not encryption** — a motivated person could reverse it. | 混淆**不是加密**，想查的人可以还原。 |
| Output files are **larger**, but compile time is unchanged. | 输出文件**变大**，但编译时间不变。 |
| If someone checks the **PDF content** (not the .tex), this tool does nothing. | 如果别人检查的是 **PDF 内容**（不是 .tex 源码），这工具没效果。 |

---

## 🤝 贡献 / Contributing

欢迎提交 PR！你有新的混淆思路（不改变语义的前提下）可以直接提。

---

## 📄 许可证 / License

MIT

---

## ⚖️ 免责声明 / Disclaimer

这是一个**隐私保护工具**，用于保护源码层面的写作风格不被分析。它不是也不用于学术不端、抄袭或规避诚信政策。使用者自行负责。
