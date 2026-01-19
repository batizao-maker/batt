"""Document audit with cognitive maturity scoring."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class AuditResult:
    path: Path
    maturity_score: float
    signals: tuple[str, ...]


KEY_SIGNALS = {
    "rationale": ["porque", "motivo", "justificativa", "rationale"],
    "evidence": ["evidencia", "evidence", "dados", "métrica", "metric"],
    "alternatives": ["alternativa", "alternatives", "opção", "trade-off"],
    "reflection": ["aprendizado", "reflexão", "insight", "lesson"],
}


def iter_documents(root: Path, extensions: Iterable[str]) -> Iterable[Path]:
    for ext in extensions:
        yield from root.rglob(f"*.{ext}")


def score_document(text: str) -> AuditResult:
    lowered = text.lower()
    signals: list[str] = []
    for signal, keywords in KEY_SIGNALS.items():
        if any(keyword in lowered for keyword in keywords):
            signals.append(signal)
    maturity_score = round(len(signals) / len(KEY_SIGNALS) * 100, 2)
    return AuditResult(path=Path(""), maturity_score=maturity_score, signals=tuple(signals))


def audit_documents(root: Path, extensions: Iterable[str] = ("md", "txt")) -> list[AuditResult]:
    results: list[AuditResult] = []
    for path in iter_documents(root, extensions):
        text = path.read_text(encoding="utf-8", errors="ignore")
        result = score_document(text)
        results.append(
            AuditResult(path=path, maturity_score=result.maturity_score, signals=result.signals)
        )
    return results


def summarize(results: Iterable[AuditResult]) -> str:
    lines = ["documento,score,signals"]
    for result in results:
        signals = "|".join(result.signals)
        lines.append(f"{result.path},{result.maturity_score},{signals}")
    return "\n".join(lines)


def main() -> None:
    root = Path.cwd()
    results = audit_documents(root)
    print(summarize(results))


if __name__ == "__main__":
    main()
