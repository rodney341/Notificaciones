from pyfcm import FCMNotification

# Tu clave del servidor de FCM
fcm_server_key = "AAAATNI-_JQ:APA91bEmaNhhxzo5FGSiyar-kVF_OAQNNG8BZIkVJnCYJdD8sJu3HjtZpISxi4N3MYlcrRP4wAXiD0JJe33BvsOsmolGCR9p2Am8S3YJ5WbvwzQ1bO9J0RM4zQGDi4e2hjA76mbouZiV"

# Crear una instancia de FCMNotification
push_service = FCMNotification(api_key=fcm_server_key)

# Datos de la notificación
message_title = "Título de la notificación"
message_body = "Cuerpo de la notificación"

# Enviar la notificación
registration_id = "fICh4HmhTpiPPxjSQeIWb4:APA91bHW1bIEHRF_bcj5ZxblAH3GtH-B5cDgW0XrTo6Coq9u9Gs3ZtaqqMhr3G7JcL16to1Ypa605Q6_78T-kLurhtSeiJ-8oY62Z2FrcLIOb7lzWW8i_ONeYaaSVDRIoHNZgkXhV6HY"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

# Imprimir el resultado
print(result)