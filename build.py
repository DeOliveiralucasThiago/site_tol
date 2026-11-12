#!/usr/bin/env python3
"""Gera o site estático da TOL Advocacia na pasta docs/ (servida pelo GitHub Pages).

Uso:   python3 build.py
Para definir o domínio (canonical + sitemap):  SITE_URL=https://seudominio.adv.br python3 build.py

Edite os dados em CONFIG e os textos em content.py. Depois rode o script de novo.
"""
import html
import json
import os
import shutil
from pathlib import Path
from urllib.parse import quote

from content import AREAS, DUVIDAS, GRUPOS, SOBRE_PARAGRAFOS, SOBRE_TITULO, FORMACAO

ROOT = Path(__file__).parent
OUT = ROOT / "docs"

CONFIG = {
    "nome_site": "TOL Advocacia",
    "advogado": "Thiago de Oliveira Lucas",
    "oab": "OAB/ES nº 27.341",
    "telefone_exibicao": "(27) 98822-0682",
    "telefone_wa": "5527988220682",
    "email": "tol.advocacia@gmail.com",
    "cidade": "Vila Velha, ES",
    "linkedin": "https://www.linkedin.com/in/deoliveiralucasthiago",
    # Domínio final (ex.: https://tol.adv.br). Vazio = sem canonical/sitemap.
    "site_url": os.environ.get("SITE_URL", "https://tol.adv.br").rstrip("/"),
}
C = CONFIG

AVISO_OAB = (
    "Este site tem caráter exclusivamente informativo, nos termos do Provimento nº 205/2021 do "
    "Conselho Federal da OAB. Não constitui oferta de serviços, captação de clientela nem promessa "
    "de resultado, e o conteúdo não substitui a consulta a um advogado."
)

ICONS = {
    "dados": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l8 3v6c0 4.5-3.2 8-8 9-4.8-1-8-4.5-8-9V6l8-3z"/><rect x="9" y="11" width="6" height="5" rx="1"/><path d="M10 11V9.5a2 2 0 014 0V11"/></svg>',
    "contrato": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/></svg>',
    "civil": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v16M7 20h10M5 7h14M5 7l-3 7a3 3 0 006 0L5 7zM19 7l-3 7a3 3 0 006 0l-3-7z"/></svg>',
    "familia": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.2c2.8-.4 5 1.7 5 4.8"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s7-6.2 7-11.5a7 7 0 10-14 0C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/></svg>',
    "oab": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l8 3v6c0 4.5-3.2 8-8 9-4.8-1-8-4.5-8-9V6l8-3z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
    "cal": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
    "chip": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="7" y="7" width="10" height="10" rx="1"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v11H9l-5 4V5z"/></svg>',
}
WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.04 2a9.9 9.9 0 00-8.5 15l-1.5 5 5.2-1.4A9.9 9.9 0 1012.04 2zm5.8 14.1c-.25.7-1.45 1.3-2 1.4-.5.07-1.1.1-1.8-.1-.4-.15-1-.3-1.7-.65-3-1.3-4.9-4.3-5.05-4.5-.15-.2-1.2-1.6-1.2-3s.75-2.1 1-2.4c.25-.3.55-.35.75-.35h.55c.18 0 .42-.07.65.5.25.6.85 2.05.9 2.2.07.15.12.3.02.5-.1.2-.15.3-.3.5l-.45.5c-.15.15-.3.3-.13.6.17.3.75 1.25 1.6 2 1.1.98 2.05 1.3 2.35 1.43.3.15.47.12.65-.07.17-.2.75-.87.95-1.17.2-.3.4-.25.67-.15.27.1 1.7.8 2 .95.3.15.5.22.57.35.07.12.07.7-.18 1.4z"/></svg>'

esc = html.escape


def wa(msg="Olá! Encontrei seu site e gostaria de conversar sobre um assunto jurídico."):
    return f"https://wa.me/{C['telefone_wa']}?text={quote(msg)}"


def brand_html(rel):
    return (
        f'<img class="b-icon" src="{rel}assets/img/logo-icone-light.png" alt="" width="46" height="53">'
        f'<span class="b-text"><img class="b-name" src="{rel}assets/img/logo-nome-light.png" alt="Thiago de Oliveira Lucas" width="240" height="13">'
        '<span class="sub">Advocacia</span></span>'
    )


def photo_file():
    for n in ("foto.jpg", "foto.jpeg", "foto.png", "foto.webp"):
        if (OUT / "assets" / "img" / n).exists():
            return n
    return None


def photo_html(rel):
    f = photo_file()
    if f:
        return f'<div class="photo"><img src="{rel}assets/img/{f}" alt="{esc(C["advogado"])}, advogado" width="640" height="800"></div>'
    return f'<div class="photo"><div class="ph"><img src="{rel}assets/img/logo-icone-light.png" alt="" width="313" height="360"><small>Foto em breve</small></div></div>'


def edu_html(dark):
    itens = "".join(f"<li>{esc(t)}</li>" for t in FORMACAO)
    cls = "ghost" if dark else "outline"
    return f'<details class="edu"><summary class="btn {cls}">Formação</summary><ul class="edu-list">{itens}</ul></details>'


def header(rel, active):
    brand_inner = brand_html(rel)
    items = [
        ("", "Início", "home"),
        ("areas-de-atuacao/", "Áreas de atuação", "areas"),
        ("duvidas/", "Dúvidas frequentes", "duvidas"),
        ("sobre/", "Sobre", "sobre"),
        ("contato/", "Contato", "contato"),
    ]
    links = "".join(
        f'<a href="{rel}{h}"{" aria-current=\"page\"" if k == active else ""}>{t}</a>' for h, t, k in items
    )
    return f"""<a class="skip" href="#conteudo">Ir para o conteúdo</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="{rel or './'}" aria-label="{esc(C['nome_site'])} — página inicial">{brand_inner}</a>
<button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
<nav class="nav" id="nav" aria-label="Principal">{links}<a class="btn" href="{wa()}" target="_blank" rel="noopener">Falar no WhatsApp</a></nav>
</div></header>"""


def footer(rel):
    areas = "".join(f'<li><a href="{rel}areas-de-atuacao/{a["slug"]}/">{esc(a["titulo"])}</a></li>' for a in AREAS)
    return f"""<footer class="site-footer"><div class="wrap">
<div class="footer-grid">
<div><div class="brand" style="margin-bottom:16px">{brand_html(rel)}</div>
<p>{esc(C['advogado'])}<br>{esc(C['oab'])}</p>
<p>Advocacia em Proteção de Dados (LGPD), Contratos, Direito Civil e Direito de Família.</p></div>
<div><h4>Navegação</h4><ul>
<li><a href="{rel or './'}">Início</a></li><li><a href="{rel}areas-de-atuacao/">Áreas de atuação</a></li>
<li><a href="{rel}duvidas/">Dúvidas frequentes</a></li><li><a href="{rel}sobre/">Sobre</a></li>
<li><a href="{rel}contato/">Contato</a></li><li><a href="{rel}privacidade/">Política de Privacidade</a></li></ul></div>
<div><h4>Áreas de atuação</h4><ul>{areas}</ul></div>
<div><h4>Contato</h4><ul>
<li><a href="{wa()}" target="_blank" rel="noopener">WhatsApp {esc(C['telefone_exibicao'])}</a></li>
<li><a href="mailto:{C['email']}">{esc(C['email'])}</a></li>
<li>{esc(C['cidade'])}<br>Atendimento presencial e online</li>
<li><a href="{C['linkedin']}" target="_blank" rel="noopener">LinkedIn</a></li></ul></div>
</div>
<div class="legal"><p>{AVISO_OAB}</p><p>© {2026} {esc(C['nome_site'])} · {esc(C['advogado'])} · {esc(C['oab'])}</p></div>
</div></footer>
<a class="wa-float" href="{wa()}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">{WA_SVG}</a>
<script src="{rel}assets/js/main.js" defer></script>"""


PAGES = []  # (url_path) para o sitemap


def page(path, title, desc, body, active="", jsonld=None, noindex=False):
    """path: '' | 'sobre/' | 'duvidas/x/'"""
    rel = "../" * (path.count("/"))
    url = f"{C['site_url']}/{path}" if C["site_url"] else ""
    full_title = title if title.startswith(C["nome_site"]) else f"{title} | {C['nome_site']}"
    canonical = f'<link rel="canonical" href="{url}">\n<meta property="og:url" content="{url}">' if url else ""
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>\n' for j in (jsonld or []))
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    og_image = (f'<meta property="og:image" content="{C["site_url"]}/assets/img/og.png">\n<meta name="twitter:card" content="summary_large_image">' if C["site_url"] else "")
    doc = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}{canonical}
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta name="theme-color" content="#0f1829">
{og_image}
<link rel="icon" href="{rel}assets/img/favicon.png" type="image/png" media="(prefers-color-scheme: light)">
<link rel="icon" href="{rel}assets/img/favicon-dark.png" type="image/png" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{rel}favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="{rel}assets/img/apple-touch-icon.png">
<link rel="preload" href="{rel}assets/fonts/cormorant-garamond-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{rel}assets/css/style.css">
{ld}</head>
<body>
{header(rel, active)}
<main id="conteudo">
{body}
</main>
{footer(rel)}
</body>
</html>
"""
    target = OUT / path
    target.mkdir(parents=True, exist_ok=True)
    (target / "index.html").write_text(doc, encoding="utf-8")
    if not noindex:
        PAGES.append(path)


def cta(rel, titulo="Ficou com alguma dúvida?", texto="Conte brevemente o seu caso. Respondo com clareza e sem compromisso de contratação."):
    return f"""<section class="cta"><div class="wrap"><h2>{titulo}</h2><p>{texto}</p>
<a class="btn" href="{wa()}" target="_blank" rel="noopener">{WA_SVG} Falar no WhatsApp</a></div></section>"""


def head(rel, crumbs, h1, lead=""):
    cr = " / ".join(f'<a href="{rel}{h}">{t}</a>' for h, t in crumbs)
    p = f"<p>{lead}</p>" if lead else ""
    return f'<div class="page-head"><div class="wrap"><div class="crumbs">{cr}</div><h1>{h1}</h1>{p}</div></div>'


def by_slug(lst):
    return {x["slug"]: x for x in lst}


# ---------------------------------------------------------------- páginas
def build_home():
    rel = ""
    cards = ""
    for a in AREAS:
        feat = ""
        tag = ""
        cards += f"""<article class="card{feat}">{tag}{ICONS[a['icone']]}<h3>{esc(a['titulo'])}</h3>
<p>{esc(a['resumo'])}</p><a class="more" href="areas-de-atuacao/{a['slug']}/">Saiba mais</a></article>"""
    d = by_slug(DUVIDAS)
    destaques = "".join(
        f'<li><a href="duvidas/{s}/">{esc(d[s]["pergunta"])}</a></li>' for s in ("lgpd-adequar-empresa", "vazamento-de-dados", "o-que-nao-pode-faltar-em-um-contrato")
    )
    resumo_sobre = "".join(f"<p>{p}</p>" for p in SOBRE_PARAGRAFOS)
    body = f"""
<section class="hero"><div class="wrap">
<span class="eyebrow">Advocacia · {esc(C['cidade'])} e online</span>
<h1>Proteção de dados e segurança jurídica para o seu negócio</h1>
<p class="lead">Atuação em LGPD, Contratos e Direito Civil, também com atendimento em Direito de Família. Orientação clara, sem juridiquês, adequada à realidade de cada cliente.</p>
<div class="hero-actions"><a class="btn" href="{wa()}" target="_blank" rel="noopener">{WA_SVG} Falar no WhatsApp</a>
<a class="btn ghost" href="areas-de-atuacao/">Conheça as áreas de atuação</a></div>
</div></section>
<section><div class="wrap">
<div class="section-head"><span class="eyebrow">Áreas de atuação</span><h2>Soluções jurídicas com foco em prevenção</h2>
<p>Atuação consultiva e contenciosa, sempre com explicações objetivas sobre cada etapa.</p></div>
<div class="grid cols-4">{cards}</div></div></section>
<section class="dark"><div class="wrap about-split">
<div><span class="eyebrow">Sobre</span><h2 class="about-title">{esc(SOBRE_TITULO)}</h2>
{resumo_sobre}
{edu_html(True)}</div>
{photo_html(rel)}
</div></section>
<section><div class="wrap narrow">
<div class="section-head"><span class="eyebrow">Dúvidas frequentes</span><h2>Respostas para perguntas comuns</h2><p>Informação jurídica em linguagem simples para você entender o seu cenário.</p></div>
<ul class="faq-list">{destaques}</ul>
<p style="text-align:center;margin-top:34px"><a class="btn outline" href="duvidas/">Ver todas as dúvidas</a></p>
</div></section>
{cta(rel, "Vamos conversar?", "Conte brevemente o que você precisa. Retorno com clareza sobre os próximos passos.")}
"""
    ld = [{
        "@context": "https://schema.org",
        "@type": "LegalService",
        "name": C["nome_site"],
        "founder": {"@type": "Person", "name": C["advogado"], "jobTitle": "Advogado"},
        "telephone": "+" + C["telefone_wa"],
        "address": {"@type": "PostalAddress", "addressLocality": "Vila Velha", "addressRegion": "ES", "addressCountry": "BR"},
        "areaServed": "BR",
        "knowsAbout": ["LGPD", "Proteção de Dados", "Contratos", "Direito Civil", "Direito de Família"],
        **({"url": C["site_url"] + "/"} if C["site_url"] else {}),
    }]
    page("", "TOL Advocacia — LGPD, Contratos e Direito Civil em Vila Velha/ES",
         "Advocacia em Vila Velha/ES com foco em LGPD e proteção de dados, contratos, direito civil e direito de família. Atendimento presencial e online.",
         body, "home", ld)


def build_areas():
    rel = "../"
    cards = ""
    for a in AREAS:
        feat = ""
        tag = ""
        cards += f"""<article class="card{feat}">{tag}{ICONS[a['icone']]}<h3>{esc(a['titulo'])}</h3>
<p>{esc(a['resumo'])}</p><a class="more" href="{a['slug']}/">Saiba mais</a></article>"""
    body = head(rel, [("", "Início")], "Áreas de atuação",
                "Atuação concentrada em poucas áreas, para oferecer orientação aprofundada em cada uma.") + \
        f'<section><div class="wrap"><div class="grid cols-2">{cards}</div></div></section>' + cta(rel)
    page("areas-de-atuacao/", "Áreas de atuação", "LGPD e proteção de dados, contratos, direito civil e direito de família em Vila Velha/ES e online.", body, "areas")

    d = by_slug(DUVIDAS)
    for a in AREAS:
        rel = "../../"
        itens = "".join(f"<li>{x}</li>" for x in a["itens"])
        passos = "".join(f"<li><strong>{t}</strong> {x}</li>" for t, x in a["passos"])
        rel_q = "".join(f'<li><a href="{rel}duvidas/{s}/">{esc(d[s]["pergunta"])}</a></li>' for s in a["duvidas"])
        outras = "".join(f'<li><a href="{rel}areas-de-atuacao/{o["slug"]}/">{esc(o["titulo"])}</a></li>' for o in AREAS if o["slug"] != a["slug"])
        extra = f'<div class="note">{a["nota"]}</div>' if a.get("nota") else ""
        body = head(rel, [("", "Início"), ("areas-de-atuacao/", "Áreas de atuação")], esc(a["titulo"]), esc(a["chamada"])) + f"""
<section class="content"><div class="wrap layout"><div>
{a['intro']}
<h2>Como posso ajudar</h2><ul>{itens}</ul>
<h2>Para quem</h2><p>{a['publico']}</p>
<h2>Como funciona</h2><ol>{passos}</ol>
{extra}
<div class="related"><h3>Dúvidas frequentes sobre o tema</h3><ul class="faq-list">{rel_q}</ul></div>
</div>
<aside class="aside">
<div class="box dark"><h3>Quer conversar sobre o seu caso?</h3><p style="font-size:.92rem">Envie uma mensagem com um breve resumo da situação.</p>
<a class="btn" href="{wa('Olá! Gostaria de conversar sobre: ' + a['titulo'])}" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a></div>
<div class="box"><h3>Outras áreas</h3><ul>{outras}</ul></div>
</aside></div></section>"""
        ld = [{"@context": "https://schema.org", "@type": "Service", "name": a["titulo"], "serviceType": a["titulo"],
               "provider": {"@type": "LegalService", "name": C["nome_site"]}, "areaServed": "BR"}]
        page(f"areas-de-atuacao/{a['slug']}/", a["titulo"], a["meta"], body, "areas", ld)


def build_duvidas():
    rel = "../"
    grupos = ""
    for g, titulo in GRUPOS:
        lis = "".join(f'<li><a href="{x["slug"]}/">{esc(x["pergunta"])}</a></li>' for x in DUVIDAS if x["grupo"] == g)
        grupos += f'<div class="faq-group"><h2>{titulo}</h2><ul class="faq-list">{lis}</ul></div>'
    body = head(rel, [("", "Início")], "Dúvidas frequentes",
                "Respostas objetivas para perguntas que clientes costumam fazer. Informação geral, que não substitui a análise do seu caso.") + \
        f'<section class="content"><div class="wrap narrow">{grupos}</div></section>' + cta(rel, "Sua dúvida não está aqui?", "Envie sua pergunta pelo WhatsApp.")
    page("duvidas/", "Dúvidas frequentes", "Perguntas e respostas sobre LGPD, contratos, cobrança, união estável e divórcio.", body, "duvidas")

    areas = by_slug(AREAS)
    for q in DUVIDAS:
        rel = "../../"
        a = areas[q["area"]]
        outras = [x for x in DUVIDAS if x["grupo"] == q["grupo"] and x["slug"] != q["slug"]][:3]
        outras_html = ""
        if outras:
            lis = "".join(f'<li><a href="{rel}duvidas/{x["slug"]}/">{esc(x["pergunta"])}</a></li>' for x in outras)
            outras_html = f'<div class="related"><h3>Leia também</h3><ul class="faq-list">{lis}</ul></div>'
        body = head(rel, [("", "Início"), ("duvidas/", "Dúvidas frequentes")], esc(q["pergunta"])) + f"""
<section class="content"><div class="wrap layout"><article>
<p class="answer">{q['resposta']}</p>
{q['corpo']}
<p class="note">Conteúdo de caráter informativo, com base na legislação em vigor na data de sua elaboração. Cada situação tem particularidades e deve ser analisada individualmente.</p>
{outras_html}
</article>
<aside class="aside">
<div class="box dark"><h3>Quer analisar o seu caso?</h3><p style="font-size:.92rem">Fale comigo e conte brevemente a sua situação.</p>
<a class="btn" href="{wa('Olá! Li a página “' + q['pergunta'] + '” e gostaria de conversar.')}" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a></div>
<div class="box"><h3>Área relacionada</h3><ul><li><a href="{rel}areas-de-atuacao/{a['slug']}/">{esc(a['titulo'])}</a></li></ul></div>
</aside></div></section>"""
        ld = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{
            "@type": "Question", "name": q["pergunta"],
            "acceptedAnswer": {"@type": "Answer", "text": q["resposta"]}}]}]
        page(f"duvidas/{q['slug']}/", q["pergunta"], q["meta"], body, "duvidas", ld)


def build_sobre():
    rel = "../"
    paras = "".join(f"<p>{p}</p>" for p in SOBRE_PARAGRAFOS)
    body = head(rel, [("", "Início")], "Sobre") + f"""
<section class="content"><div class="wrap about-page">
<div>{photo_html(rel)}</div>
<div><h2 class="about-title">{esc(SOBRE_TITULO)}</h2>{paras}
{edu_html(False)}
<p style="margin-top:28px"><a class="btn" href="{wa()}" target="_blank" rel="noopener">{WA_SVG} Falar no WhatsApp</a>
&nbsp; <a class="btn outline" href="{C['linkedin']}" target="_blank" rel="noopener">Ver LinkedIn</a></p>
</div></div></section>"""
    ld = [{"@context": "https://schema.org", "@type": "Person", "name": C["advogado"], "jobTitle": "Advogado",
           "sameAs": [C["linkedin"]], "worksFor": {"@type": "LegalService", "name": C["nome_site"]}}]
    page("sobre/", "Sobre", f"Conheça {C['advogado']}, advogado em Vila Velha/ES com atuação em LGPD, contratos, direito civil e direito de família.", body, "sobre", ld)


def build_contato():
    rel = "../"
    body = head(rel, [("", "Início")], "Contato", "Conte brevemente o que você precisa. O primeiro contato pode ser feito pelo WhatsApp.") + f"""
<section class="content"><div class="wrap layout"><div>
<ul class="contact-list">
<li><svg viewBox="0 0 24 24">{ICONS['phone'].split(">",1)[1].rsplit("</svg>",1)[0]}</svg><div><small>WhatsApp e telefone</small><a href="{wa()}" target="_blank" rel="noopener">{esc(C['telefone_exibicao'])}</a></div></li>
<li><svg viewBox="0 0 24 24">{ICONS['mail'].split(">",1)[1].rsplit("</svg>",1)[0]}</svg><div><small>E-mail</small><a href="mailto:{C['email']}">{esc(C['email'])}</a></div></li>
<li><svg viewBox="0 0 24 24">{ICONS['pin'].split(">",1)[1].rsplit("</svg>",1)[0]}</svg><div><small>Localização</small>{esc(C['cidade'])} · atendimento presencial e online, com hora marcada</div></li>
<li><svg viewBox="0 0 24 24">{ICONS['oab'].split(">",1)[1].rsplit("</svg>",1)[0]}</svg><div><small>Inscrição</small>{esc(C['advogado'])} · {esc(C['oab'])}</div></li>
</ul>
<p class="note">Ao entrar em contato, evite enviar documentos ou informações sensíveis na primeira mensagem. Descreva o assunto de forma resumida; os detalhes são tratados com sigilo na conversa seguinte. Veja a <a href="{rel}privacidade/">Política de Privacidade</a>.</p>
</div>
<aside class="aside"><div class="box dark"><h3>Atendimento rápido</h3><p style="font-size:.92rem">Clique para abrir uma conversa já com uma mensagem inicial.</p>
<a class="btn" href="{wa()}" target="_blank" rel="noopener">{WA_SVG} Falar no WhatsApp</a></div></aside>
</div></section>"""
    page("contato/", "Contato", "Entre em contato com TOL Advocacia pelo WhatsApp ou e-mail. Atendimento em Vila Velha/ES e online.", body, "contato")


def build_privacidade():
    rel = "../"
    body = head(rel, [("", "Início")], "Política de Privacidade", "Como este site trata dados pessoais.") + f"""
<section class="content"><div class="wrap narrow">
<h2>Quem é o responsável</h2>
<p>O responsável pelo tratamento de dados pessoais neste site é {esc(C['advogado'])}, advogado inscrito na {esc(C['oab'])}, com atuação em {esc(C['cidade'])}. Para qualquer assunto relacionado à proteção de dados, escreva para <a href="mailto:{C['email']}">{esc(C['email'])}</a>.</p>
<h2>Dados que este site coleta</h2>
<p>Este site é informativo e <strong>não utiliza cookies de rastreamento, ferramentas de análise de acesso, publicidade nem formulários</strong>. Também não carrega fontes ou scripts de terceiros. Os registros técnicos básicos de acesso (como endereço IP) podem ser mantidos pela empresa de hospedagem para fins de segurança e funcionamento do serviço.</p>
<h2>Contato por WhatsApp, e-mail ou telefone</h2>
<p>Se você entrar em contato, os dados que fornecer (nome, telefone, e-mail e o conteúdo da mensagem) serão usados apenas para responder à sua solicitação e, se houver contratação, para a prestação dos serviços advocatícios. A base legal é a adoção de procedimentos preliminares relacionados a contrato a pedido do titular e, depois, a execução do contrato (art. 7º, V, da LGPD). Esses dados ficam sujeitos ao sigilo profissional e não são vendidos nem compartilhados para fins de marketing.</p>
<p>Ao clicar em botões de WhatsApp ou LinkedIn, você é direcionado a serviços de terceiros, que possuem suas próprias políticas de privacidade.</p>
<h2>Por quanto tempo os dados são guardados</h2>
<p>Pelo tempo necessário para atender à sua solicitação e, em caso de contratação, pelos prazos exigidos pela legislação e pelo Código de Ética e Disciplina da OAB.</p>
<h2>Seus direitos</h2>
<p>Nos termos do art. 18 da LGPD, você pode solicitar confirmação de tratamento, acesso, correção, anonimização, eliminação, portabilidade e informações sobre compartilhamento, bem como revogar consentimento, quando for o caso. Basta enviar sua solicitação para o e-mail acima.</p>
<p class="note">Última atualização: novembro de 2026.</p>
</div></section>"""
    page("privacidade/", "Política de Privacidade", "Política de Privacidade do site TOL Advocacia.", body)


def build_404():
    body = """<section class="content"><div class="wrap narrow" style="text-align:center"><h1>Página não encontrada</h1>
<p>O endereço pode ter mudado ou não existe mais.</p><p><a class="btn dark" href="/">Voltar ao início</a></p></div></section>"""
    # 404 usa caminhos absolutos para o CSS/JS, então gera à parte
    rel = "/"
    page_html = (OUT / "index.html").read_text(encoding="utf-8")
    # reaproveita o layout da home trocando o conteúdo do <main>
    start = page_html.index('<main id="conteudo">')
    end = page_html.index("</main>") + len("</main>")
    doc = page_html[:start] + '<main id="conteudo">' + body + "</main>" + page_html[end:]
    doc = doc.replace('href="assets/', 'href="/assets/').replace('src="assets/', 'src="/assets/')
    doc = doc.replace('href="areas-de-atuacao/', 'href="/areas-de-atuacao/').replace('href="duvidas/', 'href="/duvidas/')
    doc = doc.replace('href="sobre/', 'href="/sobre/').replace('href="contato/', 'href="/contato/').replace('href="privacidade/', 'href="/privacidade/')
    doc = doc.replace('href="./"', 'href="/"')
    doc = doc.replace("<title>", '<meta name="robots" content="noindex"><title>', 1)
    (OUT / "404.html").write_text(doc, encoding="utf-8")


def build_assets():
    (OUT / "assets" / "img").mkdir(parents=True, exist_ok=True)
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    if C["site_url"]:
        (OUT / "CNAME").write_text(C["site_url"].split("//")[-1] + "\n", encoding="utf-8")
    robots = "User-agent: *\nAllow: /\n"
    if C["site_url"]:
        robots += f"Sitemap: {C['site_url']}/sitemap.xml\n"
        urls = "".join(f"<url><loc>{C['site_url']}/{p}</loc></url>" for p in sorted(PAGES))
        (OUT / "sitemap.xml").write_text(
            f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>', encoding="utf-8")
    (OUT / "robots.txt").write_text(robots, encoding="utf-8")


def main():
    # limpa apenas as páginas geradas (preserva assets/ e arquivos do usuário como CNAME)
    for d in ("areas-de-atuacao", "duvidas", "sobre", "contato", "privacidade"):
        shutil.rmtree(OUT / d, ignore_errors=True)
    build_home()
    build_areas()
    build_duvidas()
    build_sobre()
    build_contato()
    build_privacidade()
    build_404()
    build_assets()
    print(f"OK: {len(PAGES)} páginas geradas em {OUT}")
    if not C["site_url"]:
        print("Aviso: SITE_URL não definido — sem canonical e sem sitemap.xml. "
              "Quando tiver o domínio: SITE_URL=https://seudominio.adv.br python3 build.py")


if __name__ == "__main__":
    main()
