#!/usr/bin/env stack
-- stack --install-ghc runghc
import Control.Monad
import Data.Char
import Data.List
import Data.Maybe
import Data.Monoid
import Text.Regex.Posix

main :: IO ()
main = do
    input <- lines <$> getContents
    let a = head input
    let b = last input
    let c = toBase10 a
    let d = toBase10 b
    print $ c + d

toBase10 :: String -> Int
toBase10 a = let b = findBase a in conv b (length a - 1) a

findBase :: String -> Int
findBase = maximum . map charBase

charBase :: Char -> Int
charBase c = case c of
    '0' -> 1
    '1' -> 2
    '2' -> 3
    '3' -> 4
    '4' -> 5
    '5' -> 6
    '6' -> 7
    '7' -> 8
    '8' -> 9
    '9' -> 10
    'A' -> 11
    'B' -> 12
    'C' -> 13
    'D' -> 14
    'E' -> 15
    'F' -> 16

conv :: Int -> Int -> String -> Int
conv _ _ [] = 0
conv base pos (x:xs) = (base ^ pos) * (charBase x - 1) + conv base (pos-1) xs
