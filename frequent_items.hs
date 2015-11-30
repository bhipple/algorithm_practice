-- Given a list of items and an integer k, find all items that appear >=
-- k times.  Print the set of results in order that they appear in the list.
import Data.List
import qualified Data.Set as Set
import Control.Monad

-- Returns a set of all frequent integers
freqHash :: [Int] -> Int -> Set.Set Int
freqHash lst k = Set.fromAscList freqItems
    where freqCnt = map (\x -> (head x, length x)) . group . sort $ lst
          moreThanK = filter (\(a,b) -> b >= k) freqCnt
          freqItems = map fst moreThanK

freq :: Set.Set Int -> [Int] -> [Int]
freq freqHash [] = []
freq freqHash (x:xs)
    | Set.member x freqHash = (x : freq freqHash xs)
    | otherwise = freq freqHash xs

process :: Int -> [Int] -> [Int]
process k xs = nub $ freq freqs xs
    where freqs = freqHash xs k
