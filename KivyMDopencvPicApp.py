from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2


class MainApp(MDApp):

    def build(self):
        layout = MDBoxLayout(orientation="vertical")
        self.image = Image()
        layout.add_widget(self.image)
        self.save_img_button = MDRaisedButton(
            text="CLICK HERE",
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(None, None))
        self.save_img_button.bind(on_press=self.take_picture)
        layout.add_widget(self.save_img_button)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.0 / 30.0)
        return layout

    def load_video(self, *args):
        ret, frame = self.capture.read()
        self.image_frame = frame
        buffer1 = cv2.flip(frame, 0)
        buffer = buffer1.tostring()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture

    def take_picture(self, *args):
        image_name = "picture_at_20_22.png"
        cv2.imwrite(image_name, self.image_frame)


if __name__ == '__main__':
    MainApp().run()
