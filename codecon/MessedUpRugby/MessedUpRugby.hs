#!/usr/bin/env stack
-- stack --install-ghc runghc
import Control.Monad
import Data.Char
import Data.List
import Data.Maybe
import Data.Monoid
import Text.Regex.Posix

readInt :: IO Int
readInt = readLn

main :: IO ()
main = do
    n <- readInt
    let sols = solve n
    case length sols of
        0 -> putStrLn "0 0 0"
        _ -> mapM_ fmt . sort . nub $ sols

td (x,y,z) = (x+1,y,z)
kick (x,y,z) = (x,y+1,z)
conv (x,y,z) = (x,y,z+1)

solve :: Int -> [(Int, Int, Int)]
solve x = take x (map s [0 ..] !!)
    where s :: Int -> [(Int,Int,Int)]
          s n
            | n < 0 = []
            | n == 0 = [(0,0,0)]
            | n == 2 = [(0,0,1)]
            | n == 3 = [(0,1,0)]
            | n == 7 = [(1,0,0)]
            | otherwise = mconcat [td <$> s (n-7), kick <$> s (n-3), conv <$> s(n-2)]

fmt (x,y,z) = putStrLn . unwords $ map show [x,y,z]
