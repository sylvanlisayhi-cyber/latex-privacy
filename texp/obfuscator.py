import re
import random
import string

class Obfuscator:
    """Applies various harmless transformations to LaTeX source code."""

    def __init__(self, strength="medium", seed=None,
                 enable_comments=True, enable_spaces=True,
                 enable_commands=True, enable_options=True,
                 enable_quotes=True, enable_macros=True):
        """
        Args:
            strength (str): 'low', 'medium', 'high'
            seed (int): Random seed for reproducibility.
            enable_comments (bool): Insert random comments.
            enable_spaces (bool): Add harmless spaces.
            enable_commands (bool): Replace equivalent commands.
            enable_options (bool): Shuffle package options.
            enable_quotes (bool): Vary quotation marks.
            enable_macros (bool): Inject dummy macros.
        """
        self.strength = strength
        self.enable_comments = enable_comments
        self.enable_spaces = enable_spaces
        self.enable_commands = enable_commands
        self.enable_options = enable_options
        self.enable_quotes = enable_quotes
        self.enable_macros = enable_macros

        if seed is not None:
            random.seed(seed)

        # Probability multipliers for each transformation based on strength
        self.prob = {
            'low': 0.2,
            'medium': 0.5,
            'high': 0.8
        }.get(strength, 0.5)

    def obfuscate(self, tex_content):
        """Apply enabled obfuscations to the LaTeX content."""
        content = tex_content

        if self.enable_comments:
            content = self._insert_random_comments(content)
        if self.enable_spaces:
            content = self._add_harmless_spaces(content)
        if self.enable_commands:
            content = self._replace_commands(content)
        if self.enable_options:
            content = self._shuffle_package_options(content)
        if self.enable_quotes:
            content = self._vary_quotes(content)
        if self.enable_macros:
            content = self._inject_macros(content)

        return content

    def _insert_random_comments(self, content):
        """Insert random comments after certain LaTeX constructs."""
        # Lines ending with } or ; or spaces
        lines = content.splitlines(keepends=True)
        new_lines = []
        for line in lines:
            if random.random() < self.prob:
                # Only comment if line is not all whitespace and not already a comment
                stripped = line.lstrip()
                if stripped and not stripped.startswith('%'):
                    comment = f" % {self._random_string(5, 10)}"
                    new_lines.append(line.rstrip('\n') + comment + '\n')
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        return ''.join(new_lines)

    def _add_harmless_spaces(self, content):
        """Insert \\hspace{0pt} or \\ (escaped space) at random positions."""
        # Find word boundaries (letters before a period/comma/space)
        # Simple approach: after some words, add \hspace{0pt}
        def replacer(match):
            if random.random() < self.prob * 0.5:  # half the prob for spaces
                return match.group(0) + r'\hspace{0pt}'
            return match.group(0)

        # Match a word character followed by a non-letter (space, punctuation)
        pattern = r'(?<=\w)(?=[.,;:!? ])'
        content = re.sub(pattern, replacer, content, flags=re.UNICODE)

        # Also add \ (escaped space) before some punctuation
        def add_escape_space(match):
            if random.random() < self.prob * 0.3:
                return r'\ ' + match.group(0)
            return match.group(0)
        content = re.sub(r'(?<=\w)([.,;:!?])', add_escape_space, content)

        return content

    def _replace_commands(self, content):
        """Replace LaTeX commands with equivalent alternatives."""
        substitutions = [
            (r'\\textbf\{([^}]*)\}', r'{\\bf \1}'),  # \textbf{text} -> {\bf text}
            (r'{\\bf ([^}]*)}', r'\\textbf{\1}'),   # and back, randomly
            (r'\\cite\{([^}]*)\}', r'\\citep{\1}'),  # \cite -> \citep if natbib
            (r'\\citep\{([^}]*)\}', r'\\cite{\1}'),
            (r'\\emph\{([^}]*)\}', r'\\textit{\1}'),
            (r'\\textit\{([^}]*)\}', r'\\emph{\1}'),
        ]
        for pattern, repl in substitutions:
            if random.random() < self.prob:
                content = re.sub(pattern, repl, content)
        return content

    def _shuffle_package_options(self, content):
        """Randomly reorder options in \\usepackage[opt1,opt2,...]{pkg}."""
        def shuffle_options(match):
            opts = match.group(1).split(',')
            if len(opts) > 1 and random.random() < self.prob:
                random.shuffle(opts)
            return '\\usepackage[' + ','.join(opts) + ']{' + match.group(2) + '}'

        pattern = r'\\usepackage\[([^\]]*)\]\{([^}]*)\}'
        content = re.sub(pattern, shuffle_options, content)
        return content

    def _vary_quotes(self, content):
        """Replace standard double quotes with LaTeX-style backtick quotes."""
        # Replace "text" with either ``text'' or `text' (depending on context)
        def quote_repl(match):
            text = match.group(1)
            if random.random() < self.prob:
                # Use `` '' style
                return '``' + text + "''"
            elif random.random() < self.prob:
                # Use ` ' style (single quotes)
                return '`' + text + "'"
            else:
                # Keep original "
                return '"' + text + '"'
        # Only match quotes that are not already escaped or inside command
        pattern = r'(?<!\\)"([^"\\]+)(?<!\\)"'
        content = re.sub(pattern, quote_repl, content)
        return content

    def _inject_macros(self, content):
        """Inject a dummy macro definition at top and call it somewhere."""
        # Find \documentclass line to insert after
        if random.random() < self.prob * 0.7:  # lower probability to avoid clutter
            dummy_name = self._random_string(3, 6, letters=True)
            dummy_def = f"\\def\\{dummy_name}{{}}%\n"
            # Insert after first \documentclass
            lines = content.splitlines(keepends=True)
            for i, line in enumerate(lines):
                if line.strip().startswith(r'\documentclass'):
                    lines.insert(i+1, dummy_def)
                    # Also insert a call later: somewhere random, but after \begin{document}
                    doc_start = -1
                    for j in range(i, len(lines)):
                        if r'\begin{document}' in lines[j]:
                            doc_start = j
                            break
                    if doc_start != -1:
                        # Insert call at random position after \begin{document}
                        call_pos = random.randint(doc_start+1, min(doc_start+20, len(lines)-1))
                        dummy_call = f"\\{dummy_name}%\n"
                        lines.insert(call_pos, dummy_call)
                    break
            content = ''.join(lines)
        return content

    def _random_string(self, min_len=4, max_len=12, letters=False):
        """Generate random string for dummy names/comments."""
        length = random.randint(min_len, max_len)
        if letters:
            chars = string.ascii_lowercase
        else:
            chars = string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
