import cv2
import mediapipe as mp


def recognize_gesture(hand_landmarks):
    # Ambil koordinat landmark
    thumb_tip = hand_landmarks.landmark[4]
    thumb_ip = hand_landmarks.landmark[3]
    thumb_mcp = hand_landmarks.landmark[2]
    index_tip = hand_landmarks.landmark[8]
    index_mcp = hand_landmarks.landmark[5]
    middle_tip = hand_landmarks.landmark[12]
    middle_mcp = hand_landmarks.landmark[9]
    ring_tip = hand_landmarks.landmark[16]
    ring_mcp = hand_landmarks.landmark[13]
    pinky_tip = hand_landmarks.landmark[20]
    pinky_mcp = hand_landmarks.landmark[17]
    wrist = hand_landmarks.landmark[0]

    # Gesture sederhana: Jempol ke atas
    if (thumb_tip.y < thumb_ip.y < thumb_mcp.y < wrist.y and
        index_tip.y > index_mcp.y and
        middle_tip.y > middle_mcp.y and
        ring_tip.y > ring_mcp.y and
        pinky_tip.y > pinky_mcp.y):
        return "Jempol"
    
    # Gesture sederhana: jari telunjuk dan jari tengah ke atas 
    if (thumb_tip.y > thumb_ip.y and
        index_tip.y < wrist.y and
        middle_tip.y < wrist.y and
        ring_tip.y > ring_mcp.y and
        pinky_tip.y > pinky_mcp.y):
        return "Peace"
    
    # Gesture sederhana: jari telunjuk dan jari tengah ke atas 
    if (thumb_tip.y > thumb_ip.y and
        index_tip.y < wrist.y and
        middle_tip.y < wrist.y and
        ring_tip.y < wrist.y and
        pinky_tip.y > pinky_mcp.y):
        return "Tiga Jari"
    
    #gesture "telapak tangan"
    if(thumb_tip.y < wrist.y and
       index_tip.y < wrist.y and
       middle_tip.y < wrist.y and
       ring_tip.y < wrist.y and
       pinky_tip.y < wrist.y):
        return "Hai"
    
    
    
    return "Tidak Dikenali"

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("tidak dapat membuka camera anda")
    exit()

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# mulai deteksi dengan camera
while(capture.isOpened()):
    ret, frame = capture.read()
    if not ret:
        print("tidak dapat membaca frame dari camera")
        break

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    # Draw the hand annotations on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = recognize_gesture(hand_landmarks)
            #tampilkan gesture pada frame
            cv2.putText(frame, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()