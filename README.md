# VOFTools user manual

Sphinx sources for the VOFTools 6 user manual, part of AIRTools kit.

Website: https://air-hpc.github.io/voftools-manual/

Author: Joaquín López. See `docs/about.rst` for the manual notice and attribution.

## Build locally

Use Python 3.13:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m sphinx -E -b html -n -W docs _build/html
.venv/bin/python tools/check_html.py _build/html
.venv/bin/python -m http.server 8000 --bind 127.0.0.1 --directory _build/html
```

Open http://127.0.0.1:8000/ . On Windows use `.venv\Scripts\python.exe`.

## Publishing

In repository Settings → Pages, select **GitHub Actions** as the source.
The Publish manual workflow builds and validates the site, then deploys it on each push to main. It can also be started manually from Actions.
Only the generated HTML is deployed. Do not commit `_build/` or `.venv/`.

## Editing

Edit the reStructuredText pages under `docs/`. Figures, local MathJax and the downloadable PDF are included; no LaTeX installation is needed to build this website.
Changes to the original LaTeX manual are not automatically transferred to these pages. Keep the web text and downloadable PDF synchronized when updating the manual.
