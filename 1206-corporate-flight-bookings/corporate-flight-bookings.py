class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)          # extra slot avoids bounds check on `last`
        for first, last, seats in bookings:
            diff[first - 1] += seats  # convert to 0-indexed; add at range start
            diff[last]      -= seats  # subtract just past range end

        # Prefix sum turns the diff array into actual per-flight totals
        for i in range(1, n):
            diff[i] += diff[i - 1]

        return diff[:n]
        