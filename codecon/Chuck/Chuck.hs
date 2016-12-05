#!/usr/bin/env stack
-- stack --install-ghc runghc
import Data.Char
readInt :: IO Int
readInt = readLn

firstMultiple :: Int -> Int -> String
firstMultiple n cur = let i :: Int
                          i = read . take (length (show n)) $ show cur
                      in if i == n then show cur else firstMultiple n (cur + 4)

sol :: [Int]
sol = map digitToInt $ concatMap (`firstMultiple` 4) [1..]

main :: IO ()
main = do
    n <- readInt
    print $ sol !! (n - 1)
