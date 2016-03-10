-- Given a string, print all rotations of the string,
-- where a rotation is generated by moving the first character
-- to the end
import Data.List

move (x:xs) = xs ++ [x]

rotate (x:xs) sofar
    | length sofar == length (x:xs) = sofar
    | otherwise = rotate xr (sofar ++ [xr])
    where xr = xs ++ [x]

calcAndPrint t = do
    let res = rotate t []
    print $ concat (intersperse " " res)

main = do
        let s = rotate "abcd" []
        mapM_ putStrLn s