import cv2
import json
import qrcode
import os
from datetime import datetime

class QRDataExtractor:
    def __init__(self):
        self.qr_folder = "issued_certs"
        if not os.path.exists(self.qr_folder):
            os.makedirs(self.qr_folder)

    def create_data_qr(self, name, course, grade):
        """Encodes all certificate details into a single QR code."""
        cert_info = {
            "holder": name,
            "subject": course,
            "grade": grade,
            "issued_on": str(datetime.now().date()),
            "auth_code": "VERIFIED-ORG-2026"  # Digital watermark
        }
        
        # Convert dictionary to JSON string
        raw_data = json.dumps(cert_info)
        
        # Generate the QR
        qr = qrcode.QRCode(box_size=10, border=4)
        qr.add_data(raw_data)
        qr.make(fit=True)
        
        file_path = f"{self.qr_folder}/{name.replace(' ', '_')}.png"
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_path)
        print(f"✅ QR Created: {file_path}")

    def start_scanning(self):
        """Captures webcam feed and derives all info from the QR."""
        cap = cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()

        print("\n[SYSTEM] Scanner active. Show the QR to the camera. Press 'Q' to exit.")

        while True:
            success, frame = cap.read()
            if not success: break

            # Detect and Decode
            data, bbox, _ = detector.detectAndDecode(frame)

            if data:
                try:
                    # Derive all info from the decoded string
                    info = json.loads(data)
                    
                    # Formatting the extracted data for display
                    display_text = [
                        f"Status: VALID" if info.get("auth_code") == "VERIFIED-ORG-2026" else "Status: INVALID",
                        f"Name: {info.get('holder')}",
                        f"Course: {info.get('subject')}",
                        f"Grade: {info.get('grade')}",
                        f"Date: {info.get('issued_on')}"
                    ]

                    # Overlay info on the video feed
                    for i, line in enumerate(display_text):
                        color = (0, 255, 0) if "VALID" in line else (255, 255, 255)
                        cv2.putText(frame, line, (20, 50 + (i * 30)), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
                
                except json.JSONDecodeError:
                    cv2.putText(frame, "Error: Unknown QR Format", (20, 50), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            cv2.imshow("QR Information Extractor", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

# --- Run Program ---
processor = QRDataExtractor()

# Step 1: Create a data-rich QR
processor.create_data_qr("Harshad Kale", "Advanced Python", "A+")

# Step 2: Scan to derive info
processor.start_scanning()