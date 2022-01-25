function adjustImage
	%ADJUSTIMAGE Converts all images in Images to black and white
	%   Finds all images in the Images subfolder and outputs them to a folder
	%   called AdjustedImages in black and white
	files = dir('Images\*.bmp');
	mkdir("Adjusted Images");
	for file = files'
 		img = im2gray(imread("Images/" + file.name));
        img(img >= 185) = 255;  % threshold
 		img(img < 185) = 0;
        img(1:216, :) = 0;
 		imwrite(img, "Adjusted Images/Saturated " + file.name)
	end
end