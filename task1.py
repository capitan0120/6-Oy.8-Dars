class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        counter = 0
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                counter += 1
            elif i == (len(flowerbed)-1) and flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i-2] == 1:
                flowerbed[i] = 1
                counter += 1
            elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                counter += 1
        if counter >= n:
            return True
        return False
