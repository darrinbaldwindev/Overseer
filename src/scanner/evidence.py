"""Evidence extraction from normalized repository trees.

This layer records observable facts only. It deliberately does not classify
security findings or infer intent.
"""

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Evidence:
    kind: str
    path: str
    detail: str


def extract_evidence(paths: Iterable[str]) -> list[Evidence]:
    evidence: list[Evidence] = []
    for raw_path in paths:
        path = raw_path.strip().lstrip("./")
        lower = path.lower()
        if lower.startswith(".github/workflows/"):
            evidence.append(Evidence("ci_workflow", path, "GitHub Actions workflow"))
        elif lower.endswith(("/package.json", "package.json")):
            evidence.append(Evidence("dependency_manifest", path, "Node package manifest"))
        elif lower.endswith(("/pyproject.toml", "requirements.txt", "poetry.lock")):
            evidence.append(Evidence("dependency_manifest", path, "Python dependency metadata"))
        elif lower.endswith(("/go.mod", "go.sum")):
            evidence.append(Evidence("dependency_manifest", path, "Go dependency metadata"))
        elif lower.endswith(("/cargo.toml", "cargo.lock")):
            evidence.append(Evidence("dependency_manifest", path, "Rust dependency metadata"))
        elif lower.endswith("dockerfile"):
            evidence.append(Evidence("container", path, "Docker build definition"))
        elif lower.endswith((".tf", ".tfvars")):
            evidence.append(Evidence("infrastructure", path, "Terraform configuration"))
        elif lower.startswith(("test/", "tests/", "__tests__/")):
            evidence.append(Evidence("test", path, "Test-path evidence"))
        elif lower in {"readme.md", "readme.rst", "readme.txt"}:
            evidence.append(Evidence("documentation", path, "Repository README"))
    return sorted(evidence, key=lambda item: (item.kind, item.path))
