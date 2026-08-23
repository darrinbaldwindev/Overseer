"""Deterministic repository reconnaissance helpers."""

from dataclasses import dataclass, field
from typing import Iterable


@dataclass(frozen=True)
class RepositoryEvidence:
    paths: tuple[str, ...]
    languages: tuple[str, ...] = ()
    manifests: tuple[str, ...] = ()
    test_paths: tuple[str, ...] = ()
    workflow_paths: tuple[str, ...] = ()
    infrastructure_paths: tuple[str, ...] = ()
    documentation_paths: tuple[str, ...] = ()
    entrypoint_candidates: tuple[str, ...] = ()
    signals: dict[str, bool] = field(default_factory=dict)


def classify_paths(paths: Iterable[str]) -> RepositoryEvidence:
    """Extract conservative project signals from a repository tree."""
    normalized = tuple(sorted({p.strip("/") for p in paths if p and p.strip("/")}, key=str.lower))
    lower = {p.lower() for p in normalized}

    manifests = tuple(p for p in normalized if p.lower().split("/")[-1] in {
        "package.json", "pyproject.toml", "requirements.txt", "poetry.lock",
        "cargo.toml", "go.mod", "go.sum", "pom.xml", "build.gradle",
        "build.gradle.kts", "composer.json", "gemfile", "mix.exs",
    })
    tests = tuple(p for p in normalized if any(token in p.lower() for token in ("test/", "tests/", "spec/", "__tests__/")))
    workflows = tuple(p for p in normalized if p.lower().startswith(".github/workflows/"))
    infrastructure = tuple(p for p in normalized if any(token in p.lower() for token in (
        "dockerfile", "docker-compose", ".terraform/", "terraform/", "k8s/", "kubernetes/", "helm/"
    )))
    docs = tuple(p for p in normalized if p.lower().split("/")[-1] in {"readme.md", "readme", "contributing.md", "architecture.md"})
    entrypoints = tuple(p for p in normalized if p.lower().split("/")[-1] in {
        "main.py", "app.py", "server.py", "main.ts", "main.js", "index.ts", "index.js", "main.go", "main.rs"
    })

    language_signals = []
    if any(p.endswith(".py") for p in lower) or manifests and any(p.lower().endswith(("pyproject.toml", "requirements.txt")) for p in manifests):
        language_signals.append("python")
    if any(p.endswith((".js", ".jsx", ".ts", ".tsx")) for p in lower):
        language_signals.append("javascript/typescript")
    if any(p.endswith(".go") for p in lower):
        language_signals.append("go")
    if any(p.endswith(".rs") for p in lower):
        language_signals.append("rust")
    if any(p.endswith((".java", ".kt")) for p in lower):
        language_signals.append("jvm")

    return RepositoryEvidence(
        paths=normalized,
        languages=tuple(sorted(set(language_signals))),
        manifests=manifests,
        test_paths=tests,
        workflow_paths=workflows,
        infrastructure_paths=infrastructure,
        documentation_paths=docs,
        entrypoint_candidates=entrypoints,
        signals={
            "has_tests": bool(tests),
            "has_ci": bool(workflows),
            "has_documentation": bool(docs),
            "has_infrastructure": bool(infrastructure),
            "has_manifest": bool(manifests),
            "has_entrypoint_candidate": bool(entrypoints),
        },
    )
