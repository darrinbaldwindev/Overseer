from src.analysis.scoring import health_score
from src.pipeline.portfolio_dry_run import run_portfolio_dry_run


def test_portfolio_dry_run_composes_real_domain_layers():
    paths = {
        "owner/a": ["README.md", ".github/workflows/ci.yml", "tests/test_a.py"],
        "owner/b": ["README.md", ".env.local"],
    }

    result = run_portfolio_dry_run(paths, lambda repo: paths[repo], health_score)

    assert result.repositories_scanned == 2
    assert result.results[0].evidence_count == 3
    assert result.results[0].finding_count == 0
    assert result.results[1].finding_count == 1
    assert result.results[1].finding_states == ("NEW",)
