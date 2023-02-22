class Solution:
    """
    Binary search to find the minimum capacity of a ship needed to 
    transport all the weights within a certain number of days.
    """
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            """
            Check if it's possible to ship all the weights within the given 
            capacity and the given number of days.
            """
            countDay = 1
            capLeft = cap
            for weight in weights:
                capLeft -= weight
                if capLeft < 0:
                    capLeft = cap - weight
                    countDay += 1
            return countDay <= days

        # Initialize the search range
        l, r = max(weights), sum(weights)

        # Binary search
        while l <= r:
            m = (l + r) // 2
            if canShip(m):
                # Store the last capacity when it can ship
                # bc the loop might end when it can't ship
                res = m
                r = m - 1
            else:
                l = m + 1

        return res
