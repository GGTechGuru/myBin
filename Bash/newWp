#! /usr/bin/bash

for CATEG in "WorkHard" "BeautifulModernHomes" "BeautifulCars" "BeautifulModernEstates"
do
	export WP_DIR="${HOME}/Pictures/${CATEG}"

        find ${WP_DIR} -type f | sort -R | tail -1 >> /tmp/wpList
done

export IMAGE_PATH=`cat /tmp/wpList | sort -R | head -1`

# export WP_URI="file://${WP_DIR}/${IMAGE_PATH}"

export WP_URI="file://${IMAGE_PATH}"

gsettings set org.gnome.desktop.background picture-uri ${WP_URI}
