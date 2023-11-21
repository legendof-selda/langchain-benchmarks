from langchain_benchmarks.rag.tasks.semi_structured_earnings import (
    indexing,
)
from langchain_benchmarks.rag.tasks.semi_structured_earnings.indexing.retriever_registry import (
    load_docs,
)
from langchain_benchmarks.schema import RetrievalTask

DATASET_ID = "c47d9617-ab99-4d6e-a6e6-92b8daf85a7d"  # ID of public Semi-structured Earnings dataset

SEMI_STRUCTURED_EARNINGS_TASK = RetrievalTask(
    name="Semi-structured Earnings",
    dataset_id=DATASET_ID,
    retriever_factories=indexing.RETRIEVER_FACTORIES,
    architecture_factories={},
    get_docs=load_docs,
    description=(
        """\
Questions and answers based on PDFs containing tables and charts.

The task provides the raw documents as well as factory methods to easily index them
and create a retriever.

Each example is composed of a question and reference answer.

Success is measured based on the accuracy of the answer relative to the reference answer.
We also measure the faithfulness of the model's response relative to the retrieved documents (if any).
"""  # noqa: E501
    ),
)