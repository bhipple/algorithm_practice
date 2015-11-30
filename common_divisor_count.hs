-- Given two integers m and l, how many common
-- divisors do they have?

commonDivs :: Int -> Int -> Int -> [Int]
commonDivs m l x
    | (x > m) or (x > l) = []
    | mod m x == 0, mod l x == 0 = x : commonDivs m l (x+1)
    | otherwise = commonDivs m l (x+1)
