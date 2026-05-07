"""Smoke: HF domain charter stream schema for research-art-optimization."""

from __future__ import annotations

from datasets import load_dataset


def test_fashion_mnist_stream_schema() -> None:
    rows = list(
        load_dataset(
            "zalando-datasets/fashion_mnist",
            "fashion_mnist",
            split="train",
            streaming=True,
        ).take(12)
    )
    assert len(rows) == 12
    for r in rows:
        assert "label" in r and "image" in r
