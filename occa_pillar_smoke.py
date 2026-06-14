"""OCCA charter smoke — meta research_methods or minimal fallback."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any


def ensure_meta_path() -> Path | None:
    here = Path(__file__).resolve()
    for ancestor in here.parents:
        if (ancestor / "research_methods" / "occa_discovery.py").is_file():
            root = ancestor
            if str(root) not in sys.path:
                sys.path.insert(0, str(root))
            return root
    return None


def run_occa_exhaust(records: list[dict[str, Any]], *, pillar: str) -> dict[str, Any]:
    ensure_meta_path()
    try:
        from research_methods.occa_anchor import rows_from_fixture
        from research_methods.occa_causal import build_layer_graph
        from research_methods.occa_discovery import attach_derived_algebra, run_exhaust
    except ImportError:
        return _fallback_exhaust(records)

    units = rows_from_fixture(records, pillar=pillar)
    units = attach_derived_algebra(units, bases=["effect"])
    report = run_exhaust(units, max_apriori_k=3, max_explicit=200)
    report["causal_layers"] = build_layer_graph(
        units, l1_keys=["effect"], l2_tags=["effect_HI", "effect_LO"]
    )
    return report


def _fallback_exhaust(records: list[dict[str, Any]]) -> dict[str, Any]:
    effects = [float(r.get("effect", 0.0)) for r in records]
    raw = sum(effects)
    return {
        "n_units": len(records),
        "kpi_raw": raw,
        "beats_anchor": False,
        "error_zone_pct": 100.0,
        "causal_layers": {"log_only": True, "n": len(records)},
        "fallback": True,
    }
