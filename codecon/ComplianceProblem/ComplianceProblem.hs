#!/usr/bin/env stack
-- stack --install-ghc runghc
import Data.List

main :: IO ()
main = do
    input <- group . sort <$> getLine
    let r = filter (odd . length) input
    if length r <= 1 then putStrLn "yes" else putStrLn "no"
