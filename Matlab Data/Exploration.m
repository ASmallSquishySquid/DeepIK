matObj = matfile('holo3pat3pow.mat'); %reference to the file

disp(matObj.holo_3Pat3Pow(1,:));

% for i = 1:3 %up to 3 for testing purposes, but to use need up to 729
%     p_holo(i) = matObj.holo_3Pat3Pow(i,:); %point to the column within the variable within the file of interest
%     disp(p_holo) %for monitoring progress; on lab computer each i was taking ~20 seconds
% end