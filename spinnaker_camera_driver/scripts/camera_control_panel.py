#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rcl_interfaces.srv import SetParameters
from rcl_interfaces.msg import Parameter, ParameterType
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import tkinter as tk
from tkinter import ttk
import threading
from PIL import Image as PILImage, ImageTk
from rclpy.qos import qos_profile_sensor_data


class CameraControlPanel(Node):
    def __init__(self):
        super().__init__('camera_control_panel')
        
        self.declare_parameter('camera_node_name', 'flir_camera')
        self.camera_node_name = self.get_parameter('camera_node_name').value
        
        self.client_driver = self.create_client(SetParameters, f'/{self.camera_node_name}/set_parameters')
        
        self.bridge = CvBridge()
        
        self.image_sub = self.create_subscription(
            Image,
            f'/{self.camera_node_name}/image_resized',
            self.image_callback,
            qos_profile_sensor_data
        )
        
        self.root = tk.Tk()
        self.root.title("FLIR Camera Control")
        self.root.geometry("900x750")
        
        self.first_image = True
        self.canvas_w = 880
        self.canvas_h = 500
        
        self.create_widgets()
        threading.Thread(target=self.initial_load, daemon=True).start()
    
    def create_widgets(self):
        content = ttk.Frame(self.root)
        content.pack(fill=tk.BOTH, expand=True)
        
        controls_frame = ttk.Frame(content, padding=5)
        controls_frame.pack(side=tk.BOTTOM, fill=tk.X, expand=False, padx=5, pady=5)
        
        video_frame = ttk.LabelFrame(content, text="Live Feed (Resized)", padding=5)
        video_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.canvas = tk.Canvas(video_frame, width=self.canvas_w, height=self.canvas_h, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        param_grid = ttk.Frame(controls_frame)
        param_grid.pack(side=tk.TOP, fill=tk.X)
        
        exp_frame = ttk.LabelFrame(param_grid, text="Exposure", padding=5)
        exp_frame.grid(row=0, column=0, sticky="nsew", padx=2)
        
        self.exposure_auto_var = tk.StringVar(value="Off")
        ttk.Checkbutton(exp_frame, text="Auto", variable=self.exposure_auto_var,
                       onvalue="Continuous", offvalue="Off",
                       command=self.set_exposure_auto).pack(anchor=tk.W)
        
        ttk.Label(exp_frame, text="Time (us)").pack(anchor=tk.W)
        self.exposure_scale = ttk.Scale(exp_frame, from_=100, to=30000, command=self.on_exposure_slide)
        self.exposure_scale.pack(fill=tk.X)
        
        self.exposure_entry = ttk.Entry(exp_frame)
        self.exposure_entry.pack(fill=tk.X)
        self.exposure_entry.bind('<Return>', self.set_exposure_manual)
        
        gain_frame = ttk.LabelFrame(param_grid, text="Gain", padding=5)
        gain_frame.grid(row=0, column=1, sticky="nsew", padx=2)
        
        self.gain_auto_var = tk.StringVar(value="Off")
        ttk.Checkbutton(gain_frame, text="Auto", variable=self.gain_auto_var,
                       onvalue="Continuous", offvalue="Off",
                       command=self.set_gain_auto).pack(anchor=tk.W)
        
        ttk.Label(gain_frame, text="Gain (dB)").pack(anchor=tk.W)
        self.gain_scale = ttk.Scale(gain_frame, from_=0, to=30, command=self.on_gain_slide)
        self.gain_scale.pack(fill=tk.X)
        
        self.gain_entry = ttk.Entry(gain_frame)
        self.gain_entry.pack(fill=tk.X)
        self.gain_entry.bind('<Return>', self.set_gain_manual)
        
        fps_frame = ttk.LabelFrame(param_grid, text="FPS", padding=5)
        fps_frame.grid(row=0, column=2, sticky="nsew", padx=2)
        
        self.fps_enable_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(fps_frame, text="Enable", variable=self.fps_enable_var,
                       command=self.set_fps_enable).pack(anchor=tk.W)
        
        ttk.Label(fps_frame, text="Rate (Hz)").pack(anchor=tk.W)
        self.fps_scale = ttk.Scale(fps_frame, from_=1, to=120, command=self.on_fps_slide)
        self.fps_scale.pack(fill=tk.X)
        
        self.fps_entry = ttk.Entry(fps_frame)
        self.fps_entry.pack(fill=tk.X)
        self.fps_entry.bind('<Return>', self.set_fps_manual)
        
        wb_frame = ttk.LabelFrame(param_grid, text="White Balance", padding=5)
        wb_frame.grid(row=0, column=3, sticky="nsew", padx=2)
        
        self.wb_auto_var = tk.StringVar(value="Continuous")
        ttk.Checkbutton(wb_frame, text="Auto", variable=self.wb_auto_var,
                       onvalue="Continuous", offvalue="Off",
                       command=self.set_wb_auto).pack(anchor=tk.W)
        
        self.status_label = ttk.Label(controls_frame, text="Status: Ready", wraplength=780)
        self.status_label.pack(side=tk.BOTTOM, pady=5)
        
        param_grid.columnconfigure(0, weight=1)
        param_grid.columnconfigure(1, weight=1)
        param_grid.columnconfigure(2, weight=1)
        param_grid.columnconfigure(3, weight=1)
        
        self.exposure_timer = None
        self.gain_timer = None
        self.fps_timer = None
    
    def image_callback(self, msg):
        try:
            cv_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            h, w = cv_img.shape[:2]
            
            if self.first_image:
                self.first_image = False
                self.send_driver_param('balance_white_auto', 'Continuous', ParameterType.PARAMETER_STRING)
            
            scale_w = self.canvas_w / float(w)
            scale_h = self.canvas_h / float(h)
            scale = min(scale_w, scale_h)
            
            new_w = int(w * scale)
            new_h = int(h * scale)
            
            cv_img_resized = cv2.resize(cv_img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
            cv_img_rgb = cv2.cvtColor(cv_img_resized, cv2.COLOR_BGR2RGB)
            pil_img = PILImage.fromarray(cv_img_rgb)
            tk_img = ImageTk.PhotoImage(image=pil_img)
            
            x_offset = (self.canvas_w - new_w) // 2
            y_offset = (self.canvas_h - new_h) // 2
            
            self.root.after_idle(self.update_canvas, tk_img, x_offset, y_offset)
        except Exception as e:
            pass
    
    def update_canvas(self, tk_img, x, y):
        self.canvas.delete("all")
        self.canvas.create_image(x, y, anchor=tk.NW, image=tk_img)
        self.canvas.image = tk_img
    
    def initial_load(self):
        if not self.client_driver.wait_for_service(timeout_sec=2.0):
            self.root.after_idle(lambda: self.status_label.config(text="Error: Camera Driver service not found"))
            return
        self.root.after_idle(lambda: self.status_label.config(text="Services connected. Ready"))
    
    def send_driver_param(self, name, value, ptype):
        req = SetParameters.Request()
        param = Parameter()
        param.name = name
        param.value.type = ptype
        
        if ptype == ParameterType.PARAMETER_BOOL:
            param.value.bool_value = bool(value)
        elif ptype == ParameterType.PARAMETER_INTEGER:
            param.value.integer_value = int(value)
        elif ptype == ParameterType.PARAMETER_DOUBLE:
            param.value.double_value = float(value)
        elif ptype == ParameterType.PARAMETER_STRING:
            param.value.string_value = str(value)
        
        req.parameters = [param]
        self.client_driver.call_async(req)
    
    def set_exposure_auto(self):
        self.send_driver_param('exposure_auto', self.exposure_auto_var.get(), ParameterType.PARAMETER_STRING)
    
    def on_exposure_slide(self, val):
        if self.exposure_timer:
            self.exposure_timer.cancel()
        self.exposure_timer = threading.Timer(0.2, self.set_exposure_manual_slide, args=[val])
        self.exposure_timer.start()
    
    def set_exposure_manual_slide(self, val):
        self.exposure_entry.delete(0, tk.END)
        self.exposure_entry.insert(0, str(int(float(val))))
        self.send_driver_param('exposure_time', float(val), ParameterType.PARAMETER_DOUBLE)
    
    def set_exposure_manual(self, event):
        try:
            val = float(self.exposure_entry.get())
            self.exposure_scale.set(val)
            self.send_driver_param('exposure_time', val, ParameterType.PARAMETER_DOUBLE)
        except ValueError:
            pass
    
    def set_gain_auto(self):
        self.send_driver_param('gain_auto', self.gain_auto_var.get(), ParameterType.PARAMETER_STRING)
    
    def on_gain_slide(self, val):
        if self.gain_timer:
            self.gain_timer.cancel()
        self.gain_timer = threading.Timer(0.2, self.set_gain_manual_slide, args=[val])
        self.gain_timer.start()
    
    def set_gain_manual_slide(self, val):
        self.gain_entry.delete(0, tk.END)
        self.gain_entry.insert(0, str(round(float(val), 2)))
        self.send_driver_param('gain', float(val), ParameterType.PARAMETER_DOUBLE)
    
    def set_gain_manual(self, event):
        try:
            val = float(self.gain_entry.get())
            self.gain_scale.set(val)
            self.send_driver_param('gain', val, ParameterType.PARAMETER_DOUBLE)
        except ValueError:
            pass
    
    def set_fps_enable(self):
        self.send_driver_param('frame_rate_enable', self.fps_enable_var.get(), ParameterType.PARAMETER_BOOL)
    
    def on_fps_slide(self, val):
        if self.fps_timer:
            self.fps_timer.cancel()
        self.fps_timer = threading.Timer(0.2, self.set_fps_manual_slide, args=[val])
        self.fps_timer.start()
    
    def set_fps_manual_slide(self, val):
        self.fps_entry.delete(0, tk.END)
        self.fps_entry.insert(0, str(round(float(val), 2)))
        self.send_driver_param('frame_rate', float(val), ParameterType.PARAMETER_DOUBLE)
    
    def set_fps_manual(self, event):
        try:
            val = float(self.fps_entry.get())
            self.fps_scale.set(val)
            self.send_driver_param('frame_rate', val, ParameterType.PARAMETER_DOUBLE)
        except ValueError:
            pass
    
    def set_wb_auto(self):
        self.send_driver_param('balance_white_auto', self.wb_auto_var.get(), ParameterType.PARAMETER_STRING)
    
    def run(self):
        while rclpy.ok():
            rclpy.spin_once(self, timeout_sec=0.0)
            self.root.update()


def main(args=None):
    rclpy.init(args=args)
    panel = CameraControlPanel()
    try:
        panel.run()
    except KeyboardInterrupt:
        pass
    finally:
        panel.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
