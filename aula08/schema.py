from pandera import DataFrameModel, Field
from pandera.typing import Series

class SalesSchema(DataFrameModel):
    Produto: Series[str]
    Categoria: Series[str]
    Quantidade: Series[int] = Field(ge=0)
    Venda: Series[float] = Field(ge=0)
    Data: Series[str]

    class Config:
        coerce = True
        strict = True
