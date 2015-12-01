-- Given a list of positive integers and an integer k,
-- find the size of the smallest subset greater than or equal to k
import Data.List

minCt :: [Int] -> Int -> Int
minCt ss t = 1 + (length $ takeWhile (< t) ss)

checkMaxThenProceed sizeSoFar t
    | (last sizeSoFar) < t = -1
    | otherwise = minCt sizeSoFar t

testRunner ts xs = map (\t -> checkMaxThenProceed sizeSoFar t) ts
    where sxs = sortBy (flip compare) xs
          sizeSoFar = (head sxs) : zipWith (+) (tail sxs) sizeSoFar
