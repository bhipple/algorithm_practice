-- Given two integers m and l, how many common
-- divisors do they have?
commonDivs :: Int -> Int -> [Int]
commonDivs m l = [x | x <- [1..n], m `rem` x == 0, l `rem` x == 0]
    where n = max m l
