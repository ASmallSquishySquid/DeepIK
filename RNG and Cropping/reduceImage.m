function reduceImage
%REDUCEIMAGE Resizes all images in Images
%   Finds all images in the Images subfolder and outputs them to a folder
%   called ResizedImages cropped to 1020px x 1220px and scaled down by a
%   factor of 0.7.
files = dir('Images\*.bmp');
mkdir("ResizedImages");
for file = files'
    imwrite(imresize(imcrop(imread("Images/" + file.name), [490, 1200, 1219, 1019]), 0.7), "ResizedImages/Resized " + file.name)
end
end