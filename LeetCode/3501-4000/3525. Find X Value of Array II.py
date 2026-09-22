class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        cnt = [[0] * k for _ in range(4 * n)]
        prd = [1] * (4 * n)

        def initLeaf(node, val):
            r = val % k
            cnt[node] = [0] * k
            cnt[node][r] = 1
            prd[node] = r

        def merge(node):
            left = 2 * node
            right = 2 * node + 1
            lp = prd[left]
            merged = [0] * k
        
            for q in range(k):
                merged[(q * lp) % k] += cnt[right][q]
            for r in range(k):
                merged[r] += cnt[left][r]
            cnt[node] = merged
            prd[node] = (lp * prd[right]) % k

        def build(node, lo, hi):
            if lo == hi:
                initLeaf(node, nums[lo])
                return
            mid = (lo + hi) // 2
            build(2 * node, lo, mid)
            build(2 * node + 1, mid + 1, hi)
            merge(node)

        def update(node, lo, hi, pos, val):
            if lo == hi:
                initLeaf(node, val)
                return
            mid = (lo + hi) // 2
            if pos <= mid:
                update(2 * node, lo, mid, pos, val)
            else:
                update(2 * node + 1, mid + 1, hi, pos, val)
            merge(node)

        def query(node, lo, hi, ql, qr):
            if ql <= lo and hi <= qr:
                return list(cnt[node]), prd[node]
            mid = (lo + hi) // 2
            if qr <= mid:
                return query(2 * node, lo, mid, ql, qr)
            if ql > mid:
                return query(2 * node + 1, mid + 1, hi, ql, qr)
            l_cnt, l_prd = query(2 * node, lo, mid, ql, qr)
            r_cnt, r_prd = query(2 * node + 1, mid + 1, hi, ql, qr)
            merged_cnt = [0] * k
            for q in range(k):
                merged_cnt[(q * l_prd) % k] += r_cnt[q]
            for r in range(k):
                merged_cnt[r] += l_cnt[r]
            return merged_cnt, (l_prd * r_prd) % k

        build(1, 0, n - 1)

        result = []
        for index, value, start, x in queries:
            nums[index] = value
            update(1, 0, n - 1, index, value)

            range_counts, _ = query(1, 0, n - 1, start, n - 1)
            result.append(range_counts[x])

        return result