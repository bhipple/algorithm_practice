-- Given two integers m and l, how many common
-- divisors do they have?
import Data.List

-- This one works, but is too slow
commonDivs :: Int -> Int -> [Int]
commonDivs m l = [x | x <- [1..n], m `rem` x == 0, l `rem` x == 0]
    where n = max m l

-- This method is also ineffficient, but awesome (and fast enough)
powerset :: [a] -> [[a]]
powerset [] = [[]]
powerset (x:xs) = powerset xs ++ map (x:) (powerset xs)

factors :: Int -> Int -> [Int]
factors n t
    | n == 1 = []
    | t == n = [n]
    | n `rem` t == 0 = t : factors (n `div` t) t
    | otherwise = factors n (t+1)

primeFacts :: Int -> [Int]
primeFacts n = factors n 2

-- Like regular intersection, except it takes into account
-- duplicate occurences properly
intersect' xs ys = xs \\ (xs \\ ys)

commonPrimeFacts m l = intersect' (primeFacts m) (primeFacts l)

commonCnt m l = length divisors
    where
        commonFacts = commonPrimeFacts m l
        pset = powerset commonFacts
        divisors = nub $ map product pset

main = do
        print . show $ commonCnt 100000000 100000000
