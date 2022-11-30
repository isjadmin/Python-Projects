pip3 install -r requirement.txt


sudo cp <ENTER PATH OF "file_sorting_service" FILE> "/etc/init.d/file_sorting_service"

sudo cp <ENTER PATH OF "update_candidate_info_service" FILE> "/etc/init.d/update_candidate_info_service"


sudo chmod +x /etc/init.d/file_sorting_service

sudo chmod +x /etc/init.d/update_candidate_info_service


service file_sorting_service start

service update_candidate_info_service start
