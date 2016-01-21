-- Playing with the example code from
-- https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf
-- to generate lazyily evaluated infinite lists of
-- prime numbers.
import qualified Data.Map as Map

-- By trial division
trialPrimes = 2 : [x | x <- [3..], isprime x]
isprime x = all (\p -> x `mod` p > 0) (factorsToTry x)
    where
        factorsToTry x = takeWhile (\p -> p*p <= x) trialPrimes

-- With a map. Significantly improved asymptotic performance,
-- with significantly worse constant factors
mapSieve :: [Int] -> [Int]
mapSieve xs = sieve' xs Map.empty
    where
        sieve' [] table = []
        sieve' (x:xs) table =
            case Map.lookup x table of
                Nothing -> x : sieve' xs (Map.insert (x*x) [x] table)
                Just facts -> sieve' xs (foldl reinsert (Map.delete x table) facts)
              where
                reinsert table prime = Map.insertWith (++) (x+prime) [prime] table
mapPrimes = mapSieve [2..]
