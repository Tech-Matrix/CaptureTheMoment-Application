from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class CameraApp(App):


    def build(self):
        '''

        
        :return:
        '''



        self.camera_obj = Camera()
        self.camera_obj.resolution = (800,800)


        #button
        button_obj = Button(text = "Capture!")
        button_obj.size_hint= (.5, .2)
        button_obj.pos_hint = {'x':.25, 'y':.25}
        button_obj.bind(on_press = self.take_image)


        #Layout
        layout = BoxLayout()
        layout.add_widget(self.camera_obj)
        layout.add_widget(button_obj)
        return layout


    def take_image(self, *args):
        print("Picture is being captured!")
        self.camera_obj.export_to_png("./selfie.png")
        

if __name__=='__main__':
    CameraApp().run()
