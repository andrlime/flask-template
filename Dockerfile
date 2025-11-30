FROM python:3.14-trixie AS base

FROM base AS deps
WORKDIR /app

COPY pyproject.toml uv.lock* ./

RUN pip install uv

FROM deps AS dev
WORKDIR /app

COPY --from=deps /app/. .
COPY . .

ENV PORT=9000
CMD ["uv", "run", "main.py"]

FROM deps AS prod
WORKDIR /app

COPY --from=deps /app/. .
COPY . .

ENV PORT=9000
CMD uv run waitress-serve --port=$PORT --call template.flask.factory:create_flask_app
