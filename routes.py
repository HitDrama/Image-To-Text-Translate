from flask import Blueprint
from controllers.opencv_controller import home

from controllers.video_controller import video_feed,video_page,record_video
from controllers.license_controller import license_plate
from controllers.image_controller import image_to_text


opencv=Blueprint("opencv",__name__)

#định nghĩa router
opencv.route("/",methods=["GET","POST"])(home)
# opencv.route("/video-page",methods=["GET","POST"])(video_page)
# opencv.route("/video-feed",methods=["GET","POST"])(video_feed)
# opencv.route("/record-video",methods=["GET","POST"])(record_video)
# opencv.route("/license", methods=["GET", "POST"])(license_plate)

opencv.route("/image-to-text", methods=["GET", "POST"])(image_to_text)

