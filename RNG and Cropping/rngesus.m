function [random_num] = rngesus(matr)
%RNGesus Generates a random row number to use.
%   Returns a random number between 1 and the number of rows in a given
%   matrix. In order to pull a random pattern. This responds to changes in
%   the given matrix's size.
rows = size(matr, 1);
random_num = randi(rows, 1);
end