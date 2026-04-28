"""Inject MuscleLove Compass Network footer into output/site HTML files.

Idempotent: skips files where the marker class "compass-network" is already present.
Designed to run inside the GitHub Actions deploy-pages workflow AFTER SiteGenerator
build_site() and BEFORE upload-pages-artifact.
"""
from __future__ import annotations

import re
from pathlib import Path

OUTPUT_DIR = Path("output/site")
SELF_SLUG_FILE = Path(".compass_self_slug")
ACCENT = "#0ea5e9"
TITLE = "🧭 MuscleLove Compass Network"
DESC = "退職・婚活・不動産・保険・通信・食生活・自動車など、生活上の重要な選択を比較・最適化する特化ブログネットワーク。"
SITES = [["taishoku-navi", "退職代行ナビ"], ["matching-compass", "マッチングアプリコンパス"], ["fudosan-compass", "不動産投資コンパス"], ["vod-compass", "VODコンパス"], ["kuruma-compass", "クルマコンパス"], ["electric-compass", "電力比較コンパス"], ["hoken-compass", "保険コンパス"], ["shokuzai-compass", "食材宅配コンパス"], ["pet-hoken-compass", "ペット保険コンパス"], ["datsumo-compass", "脱毛コンパス"]]
MARKER = "compass-network"


def build_footer(self_slug: str) -> str:
    links = []
    for slug, label in SITES:
        if slug == self_slug:
            continue
        url = f"https://musclelove-777.github.io/{slug}/"
        links.append(
            f'        <a href="{url}" '
            f'style="padding:6px 12px;background:#fff;border:1px solid #bae6fd;'
            f'border-radius:4px;text-decoration:none;color:#0c4a6e;">{label}</a>'
        )
    links_html = "\n".join(links)
    return (
        f'<footer class="{MARKER}" style="margin-top:60px;padding:30px 20px;'
        f'background:#f0f9ff;border-top:2px solid {ACCENT};font-size:0.9rem;">\n'
        '  <div style="max-width:900px;margin:0 auto;">\n'
        f'    <h3 style="margin-bottom:12px;color:#0c4a6e;">{TITLE}</h3>\n'
        f'    <p style="margin-bottom:14px;color:#0c4a6e;">{DESC}</p>\n'
        '    <div style="display:flex;flex-wrap:wrap;gap:8px;">\n'
        f"{links_html}\n"
        '    </div>\n'
        '  </div>\n'
        '</footer>'
    )


def detect_self_slug() -> str:
    if SELF_SLUG_FILE.exists():
        return SELF_SLUG_FILE.read_text(encoding="utf-8").strip()
    repo = (
        Path.cwd().name
        if Path.cwd().name not in {".", ""}
        else ""
    )
    return repo


def patch_html(path: Path, footer: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        return False
    if re.search(r"</body>", text, re.IGNORECASE):
        new_text = re.sub(r"</body>", footer + "\n</body>", text, count=1, flags=re.IGNORECASE)
    else:
        new_text = text + "\n" + footer + "\n"
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    if not OUTPUT_DIR.exists():
        print(f"[compass-footer] {OUTPUT_DIR} not found; skip.")
        return 0
    self_slug = detect_self_slug()
    footer = build_footer(self_slug)
    patched = 0
    skipped = 0
    for html_path in OUTPUT_DIR.rglob("*.html"):
        if patch_html(html_path, footer):
            patched += 1
        else:
            skipped += 1
    print(f"[compass-footer] self_slug={self_slug} patched={patched} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
