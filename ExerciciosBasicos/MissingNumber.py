"""Objetivo: encontrar o número que está faltando em uma lista.

Tu recebe uma lista com números únicos de 0 até n, mas um deles está faltando. Descobre qual é!"""

"""Exemplos:
nums = [3, 0, 1]
# Resultado: 2

nums = [0, 1]
# Resultado: 2

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# Resultado: 8
"""


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i