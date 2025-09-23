Создадим паттерн `DataframeProcessingPipeline` для обработки данных по единой схеме.

```python
from abc import ABC, abstractmethod
import polars as pl


class BaseDataframeProcessor(ABC):
	@abstractmethod
	def process(self, df: pl.Dataframe) -> pl.DataFrame:
		raise NotImplementedError("Method must be implemented in child class")


class AdultClientsFilter(BaseDataframeProcessor):
	def process(self, df: pl.Dataframe) -> pl.DataFrame:
		return df.filter(pl.col("AGE") >= 18)


class RowsWithNullDeleter(BaseDataframeProcessor):
	def process(self, df: pl.Dataframe) -> pl.DataFrame:
		return df.drop_nulls()


class DataframeProcessingPipeline(ABC):
	def __init__(self):
		self.pipeline = []

	def add(self, processor: list[BaseDataframeProcessor]) -> None:
		self.pipeline.extend(processor)

	def run(self, data: pl.DataFrame) -> pl.DataFrame:
		if len(self.pipeline) == 0:
			raise AssertionError("Pipeline is empty")
		df_result = data.clone()
		for processor in self.pipeline:
			df_result = processor.process(df_result)
		return df_result


def main() -> None:
	df = pl.DataFrame(...)
	processing_pipeline = DataframeProcessingPipeline()
	processing_pipeline.add(
		[
			AdultClientsFilter(),
			RowsWithNullDeleter()
		]
	)
	df_processed = processing_pipeline.run(df)

```

