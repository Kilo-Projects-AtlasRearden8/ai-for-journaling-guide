#!/usr/bin/env python3
"""
Static site generator for the AI for Journaling beginner manual.

Converts docs/*.md into site/*.html with a consistent template.
Also provides a built-in test suite (run_tests()) for verification.

Usage:
    python3 build.py          # build the site
    python3 build.py --test   # run validation tests
    python3 build.py --serve  # build and serve locally
"""

import os
import re
import sys
import html
import shutil

try:
    import markdown
except ImportError:
    sys.stderr.write("Error: Python 'markdown' module is required.\n")
    sys.stderr.write("Install with: pip install markdown\n")
    sys.exit(1)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "docs")
SITE_DIR = os.path.join(BASE_DIR, "site")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

SITE_TITLE = "AI for Journaling — A Beginner's Manual"
SITE_AUTHOR = "Asdale Dynamics, LLC"
SITE_DESCRIPTION = (
    "A warm, low-pressure guide to using AI as a journaling companion. "
    "Reflection prompts, mood tracking, entry organization, and actionable "
    "insights — with strong privacy rules and a local-first mindset."
)

COPYRIGHT_LINE = "Copyright (c) 2026 Asdale Dynamics, LLC"

NAV_LINKS = [
    ("index", "Home"),
    ("getting-started", "Getting Started"),
    ("privacy", "Privacy Rules"),
    ("reflection-prompts", "Reflection Prompts"),
    ("mood-tracking", "Mood Tracking"),
    ("organizing", "Organizing Entries"),
    ("insights", "Turning Notes into Insights"),
    ("templates", "Printable Templates"),
]


def build_nav(current_page):
    links = []
    for slug, label in NAV_LINKS:
        if slug == current_page:
            links.append(f'<a href="{slug}.html" class="nav-link active">{label}</a>')
        else:
            links.append(f'<a href="{slug}.html" class="nav-link">{label}</a>')
    return "\n    ".join(links)


def render_page(slug, title, content_html):
    nav = build_nav(slug)
    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title)} | {html.escape(SITE_TITLE)}</title>
    <meta name="description" content="{html.escape(SITE_DESCRIPTION)}">
    <meta name="author" content="{html.escape(SITE_AUTHOR)}">
    <link rel="icon" href="data:,">
    <style>
{read_css()}
    </style>
</head>
<body>
    <header class="site-header">
        <h1><span class="ai-icon">🤖</span> AI for Journaling</h1>
        <p class="subtitle">A Beginner's Manual</p>
        <nav class="site-nav">
            <div class="nav-group">
                {nav}
            </div>
        </nav>
    </header>

    <main class="site-main">
        <article class="content">
            <h1>{title}</h1>
{content_html}
        </article>
    </main>

    <footer class="site-footer">
        <p>{html.escape(COPYRIGHT_LINE)} &middot; Built with care, privacy-first.</p>
        <p class="small">This guide is for educational purposes. AI journaling aids
        are companions, not replacements for human reflection or professional care.</p>
    </footer>
</body>
</html>"""
    return page_html


def read_css():
    css_path = os.path.join(BASE_DIR, "assets", "style.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


def markdown_to_html(md_text):
    md = markdown.Markdown(
        extensions=[
            "extra",
            "sane_lists",
            "toc",
            "nl2br",
            "md_in_html",
        ],
        extension_configs={
            "toc": {"permalink": False, "title": "Table of Contents"},
        },
    )
    return md.convert(md_text)


def build_site():
    os.makedirs(SITE_DIR, exist_ok=True)

    md_files = sorted(
        f for f in os.listdir(DOCS_DIR)
        if f.endswith(".md")
    )

    generated = []

    for md_file in md_files:
        slug = os.path.splitext(md_file)[0]
        md_path = os.path.join(DOCS_DIR, md_file)
        with open(md_path, "r", encoding="utf-8") as f:
            md_text = f.read()

        title_match = re.match(r"^# (.+)$", md_text.strip().split("\n")[0], re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()
        else:
            title = slug.replace("-", " ").title()

        body_md = re.sub(r"^# .+\n", "", md_text.strip(), count=1)

        content_html = markdown_to_html(body_md)

        page_html = render_page(slug, title, content_html)

        out_path = os.path.join(SITE_DIR, f"{slug}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_html)

        generated.append(out_path)

    copy_static_assets()

    print(f"Build complete: {len(generated)} pages generated in {SITE_DIR}/")
    for path in generated:
        print(f"  - {os.path.basename(path)}")


def copy_static_assets():
    if os.path.exists(TEMPLATES_DIR):
        dest = os.path.join(SITE_DIR, "templates")
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(TEMPLATES_DIR, dest)


def serve_site():
    build_site()
    import http.server
    import socketserver

    handler = http.server.SimpleHTTPRequestHandler
    port = 8000
    os.chdir(SITE_DIR)
    print(f"Serving on http://localhost:{port}/")
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            httpd.serve_forever()
    except OSError:
        print(f"Port {port} is busy. Try: python3 -m http.server {port} --directory site/")


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def check_tag_balance(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    for tag in ["html", "head", "body", "main", "article", "footer", "nav", "header"]:
        open_count = len(re.findall(rf"<{tag}[\s>]", content))
        close_count = len(re.findall(rf"</{tag}>", content))
        if open_count != close_count:
            return f"Tag mismatch in {filepath}: <{tag}>={open_count} </{tag}>={close_count}"
    return None


def check_no_secrets(filepath):
    secret_patterns = [
        (r"(?i)api[_-]?key\s*[:=]\s*['\"]?[a-zA-Z0-9]{20,}", "API key"),
        (r"(?i)secret\s*[:=]\s*['\"]?[a-zA-Z0-9]{16,}", "Secret"),
        (r"(?i)password\s*[:=]\s*['\"]?[a-zA-Z0-9]{8,}", "Password"),
        (r"(?i)aws_access_key_id", "AWS key"),
        (r"(?i)BEGIN.*PRIVATE.*KEY", "Private key"),
        (r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b", "Credit card number"),
    ]
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    for pattern, label in secret_patterns:
        if re.search(pattern, content):
            return f"Potential {label} found in {filepath}"
    return None


def check_license():
    license_path = os.path.join(BASE_DIR, "LICENSE")
    if not os.path.exists(license_path):
        return "LICENSE file not found"
    with open(license_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "MIT License" not in content:
        return "LICENSE is not an MIT License"
    if COPYRIGHT_LINE not in content:
        return f"LICENSE copyright line mismatch (expected: {COPYRIGHT_LINE})"
    return None


def check_readme_credit():
    readme_path = os.path.join(BASE_DIR, "README.md")
    if not os.path.exists(readme_path):
        return "README.md not found"
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "Asdale Dynamics, LLC" not in content:
        return "README.md does not credit Asdale Dynamics, LLC"
    return None


def check_templates():
    required = ["printable.css"]
    for name in required:
        path = os.path.join(TEMPLATES_DIR, name)
        if not os.path.exists(path):
            return f"Missing template file: templates/{name}"
    html_templates = [
        f for f in os.listdir(TEMPLATES_DIR)
        if f.endswith(".html")
    ] if os.path.exists(TEMPLATES_DIR) else []
    if len(html_templates) < 3:
        return f"Expected at least 3 HTML templates, found {len(html_templates)}"
    return None


def check_source_files():
    docs = [f for f in os.listdir(DOCS_DIR) if f.endswith(".md")] if os.path.exists(DOCS_DIR) else []
    expected_slugs = [slug for slug, _ in NAV_LINKS if slug != "index"]
    expected_files = [f"{slug}.md" for slug in expected_slugs]
    missing = [f for f in expected_files if f not in docs]
    if missing:
        return f"Missing docs: {missing}"
    return None


def run_tests():
    print("=" * 60)
    print("Running verification tests...")
    print("=" * 60)

    failures = []

    build_site()

    print("\n[1] Build ran without errors")
    print("  PASS")

    print("\n[2] Checking all pages generated")
    expected_pages = [f"{slug}.html" for slug, _ in NAV_LINKS]
    for page in expected_pages:
        path = os.path.join(SITE_DIR, page)
        if not os.path.exists(path):
            failures.append(f"Missing generated page: site/{page}")
    if not any(f.startswith("Missing generated page") for f in failures):
        print(f"  PASS — {len(expected_pages)} pages found")

    print("\n[3] Checking HTML tag balance")
    for page in expected_pages:
        path = os.path.join(SITE_DIR, page)
        if os.path.exists(path):
            err = check_tag_balance(path)
            if err:
                failures.append(err)
    if not any("Tag mismatch" in f for f in failures):
        print("  PASS — all HTML tags balanced")

    print("\n[4] Scanning for secrets/API keys/personal data")
    scan_files = []
    for root, _, files in os.walk(BASE_DIR):
        for fname in files:
            if fname.endswith((".md", ".html", ".py", ".css")):
                scan_files.append(os.path.join(root, fname))
    secret_found = False
    skip_names = {"STATUS.md", "build.py", "AGENTS.md"}
    for path in scan_files:
        if os.path.basename(path) in skip_names:
            continue
        err = check_no_secrets(path)
        if err:
            failures.append(err)
            secret_found = True
    if not secret_found:
        print(f"  PASS — no secrets found in {len(scan_files)} files")

    print("\n[5] Checking LICENSE copyright line")
    err = check_license()
    if err:
        failures.append(err)
    else:
        print(f"  PASS — {COPYRIGHT_LINE}")

    print("\n[6] Checking README credits Asdale Dynamics, LLC")
    err = check_readme_credit()
    if err:
        failures.append(err)
    else:
        print("  PASS")

    print("\n[7] Checking templates are present and printable")
    err = check_templates()
    if err:
        failures.append(err)
    else:
        print("  PASS")

    print("\n[8] Checking docs/ source files")
    err = check_source_files()
    if err:
        failures.append(err)
    else:
        print("  PASS")

    print("\n" + "=" * 60)
    if failures:
        print(f"FAILED — {len(failures)} issue(s):")
        for f in failures:
            print(f"  - {f}")
        return False
    else:
        print("ALL TESTS PASSED")
        return True


if __name__ == "__main__":
    if "--test" in sys.argv:
        success = run_tests()
        sys.exit(0 if success else 1)
    elif "--serve" in sys.argv:
        serve_site()
    else:
        build_site()
