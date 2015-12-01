-- Given two lists A and B, find the set of numbers
-- that appear more frequently in B
import Data.List
import Data.Map

minVal xs ys = min (minimum xs) (minimum ys)

buildMap hasher xs = fromList freqCnt
    where freqCnt = Data.List.map (\x -> (hasher $ head x, length x)) . group . sort $ xs

differ _ [] = []
differ xMap (y:ys)
    | Data.Map.lookup k xMap == v = differ xMap ys
    | otherwise = v : differ xMap ys
    where k = fst y
          v = snd y

diff :: (Num a, Ord a) => [a] -> [a] -> Map a Int
diff xs ys = differ xMap (toList yMap)
    where minV = minVal xs ys
          hasher = flip (-) minV
          unhasher = (+) minV
          builder = buildMap hasher
          xMap = builder xs
          yMap = builder ys
