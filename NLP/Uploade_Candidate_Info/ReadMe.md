pip3 install -r requirement.txt

sudo apt-get install python3-requests

sudo apt-get install python3-mysql.connector

sudo apt-get install python3-openpyxl


Edit the "config.json" file with appropriate details


provide absolute path for "config.json" file in
1."updating_candidate_info.py" at line 17 and 2."file_sorting_with_thread.py" at line 18


Cross verify "directory" path in line no. 11 in both 1."file_sorting_service", 2."update_candidate_info_service" files


sudo cp <ENTER PATH OF "file_sorting_service" FILE> "/etc/init.d/file_sorting_service"

sudo cp <ENTER PATH OF "update_candidate_info_service" FILE> "/etc/init.d/update_candidate_info_service"


sudo chmod +x /etc/init.d/file_sorting_service

sudo chmod +x /etc/init.d/update_candidate_info_service


To Start the Services

sudo service file_sorting_service start

sudo service update_candidate_info_service start


To Stop the Services

sudo service file_sorting_service stop

sudo service update_candidate_info_service stop


To check Status of the Services

sudo service file_sorting_service status

sudo service update_candidate_info_service status


To check the logs

cat file_sorting_with_thread.log (check the absolute path)

cat updating_candidate_info.log (check the absolute path)
