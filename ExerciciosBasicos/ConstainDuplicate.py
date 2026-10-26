"""Objetivo: descobrir se uma lista possui algum número repetido.

Você vai receber uma lista de números inteiros nums. Sua missão é retornar:
- True se algum número aparecer duas ou mais vezes.
- False se todos os números forem diferentes."""

"""nums = [1, 2, 3, 1]
# Resultado: True

nums = [1, 2, 3, 4]
# Resultado: False"""


nums = [1, 2, 3, 1]



class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        duplicados = len(nums) != len(set(nums))
        if duplicados == True:
            return True
        else:
            return False