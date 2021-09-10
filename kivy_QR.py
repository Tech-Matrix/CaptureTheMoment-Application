from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import cv2
import numpy as np


class CameraApp(App):


    def build(self):
        '''
        
        :return:
        '''



        self.camera_obj = Camera()
        self.camera_obj.resolution = (800,800)
        
        #button
        button1 = Button(text = "Capture!",size_hint= (.5, .2),pos_hint = {'x':.25, 'y':.25})
        #button_obj.size_hint= (.5, .2)
        #button_obj.pos_hint = {'x':.25, 'y':.25}
        button1.bind(on_press = self.take_image)


        #button
        button2 = Button(text = "QR code scan!",size_hint= (.5, .2),pos_hint = {'x':.25, 'y':.25})
        #button_obj.size_hint= (.5, .2)
        #button_obj.pos_hint = {'x':.25, 'y':.25}
        button2.bind(on_press = self.QR_code)


        #Layout
        layout = BoxLayout()
        layout.add_widget(self.camera_obj)
        layout.add_widget(button1)
        layout.add_widget(button2)
        return layout


    def take_image(self, *args):
        print("Picture is being captured!")
        self.camera_obj.export_to_png("./selfie.png")

    def QR_code(self, *args):
        #print("QR code is being detected!")
        vid = cv2.VideoCapture(0)
        qrCodeDetector = cv2.QRCodeDetector()
        while True:
                ret,frame=vid.read()
                cv2.imshow('frame',frame)
                decodedText, points, _ = qrCodeDetector.detectAndDecode(frame)
                if points is not None:
    # QR Code detected handling code
                        print(decodedText)
                else:
                        print("QR code not detected")	
                #if cv2.waitKey(1) & 0xFF==ord('q'):
                        #break
        vid.release()

if __name__=='__main__':
    CameraApp().run()
