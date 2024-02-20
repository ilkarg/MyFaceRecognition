# MyFaceRecognition

## Пример
```python
from my_face_recognition import recognition

my_face = "face.jpg"
base = ["face1.jpg", "face2.jpg", "face3.jpg"]

result = recognition(my_face, base)
print("result - {}".format(result))
```

my_face - Лицо которое сверяется с базой на наличие в базе
base - База лиц с которой сверяется лицо