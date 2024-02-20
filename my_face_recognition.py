import face_recognition

def recognition(verifiable_face, faces_base):
    result = None
    check_face, check_face_encoding = None, None

    try:
        check_face = face_recognition.load_image_file(verifiable_face)
        check_face_encoding = face_recognition.face_encodings(check_face)[0]
    except IndexError:
        return "Не удалось распознать лицо"

    for face in faces_base:        
        current_face, current_face_encoding = None, None
        correct_face = True

        try:
            current_face = face_recognition.load_image_file(face)
            current_face_encoding = face_recognition.face_encodings(current_face)[0]
        except IndexError:
            print("[DEBUG]: Не удалось распознать лицо из Базы Данных; Файл: {}".format(face))
            correct_face = False
        
        if correct_face:
            results = face_recognition.compare_faces([check_face_encoding], current_face_encoding)
            if any(results):
                return "Совпадение! Добро пожаловать!"
            
            result = "Ошибка! Вас в базе нет"
    
    return result