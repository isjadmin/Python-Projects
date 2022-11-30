mkdir "/home/ubuntu/python_files/file_sorting"
mkdir "/home/ubuntu/Resume_Downloads"

cp "/home/ubuntu/python_files/file_sorting/service_bash" "/etc/init.d/service_bash"

chmod +x /etc/init.d/service_bash

service service_bash start
