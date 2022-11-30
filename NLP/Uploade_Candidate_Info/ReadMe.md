pip3 install -r requirement.txt

cp "/home/ubuntu/python_files/file_sorting_service" "/etc/init.d/file_sorting_service"

cp "/home/ubuntu/python_files/update_candidate_info_service" "/etc/init.d/update_candidate_info_service"

chmod +x /etc/init.d/file_sorting_service
chmod +x /etc/init.d/update_candidate_info_service

service file_sorting_service start
service update_candidate_info_service start
