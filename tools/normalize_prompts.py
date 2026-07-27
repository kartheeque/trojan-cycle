#!/usr/bin/env python3
"""Normalise issue prompt blocks into copy-paste-ready form.

Each panel block gains a single fenced code block containing everything the
image generator needs, in this order:

    1. an explicit aspect-ratio / framing directive
    2. the reference-identity instruction (positional: "first attached image is ...")
    3. the canonical PROMPT text, verbatim

ATTACH stays outside the block as the file manifest (which files to attach).
REF-BIRTH stays outside as a pipeline instruction. MATCH LINE is absorbed into
the block, since the identity mapping must travel with the pasted text.

The canonical prompt wording is never altered - only relocated. Where the
identity mapping cannot be derived with confidence the block is marked
NEEDS REVIEW rather than guessed, because a wrong mapping propagates into
every later panel of that character.

Usage:
    python3 tools/normalize_prompts.py issues/issue-02/prompts.md [--write]
"""
import re, sys, pathlib

ASPECT = {
    'standard 4:3':   '4:3 landscape (standard comic panel)',
    'close-up 4:3':   '4:3 landscape (standard comic panel)',
    'wide 16:9':      '16:9 wide landscape panel',
    'full page 3:4':  '3:4 tall portrait (full page)',
    'tall 2:3':       '2:3 tall portrait panel',
    'tall 3:4':       '3:4 tall portrait panel',
}
ORDINALS = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']


def aspect_of(head):
    """Pull the aspect phrase out of the panel heading."""
    for key in sorted(ASPECT, key=len, reverse=True):
        if key in head:
            return ASPECT[key]
    return None


def refs_in(text):
    return re.findall(r'refs/[\w\-]+\.png', text or '')


def build_identity(attach_line, match_line):
    """Return (instruction, status). status: ok | none | review."""
    refs = refs_in(attach_line)
    if not refs:
        return None, 'none'
    if not match_line:
        return None, 'review'

    ml = match_line.strip()

    # Already a written instruction (issue-01 house style) - keep verbatim.
    if ml.startswith('"') and ml.endswith('"'):
        return ml.strip('"'), 'ok'

    # Already names the ref paths explicitly - keep verbatim, just prefix.
    if len(refs_in(ml)) >= len(refs):
        return ml, 'ok'

    def clean(s):
        return s.strip().strip('"').strip("'").strip().rstrip('.').strip()

    # Single reference: take the whole line as the descriptor. Never tokenise
    # on quotes here - descriptors routinely contain possessive apostrophes
    # ("a hand on each son's shoulder") and naive quote-splitting truncates them.
    if len(refs) == 1:
        lead = re.sub(r'^map each[^:;]*[:;]', '', ml).strip()
        return (f'Match the attached reference image exactly: it is {clean(lead)} '
                f'({refs[0]}) - reproduce that face, hair and apparent age exactly.'), 'ok'

    # Several references. Double quotes are unambiguous; otherwise split on the
    # ' / ' separator the shorthand uses, which is apostrophe-safe.
    quoted = re.findall(r'"([^"]+)"', ml)
    if len(quoted) != len(refs):
        tail = re.sub(r'^map each[^:;]*[:;]', '', ml).strip()
        if '/' in tail:
            quoted = [p for p in (clean(x) for x in tail.split('/')) if p]
    quoted = [clean(q) for q in quoted if clean(q)]

    # One quoted run covering several subjects, separated by semicolons.
    if len(quoted) == 1 and len(refs) > 1 and ';' in quoted[0]:
        parts = [p.strip() for p in quoted[0].split(';') if p.strip()]
        if len(parts) == len(refs):
            quoted = parts

    # Unquoted but semicolon-separated after the "map each" lead-in.
    if len(quoted) != len(refs) and len(refs) > 1:
        tail = re.sub(r'^map each[^:;]*[:;]', '', ml).strip()
        parts = [p.strip().rstrip('.') for p in tail.split(';') if p.strip()]
        if len(parts) == len(refs):
            quoted = parts

    if len(quoted) == len(refs):
        parts = [
            f'the {ORDINALS[i]} attached image is {quoted[i]} ({refs[i]}) - '
            f'reproduce that face, hair and apparent age exactly'
            for i in range(len(refs))
        ]
        return 'Match the attached reference images exactly: ' + '; '.join(parts) + '.', 'ok'

    return ml, 'review'


def transform(text):
    """Rewrite every panel block in a prompts.md file."""
    out, stats = [], {'ok': 0, 'none': 0, 'review': 0, 'skipped': 0}
    chunks = re.split(r'(?m)^(?=### i)', text)
    for chunk in chunks:
        if not chunk.startswith('### i'):
            out.append(chunk)
            continue
        if '```' in chunk:                      # already normalised
            out.append(chunk); stats['skipped'] += 1; continue

        lines = chunk.split('\n')
        head = lines[0]

        # Capture the prompt body only: stop at REF-BIRTH, the next panel
        # heading, or a '---' page separator, and keep whatever follows so it
        # can be re-emitted verbatim instead of swallowed into the code block.
        m = re.search(r'(?ms)^PROMPT:[ ]*(.*?)(?=\n(?:REF-BIRTH|###\s|---\s*$)|\Z)', chunk)
        if not m:
            out.append(chunk); stats['skipped'] += 1; continue
        prompt = m.group(1).strip()
        tail = chunk[m.end():]

        attach = next((l for l in lines if l.startswith('ATTACH')), None)
        match  = next((l for l in lines if l.startswith('MATCH LINE:')), None)
        refb   = None
        match_body = match.split('MATCH LINE:', 1)[1].strip() if match else None

        identity, status = build_identity(attach, match_body)
        stats[status] += 1

        body = []
        asp = aspect_of(head)
        if asp:
            body.append(f'Aspect ratio {asp}.')
        if identity:
            body.append(identity)
        body.append(prompt)

        new = [head]
        if attach:
            new.append(attach)
        if status == 'review':
            new.append('MATCH-REVIEW: the identity mapping could not be derived '
                       'automatically. The original shorthand is preserved verbatim '
                       'inside the block below - rewrite it as an explicit positional '
                       'instruction ("the first attached image is ...") before generating.')
        new.append('PROMPT:')
        new.append('```text')
        new.append('\n\n'.join(body))
        new.append('```')
        rendered = '\n'.join(new)
        # tail still holds REF-BIRTH and/or the '---' page separator verbatim
        if not tail.startswith('\n'):
            rendered += '\n'
        out.append(rendered + tail)
    return ''.join(out), stats


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    write = '--write' in sys.argv
    if not args:
        print(__doc__); sys.exit(1)
    for path in args:
        p = pathlib.Path(path)
        new, stats = transform(p.read_text())
        print(f'{path}: mapped={stats["ok"]} no-refs={stats["none"]} '
              f'needs-review={stats["review"]} already-done={stats["skipped"]}')
        if write:
            p.write_text(new)
            print(f'  written')


if __name__ == '__main__':
    main()
