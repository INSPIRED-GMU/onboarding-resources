This page is intended for those who wish to use the Fira Code fonts in the LaTeX *output* files. If you wish to use Fira Code to display your LaTeX source files, then please check whether your LaTeX editor supports Fira Code or not.

## Activate ligatures in `lstlisting`

The [`lstfiracode`](https://ctan.org/pkg/lstfiracode) package defines `FiraCodeStyle` for the use with the [`listings`](https://ctan.org/pkg/listings) package. Here is a sample LaTeX document:

```tex
% !TeX program = XeLaTeX or LuaLaTeX
% !TeX encoding = UTF-8 Unicode
\documentclass{article}
\usepackage{fontspec}
\setmonofont{Fira Code}[
  Contextuals=Alternate  % Activate the calt feature
]
\usepackage{listings}
\usepackage{lstfiracode} % https://ctan.org/pkg/lstfiracode
\lstset{
  language=C++,
  style=FiraCodeStyle,   % Use predefined FiraCodeStyle
  basicstyle=\ttfamily   % Use \ttfamily for source code listings
}
\begin{document}
\begin{lstlisting}
/* A simple C++ program */
int main() {
    cout << "Hello World"; // prints Hello World
    return 0;
}
\end{lstlisting}
\end{document}
```

## Activate ligatures in `verbatim`

The [`lstfiracode`](https://ctan.org/pkg/lstfiracode) package also supports the `verbatim` environment. Here is a sample LaTeX document:

```tex
% !TeX program = XeLaTeX or LuaLaTeX
% !TeX encoding = UTF-8 Unicode
\documentclass{article}
\usepackage{fontspec}
\setmonofont{Fira Code}[
  Contextuals=Alternate  % Activate the calt feature
]
\usepackage{listings}
\usepackage{lstfiracode} % https://ctan.org/pkg/lstfiracode
\begin{document}
\ActivateVerbatimLigatures
\begin{verbatim}
A<-www>>=B
\end{verbatim}
\end{document}
```

If you do not wish to load the `lstfiracode` package, here is another solution:

```tex
% !TeX program = XeLaTeX or LuaLaTeX
% !TeX encoding = UTF-8 Unicode
\documentclass{article}
\usepackage{fontspec}
\setmonofont{Fira Code}[
  Contextuals=Alternate  % Activate the calt feature
]
\makeatletter
\renewcommand*\verbatim@nolig@list{} % Empty the no-ligature list
\makeatother
\begin{document}
\begin{verbatim}
A<-www>>=B
\end{verbatim}
\end{document}
```