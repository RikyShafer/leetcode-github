class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
          # 1. מתחילים בטווח שמתחיל ב-1 (המספר הראשון) ומסתיים ב-n (האורך של המערך פחות 1)
        low = 1
        high = len(nums) - 1  # כי יש n+1 מספרים בטווח [1, n]
                # 2. נכנסים ללולאת חיפוש בינארי כל עוד low קטן מ-high
        while low < high:
            # 3. מחשבים את האמצע של הטווח (mid) בין low ל-high
            mid = (low + high) // 2

            # 4. סופרים כמה מספרים במערך הם קטנים או שווים ל-mid
            #    אם יש יותר מדי מספרים כאלה, אנחנו יודעים שהכפילות נמצאת בטווח הקטן
            count = sum(num <= mid for num in nums)

            # 5. אם יש יותר מדי מספרים שמממשים את התנאי, הכפילות בטווח הנמוך
            if count > mid:
                high = mid  # צמצמנו את הטווח העליון
            else:
                low = mid + 1  # צמצמנו את הטווח התחתון

        # 6. בסוף, ה-low מצביע על המספר החוזר במערך
        return low