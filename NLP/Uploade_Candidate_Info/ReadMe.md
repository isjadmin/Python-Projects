pip3 install -r requirement.txt


Cross verify "directory" path in line no. 11 in both 1."file_sorting_service", 2."update_candidate_info_service" files


sudo cp <ENTER PATH OF "file_sorting_service" FILE> "/etc/init.d/file_sorting_service"

sudo cp <ENTER PATH OF "update_candidate_info_service" FILE> "/etc/init.d/update_candidate_info_service"


sudo chmod +x /etc/init.d/file_sorting_service

sudo chmod +x /etc/init.d/update_candidate_info_service


service file_sorting_service start

service update_candidate_info_service start


NOTE: If any error occurs while reading "config.json" file please provide absolute path for "config.json" file in
1."updating_candidate_info.py" at line 17 and 2."file_sorting_with_thread.py" at line 18
