# pandoc-displaymath2equations

Replace blocks of displaymath with the equation environment.

## Effect

Content that would usually generate output like this:

```latex
\[
1 + 1 = 2
\]
```

will instead generate a block like this:

```latex
\begin{equation}
1 + 1 = 2
\end{equation}
```

## Usage

Install 

## Caveat

This is a **very** simple filter.
For a solution with all the bells and whistles use the (seemingly unmaintained) [pandoc-eqnos](https://github.com/tomduck/pandoc-eqnos).
