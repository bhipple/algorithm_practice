-- Given two lists A and B, find the set of numbers
-- that appear more frequently in B
import Data.List
freqPair xs = map (\x -> (head x, length x)) . group . sort $ xs

differ :: Eq a => [(a,a)] -> [(a,a)] -> [a]
differ _ [] = []
differ [] (y:ys) = (fst y) : differ [] ys
differ (x:xs) (y:ys)
    | ((fst x) == (fst y)) && ((snd x) == (snd y)) = differ xs ys
    | fst x == fst y = (fst y) : differ xs ys
    | otherwise = (fst y) : differ (x:xs) ys

diff xs ys = differ (freqPair xs) (freqPair ys)
