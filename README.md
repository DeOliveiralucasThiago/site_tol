# TOL Advocacia — site

Site estático (HTML/CSS), publicado pelo GitHub Pages a partir da pasta `docs/`.

- Textos: `content.py` · Dados de contato e estrutura: `build.py`
- Regenerar o site: `python3 build.py` (requer Python 3)
- Logo: originais em `brand/`; para regerar as variações, `python3 tools/make_logo.py` (requer Pillow)
- Foto: salvar como `docs/assets/img/foto.jpg` e rodar `python3 build.py`
- Domínio: `tol.adv.br` (arquivo `docs/CNAME`)
