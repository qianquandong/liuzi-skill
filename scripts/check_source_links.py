#!/usr/bin/env python3
"""Check local Markdown targets and optionally probe external HTTP links."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import unquote, urlparse

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)")


def markdown_files(targets: list[str]) -> list[Path]:
    files: list[Path] = []
    for raw in targets:
        path = Path(raw)
        if path.is_dir():
            files.extend(sorted(item for item in path.rglob("*.md") if ".git" not in item.parts))
        elif path.suffix.lower() == ".md":
            files.append(path)
    return sorted(set(files))


def probe(url: str, timeout: float) -> str | None:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "liuzi-skill-link-check/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            if response.status >= 400:
                return f"HTTP {response.status}"
    except urllib.error.HTTPError as exc:
        if exc.code in {403, 405, 429}:
            return None
        return f"HTTP {exc.code}"
    except (urllib.error.URLError, TimeoutError) as exc:
        return str(exc)
    return None


def check(files: list[Path], network: bool, timeout: float) -> list[str]:
    errors: list[str] = []
    seen_urls: set[str] = set()
    for file in files:
        text = file.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip("<>")
            if target.startswith(("#", "mailto:", "data:")):
                continue
            parsed = urlparse(target)
            if parsed.scheme in {"http", "https"}:
                if not parsed.netloc:
                    errors.append(f"{file}: malformed URL {target}")
                elif network and target not in seen_urls:
                    seen_urls.add(target)
                    problem = probe(target, timeout)
                    if problem:
                        errors.append(f"{file}: {target}: {problem}")
                continue
            if parsed.scheme:
                continue
            local = (file.parent / unquote(parsed.path)).resolve()
            if not local.exists():
                errors.append(f"{file}: missing local target {target}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("targets", nargs="*", default=["."], help="Markdown files or directories")
    parser.add_argument("--network", action="store_true", help="also probe external HTTP links")
    parser.add_argument("--timeout", type=float, default=8.0)
    args = parser.parse_args()
    files = markdown_files(args.targets)
    if not files:
        print("error: no Markdown files found", file=sys.stderr)
        return 2
    errors = check(files, args.network, args.timeout)
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print(f"links: valid ({len(files)} Markdown files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
