Исходный код:

```python
import polars as pl

class DataframePreprocessor:
    def __init__(self, data: pl.DataFrame):
        self.df = data

    def drop_nulls(self, columns: list[str]) -> 'DataframePreprocessor':
        if len(columns):
            self.df = self.df.drop_nulls(subset=columns)
        else:
            self.df = self.df.drop_nulls()
        return self

    def cast_column(
	    self, 
	    column: str, 
	    dtype: pl.datatypes.DataType
	) ->'DataframePreprocessor':
        self.df = self.df.with_columns(
            pl.col(column).cast(dtype).alias(column)
        )
        return self

    def filter_rows(self, condition: pl.Expr) -> 'DataframePreprocessor':
        self.df = self.df.filter(condition)
        return self

    def add_column(self, name: str, expr: pl.Expr) -> 'DataframePreprocessor':
        self.df = self.df.with_columns(expr.alias(name))
        return self

	def get_data(self) -> pl.DataFrame:
		return self.df
```

Экземпляр данного класса содержит некоторый датафрейм, который изменяется при вызове отдельных методов.

Код, переписанный в функциональном стиле:

```python
import polars as pl

def drop_nulls_in_dataframe(data: pl.DataFrame, columns: list[str]) -> pl.DataFrame:
	if len(columns):
		return data.drop_nulls(subset=columns)
	return data.drop_nulls()

def convert_column_type_in_dataframe(
	data: pl.DataFrame, 
	column: str, 
	dtype: pl.datatypes.DataType
): -> pl.DataFrame
    return data.with_columns(
        pl.col(column).cast(dtype).alias(column)
    )

def filter_rows_in_dataframe(
	data: pl.DataFrame, 
	condition: pl.Expr
) -> pl.DataFrame:
    return data.filter(condition)

def add_column_to_dataframe(
	data: pl.DataFrame,
	name: str, 
	expr: pl.Expr
) -> pl.DataFrame:
    return data.with_columns(expr.alias(name))		
```

Исходный класс разбит на обособленные чистые функции, каждая из которых принимает на вход некоторый датафрейм и возвращает его изменённую версию, не меняя исходного объекта.
