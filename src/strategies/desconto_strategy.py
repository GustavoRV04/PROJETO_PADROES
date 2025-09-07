
from abc import ABC, abstractmethod

class DescontoStrategy(ABC):
    @abstractmethod
    def calcular_desconto(self, preco: float) -> float:
        pass

class DescontoBlackFriday(DescontoStrategy):
    def calcular_desconto(self, preco: float) -> float:
        return preco * 0.25  # 25% de desconto

class DescontoEstudante(DescontoStrategy):
    def calcular_desconto(self, preco: float) -> float:
        return preco * 0.15  # 15% de desconto

class SemDesconto(DescontoStrategy):
    def calcular_desconto(self, preco: float) -> float:
        return 0.0