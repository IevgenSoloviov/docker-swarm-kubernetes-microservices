#!/bin/bash
echo "Recuperacio Apache executada: $(date)" >> /tmp/recuperacio_apache.log
sudo systemctl start apache2
