These are my thoughts about a liblinear fork.

A lot of people would benefit from warm-restarts in the code. This seems easy to do, with a few localized changes in the train function, something like this: https://github.com/fabianp/scikit-learn/commit/fb4cde11f5e9c5ab371eda90766f77fd60d6f3d6

However, later I realized that this does not have any impact on performance, since coef is zeroed at the start of the coordinate descent algorithm (see function solve_l1r_lr in linear.cpp), so this would mean A LOT of small changes over all the code.

