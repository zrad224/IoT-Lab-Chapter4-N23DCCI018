import random  # Thư viện dùng để tạo các số ngẫu nhiên 

# --- BƯỚC 1: Lớp giả lập đèn LED (SimLED)  ---
class SimLED:
    def __init__(self, pin, name="LED"):
        self.pin = pin      # Lưu số chân GPIO giả lập 
        self.name = name    # Tên định danh cho đèn 
        self.is_on = False  # Trạng thái ban đầu là TẮT 

    def on(self):
        """Hàm bật đèn LED"""
        self.is_on = True
        print(f"[{self.name} pin {self.pin}] ON") # In trạng thái BẬT ra terminal 

    def off(self):
        """Hàm tắt đèn LED"""
        self.is_on = False
        print(f"[{self.name} pin {self.pin}] OFF") # In trạng thái TẮT ra terminal 

    def blink(self, on_time=1, off_time=1):
        """Giả lập nháy đèn LED với thời gian bật và tắt"""
        print(f"[{self.name}] BLINK on={on_time}s off={off_time}s") [cite: 23]


# --- BƯỚC 2: Lớp giả lập cảm biến siêu âm (SimUltrasonic)  ---
class SimUltrasonic:
    def __init__(self, echo, trigger, base_distance=50.0):
        self.echo = echo
        self.trigger = trigger
        self.base_distance = base_distance # Khoảng cách gốc làm mốc đo 

    @property
    def distance(self):
        """Hàm trả về khoảng cách đo được có kèm nhiễu Gaussian để giống cảm biến thật"""
        # Sử dụng nhiễu Gaussian với độ lệch chuẩn σ = 2.0 cm 
        raw = random.gauss(self.base_distance, 2.0) 
        # Giới hạn giá trị trả về trong khoảng [2, 400] tương ứng thông số của HC-SR04 
        return max(2, min(400, raw)) 

    def set_base(self, new_val):
        """Cài đặt lại khoảng cách mốc đo (giới hạn từ 2 đến 400)"""
        self.base_distance = max(2, min(400, new_val)) [cite: 23]


# --- BƯỚC 3: Lớp giả lập biến trở (SimPotentiometer)  ---
class SimPotentiometer:
    def __init__(self, channel=0, initial_value=0.5):
        self._value = initial_value # Giá trị khởi tạo (từ 0.0 đến 1.0) 

    @property
    def value(self):
        """Lấy giá trị hiện tại của biến trở"""
        return self._value

    def set_value(self, v):
        """Cài đặt giá trị mới cho biến trở, giới hạn trong khoảng [0.0, 1.0]"""
        self._value = max(0.0, min(1.0, float(v))) [cite: 23]


# --- BƯỚC 4: Chạy thử module (Test module)  ---
if __name__ == "__main__":
    # Thử nghiệm với LED
    led = SimLED(17, "TestLED")
    led.on()
    led.off()

    # Thử nghiệm với cảm biến siêu âm
    us = SimUltrasonic(echo=24, trigger=23)
    print("Đang đọc khoảng cách từ cảm biến siêu âm:")
    for i in range(5):
        # In giá trị khoảng cách lấy sau dấu phẩy 1 chữ số
        print(f"  Mẫu {i+1}: {us.distance:.1f} cm") [cite: 23]

    # Thử nghiệm với biến trở
    pot = SimPotentiometer()
    print(f"  Giá trị Pot ban đầu: {pot.value}")
    pot.set_value(0.8) # Thay đổi giá trị lên 0.8 
    print(f"  Giá trị Pot sau khi chỉnh: {pot.value}")
