"""Dựng các trang HTML của site tài liệu shipfast từ content.py vào site/src/.

Chạy: python3 site/gen/build.py (sau đó npm run build trong site/).
"""

from html import escape as esc
from pathlib import Path

import content as C

GEN = Path(__file__).parent
SRC = GEN.parent / "src"
HEADER = (GEN / "header.html").read_text()
WAVES = (GEN / "waves.html").read_text()

ARROW = '<svg class="size-4 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>'
ARROW_L = '<svg class="size-4 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5"/><path d="m12 19-7-7 7-7"/></svg>'
COPY = ('<svg data-icon="chep" class="size-4 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>'
        '<svg data-icon="da-chep" class="size-4 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>')

ROLE_STYLE = {
    "PO": "bg-secondary text-foreground",
    "Orchestrator": "bg-primary text-primary-foreground",
    "Bộ phận": "bg-surface text-foreground ring-1 ring-border-strong ring-inset",
}

GROUP_NAME = {g[0]: g[1] for g in C.GROUPS}
ORDER = [p for g in C.GROUPS for p in C.PROCESSES if p["group"] == g[0]]


def role_badges(roles):
    return "".join(f'<span class="inline-flex h-6 items-center rounded-full px-2.5 text-xs font-medium {ROLE_STYLE[r]}">{esc(r)}</span>' for r in roles)


def code_box(cmd):
    return (f'<div class="flex min-w-0 items-center gap-2 rounded-xl border border-border-strong bg-surface py-1 pr-1 pl-4">'
            f'<code class="min-w-0 flex-1 overflow-x-auto py-2 font-mono text-sm whitespace-nowrap text-foreground">{esc(cmd)}</code>'
            f'<button type="button" data-copy="{esc(cmd)}" aria-label="Chép lệnh" class="inline-flex size-8 shrink-0 cursor-pointer items-center justify-center rounded-lg text-muted outline-hidden hover:bg-foreground/5 hover:text-foreground">{COPY}</button></div>')


def terminal(lines, title="~/du-an — claude"):
    """Cửa sổ dạng Claude Code: dòng của PO có dấu '>', câu trả lời và lời gọi tool có chấm đầu dòng."""
    dot = lambda c: f'<span class="mt-[0.55em] size-2 shrink-0 rounded-full {c}" aria-hidden="true"></span>'
    items = []
    for line in lines:
        kind = line[0]
        if kind == "user":
            items.append(f'<li class="rounded-lg bg-secondary px-3 py-2 text-foreground [overflow-wrap:anywhere]"><span class="text-muted">&gt; </span>{esc(line[1])}</li>')
        elif kind == "ai":
            items.append(f'<li class="flex gap-2.5 pr-2">{dot("bg-foreground")}<p class="min-w-0 text-pretty text-foreground">{esc(line[1])}</p></li>')
        else:
            _, who, arg, res = line
            items.append(f'<li class="flex gap-2.5 pr-2">{dot("bg-emerald-400")}<div class="min-w-0 [overflow-wrap:anywhere]"><p><span class="font-semibold text-foreground">{esc(who)}</span> <span class="text-muted">({esc(arg)})</span></p><p class="text-muted"><span aria-hidden="true">└&nbsp;</span>{esc(res)}</p></div></li>')
    return (f'<div class="force-dark flex min-w-0 flex-col overflow-hidden rounded-2xl border border-border bg-surface font-mono text-xs leading-relaxed text-foreground sm:text-sm">'
            f'<div class="flex h-10 items-center gap-2 border-b border-border px-4"><span class="size-3 rounded-full bg-foreground/15"></span><span class="size-3 rounded-full bg-foreground/15"></span><span class="size-3 rounded-full bg-foreground/15"></span><span class="ml-2 truncate text-xs text-muted">{esc(title)}</span></div>'
            f'<ol class="flex flex-col gap-3 p-4">{"".join(items)}</ol></div>')


def table(rows):
    """Bảng dữ liệu; dưới khổ sm mỗi dòng xếp dọc, mỗi ô có nhãn cột ở trên."""
    head, *body = rows
    th = "".join(f'<th scope="col" class="px-4 py-2.5 text-left text-xs font-medium text-muted">{esc(h)}</th>' for h in head)
    def cell(label, value):
        return (f'<td data-label="{esc(label)}" class="px-4 py-3 align-top text-sm text-pretty text-foreground max-sm:block max-sm:py-1 '
                f'max-sm:before:mb-0.5 max-sm:before:block max-sm:before:text-xs max-sm:before:font-medium max-sm:before:text-muted max-sm:before:content-[attr(data-label)]">{esc(value)}</td>')
    tr = "".join('<tr class="border-t border-border max-sm:block max-sm:py-2 max-sm:first:border-t-0">' + "".join(cell(h, c) for h, c in zip(head, r)) + "</tr>" for r in body)
    return (f'<div class="overflow-x-auto rounded-2xl border border-border bg-surface"><table class="w-full border-collapse max-sm:block">'
            f'<thead class="max-sm:hidden"><tr>{th}</tr></thead><tbody class="max-sm:block">{tr}</tbody></table></div>')


def page(title, body, desc):
    return f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}" />
<meta property="og:title" content="{esc(title)}" />
<meta property="og:description" content="{esc(desc)}" />
<meta property="og:type" content="website" />
<meta name="theme-color" content="#f4f4f6" />
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg" />
<link rel="preload" href="assets/fonts/inter-vietnamese-wght-normal.woff2" as="font" type="font/woff2" crossorigin />
<link rel="stylesheet" href="assets/style.css" />
<script>if (!navigator.webdriver) document.documentElement.classList.add("js");</script>
</head>
<body>
{body}
<script src="assets/app.js" defer></script>
</body>
</html>
"""


def footer():
    link = lambda h, l: f'<a href="{h}" class="inline-flex h-8 items-center px-1 hover:text-foreground">{l}</a>'
    brand = HEADER[HEADER.index('<a href="./"'):HEADER.index('</a>', HEADER.index('<a href="./"')) + 4]
    return (f'<footer class="border-t border-border bg-surface"><div class="mx-auto flex max-w-6xl flex-col gap-4 px-4 py-6 sm:flex-row sm:items-center sm:justify-between sm:px-6">'
            f'<div class="flex items-center gap-3">{brand}<span class="text-xs text-muted">MIT · mô hình làm việc theo wave</span></div>'
            f'<nav class="flex flex-wrap gap-x-4 gap-y-2 text-sm text-foreground/70">{link("./#quy-trinh", "Quy trình")}{link("ap-dung.html", "Áp dụng")}{link(C.SITE["repo"], "GitHub")}{link(C.SITE["pypi"], "PyPI")}</nav></div></footer>')


def section_head(eyebrow, title, desc=None, anchor=None):
    a = f' id="{anchor}"' if anchor else ""
    d = f'<p class="max-w-2xl text-sm text-pretty text-muted">{esc(desc)}</p>' if desc else ""
    return f'<div{a} class="mb-5 flex scroll-mt-20 flex-col gap-1.5"><span class="text-xs font-medium text-muted">{esc(eyebrow)}</span><h2 class="text-lg font-semibold text-balance text-foreground">{esc(title)}</h2>{d}</div>'


def process_card(p, numbered):
    outs = ", ".join(o[0] for o in p["outputs"][:3])
    meta = []
    meta.append(f'<div class="flex flex-wrap items-center gap-1.5">{role_badges(p["roles"])}</div>')
    if outs:
        meta.append(f'<p class="text-xs text-muted"><span class="font-medium text-foreground/80">Đầu ra:</span> <span class="font-mono">{esc(outs)}</span></p>')
    if p["gate"]:
        meta.append(f'<p class="text-xs text-pretty text-muted"><span class="font-medium text-foreground/80">Cổng:</span> {esc(p["gate"])}</p>')
    badge = (f'<span class="grid size-8 shrink-0 place-items-center rounded-full bg-primary text-sm font-semibold text-primary-foreground tabular-nums">{esc(p["code"])}</span>' if numbered
             else f'<span class="inline-flex h-6 w-fit items-center rounded-lg bg-secondary px-2 font-mono text-xs font-medium text-foreground">{esc(p["code"])}</span>')
    return (f'<a href="{p["slug"]}.html" class="group flex gap-4 rounded-2xl border border-border bg-surface p-5 transition-colors hover:border-border-strong">'
            f'{badge if numbered else ""}<div class="flex min-w-0 flex-1 flex-col gap-2">{"" if numbered else badge}'
            f'<h3 class="text-base font-semibold text-balance text-foreground">{esc(p["name"])}</h3>'
            f'<p class="text-sm text-pretty text-muted">{esc(p["goal"])}</p>{"".join(meta)}'
            f'<span class="mt-1 inline-flex items-center gap-1.5 text-sm font-medium text-primary">Xem chi tiết {ARROW}</span></div></a>')


def build_index():
    S = C.SITE
    roles = "".join(
        f'<li class="flex flex-col gap-2 rounded-2xl border border-border bg-surface p-5"><span class="w-fit">{role_badges([n])}</span>'
        f'<span class="text-xs text-muted">{esc(who)}</span><p class="text-sm text-pretty text-foreground">{esc(d)}</p></li>'
        for n, who, d in C.ROLES)
    groups = []
    for gid, gname, gdesc in C.GROUPS:
        items = [p for p in C.PROCESSES if p["group"] == gid]
        if gid == "wave":
            cards = f'<ol data-stagger class="flex flex-col gap-3">{"".join("<li>" + process_card(p, True) + "</li>" for p in items)}</ol>'
        else:
            cols = "md:grid-cols-2" if len(items) > 1 else ""
            cards = f'<div data-stagger class="grid grid-cols-1 gap-3 {cols}">{"".join(process_card(p, False) for p in items)}</div>'
        groups.append(f'<div class="flex flex-col gap-3"><div class="flex flex-col gap-1"><h3 class="text-base font-semibold text-foreground">{esc(gname)}</h3><p class="text-sm text-muted">{esc(gdesc)}</p></div>{cards}</div>')
    apply_cards = (
        f'<div data-stagger class="grid grid-cols-1 gap-3 md:grid-cols-2">'
        f'<a href="ap-dung.html#thu-cong" class="flex flex-col gap-2 rounded-2xl border border-border bg-surface p-5 hover:border-border-strong"><h3 class="text-base font-semibold text-foreground">Áp thủ công</h3><p class="text-sm text-pretty text-muted">Chép bộ khung tài liệu vào dự án, làm theo từng trang quy trình. Dùng được với mọi công cụ AI.</p><span class="mt-1 inline-flex items-center gap-1.5 text-sm font-medium text-primary">Xem hướng dẫn {ARROW}</span></a>'
        f'<a href="ap-dung.html#shipfast-mcp" class="flex flex-col gap-2 rounded-2xl border border-border bg-surface p-5 hover:border-border-strong"><h3 class="text-base font-semibold text-foreground">Dùng shipfast-mcp</h3><p class="text-sm text-pretty text-muted">MCP server tự dựng khung, cấp mã, kiểm hồ sơ và nâng cấp khung bằng three-way merge. Không bắt buộc.</p><span class="mt-1 inline-flex items-center gap-1.5 text-sm font-medium text-primary">Xem cách cài {ARROW}</span></a></div>')
    entries = "".join(
        f'<a href="{h}" class="flex min-w-0 flex-col gap-1 rounded-xl border border-border bg-surface p-4 hover:border-border-strong">'
        f'<span class="inline-flex items-center gap-1.5 text-sm font-medium text-foreground">{esc(n)} {ARROW}</span><span class="text-xs text-pretty text-muted">{esc(d)}</span></a>'
        for n, d, h in S["entries"])
    hero = (f'<section data-hero class="flex min-w-0 flex-col gap-5">'
            f'<h1 class="max-w-3xl text-2xl font-bold tracking-tight text-balance text-foreground sm:text-3xl">{esc(S["headline"])}</h1>'
            f'<p class="max-w-2xl text-base text-pretty text-muted">{esc(S["lead"])}</p>'
            f'<div class="grid max-w-4xl grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-4">{entries}</div></section>')
    body = (HEADER + "\n" + WAVES + f'\n<main class="mx-auto flex max-w-6xl flex-col gap-12 px-4 py-10 sm:px-6">{hero}'
            f'<section data-reveal>{section_head("Mô hình", "Ba vai, mỗi vai một việc", "Người giữ quyền quyết định; AI điều phối và thực hiện; mọi trạng thái nằm trong file của repo.", "mo-hinh")}'
            f'<ol data-stagger class="grid grid-cols-1 gap-3 md:grid-cols-3">{roles}</ol>'
            f'<a href="to-chuc.html" class="mt-4 inline-flex h-8 items-center gap-1.5 text-sm font-medium text-primary">Tổ chức và vai trò {ARROW}</a></section>'
            f'<section data-reveal>{section_head("Quy trình", "Từng quy trình, bấm vào để xem chi tiết", None, "quy-trinh")}<div class="flex flex-col gap-10">{"".join(groups)}</div></section>'
            f'<section data-reveal>{section_head("Áp dụng", "Hai cách đưa mô hình vào dự án", None, "ap-dung")}{apply_cards}</section>'
            f'</main>' + footer())
    (SRC / "index.html").write_text(page(f"{S['title']} · Mô hình làm việc theo wave giữa người và AI", body, S["headline"] + ". " + S["lead"]))


def toc(entries):
    return ('<nav aria-label="Mục lục" class="sticky top-20 hidden flex-col gap-1 text-sm lg:flex">'
            '<p class="mb-1 text-xs font-medium text-muted">Mục lục</p>'
            + "".join(f'<a href="#{a}" title="{esc(t)}" class="truncate rounded-lg px-2 py-1.5 text-foreground/70 hover:bg-foreground/5 hover:text-foreground">{i:02d} {esc(t)}</a>' for i, (a, t) in enumerate(entries, 1))
            + '</nav>')


def build_process(p, prev, nxt):
    entries, blocks = [], []

    def add(anchor, title, html):
        entries.append((anchor, title))
        n = len(entries)
        blocks.append(f'<section id="{anchor}" class="flex scroll-mt-20 flex-col gap-3"><h2 class="text-lg font-semibold text-foreground"><span class="mr-2 text-muted tabular-nums">{n:02d}</span>{esc(title)}</h2>{html}</section>')

    if p["inputs"]:
        add("dau-vao", "Đầu vào", "<ul class=\"flex list-disc flex-col gap-1.5 pl-5 text-sm text-foreground marker:text-muted\">" + "".join(f"<li>{esc(i)}</li>" for i in p["inputs"]) + "</ul>")
    add("cac-buoc", "Các bước", '<ol class="flex flex-col gap-2">' + "".join(
        f'<li class="flex gap-3 rounded-xl border border-border bg-surface p-4"><span class="grid size-6 shrink-0 place-items-center rounded-full bg-secondary text-xs font-semibold text-foreground tabular-nums">{i}</span><p class="text-sm text-pretty text-foreground">{esc(s)}</p></li>'
        for i, s in enumerate(p["steps"], 1)) + "</ol>")
    for title, kind, data in p.get("sections", []):
        anchor = "-".join(title.lower().split())[:40]
        html = table(data) if kind == "table" else f'<pre class="overflow-x-auto rounded-xl border border-border bg-surface p-4 font-mono text-xs leading-relaxed text-foreground sm:text-sm">{esc(data)}</pre>'
        add(anchor, title, html)
    if p["outputs"]:
        add("dau-ra", "Đầu ra", table([("File", "Nội dung")] + list(p["outputs"])))
    if p["cases"]:
        add("tinh-huong", "Tình huống thường gặp", table([("Tình huống", "Làm gì")] + list(p["cases"])))
    if p.get("example"):
        add("vi-du", "Ví dụ", terminal(p["example"]))
    if p["tools"]:
        add("cong-cu", "Công cụ hỗ trợ", '<p class="text-sm text-muted">Nếu dùng shipfast-mcp; không bắt buộc.</p>' + table([("Tool", "Việc")] + list(p["tools"])))

    nav = '<div class="mt-4 grid grid-cols-1 gap-3 border-t border-border pt-6 sm:grid-cols-2">'
    nav += (f'<a href="{prev["slug"]}.html" class="flex flex-col gap-1 rounded-xl border border-border bg-surface p-4 hover:border-border-strong"><span class="inline-flex items-center gap-1.5 text-xs text-muted">{ARROW_L} Trước</span><span class="text-sm font-medium text-foreground">{esc(prev["name"])}</span></a>' if prev else "<span></span>")
    nav += (f'<a href="{nxt["slug"]}.html" class="flex flex-col items-end gap-1 rounded-xl border border-border bg-surface p-4 text-right hover:border-border-strong"><span class="inline-flex items-center gap-1.5 text-xs text-muted">Tiếp {ARROW}</span><span class="text-sm font-medium text-foreground">{esc(nxt["name"])}</span></a>' if nxt else "")
    nav += "</div>"

    summary = (f'<div class="grid grid-cols-1 gap-3 sm:grid-cols-2">'
               f'<div class="flex flex-col gap-2 rounded-xl border border-border bg-surface p-4"><span class="text-xs font-medium text-muted">Ai làm</span><div class="flex flex-wrap gap-1.5">{role_badges(p["roles"])}</div></div>'
               + (f'<div class="flex flex-col gap-2 rounded-xl border border-border bg-surface p-4"><span class="text-xs font-medium text-muted">Cổng sang bước sau</span><p class="text-sm text-pretty text-foreground">{esc(p["gate"])}</p></div>' if p["gate"] else "")
               + "</div>")
    head = (f'<nav aria-label="Đường dẫn" class="flex flex-wrap items-center gap-1.5 text-sm text-muted"><a href="./#quy-trinh" class="inline-flex h-8 items-center hover:text-foreground">Tổng quan</a><span aria-hidden="true">/</span><span>{esc(GROUP_NAME[p["group"]])}</span><span aria-hidden="true">/</span><span class="text-foreground">{esc(p["name"])}</span></nav>'
            f'<div class="flex flex-col gap-3"><span class="inline-flex h-6 w-fit items-center rounded-lg bg-secondary px-2 font-mono text-xs font-medium text-foreground">{esc(p["code"])}</span>'
            f'<h1 class="text-xl font-semibold text-balance text-foreground">{esc(p["name"])}</h1><p class="max-w-2xl text-base text-pretty text-muted">{esc(p["goal"])}</p></div>{summary}')
    body = (HEADER + f'\n<main class="mx-auto max-w-6xl px-4 py-8 sm:px-6"><div class="grid grid-cols-1 gap-10 lg:grid-cols-[minmax(0,1fr)_14rem]">'
            f'<article class="flex min-w-0 flex-col gap-8">{head}{"".join(blocks)}{nav}</article><aside class="hidden lg:block">{toc(entries)}</aside></div></main>' + footer())
    (SRC / f'{p["slug"]}.html').write_text(page(f'{p["name"]} · shipfast', body, p["goal"]))


def build_apply():
    A = C.APPLY
    manual = '<ol class="flex flex-col gap-2">' + "".join(
        f'<li class="flex gap-3 rounded-xl border border-border bg-surface p-4"><span class="grid size-6 shrink-0 place-items-center rounded-full bg-secondary text-xs font-semibold text-foreground">{i}</span><p class="text-sm text-pretty text-foreground">{esc(s)}</p></li>'
        for i, s in enumerate(A["manual"], 1)) + "</ol>"
    mcp = "".join(f'<div class="flex flex-col gap-2"><span class="text-sm font-medium text-foreground">{esc(n)}</span>{code_box(c)}</div>' for n, c in A["mcp"])
    blocks = (f'<section id="thu-cong" class="flex scroll-mt-20 flex-col gap-3"><h2 class="text-lg font-semibold text-foreground"><span class="mr-2 text-muted">01</span>Áp thủ công</h2>{manual}</section>'
              f'<section id="shipfast-mcp" class="flex scroll-mt-20 flex-col gap-3"><h2 class="text-lg font-semibold text-foreground"><span class="mr-2 text-muted">02</span>Dùng shipfast-mcp</h2><div class="flex flex-col gap-4">{mcp}</div>'
              f'<p class="text-sm text-pretty text-muted">{esc(A["mcp_note"])}</p><p class="text-sm"><a href="{C.SITE["pypi"]}" class="font-medium text-primary">Gói trên PyPI</a> · <a href="{C.SITE["repo"]}" class="font-medium text-primary">Mã nguồn trên GitHub</a></p></section>')
    head = (f'<nav aria-label="Đường dẫn" class="flex flex-wrap items-center gap-1.5 text-sm text-muted"><a href="./" class="inline-flex h-8 items-center hover:text-foreground">Tổng quan</a><span aria-hidden="true">/</span><span class="text-foreground">{esc(A["name"])}</span></nav>'
            f'<div class="flex flex-col gap-3"><h1 class="text-xl font-semibold text-foreground">{esc(A["name"])}</h1><p class="max-w-2xl text-base text-pretty text-muted">{esc(A["lead"])}</p></div>')
    body = HEADER + f'\n<main class="mx-auto max-w-3xl px-4 py-8 sm:px-6"><article class="flex flex-col gap-8">{head}{blocks}</article></main>' + footer()
    (SRC / "ap-dung.html").write_text(page(f'{A["name"]} · shipfast', body, A["lead"]))


if __name__ == "__main__":
    build_index()
    for i, p in enumerate(ORDER):
        build_process(p, ORDER[i - 1] if i > 0 else None, ORDER[i + 1] if i + 1 < len(ORDER) else None)
    build_apply()
    print(f"{len(ORDER) + 2} trang")
