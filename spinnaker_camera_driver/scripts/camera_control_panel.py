#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rcl_interfaces.srv import SetParameters, GetParameters
from rcl_interfaces.msg import Parameter, ParameterType, ParameterValue
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge
import cv2
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import queue
from PIL import Image as PILImage, ImageTk

class CameraControlPanel(Node):
    def __init__(self):
        super().__init__('camera_control_panel')
        self.declare_parameter('camera_node_name', '/flir_camera')
        self.camera_node_name = self.get_parameter('camera_node_name').value
        
        self.client = self.create_client(SetParameters, f'{self.camera_node_name}/set_parameters')
        self.get_client = self.create_client(GetParameters, f'{self.camera_node_name}/get_parameters')
        
        # Image subscription
        self.bridge = CvBridge()
        self.image_sub = self.create_subscription(
            Image, 
            f'{self.camera_node_name}/image_raw', 
            self.image_callback, 
            1)
        
        self.root = tk.Tk()
        self.root.title("FLIR Camera Control")
        self.root.geometry("800x1000")
        
        # Queue for thread-safe UI updates
        self.gui_queue = queue.Queue()
        
        self.create_widgets()
        
        # Start queue processing
        self.process_queue()
        
        # Start a thread to check connection and load initial values
        threading.Thread(target=self.initial_load, daemon=True).start()

    def process_queue(self):
        try:
            while True:
                task = self.gui_queue.get_nowait()
                task()
        except queue.Empty:
            pass
        finally:
            self.root.after(10, self.process_queue) # Faster update for video

    def initial_load(self):
        if not self.client.wait_for_service(timeout_sec=2.0):
             self.update_status("Waiting for camera node...")
             
        # Initial Get of parameters
        self.refresh_all_parameters()

    def create_widgets(self):
        # Layout: Controls at bottom (packed first to guarantee space), Video on top
        
        content = ttk.Frame(self.root)
        content.pack(fill=tk.BOTH, expand=True)
        
        # Controls Frame - MUST be packed BEFORE video so it gets space first
        controls_frame = ttk.Frame(content, padding="5")
        controls_frame.pack(side=tk.BOTTOM, fill=tk.X, expand=False, padx=5, pady=5)
        
        # Video Frame - takes remaining space
        video_frame = ttk.LabelFrame(content, text="Live Feed", padding="5")
        video_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.video_label = ttk.Label(video_frame, text="Waiting for image...")
        self.video_label.pack(fill=tk.BOTH, expand=True)

        # Node Connection
        conn_frame = ttk.LabelFrame(controls_frame, text="Connection", padding="5")
        conn_frame.pack(side=tk.TOP, fill=tk.X, pady=5)
        
        ttk.Label(conn_frame, text="Node Name:").pack(side=tk.LEFT)
        self.node_name_entry = ttk.Entry(conn_frame)
        self.node_name_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.node_name_entry.insert(0, self.camera_node_name)
        ttk.Button(conn_frame, text="Reconnect", command=self.reconnect).pack(side=tk.LEFT)

        # Parameter Grid
        param_grid = ttk.Frame(controls_frame)
        param_grid.pack(side=tk.TOP, fill=tk.X)
        
        # Exposure
        exp_frame = ttk.LabelFrame(param_grid, text="Exposure", padding="5")
        exp_frame.grid(row=0, column=0, sticky="nsew", padx=2)
        
        self.exposure_auto_var = tk.StringVar(value="Off")
        ttk.Checkbutton(exp_frame, text="Auto", variable=self.exposure_auto_var, 
                        onvalue="Continuous", offvalue="Off", command=self.set_exposure_auto).pack(anchor=tk.W)
        
        ttk.Label(exp_frame, text="Time (us):").pack(anchor=tk.W)
        self.exposure_scale = ttk.Scale(exp_frame, from_=100, to=30000, command=self.on_exposure_slide)
        self.exposure_scale.pack(fill=tk.X)
        self.exposure_entry = ttk.Entry(exp_frame)
        self.exposure_entry.pack(fill=tk.X)
        self.exposure_entry.bind('<Return>', self.set_exposure_manual)
        
        # Gain
        gain_frame = ttk.LabelFrame(param_grid, text="Gain", padding="5")
        gain_frame.grid(row=0, column=1, sticky="nsew", padx=2)
        
        self.gain_auto_var = tk.StringVar(value="Off")
        ttk.Checkbutton(gain_frame, text="Auto", variable=self.gain_auto_var, 
                        onvalue="Continuous", offvalue="Off", command=self.set_gain_auto).pack(anchor=tk.W)
        
        ttk.Label(gain_frame, text="dB:").pack(anchor=tk.W)
        self.gain_scale = ttk.Scale(gain_frame, from_=0, to=30, command=self.on_gain_slide)
        self.gain_scale.pack(fill=tk.X)
        self.gain_entry = ttk.Entry(gain_frame)
        self.gain_entry.pack(fill=tk.X)
        self.gain_entry.bind('<Return>', self.set_gain_manual)

        # FPS
        fps_frame = ttk.LabelFrame(param_grid, text="FPS", padding="5")
        fps_frame.grid(row=0, column=2, sticky="nsew", padx=2)
        
        self.fps_enable_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(fps_frame, text="Enable", variable=self.fps_enable_var, 
                        command=self.set_fps_enable).pack(anchor=tk.W)
        
        ttk.Label(fps_frame, text="Rate:").pack(anchor=tk.W)
        self.fps_scale = ttk.Scale(fps_frame, from_=1, to=120, command=self.on_fps_slide)
        self.fps_scale.pack(fill=tk.X)
        self.fps_entry = ttk.Entry(fps_frame)
        self.fps_entry.pack(fill=tk.X)
        self.fps_entry.bind('<Return>', self.set_fps_manual)

        # Resolution
        res_frame = ttk.LabelFrame(controls_frame, text="Resolution", padding="5")
        res_frame.pack(side=tk.TOP, fill=tk.X, pady=5)
        
        ttk.Label(res_frame, text="W:").pack(side=tk.LEFT)
        self.width_entry = ttk.Entry(res_frame, width=6)
        self.width_entry.pack(side=tk.LEFT, padx=2)
        
        ttk.Label(res_frame, text="H:").pack(side=tk.LEFT)
        self.height_entry = ttk.Entry(res_frame, width=6)
        self.height_entry.pack(side=tk.LEFT, padx=2)
        
        ttk.Label(res_frame, text="Off X:").pack(side=tk.LEFT)
        self.offset_x_entry = ttk.Entry(res_frame, width=6)
        self.offset_x_entry.pack(side=tk.LEFT, padx=2)
        
        ttk.Label(res_frame, text="Off Y:").pack(side=tk.LEFT)
        self.offset_y_entry = ttk.Entry(res_frame, width=6)
        self.offset_y_entry.pack(side=tk.LEFT, padx=2)
        
        ttk.Button(res_frame, text="Set", command=self.set_resolution).pack(side=tk.LEFT, padx=5)

        # Binning
        bin_frame = ttk.LabelFrame(controls_frame, text="Binning", padding="5")
        bin_frame.pack(side=tk.TOP, fill=tk.X, pady=5)
        
        ttk.Label(bin_frame, text="X:").pack(side=tk.LEFT)
        self.bin_x_entry = ttk.Entry(bin_frame, width=6)
        self.bin_x_entry.pack(side=tk.LEFT, padx=2)
        
        ttk.Label(bin_frame, text="Y:").pack(side=tk.LEFT)
        self.bin_y_entry = ttk.Entry(bin_frame, width=6)
        self.bin_y_entry.pack(side=tk.LEFT, padx=2)
        
        ttk.Button(bin_frame, text="Set", command=self.set_binning).pack(side=tk.LEFT, padx=5)

        # Status
        self.status_label = ttk.Label(controls_frame, text="Status: Ready", wraplength=480)
        self.status_label.pack(side=tk.BOTTOM, pady=5)
        
        # Debounce timers
        self.exposure_timer = None
        self.gain_timer = None
        self.fps_timer = None
        
        # Grid scaling
        param_grid.columnconfigure(0, weight=1)
        param_grid.columnconfigure(1, weight=1)
        param_grid.columnconfigure(2, weight=1)

    def image_callback(self, msg):
        # Convert ROS Image to OpenCV
        try:
            cv_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            
            # Resize to fit label (max 640x480 for display performance)
            h, w = cv_img.shape[:2]
            target_w = 640
            scale = target_w / w
            target_h = int(h * scale)
            
            cv_img_small = cv2.resize(cv_img, (target_w, target_h))
            
            # Convert to PIL
            cv_img_rgb = cv2.cvtColor(cv_img_small, cv2.COLOR_BGR2RGB)
            pil_img = PILImage.fromarray(cv_img_rgb)
            
            # Pass PIL image to queue. Create ImageTk in the GUI update task.
            self.gui_queue.put(lambda: self.update_video_label(pil_img))
            
        except Exception as e:
            self.get_logger().warn(f"Image callback error: {e}")

    def update_video_label(self, pil_img):
        try:
            tk_img = ImageTk.PhotoImage(image=pil_img, master=self.root)
            self.video_label.configure(image=tk_img, text="")
            self.video_label.image = tk_img # Keep reference!
        except Exception as e:
            print(f"Error updating video label: {e}")

    def reconnect(self):
        new_node = self.node_name_entry.get()
        if new_node != self.camera_node_name:
            self.camera_node_name = new_node
            self.client = self.create_client(SetParameters, f'{self.camera_node_name}/set_parameters')
            self.get_client = self.create_client(GetParameters, f'{self.camera_node_name}/get_parameters')
            
            # Re-subscribe
            if self.image_sub:
                self.destroy_subscription(self.image_sub)
            self.image_sub = self.create_subscription(
                Image, 
                f'{self.camera_node_name}/image_raw', 
                self.image_callback, 
                1)
                
            self.refresh_all_parameters()

    def refresh_all_parameters(self):
        names = [
            'exposure_auto', 'exposure_time',
            'gain_auto', 'gain',
            'frame_rate_enable', 'frame_rate',
            'image_width', 'image_height', 'offset_x', 'offset_y',
            'binning_x', 'binning_y'
        ]
        
        if not self.get_client.wait_for_service(timeout_sec=1.0):
            self.update_status("Status: Camera service not available")
            return

        req = GetParameters.Request()
        req.names = names
        future = self.get_client.call_async(req)
        future.add_done_callback(self.on_get_params_done)

    def on_get_params_done(self, future):
        try:
            res = future.result()
            self.gui_queue.put(lambda: self.update_ui_with_params(res))
        except Exception as e:
            self.update_status(f"Status: Failed to get parameters: {e}")

    def update_ui_with_params(self, res):
        try:
            p_values = res.values
            if len(p_values) >= 12:
                # Exposure
                # Check parameter type, it might be NOT_SET or invalid if parameter doesn't exist
                if p_values[0].type == ParameterType.PARAMETER_STRING:
                    self.exposure_auto_var.set(p_values[0].string_value)
                if p_values[1].type == ParameterType.PARAMETER_DOUBLE:
                    self.exposure_scale.set(p_values[1].double_value)
                    self.update_entry(self.exposure_entry, str(p_values[1].double_value))
                
                # Gain
                if p_values[2].type == ParameterType.PARAMETER_STRING:
                    self.gain_auto_var.set(p_values[2].string_value)
                if p_values[3].type == ParameterType.PARAMETER_DOUBLE:
                    self.gain_scale.set(p_values[3].double_value)
                    self.update_entry(self.gain_entry, str(p_values[3].double_value))
                
                # FPS
                if p_values[4].type == ParameterType.PARAMETER_BOOL:
                    self.fps_enable_var.set(p_values[4].bool_value)
                if p_values[5].type == ParameterType.PARAMETER_DOUBLE:
                    self.fps_scale.set(p_values[5].double_value)
                    self.update_entry(self.fps_entry, str(p_values[5].double_value))
                    
                # Resolution
                if p_values[6].type == ParameterType.PARAMETER_INTEGER:
                    self.update_entry(self.width_entry, str(p_values[6].integer_value))
                if p_values[7].type == ParameterType.PARAMETER_INTEGER:
                    self.update_entry(self.height_entry, str(p_values[7].integer_value))
                if p_values[8].type == ParameterType.PARAMETER_INTEGER:
                    self.update_entry(self.offset_x_entry, str(p_values[8].integer_value))
                if p_values[9].type == ParameterType.PARAMETER_INTEGER:
                    self.update_entry(self.offset_y_entry, str(p_values[9].integer_value))

                # Binning
                if p_values[10].type == ParameterType.PARAMETER_INTEGER:
                    self.update_entry(self.bin_x_entry, str(p_values[10].integer_value))
                if p_values[11].type == ParameterType.PARAMETER_INTEGER:
                    self.update_entry(self.bin_y_entry, str(p_values[11].integer_value))
                    
            self.update_status(f"Status: Parameters loaded from {self.camera_node_name}")
        except Exception as e:
             self.update_status(f"Status: Error updating UI: {e}")

    def update_status(self, text):
        self.gui_queue.put(lambda: self.status_label.config(text=text))

    def update_entry(self, entry, value):
        if threading.current_thread() is threading.main_thread():
             entry.delete(0, tk.END)
             entry.insert(0, value)
        else:
             self.gui_queue.put(lambda: self.update_entry(entry, value))

    def send_param(self, name, value, p_type):
        req = SetParameters.Request()
        param = Parameter()
        param.name = name
        
        pval = ParameterValue()
        pval.type = p_type
        
        if p_type == ParameterType.PARAMETER_BOOL:
            pval.bool_value = bool(value)
        elif p_type == ParameterType.PARAMETER_INTEGER:
            pval.integer_value = int(value)
        elif p_type == ParameterType.PARAMETER_DOUBLE:
            pval.double_value = float(value)
        elif p_type == ParameterType.PARAMETER_STRING:
            pval.string_value = str(value)
            
        param.value = pval
        req.parameters = [param]
        
        if self.client.service_is_ready():
            future = self.client.call_async(req)
            future.add_done_callback(lambda f: self.on_set_param_done(f, name))
        else:
            self.update_status("Status: Service not ready")

    def on_set_param_done(self, future, name):
        try:
            res = future.result()
            if res.results[0].successful:
                self.update_status(f"Status: Set {name} successfully")
            else:
                self.update_status(f"Status: Failed to set {name}: {res.results[0].reason}")
        except Exception as e:
             self.update_status(f"Status: Error setting {name}: {e}")

    # Exposure Callbacks
    def set_exposure_auto(self):
        val = self.exposure_auto_var.get()
        self.send_param("exposure_auto", val, ParameterType.PARAMETER_STRING)
        
    def on_exposure_slide(self, val):
        if self.exposure_timer:
            self.exposure_timer.cancel()
        self.exposure_timer = threading.Timer(0.2, self.set_exposure_manual_from_slide, args=[val])
        self.exposure_timer.start()
        
    def set_exposure_manual_from_slide(self, val):
        self.update_entry(self.exposure_entry, str(float(val)))
        self.send_param("exposure_time", float(val), ParameterType.PARAMETER_DOUBLE)

    def set_exposure_manual(self, event):
        try:
            val = float(self.exposure_entry.get())
            self.exposure_scale.set(val)
            self.send_param("exposure_time", val, ParameterType.PARAMETER_DOUBLE)
        except ValueError:
            pass

    # Gain Callbacks
    def set_gain_auto(self):
        val = self.gain_auto_var.get()
        self.send_param("gain_auto", val, ParameterType.PARAMETER_STRING)

    def on_gain_slide(self, val):
        if self.gain_timer:
             self.gain_timer.cancel()
        self.gain_timer = threading.Timer(0.2, self.set_gain_manual_from_slide, args=[val])
        self.gain_timer.start()

    def set_gain_manual_from_slide(self, val):
        self.update_entry(self.gain_entry, str(float(val)))
        self.send_param("gain", float(val), ParameterType.PARAMETER_DOUBLE)

    def set_gain_manual(self, event):
        try:
            val = float(self.gain_entry.get())
            self.gain_scale.set(val)
            self.send_param("gain", val, ParameterType.PARAMETER_DOUBLE)
        except ValueError:
            pass

    # FPS Callbacks
    def set_fps_enable(self):
        val = self.fps_enable_var.get()
        self.send_param("frame_rate_enable", val, ParameterType.PARAMETER_BOOL)

    def on_fps_slide(self, val):
        if self.fps_timer:
            self.fps_timer.cancel()
        self.fps_timer = threading.Timer(0.2, self.set_fps_manual_from_slide, args=[val])
        self.fps_timer.start()
        
    def set_fps_manual_from_slide(self, val):
        self.update_entry(self.fps_entry, str(float(val)))
        self.send_param("frame_rate", float(val), ParameterType.PARAMETER_DOUBLE)
        
    def set_fps_manual(self, event):
         try:
            val = float(self.fps_entry.get())
            self.fps_scale.set(val)
            self.send_param("frame_rate", val, ParameterType.PARAMETER_DOUBLE)
         except ValueError:
            pass

    # Resolution Callbacks
    def set_resolution(self):
        try:
             w = int(self.width_entry.get())
             h = int(self.height_entry.get())
             off_x = int(self.offset_x_entry.get())
             off_y = int(self.offset_y_entry.get())
             
             # Just send the params — C++ driver handles stop/restart streaming
             req = SetParameters.Request()
             
             p_w = Parameter()
             p_w.name = "image_width"
             p_w.value.type = ParameterType.PARAMETER_INTEGER
             p_w.value.integer_value = w
             
             p_h = Parameter()
             p_h.name = "image_height"
             p_h.value.type = ParameterType.PARAMETER_INTEGER
             p_h.value.integer_value = h
             
             p_ox = Parameter()
             p_ox.name = "offset_x"
             p_ox.value.type = ParameterType.PARAMETER_INTEGER
             p_ox.value.integer_value = off_x
             
             p_oy = Parameter()
             p_oy.name = "offset_y"
             p_oy.value.type = ParameterType.PARAMETER_INTEGER
             p_oy.value.integer_value = off_y
             
             req.parameters = [p_w, p_h, p_ox, p_oy]
             future = self.client.call_async(req)
             future.add_done_callback(lambda f: self.on_set_param_done(f, "Resolution"))
             
        except ValueError:
            messagebox.showerror("Error", "Invalid integer values for resolution")

    # Binning Callbacks
    def set_binning(self):
        try:
             bx = int(self.bin_x_entry.get())
             by = int(self.bin_y_entry.get())
             
             # Just send the params — C++ driver handles stop/restart streaming
             req = SetParameters.Request()
             
             p_x = Parameter()
             p_x.name = "binning_x"
             p_x.value.type = ParameterType.PARAMETER_INTEGER
             p_x.value.integer_value = bx
             
             p_y = Parameter()
             p_y.name = "binning_y"
             p_y.value.type = ParameterType.PARAMETER_INTEGER
             p_y.value.integer_value = by
             
             req.parameters = [p_x, p_y]
             future = self.client.call_async(req)
             future.add_done_callback(lambda f: self.on_set_param_done(f, "Binning"))
             
        except ValueError:
            messagebox.showerror("Error", "Invalid integer values for binning")

    def run(self):
        while rclpy.ok():
             rclpy.spin_once(self, timeout_sec=0.01) # Faster spin to keep up with video
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
